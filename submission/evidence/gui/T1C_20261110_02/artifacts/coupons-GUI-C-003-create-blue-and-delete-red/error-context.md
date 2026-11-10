# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: coupons.spec.mjs >> GUI-C-003: create blue and delete red
- Location: tools/gui/tests/coupons.spec.mjs:31:1

# Error details

```
Error: expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false
```

# Page snapshot

```yaml
- generic [ref=e3]:
  - generic [ref=e4]:
    - heading "EShop Admin" [level=1] [ref=e5]
    - list [ref=e6]:
      - listitem [ref=e7] [cursor=pointer]: Dashboard
      - listitem [ref=e8] [cursor=pointer]: Danh mục
      - listitem [ref=e9] [cursor=pointer]: Sản phẩm
      - listitem [ref=e10] [cursor=pointer]: Mã Giảm Giá
      - listitem [ref=e11] [cursor=pointer]: Đơn hàng
      - listitem [ref=e12] [cursor=pointer]: Người dùng
      - listitem [ref=e13] [cursor=pointer]: Đăng xuất
  - generic [ref=e15]:
    - heading "Quản lý Mã Giảm Giá" [level=2] [ref=e16]
    - generic [ref=e17]:
      - heading "Tạo mã giảm giá mới" [level=3] [ref=e18]
      - generic [ref=e19]:
        - 'textbox "Mã coupon (VD: SAVE10)" [ref=e20]'
        - combobox [ref=e21]:
          - option "Phần trăm (%)" [selected]
          - option "Số tiền cố định (₫)"
        - 'spinbutton "Giá trị % (VD: 10)" [ref=e22]'
        - spinbutton "Đơn tối thiểu (₫)" [ref=e23]: "0"
        - textbox [ref=e24]:
          - /placeholder: Ngày hết hạn
        - spinbutton "Số lần dùng tối đa/người" [ref=e25]: "1"
      - button "Tạo mã" [ref=e26] [cursor=pointer]
    - table [ref=e27]:
      - rowgroup [ref=e28]:
        - row [ref=e29]:
          - columnheader "Mã" [ref=e30]
          - columnheader "Loại" [ref=e31]
          - columnheader "Giá trị" [ref=e32]
          - columnheader "Đơn tối thiểu" [ref=e33]
          - columnheader "Hết hạn" [ref=e34]
          - columnheader "Giới hạn/người" [ref=e35]
          - columnheader "Hành động" [ref=e36]
      - rowgroup [ref=e37]:
        - row [ref=e38]:
          - cell "SAVE10" [ref=e39]
          - cell "Phần trăm" [ref=e40]
          - cell "10%" [ref=e41]
          - cell "300,000 ₫" [ref=e42]
          - cell "2099-12-31" [ref=e43]
          - cell "1 lần" [ref=e44]
          - cell [ref=e45]:
            - button "Xóa" [ref=e46] [cursor=pointer]
        - row [ref=e47]:
          - cell "BIGBUY" [ref=e48]
          - cell "Cố định" [ref=e49]
          - cell "50,000 ₫" [ref=e50]
          - cell "500,000 ₫" [ref=e51]
          - cell "2099-12-31" [ref=e52]
          - cell "1 lần" [ref=e53]
          - cell [ref=e54]:
            - button "Xóa" [ref=e55] [cursor=pointer]
        - row [ref=e56]:
          - cell "VIP100" [ref=e57]
          - cell "Cố định" [ref=e58]
          - cell "100,000 ₫" [ref=e59]
          - cell "300,000 ₫" [ref=e60]
          - cell "2099-12-31" [ref=e61]
          - cell "2 lần" [ref=e62]
          - cell [ref=e63]:
            - button "Xóa" [ref=e64] [cursor=pointer]
        - row [ref=e65]:
          - cell "EXPIRED" [ref=e66]
          - cell "Phần trăm" [ref=e67]
          - cell "20%" [ref=e68]
          - cell "100,000 ₫" [ref=e69]
          - cell "Hết hạn" [ref=e70]
          - cell "1 lần" [ref=e71]
          - cell [ref=e72]:
            - button "Xóa" [ref=e73] [cursor=pointer]
```

# Test source

