import {test,expect} from '../fixtures/checkout.mjs';

async function capture(info,page,name,data,failed){
 await info.attach(name,{body:JSON.stringify({...data,observedAt:new Date().toISOString()},null,2),contentType:'application/json'});
 if(failed){const p=info.outputPath(`${name}.png`);await page.screenshot({path:p});await info.attach('failed-vector-screenshot',{path:p,contentType:'image/png'});}
}
test('GUI-B-001: consistent displayed money units',async({shop,page})=>{
 await shop.prepare(500001);const c=await shop.seedCoupon();const r=await shop.ui.apply(c.code);expect(r.status).toBe(200);
 await expect(shop.ui.saving).toHaveText(/Tiết kiệm:\s*50[,.\s]000\s*₫/);
 await expect(shop.ui.final).toHaveText(/Thành tiền:\s*450[,.\s]001\s*₫/);
 await expect(page.getByText(/^Tổng thanh toán:/)).toHaveText(/450[,.\s]001\s*₫/);
});
test('GUI-B-002: blank and whitespace codes do not apply',async({shop})=>{
 await shop.prepare(300001);
 for(const code of ['', '   ']){await shop.ui.code.fill(code);await expect(shop.ui.applyButton).toBeDisabled();await expect(shop.ui.saving).toHaveCount(0);}
 expect(shop.ui.events.requests).toHaveLength(0);
});
test('GUI-B-003: editing applied code clears stale reduction',async({shop,page})=>{
 await shop.prepare(500001);const c=await shop.seedCoupon();await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();
 await shop.ui.code.fill(c.code+'X');await expect(shop.ui.saving).toHaveCount(0);await expect(shop.ui.final).toHaveCount(0);
 await expect(page.getByText(/^Tổng thanh toán:/)).toHaveText(/500[,.\s]001\s*₫/);
 await shop.ui.code.fill('');await expect(shop.ui.applyButton).toBeDisabled();
});
test('GUI-B-004: checkout breadcrumb allows return navigation',async({shop,page})=>{
 await shop.prepare(300001);
 const breadcrumb=page.getByRole('navigation',{name:/breadcrumb|đường dẫn/i});await expect(breadcrumb).toBeVisible();
 await breadcrumb.getByRole('link',{name:/giỏ hàng/i}).click();await expect(page).toHaveURL(/\/cart$/);
});
test('GUI-B-005: valid percentage and fixed boundary results',async({shop,page},info)=>{
 for(const v of [{code:'SAVE10',total:300000,discount:30000},{code:'SAVE10',total:300001,discount:30000.1},{code:'BIGBUY',total:500000,discount:50000},{code:'BIGBUY',total:500001,discount:50000}]){
  await shop.prepare(v.total);const result=await shop.ui.apply(v.code);
  const expectedFinal=v.total-v.discount;
  const mismatch=result.status!==200||!Number.isFinite(result.body.discount_amount)||!Number.isFinite(result.body.final_amount)||Math.abs(result.body.discount_amount-v.discount)>0.001||Math.abs(result.body.final_amount-expectedFinal)>0.001;
  await capture(info,page,`valid-${v.code}-${v.total}`,{input:v,expectedFinal,result},mismatch);
  expect.soft(result.status,`${v.code} at total ${v.total}`).toBe(200);
  if(result.status===200){
   expect.soft(result.body.discount_amount).toBeCloseTo(v.discount,2);expect.soft(result.body.final_amount).toBeCloseTo(expectedFinal,2);
   const saving=await page.evaluate(n=>n.toLocaleString(),v.discount),final=await page.evaluate(n=>n.toLocaleString(),expectedFinal);
   await expect.soft(shop.ui.saving).toHaveText(`Tiết kiệm: ${saving} ₫`);await expect.soft(shop.ui.final).toHaveText(`Thành tiền: ${final} ₫`);
  }
 }
});
test('GUI-B-006: C1-C5 invalid eligibility and usage boundaries',async({shop,page},info)=>{
 const inactive=await shop.inactive();
 const cases=[{name:'nonexistent',code:`NONE_${process.env.GUI_RUN_ID}`,total:500001,accept:false},{name:'inactive',code:inactive.code,total:500001,accept:false},{name:'expired',code:'EXPIRED',total:500001,accept:false},{name:'below-minimum',code:'SAVE10',total:299999,accept:false}];
 for(const used of [1,2,3]){const c=await shop.seedCoupon({max_uses_per_user:2});await shop.usage(c,used);cases.push({name:`usage-${used}-limit-2`,code:c.code,total:500001,accept:used<2});}
 const c=await shop.seedCoupon();cases.push({name:'missing-auth',code:c.code,total:500001,accept:false},{name:'expired-jwt',code:c.code,total:500001,accept:false});
 for(const v of cases){
  await shop.prepare(v.total);
  if(v.name==='missing-auth'){await page.getByRole('button',{name:'Thoát',exact:true}).click();await expect(page.getByRole('link',{name:'Đăng nhập',exact:true})).toBeVisible();}
  if(v.name==='expired-jwt'){
   shop.ui.events.fixtures.push({mode:'Expired JWT transport fixture',exp:1,scope:'Only outgoing apply-coupon Authorization header replaced; real backend response retained'});
   await page.route('**/api/apply-coupon',r=>r.continue({headers:{...r.request().headers(),authorization:`Bearer ${shop.expired}`}}));
  }
  const result=await shop.ui.apply(v.code);const accepted=result.status===200;
  await capture(info,page,`eligibility-${v.name}`,{case:v,result,transportFixture:v.name==='expired-jwt'?'signed expired JWT exp=1':null},accepted!==v.accept);
  expect.soft(accepted,v.name).toBe(v.accept);
  if(!accepted){await expect.soft(shop.ui.error).toBeVisible();await expect.soft(shop.ui.saving).toHaveCount(0);}
  else if(v.accept)await expect.soft(shop.ui.saving).toBeVisible();
  await page.unroute('**/api/apply-coupon');
 }
});
test('GUI-B-007: pending state prevents duplicate apply',async({shop,page})=>{
 await shop.prepare(500001);const c=await shop.seedCoupon();let release;const gate=new Promise(resolve=>release=resolve);let intercepted=0;
 await page.route('**/api/apply-coupon',async route=>{intercepted++;const actual=await route.fetch();await gate;await route.fulfill({response:actual});});
 shop.ui.events.fixtures.push({mode:'Hold real backend response until pending UI has been checked',fabricatedResponse:false});
 try{
  await shop.ui.code.fill(c.code);await shop.ui.applyButton.click();await expect(shop.ui.applyButton).toBeDisabled();await expect(shop.ui.applyButton).toHaveText('...');
  await shop.ui.applyButton.click({force:true});await expect.poll(()=>intercepted).toBe(1);
 }finally{release();}
 await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.applyButton).toBeEnabled();
});
test('GUI-B-008: recover after bad code and transport failure',async({shop,page})=>{
 await shop.prepare(500001);const c=await shop.seedCoupon();await shop.ui.apply(`NONE_${process.env.GUI_RUN_ID}`);await expect(shop.ui.error).toBeVisible();
 await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.error).toHaveCount(0);
 await page.route('**/api/apply-coupon',r=>r.abort('failed'));shop.ui.events.fixtures.push({mode:'Transport abort for apply-coupon recovery'});
 await shop.ui.code.fill(c.code);const failed=page.waitForEvent('requestfailed',{predicate:r=>r.url().endsWith('/api/apply-coupon')});await shop.ui.applyButton.click();await failed;
 await expect(shop.ui.error).toBeVisible();await page.unroute('**/api/apply-coupon');
 await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.error).toHaveCount(0);await expect(shop.ui.applyButton).toBeEnabled();
});
