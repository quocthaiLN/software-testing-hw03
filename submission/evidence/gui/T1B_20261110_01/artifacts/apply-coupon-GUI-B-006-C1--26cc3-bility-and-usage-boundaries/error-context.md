# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: apply-coupon.spec.mjs >> GUI-B-006: C1-C5 invalid eligibility and usage boundaries
- Location: tools/gui/tests/apply-coupon.spec.mjs:43:1

# Error details

```
Error: missing-auth

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

```
Error: expired-jwt

expect(received).toBe(expected) // Object.is equality

Expected: false
Received: true
```

# Page snapshot

```yaml
- generic [ref=f8e3]:
  - banner [ref=f8e4]:
    - link "EShop" [ref=f8e5] [cursor=pointer]:
      - /url: /
    - navigation [ref=f8e6]:
      - link "Giỏ hàng" [ref=f8e7] [cursor=pointer]:
        - /url: /cart
      - generic [ref=f8e8]:
        - link "Chào, HW03 Coupon UI" [ref=f8e9] [cursor=pointer]:
          - /url: /profile
        - button "Thoát" [ref=f8e10] [cursor=pointer]
  - main [ref=f8e11]:
    - generic [ref=f8e12]:
      - heading "Xác Nhận Đơn Hàng" [level=2] [ref=f8e13]
      - generic [ref=f8e14]:
        - heading "Sản phẩm:" [level=3] [ref=f8e15]
        - list [ref=f8e16]:
          - listitem [ref=f8e17]: T1B_T1B_20261110_01_bd36bf0c37_8 x 1 — 500,001 ₫
      - generic [ref=f8e18]:
        - generic [ref=f8e19]: "Tổng tiền thanh toán (VND):"
        - spinbutton [ref=f8e20]: "500001"
      - generic [ref=f8e21]:
        - generic [ref=f8e22]: Mã Giảm Giá
        - generic [ref=f8e23]:
          - textbox "Nhập mã giảm giá..." [ref=f8e24]: T1_T1B_20261110_01_36BF0C37_4
          - button "Áp dụng" [ref=f8e25] [cursor=pointer]
        - generic [ref=f8e26]:
          - paragraph [ref=f8e27]: ✅ Áp dụng thành công! Giảm 50,000 ₫
          - paragraph [ref=f8e28]:
            - text: "Tiết kiệm:"
            - strong [ref=f8e29]: 50,000 ₫
          - paragraph [ref=f8e30]:
            - text: "Thành tiền:"
            - strong [ref=f8e31]: 450,001 ₫
      - generic [ref=f8e32]: "Tổng thanh toán: 450,001 ₫"
      - button "Xác Nhận Thanh Toán" [ref=f8e34] [cursor=pointer]
  - contentinfo [ref=f8e35]: © 2026 EShop SUT. Dành cho mục đích kiểm thử.