```ts
  1   | import {test,expect} from '../fixtures/admin.mjs';
  2   | 
  3   | async function create(admin,adminApi,overrides={},method='click'){
  4   |  const data=adminApi.fresh(overrides);await admin.fill(data);const result=await admin.submit(method);
  5   |  if(!result.clientBlocked&&result.status===200)await expect(admin.row(data.code)).toBeVisible();
  6   |  return {data,...result};
  7   | }
  8   | async function vector(admin,adminApi,info,field,value,shouldAccept,extra={}){
  9   |  const before=new Set((await adminApi.list()).map(c=>c.id));
  10  |  const r=await create(admin,adminApi,{...extra,[field]:value});
  11  |  const saved=(await adminApi.list()).find(c=>c.code===r.data.code&&!before.has(c.id));
  12  |  const observation={field,value,shouldAccept,clientBlocked:r.clientBlocked,httpStatus:r.status,saved:saved??null,observedAt:new Date().toISOString()};
  13  |  await info.attach(`vector-${field}-${value}-${extra.type??'default'}`,{body:JSON.stringify(observation,null,2),contentType:'application/json'});
  14  |  if(!shouldAccept&&saved){
  15  |   await admin.row(r.data.code).scrollIntoViewIfNeeded();
  16  |   const shot=info.outputPath(`unexpected-${field}-${value}-${extra.type??'default'}.png`);
  17  |   await admin.page.screenshot({path:shot});await info.attach('failed-vector-screenshot',{path:shot,contentType:'image/png'});
  18  |  }
  19  |  expect.soft(Boolean(saved),`${field}=${value}`).toBe(shouldAccept);
  20  | }
  21  | 
  22  | test('GUI-C-001: Vietnamese coupon content',async({admin})=>{
  23  |  await expect(admin.heading).toHaveText('Quản lý Mã Giảm Giá');
  24  |  await expect(admin.create).toHaveText('Tạo mã');
  25  |  await expect(admin.page.getByRole('columnheader')).toHaveText(['Mã','Loại','Giá trị','Đơn tối thiểu','Hết hạn','Giới hạn/người','Hành động']);
  26  | });
  27  | test('GUI-C-002: one descriptive h1',async({admin})=>{
  28  |  await expect(admin.page.getByRole('heading',{level:1})).toHaveCount(1);
  29  |  await expect(admin.page.getByRole('heading',{level:1})).toContainText(/Mã Giảm Giá/i);
  30  | });
  31  | test('GUI-C-003: create blue and delete red',async({admin})=>{
  32  |  const rgb=await admin.create.evaluate(e=>getComputedStyle(e).backgroundColor.match(/\d+/g).map(Number));
> 33  |  expect(rgb[2]>rgb[0]&&rgb[2]>rgb[1]).toBe(true);
      |                                       ^ Error: expect(received).toBe(expected) // Object.is equality
  34  |  const red=await admin.page.getByRole('button',{name:'Xóa',exact:true}).first().evaluate(e=>getComputedStyle(e).backgroundColor.match(/\d+/g).map(Number));
  35  |  expect(red[0]>red[1]&&red[0]>red[2]).toBe(true);
  36  | });
  37  | test('GUI-C-004: correct units for percent and fixed',async({admin,adminApi})=>{
  38  |  const p=await adminApi.seed({type:'percent',discount_value:10,min_order_amount:300000});
  39  |  const f=await adminApi.seed({type:'fixed',discount_value:50000,min_order_amount:500000});
  40  |  await admin.goto();
  41  |  await expect(admin.row(p.code).getByRole('cell').nth(2)).toHaveText('10%');
  42  |  await expect(admin.row(f.code).getByRole('cell').nth(2)).toHaveText(/50[,.\s]000\s*₫/);
  43  |  await expect(admin.row(f.code).getByRole('cell').nth(3)).toHaveText(/500[,.\s]000\s*₫/);
  44  | });
  45  | test('GUI-C-005: table values match stored coupon',async({admin,adminApi})=>{
  46  |  const c=await adminApi.seed({min_order_amount:123000,max_uses_per_user:2});await admin.goto();
  47  |  await expect(admin.row(c.code).getByRole('cell')).toHaveText([c.code,'Phần trăm','10%',/123[,.\s]000\s*₫/,'2099-12-31','2 lần','Xóa']);
  48  | });
  49  | test('GUI-C-006: form does not overlap on resize',async({admin,page})=>{
  50  |  for(const width of [1280,390]){
  51  |   await page.setViewportSize({width,height:width===1280?800:844});
  52  |   const overlaps=await admin.form.locator('input,select').evaluateAll(es=>{
  53  |    const rs=es.map(e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom};});
  54  |    return rs.flatMap((a,i)=>rs.slice(i+1).filter(b=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>2).map(b=>({a,b})));
  55  |   });
  56  |   expect(overlaps,`overlap at viewport ${width}`).toEqual([]);
  57  |   await expect(admin.create).toBeVisible();
  58  |  }
  59  | });
  60  | test('GUI-C-007: persistent labels and required markers',async({admin})=>{
  61  |  await expect(admin.form.locator('label')).toHaveCount(6);
  62  |  for(const label of await admin.form.locator('label').all())await expect(label).toContainText('*');
  63  | });
  64  | test('GUI-C-008: empty and whitespace code rejected',async({admin,adminApi},info)=>{
  65  |  await vector(admin,adminApi,info,'code','',false);
  66  |  await vector(admin,adminApi,info,'code','   ',false);
  67  | });
  68  | test('GUI-C-009: duplicate code rejected',async({admin,adminApi})=>{
  69  |  const c=await adminApi.seed();await admin.goto();await admin.fill(c);const reply=await admin.submit();
  70  |  expect(reply.status).toBeGreaterThanOrEqual(400);
  71  |  const rows=(await adminApi.list()).filter(x=>x.code===c.code);expect(rows).toHaveLength(1);
  72  |  await expect(admin.row(c.code)).toHaveCount(1);
  73  | });
  74  | test('GUI-C-010: type choices and keyboard selection',async({admin})=>{
  75  |  await expect(admin.type.getByRole('option')).toHaveText(['Phần trăm (%)','Số tiền cố định (₫)']);
  76  |  await admin.type.selectOption('percent');await admin.type.press('ArrowDown');await expect(admin.type).toHaveValue('fixed');
  77  |  await admin.type.press('Escape');await expect(admin.type).toHaveValue('fixed');
  78  | });
  79  | test('GUI-C-011: discount value boundaries',async({admin,adminApi},info)=>{
  80  |  for(const type of ['percent','fixed'])for(const value of [-1,0,1])await vector(admin,adminApi,info,'discount_value',value,value>0,{type});
  81  | });
  82  | test('GUI-C-012: minimum order boundaries',async({admin,adminApi},info)=>{
  83  |  for(const value of [-1,0,1])await vector(admin,adminApi,info,'min_order_amount',value,value>=0);
  84  | });
  85  | test('GUI-C-013: uses-per-user boundaries',async({admin,adminApi},info)=>{
  86  |  for(const value of [0,1,2])await vector(admin,adminApi,info,'max_uses_per_user',value,value>=1);
  87  | });
  88  | test('GUI-C-014: all mandatory fields reject empty values',async({admin,adminApi},info)=>{
  89  |  for(const field of ['discount_value','min_order_amount','expired_at','max_uses_per_user'])await vector(admin,adminApi,info,field,'',false);
  90  | });
  91  | test('GUI-C-015: leap date and invalid date picker values',async({admin},info)=>{
  92  |  await admin.expires.fill('2028-02-29');await expect(admin.expires).toHaveValue('2028-02-29');
  93  |  for(const invalid of ['2027-02-29','2026-04-31']){
  94  |   let nativeRejection='';
  95  |   try{await admin.expires.fill(invalid);}catch(e){if(!/Malformed value/.test(e.message))throw e;nativeRejection=e.message.split('\n')[0];}
  96  |   await expect(admin.expires).not.toHaveValue(invalid);
  97  |   await info.attach(`date-${invalid}`,{body:JSON.stringify({requested:invalid,value:await admin.expires.inputValue(),nativeRejection,scope:'Native date control rejection; not backend date validation'}),contentType:'application/json'});
  98  |  }
  99  | });
  100 | test('GUI-C-016: discount hint follows type',async({admin})=>{
  101 |  await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
  102 |  await admin.type.selectOption('fixed');await expect(admin.value).toHaveAttribute('placeholder',/Số tiền.*₫|Số tiền.*50000/);
  103 |  await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
  104 | });
  105 | test('GUI-C-017: form tab order',async({admin})=>{
  106 |  await admin.code.focus();
  107 |  for(const target of [admin.type,admin.value,admin.minimum,admin.expires]){await admin.page.keyboard.press('Tab');await expect(target).toBeFocused();}
  108 |  // The native date picker has multiple internal fields; leaving it may take several Tabs.
  109 |  let reached=false;
  110 |  for(let i=0;i<5;i++){await admin.page.keyboard.press('Tab');if(await admin.limit.evaluate(e=>e===document.activeElement)){reached=true;break;}}
  111 |  expect(reached).toBe(true);await admin.page.keyboard.press('Shift+Tab');await expect(admin.expires).toBeFocused();
  112 | });
  113 | test('GUI-C-018: create using Enter and click',async({admin,adminApi})=>{
  114 |  for(const method of ['enter','click']){const r=await create(admin,adminApi,{},method);expect(r.status).toBe(200);await expect(admin.row(r.data.code)).toHaveCount(1);}
  115 | });
  116 | test('GUI-C-019: coupons tab opens correct screen',async({admin})=>{
  117 |  await expect(admin.heading).toBeVisible();await expect(admin.create).toBeVisible();await expect(admin.page.getByRole('table')).toBeVisible();
  118 | });
  119 | test('GUI-C-020: active tab highlighted',async({admin})=>{
  120 |  await expect(admin.tab).toHaveClass(/text-blue-400/);
  121 |  await admin.page.getByText('Dashboard',{exact:true}).click();await expect(admin.tab).not.toHaveClass(/text-blue-400/);
  122 |  await admin.tab.click();await expect(admin.tab).toHaveClass(/text-blue-400/);
  123 | });
  124 | test('GUI-C-021: tab reachable by keyboard',async({admin,page})=>{
  125 |  await admin.page.getByText('Dashboard',{exact:true}).click();
  126 |  let reached=false;
  127 |  for(let i=0;i<18;i++){await page.keyboard.press('Tab');if(await admin.tab.evaluate(e=>e===document.activeElement)){reached=true;break;}}
  128 |  expect(reached,'Coupons nav must be keyboard focusable').toBe(true);
  129 |  await page.keyboard.press('Enter');await expect(admin.heading).toBeVisible();
  130 | });
  131 | test('GUI-C-022: navigating away does not mutate coupon data',async({admin,adminApi})=>{
  132 |  const before=await adminApi.list();const data=adminApi.fresh();await admin.fill(data);
  133 |  await admin.page.getByText('Dashboard',{exact:true}).click();await admin.tab.click();
```