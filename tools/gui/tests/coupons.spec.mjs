import {test,expect} from '../fixtures/admin.mjs';

async function create(admin,adminApi,overrides={},method='click'){
 const data=adminApi.fresh(overrides);await admin.fill(data);const result=await admin.submit(method);
 if(!result.clientBlocked&&result.status===200)await expect(admin.row(data.code)).toBeVisible();
 return {data,...result};
}
async function vector(admin,adminApi,info,field,value,shouldAccept,extra={}){
 const before=new Set((await adminApi.list()).map(c=>c.id));
 const r=await create(admin,adminApi,{...extra,[field]:value});
 const saved=(await adminApi.list()).find(c=>c.code===r.data.code&&!before.has(c.id));
 const observation={field,value,shouldAccept,clientBlocked:r.clientBlocked,httpStatus:r.status,saved:saved??null,observedAt:new Date().toISOString()};
 await info.attach(`vector-${field}-${value}-${extra.type??'default'}`,{body:JSON.stringify(observation,null,2),contentType:'application/json'});
 if(!shouldAccept&&saved){
  await admin.row(r.data.code).scrollIntoViewIfNeeded();
  const shot=info.outputPath(`unexpected-${field}-${value}-${extra.type??'default'}.png`);
  await admin.page.screenshot({path:shot});await info.attach('failed-vector-screenshot',{path:shot,contentType:'image/png'});
 }
 expect.soft(Boolean(saved),`${field}=${value}`).toBe(shouldAccept);
}