```

# Test source

```ts
  1  | import {test,expect} from '../fixtures/checkout.mjs';
  2  | 
  3  | async function capture(info,page,name,data,failed){
  4  |  await info.attach(name,{body:JSON.stringify({...data,observedAt:new Date().toISOString()},null,2),contentType:'application/json'});
  5  |  if(failed){const p=info.outputPath(`${name}.png`);await page.screenshot({path:p});await info.attach('failed-vector-screenshot',{path:p,contentType:'image/png'});}
  6  | }
  7  | test('GUI-B-001: consistent displayed money units',async({shop,page})=>{
  8  |  await shop.prepare(500001);const c=await shop.seedCoupon();const r=await shop.ui.apply(c.code);expect(r.status).toBe(200);
  9  |  await expect(shop.ui.saving).toHaveText(/Tiết kiệm:\s*50[,.\s]000\s*₫/);
  10 |  await expect(shop.ui.final).toHaveText(/Thành tiền:\s*450[,.\s]001\s*₫/);
  11 |  await expect(page.getByText(/^Tổng thanh toán:/)).toHaveText(/450[,.\s]001\s*₫/);
  12 | });
  13 | test('GUI-B-002: blank and whitespace codes do not apply',async({shop})=>{
  14 |  await shop.prepare(300001);
  15 |  for(const code of ['', '   ']){await shop.ui.code.fill(code);await expect(shop.ui.applyButton).toBeDisabled();await expect(shop.ui.saving).toHaveCount(0);}
  16 |  expect(shop.ui.events.requests).toHaveLength(0);
  17 | });
  18 | test('GUI-B-003: editing applied code clears stale reduction',async({shop,page})=>{
  19 |  await shop.prepare(500001);const c=await shop.seedCoupon();await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();
  20 |  await shop.ui.code.fill(c.code+'X');await expect(shop.ui.saving).toHaveCount(0);await expect(shop.ui.final).toHaveCount(0);
  21 |  await expect(page.getByText(/^Tổng thanh toán:/)).toHaveText(/500[,.\s]001\s*₫/);
  22 |  await shop.ui.code.fill('');await expect(shop.ui.applyButton).toBeDisabled();
  23 | });
  24 | test('GUI-B-004: checkout breadcrumb allows return navigation',async({shop,page})=>{
  25 |  await shop.prepare(300001);
  26 |  const breadcrumb=page.getByRole('navigation',{name:/breadcrumb|đường dẫn/i});await expect(breadcrumb).toBeVisible();
  27 |  await breadcrumb.getByRole('link',{name:/giỏ hàng/i}).click();await expect(page).toHaveURL(/\/cart$/);
  28 | });
  29 | test('GUI-B-005: valid percentage and fixed boundary results',async({shop,page},info)=>{
  30 |  for(const v of [{code:'SAVE10',total:300000,discount:30000},{code:'SAVE10',total:300001,discount:30000.1},{code:'BIGBUY',total:500000,discount:50000},{code:'BIGBUY',total:500001,discount:50000}]){
  31 |   await shop.prepare(v.total);const result=await shop.ui.apply(v.code);
  32 |   const expectedFinal=v.total-v.discount;
  33 |   const mismatch=result.status!==200||!Number.isFinite(result.body.discount_amount)||!Number.isFinite(result.body.final_amount)||Math.abs(result.body.discount_amount-v.discount)>0.001||Math.abs(result.body.final_amount-expectedFinal)>0.001;
  34 |   await capture(info,page,`valid-${v.code}-${v.total}`,{input:v,expectedFinal,result},mismatch);
  35 |   expect.soft(result.status,`${v.code} at total ${v.total}`).toBe(200);
  36 |   if(result.status===200){
  37 |    expect.soft(result.body.discount_amount).toBeCloseTo(v.discount,2);expect.soft(result.body.final_amount).toBeCloseTo(expectedFinal,2);
  38 |    const saving=await page.evaluate(n=>n.toLocaleString(),v.discount),final=await page.evaluate(n=>n.toLocaleString(),expectedFinal);
  39 |    await expect.soft(shop.ui.saving).toHaveText(`Tiết kiệm: ${saving} ₫`);await expect.soft(shop.ui.final).toHaveText(`Thành tiền: ${final} ₫`);
  40 |   }
  41 |  }
  42 | });
  43 | test('GUI-B-006: C1-C5 invalid eligibility and usage boundaries',async({shop,page},info)=>{
  44 |  const inactive=await shop.inactive();
  45 |  const cases=[{name:'nonexistent',code:`NONE_${process.env.GUI_RUN_ID}`,total:500001,accept:false},{name:'inactive',code:inactive.code,total:500001,accept:false},{name:'expired',code:'EXPIRED',total:500001,accept:false},{name:'below-minimum',code:'SAVE10',total:299999,accept:false}];
  46 |  for(const used of [1,2,3]){const c=await shop.seedCoupon({max_uses_per_user:2});await shop.usage(c,used);cases.push({name:`usage-${used}-limit-2`,code:c.code,total:500001,accept:used<2});}
  47 |  const c=await shop.seedCoupon();cases.push({name:'missing-auth',code:c.code,total:500001,accept:false},{name:'expired-jwt',code:c.code,total:500001,accept:false});
  48 |  for(const v of cases){
  49 |   await shop.prepare(v.total);
  50 |   if(v.name==='missing-auth'){await page.getByRole('button',{name:'Thoát',exact:true}).click();await expect(page.getByRole('link',{name:'Đăng nhập',exact:true})).toBeVisible();}
  51 |   if(v.name==='expired-jwt'){
  52 |    shop.ui.events.fixtures.push({mode:'Expired JWT transport fixture',exp:1,scope:'Only outgoing apply-coupon Authorization header replaced; real backend response retained'});
  53 |    await page.route('**/api/apply-coupon',r=>r.continue({headers:{...r.request().headers(),authorization:`Bearer ${shop.expired}`}}));
  54 |   }
  55 |   const result=await shop.ui.apply(v.code);const accepted=result.status===200;
  56 |   await capture(info,page,`eligibility-${v.name}`,{case:v,result,transportFixture:v.name==='expired-jwt'?'signed expired JWT exp=1':null},accepted!==v.accept);
> 57 |   expect.soft(accepted,v.name).toBe(v.accept);
     |                                ^ Error: expired-jwt
  58 |   if(!accepted){await expect.soft(shop.ui.error).toBeVisible();await expect.soft(shop.ui.saving).toHaveCount(0);}
  59 |   else if(v.accept)await expect.soft(shop.ui.saving).toBeVisible();
  60 |   await page.unroute('**/api/apply-coupon');
  61 |  }
  62 | });
  63 | test('GUI-B-007: pending state prevents duplicate apply',async({shop,page})=>{
  64 |  await shop.prepare(500001);const c=await shop.seedCoupon();let release;const gate=new Promise(resolve=>release=resolve);let intercepted=0;
  65 |  await page.route('**/api/apply-coupon',async route=>{intercepted++;const actual=await route.fetch();await gate;await route.fulfill({response:actual});});
  66 |  shop.ui.events.fixtures.push({mode:'Hold real backend response until pending UI has been checked',fabricatedResponse:false});
  67 |  try{
  68 |   await shop.ui.code.fill(c.code);await shop.ui.applyButton.click();await expect(shop.ui.applyButton).toBeDisabled();await expect(shop.ui.applyButton).toHaveText('...');
  69 |   await shop.ui.applyButton.click({force:true});await expect.poll(()=>intercepted).toBe(1);
  70 |  }finally{release();}
  71 |  await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.applyButton).toBeEnabled();
  72 | });
  73 | test('GUI-B-008: recover after bad code and transport failure',async({shop,page})=>{
  74 |  await shop.prepare(500001);const c=await shop.seedCoupon();await shop.ui.apply(`NONE_${process.env.GUI_RUN_ID}`);await expect(shop.ui.error).toBeVisible();
  75 |  await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.error).toHaveCount(0);
  76 |  await page.route('**/api/apply-coupon',r=>r.abort('failed'));shop.ui.events.fixtures.push({mode:'Transport abort for apply-coupon recovery'});
  77 |  await shop.ui.code.fill(c.code);const failed=page.waitForEvent('requestfailed',{predicate:r=>r.url().endsWith('/api/apply-coupon')});await shop.ui.applyButton.click();await failed;
  78 |  await expect(shop.ui.error).toBeVisible();await page.unroute('**/api/apply-coupon');
  79 |  await shop.ui.apply(c.code);await expect(shop.ui.saving).toBeVisible();await expect(shop.ui.error).toHaveCount(0);await expect(shop.ui.applyButton).toBeEnabled();
  80 | });
  81 | 
```