test('GUI-C-001: Vietnamese coupon content',async({admin})=>{
 await expect(admin.heading).toHaveText('Quản lý Mã Giảm Giá');
 await expect(admin.create).toHaveText('Tạo mã');
 await expect(admin.page.getByRole('columnheader')).toHaveText(['Mã','Loại','Giá trị','Đơn tối thiểu','Hết hạn','Giới hạn/người','Hành động']);
});
test('GUI-C-002: one descriptive h1',async({admin})=>{
 await expect(admin.page.getByRole('heading',{level:1})).toHaveCount(1);
 await expect(admin.page.getByRole('heading',{level:1})).toContainText(/Mã Giảm Giá/i);
});
test('GUI-C-003: create blue and delete red',async({admin})=>{
 const rgb=await admin.create.evaluate(e=>getComputedStyle(e).backgroundColor.match(/\d+/g).map(Number));
 expect(rgb[2]>rgb[0]&&rgb[2]>rgb[1]).toBe(true);
 const red=await admin.page.getByRole('button',{name:'Xóa',exact:true}).first().evaluate(e=>getComputedStyle(e).backgroundColor.match(/\d+/g).map(Number));
 expect(red[0]>red[1]&&red[0]>red[2]).toBe(true);
});
test('GUI-C-004: correct units for percent and fixed',async({admin,adminApi})=>{
 const p=await adminApi.seed({type:'percent',discount_value:10,min_order_amount:300000});
 const f=await adminApi.seed({type:'fixed',discount_value:50000,min_order_amount:500000});
 await admin.goto();
 await expect(admin.row(p.code).getByRole('cell').nth(2)).toHaveText('10%');
 await expect(admin.row(f.code).getByRole('cell').nth(2)).toHaveText(/50[,.\s]000\s*₫/);
 await expect(admin.row(f.code).getByRole('cell').nth(3)).toHaveText(/500[,.\s]000\s*₫/);
});
test('GUI-C-005: table values match stored coupon',async({admin,adminApi})=>{
 const c=await adminApi.seed({min_order_amount:123000,max_uses_per_user:2});await admin.goto();
 await expect(admin.row(c.code).getByRole('cell')).toHaveText([c.code,'Phần trăm','10%',/123[,.\s]000\s*₫/,'2099-12-31','2 lần','Xóa']);
});
test('GUI-C-006: form does not overlap on resize',async({admin,page})=>{
 for(const width of [1280,390]){
  await page.setViewportSize({width,height:width===1280?800:844});
  const overlaps=await admin.form.locator('input,select').evaluateAll(es=>{
   const rs=es.map(e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom};});
   return rs.flatMap((a,i)=>rs.slice(i+1).filter(b=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>2).map(b=>({a,b})));
  });
  expect(overlaps,`overlap at viewport ${width}`).toEqual([]);
  await expect(admin.create).toBeVisible();
 }
});
test('GUI-C-007: persistent labels and required markers',async({admin})=>{
 await expect(admin.form.locator('label')).toHaveCount(6);
 for(const label of await admin.form.locator('label').all())await expect(label).toContainText('*');
});
test('GUI-C-008: empty and whitespace code rejected',async({admin,adminApi},info)=>{
 await vector(admin,adminApi,info,'code','',false);
 await vector(admin,adminApi,info,'code','   ',false);
});
test('GUI-C-009: duplicate code rejected',async({admin,adminApi})=>{
 const c=await adminApi.seed();await admin.goto();await admin.fill(c);const reply=await admin.submit();
 expect(reply.status).toBeGreaterThanOrEqual(400);
 const rows=(await adminApi.list()).filter(x=>x.code===c.code);expect(rows).toHaveLength(1);
 await expect(admin.row(c.code)).toHaveCount(1);
});
test('GUI-C-010: type choices and keyboard selection',async({admin})=>{
 await expect(admin.type.getByRole('option')).toHaveText(['Phần trăm (%)','Số tiền cố định (₫)']);
 await admin.type.selectOption('percent');await admin.type.press('ArrowDown');await expect(admin.type).toHaveValue('fixed');
 await admin.type.press('Escape');await expect(admin.type).toHaveValue('fixed');
});
test('GUI-C-011: discount value boundaries',async({admin,adminApi},info)=>{
 for(const type of ['percent','fixed'])for(const value of [-1,0,1])await vector(admin,adminApi,info,'discount_value',value,value>0,{type});
});
test('GUI-C-012: minimum order boundaries',async({admin,adminApi},info)=>{
 for(const value of [-1,0,1])await vector(admin,adminApi,info,'min_order_amount',value,value>=0);
});
test('GUI-C-013: uses-per-user boundaries',async({admin,adminApi},info)=>{
 for(const value of [0,1,2])await vector(admin,adminApi,info,'max_uses_per_user',value,value>=1);
});
test('GUI-C-014: all mandatory fields reject empty values',async({admin,adminApi},info)=>{
 for(const field of ['discount_value','min_order_amount','expired_at','max_uses_per_user'])await vector(admin,adminApi,info,field,'',false);
});
test('GUI-C-015: leap date and invalid date picker values',async({admin},info)=>{
 await admin.expires.fill('2028-02-29');await expect(admin.expires).toHaveValue('2028-02-29');
 for(const invalid of ['2027-02-29','2026-04-31']){
  let nativeRejection='';
  try{await admin.expires.fill(invalid);}catch(e){if(!/Malformed value/.test(e.message))throw e;nativeRejection=e.message.split('\n')[0];}
  await expect(admin.expires).not.toHaveValue(invalid);
  await info.attach(`date-${invalid}`,{body:JSON.stringify({requested:invalid,value:await admin.expires.inputValue(),nativeRejection,scope:'Native date control rejection; not backend date validation'}),contentType:'application/json'});
 }
});
test('GUI-C-016: discount hint follows type',async({admin})=>{
 await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
 await admin.type.selectOption('fixed');await expect(admin.value).toHaveAttribute('placeholder',/Số tiền.*₫|Số tiền.*50000/);
 await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
});
test('GUI-C-017: form tab order',async({admin})=>{
 await admin.code.focus();
 for(const target of [admin.type,admin.value,admin.minimum,admin.expires]){await admin.page.keyboard.press('Tab');await expect(target).toBeFocused();}
 // The native date picker has multiple internal fields; leaving it may take several Tabs.
 let reached=false;
 for(let i=0;i<5;i++){await admin.page.keyboard.press('Tab');if(await admin.limit.evaluate(e=>e===document.activeElement)){reached=true;break;}}
 expect(reached).toBe(true);await admin.page.keyboard.press('Shift+Tab');await expect(admin.expires).toBeFocused();
});
test('GUI-C-018: create using Enter and click',async({admin,adminApi})=>{
 for(const method of ['enter','click']){const r=await create(admin,adminApi,{},method);expect(r.status).toBe(200);await expect(admin.row(r.data.code)).toHaveCount(1);}
});
test('GUI-C-019: coupons tab opens correct screen',async({admin})=>{
 await expect(admin.heading).toBeVisible();await expect(admin.create).toBeVisible();await expect(admin.page.getByRole('table')).toBeVisible();
});
test('GUI-C-020: active tab highlighted',async({admin})=>{
 await expect(admin.tab).toHaveClass(/text-blue-400/);
 await admin.page.getByText('Dashboard',{exact:true}).click();await expect(admin.tab).not.toHaveClass(/text-blue-400/);
 await admin.tab.click();await expect(admin.tab).toHaveClass(/text-blue-400/);
});
test('GUI-C-021: tab reachable by keyboard',async({admin,page})=>{
 await admin.page.getByText('Dashboard',{exact:true}).click();
 let reached=false;
 for(let i=0;i<18;i++){await page.keyboard.press('Tab');if(await admin.tab.evaluate(e=>e===document.activeElement)){reached=true;break;}}
 expect(reached,'Coupons nav must be keyboard focusable').toBe(true);
 await page.keyboard.press('Enter');await expect(admin.heading).toBeVisible();
});
test('GUI-C-022: navigating away does not mutate coupon data',async({admin,adminApi})=>{
 const before=await adminApi.list();const data=adminApi.fresh();await admin.fill(data);
 await admin.page.getByText('Dashboard',{exact:true}).click();await admin.tab.click();
 const after=await adminApi.list();expect(after).toEqual(before);await expect(admin.row(data.code)).toHaveCount(0);
});
test('GUI-C-023: successful create persists on reload',async({admin,adminApi})=>{
 for(const type of ['percent','fixed']){const r=await create(admin,adminApi,{type});expect(r.status).toBe(200);await admin.goto();await expect(admin.row(r.data.code)).toBeVisible();}
});
test('GUI-C-024: error understandable and above submit',async({admin,adminApi})=>{
 const duplicate=await adminApi.seed();await admin.goto();await admin.fill(duplicate);await admin.submit();
 const inline=admin.page.getByText(/mã.*tồn tại|trùng mã|không thể tạo/i).filter({visible:true});
 await expect(inline).toBeVisible();
 const error=await inline.boundingBox(),button=await admin.create.boundingBox();expect(error.bottom??error.y+error.height).toBeLessThanOrEqual(button.y);
});
test('GUI-C-025: delete can be cancelled or undone',async({admin,adminApi})=>{
 const c=await adminApi.seed();await admin.goto();await admin.row(c.code).getByRole('button',{name:'Xóa',exact:true}).click();
 const canConfirm=admin.events.dialogs.some(d=>d.type==='confirm');
 let undoOffered=false;
 if(!canConfirm){
  const undo=admin.page.getByRole('button',{name:/hoàn tác/i});undoOffered=(await undo.count())>0;
  if(undoOffered)await undo.click();
  else{
   await expect.poll(()=>admin.events.requests.some(r=>r.method==='DELETE'&&r.url.endsWith(`/${c.id}`))).toBe(true);
   await expect(admin.row(c.code)).toHaveCount(0);
  }
 }
 expect(canConfirm||undoOffered,'confirm/cancel or undo offered').toBe(true);
 await expect(admin.row(c.code)).toBeVisible();
});
test('GUI-C-026: delete only target coupon and persist',async({admin,adminApi})=>{
 const a=await adminApi.seed(),b=await adminApi.seed();await admin.goto();admin.confirm='accept';
 await admin.row(a.code).getByRole('button',{name:'Xóa',exact:true}).click();await expect(admin.row(a.code)).toHaveCount(0);
 await admin.goto();await expect(admin.row(a.code)).toHaveCount(0);await expect(admin.row(b.code)).toBeVisible();
 const stored=(await adminApi.list()).find(c=>c.code===b.code);expect(stored.discount_value).toBe(b.discount_value);
});
test('GUI-C-027: empty-state UI using isolated empty API fixture',async({admin,page},info)=>{
 await page.route('**/api/coupons',r=>r.fulfill({status:200,contentType:'application/json',body:'[]'}));
 await admin.goto();await expect(page.getByRole('table').locator('tbody tr')).toHaveCount(0);
 await info.attach('fixture-mode',{body:JSON.stringify({mode:'Controlled API empty response; no backend data deleted',response:[]}),contentType:'application/json'});
 await expect(page.getByText(/chưa có mã|không có mã|danh sách.*trống/i)).toBeVisible();
});
test('GUI-C-028: network load error is visible and recoverable',async({admin,page},info)=>{
 await page.route('**/api/coupons',r=>r.abort('failed'));
 await info.attach('fixture-mode',{body:JSON.stringify({mode:'Transport fault injection: GET /api/coupons aborted; create/delete variants not reached if load assertion fails'}),contentType:'application/json'});
 await admin.goto();
 await expect(page.getByText(/lỗi.*tải|không thể.*tải|thử lại/i)).toBeVisible();
 await page.unroute('**/api/coupons');await admin.goto();await expect(page.getByRole('table')).toBeVisible();
});
