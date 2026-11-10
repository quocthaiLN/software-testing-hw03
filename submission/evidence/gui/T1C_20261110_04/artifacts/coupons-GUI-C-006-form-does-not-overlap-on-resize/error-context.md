# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: coupons.spec.mjs >> GUI-C-006: form does not overlap on resize
- Location: tools/gui/tests/coupons.spec.mjs:49:1

# Error details

```
Error: input cannot show even one glyph at viewport 390

expect(received).toEqual(expected) // deep equality

- Expected  -  1
+ Received  + 22

- Array []
+ Array [
+   Object {
+     "available": 0,
+     "firstGlyph": 8.896011352539062,
+     "placeholder": "Mã coupon (VD: SAVE10)",
+   },
+   Object {
+     "available": 0,
+     "firstGlyph": 9.152023315429688,
+     "placeholder": "Giá trị % (VD: 10)",
+   },
+   Object {
+     "available": 0,
+     "firstGlyph": 9.152023315429688,
+     "placeholder": "Đơn tối thiểu (₫)",
+   },
+   Object {
+     "available": 0,
+     "firstGlyph": 9.152023315429688,
+     "placeholder": "Số lần dùng tối đa/người",
+   },
+ ]
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
        - 'textbox "Mã coupon (VD: SAVE10)" [ref=e20]': T1
        - combobox [ref=e21]:
          - option "Phần trăm (%)" [selected]
          - option "Số tiền cố định (₫)"
        - 'spinbutton "Giá trị % (VD: 10)" [ref=e22]': "10"
        - spinbutton "Đơn tối thiểu (₫)" [ref=e23]: "0"
        - textbox [active] [ref=e24]:
          - /placeholder: Ngày hết hạn
          - text: 2099-12-31
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
        - row [ref=e74]:
          - cell "T1_T1C_20261110_02_C3CCC90C_0" [ref=e75]
          - cell "Phần trăm" [ref=e76]
          - cell "10%" [ref=e77]
          - cell "300,000 ₫" [ref=e78]
          - cell "2099-12-31" [ref=e79]
          - cell "1 lần" [ref=e80]
          - cell [ref=e81]:
            - button "Xóa" [ref=e82] [cursor=pointer]
        - row [ref=e83]:
          - cell "T1_T1C_20261110_02_C3CCC90C_1" [ref=e84]
          - cell "Cố định" [ref=e85]
          - cell "50,000 ₫" [ref=e86]
          - cell "500,000 ₫" [ref=e87]
          - cell "2099-12-31" [ref=e88]
          - cell "1 lần" [ref=e89]
          - cell [ref=e90]:
            - button "Xóa" [ref=e91] [cursor=pointer]
        - row [ref=e92]:
          - cell "T1_T1C_20261110_02_A02CA8AF_0" [ref=e93]
          - cell "Phần trăm" [ref=e94]
          - cell "10%" [ref=e95]
          - cell "123,000 ₫" [ref=e96]
          - cell "2099-12-31" [ref=e97]
          - cell "2 lần" [ref=e98]
          - cell [ref=e99]:
            - button "Xóa" [ref=e100] [cursor=pointer]
        - row [ref=e101]:
          - cell [ref=e102]
          - cell "Phần trăm" [ref=e103]
          - cell "10%" [ref=e104]
          - cell "0 ₫" [ref=e105]
          - cell "2099-12-31" [ref=e106]
          - cell "1 lần" [ref=e107]
          - cell [ref=e108]:
            - button "Xóa" [ref=e109] [cursor=pointer]
        - row [ref=e110]:
          - cell "T1_T1C_20261110_02_098BFA10_0" [ref=e111]
          - cell "Phần trăm" [ref=e112]
          - cell "10%" [ref=e113]
          - cell "0 ₫" [ref=e114]
          - cell "2099-12-31" [ref=e115]
          - cell "1 lần" [ref=e116]
          - cell [ref=e117]:
            - button "Xóa" [ref=e118] [cursor=pointer]
        - row [ref=e119]:
          - cell "T1_T1C_20261110_02_22873FFD_0" [ref=e120]
          - cell "Phần trăm" [ref=e121]
          - cell "-1%" [ref=e122]
          - cell "0 ₫" [ref=e123]
          - cell "2099-12-31" [ref=e124]
          - cell "1 lần" [ref=e125]
          - cell [ref=e126]:
            - button "Xóa" [ref=e127] [cursor=pointer]
        - row [ref=e128]:
          - cell "T1_T1C_20261110_02_22873FFD_1" [ref=e129]
          - cell "Phần trăm" [ref=e130]
          - cell "0%" [ref=e131]
          - cell "0 ₫" [ref=e132]
          - cell "2099-12-31" [ref=e133]
          - cell "1 lần" [ref=e134]
          - cell [ref=e135]:
            - button "Xóa" [ref=e136] [cursor=pointer]
        - row [ref=e137]:
          - cell "T1_T1C_20261110_02_22873FFD_2" [ref=e138]
          - cell "Phần trăm" [ref=e139]
          - cell "1%" [ref=e140]
          - cell "0 ₫" [ref=e141]
          - cell "2099-12-31" [ref=e142]
          - cell "1 lần" [ref=e143]
          - cell [ref=e144]:
            - button "Xóa" [ref=e145] [cursor=pointer]
        - row [ref=e146]:
          - cell "T1_T1C_20261110_02_22873FFD_3" [ref=e147]
          - cell "Cố định" [ref=e148]
          - cell "-1 ₫" [ref=e149]
          - cell "0 ₫" [ref=e150]
          - cell "2099-12-31" [ref=e151]
          - cell "1 lần" [ref=e152]
          - cell [ref=e153]:
            - button "Xóa" [ref=e154] [cursor=pointer]
        - row [ref=e155]:
          - cell "T1_T1C_20261110_02_22873FFD_4" [ref=e156]
          - cell "Cố định" [ref=e157]
          - cell "0 ₫" [ref=e158]
          - cell "0 ₫" [ref=e159]
          - cell "2099-12-31" [ref=e160]
          - cell "1 lần" [ref=e161]
          - cell [ref=e162]:
            - button "Xóa" [ref=e163] [cursor=pointer]
        - row [ref=e164]:
          - cell "T1_T1C_20261110_02_22873FFD_5" [ref=e165]
          - cell "Cố định" [ref=e166]
          - cell "1 ₫" [ref=e167]
          - cell "0 ₫" [ref=e168]
          - cell "2099-12-31" [ref=e169]
          - cell "1 lần" [ref=e170]
          - cell [ref=e171]:
            - button "Xóa" [ref=e172] [cursor=pointer]
        - row [ref=e173]:
          - cell "T1_T1C_20261110_02_019F2B15_0" [ref=e174]
          - cell "Phần trăm" [ref=e175]
          - cell "10%" [ref=e176]
          - cell "-1 ₫" [ref=e177]
          - cell "2099-12-31" [ref=e178]
          - cell "1 lần" [ref=e179]
          - cell [ref=e180]:
            - button "Xóa" [ref=e181] [cursor=pointer]
        - row [ref=e182]:
          - cell "T1_T1C_20261110_02_019F2B15_1" [ref=e183]
          - cell "Phần trăm" [ref=e184]
          - cell "10%" [ref=e185]
          - cell "0 ₫" [ref=e186]
          - cell "2099-12-31" [ref=e187]
          - cell "1 lần" [ref=e188]
          - cell [ref=e189]:
            - button "Xóa" [ref=e190] [cursor=pointer]
        - row [ref=e191]:
          - cell "T1_T1C_20261110_02_019F2B15_2" [ref=e192]
          - cell "Phần trăm" [ref=e193]
          - cell "10%" [ref=e194]
          - cell "1 ₫" [ref=e195]
          - cell "2099-12-31" [ref=e196]
          - cell "1 lần" [ref=e197]
          - cell [ref=e198]:
            - button "Xóa" [ref=e199] [cursor=pointer]
        - row [ref=e200]:
          - cell "T1_T1C_20261110_02_94682DFC_1" [ref=e201]
          - cell "Phần trăm" [ref=e202]
          - cell "10%" [ref=e203]
          - cell "0 ₫" [ref=e204]
          - cell "2099-12-31" [ref=e205]
          - cell "1 lần" [ref=e206]
          - cell [ref=e207]:
            - button "Xóa" [ref=e208] [cursor=pointer]
        - row [ref=e209]:
          - cell "T1_T1C_20261110_02_94682DFC_2" [ref=e210]
          - cell "Phần trăm" [ref=e211]
          - cell "10%" [ref=e212]
          - cell "0 ₫" [ref=e213]
          - cell "2099-12-31" [ref=e214]
          - cell "2 lần" [ref=e215]
          - cell [ref=e216]:
            - button "Xóa" [ref=e217] [cursor=pointer]
        - row [ref=e218]:
          - cell "T1_T1C_20261110_02_50195D20_1" [ref=e219]
          - cell "Phần trăm" [ref=e220]
          - cell "10%" [ref=e221]
          - cell "₫" [ref=e222]
          - cell "2099-12-31" [ref=e223]
          - cell "1 lần" [ref=e224]
          - cell [ref=e225]:
            - button "Xóa" [ref=e226] [cursor=pointer]
        - row [ref=e227]:
          - cell "T1_T1C_20261110_02_50195D20_3" [ref=e228]
          - cell "Phần trăm" [ref=e229]
          - cell "10%" [ref=e230]
          - cell "0 ₫" [ref=e231]
          - cell "2099-12-31" [ref=e232]
          - cell "1 lần" [ref=e233]
          - cell [ref=e234]:
            - button "Xóa" [ref=e235] [cursor=pointer]
        - row [ref=e236]:
          - cell "T1_T1C_20261110_02_753A5AB7_0" [ref=e237]
          - cell "Phần trăm" [ref=e238]
          - cell "10%" [ref=e239]
          - cell "0 ₫" [ref=e240]
          - cell "2099-12-31" [ref=e241]
          - cell "1 lần" [ref=e242]
          - cell [ref=e243]:
            - button "Xóa" [ref=e244] [cursor=pointer]
        - row [ref=e245]:
          - cell "T1_T1C_20261110_02_753A5AB7_1" [ref=e246]
          - cell "Phần trăm" [ref=e247]
          - cell "10%" [ref=e248]
          - cell "0 ₫" [ref=e249]
          - cell "2099-12-31" [ref=e250]
          - cell "1 lần" [ref=e251]
          - cell [ref=e252]:
            - button "Xóa" [ref=e253] [cursor=pointer]
        - row [ref=e254]:
          - cell "T1_T1C_20261110_02_2D1045AB_0" [ref=e255]
          - cell "Phần trăm" [ref=e256]
          - cell "10%" [ref=e257]
          - cell "0 ₫" [ref=e258]
          - cell "2099-12-31" [ref=e259]
          - cell "1 lần" [ref=e260]
          - cell [ref=e261]:
            - button "Xóa" [ref=e262] [cursor=pointer]
        - row [ref=e263]:
          - cell "T1_T1C_20261110_02_2D1045AB_1" [ref=e264]
          - cell "Cố định" [ref=e265]
          - cell "10 ₫" [ref=e266]
          - cell "0 ₫" [ref=e267]
          - cell "2099-12-31" [ref=e268]
          - cell "1 lần" [ref=e269]
          - cell [ref=e270]:
            - button "Xóa" [ref=e271] [cursor=pointer]
        - row [ref=e272]:
          - cell "T1_T1C_20261110_02_706320A9_0" [ref=e273]
          - cell "Phần trăm" [ref=e274]
          - cell "10%" [ref=e275]
          - cell "0 ₫" [ref=e276]
          - cell "2099-12-31" [ref=e277]
          - cell "1 lần" [ref=e278]
          - cell [ref=e279]:
            - button "Xóa" [ref=e280] [cursor=pointer]
        - row [ref=e281]:
          - cell "T1_T1C_20261110_02_BB99209C_1" [ref=e282]
          - cell "Phần trăm" [ref=e283]
          - cell "10%" [ref=e284]
          - cell "0 ₫" [ref=e285]
          - cell "2099-12-31" [ref=e286]
          - cell "1 lần" [ref=e287]
          - cell [ref=e288]:
            - button "Xóa" [ref=e289] [cursor=pointer]
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
  33  |  expect(rgb[2]>rgb[0]&&rgb[2]>rgb[1]).toBe(true);
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
  50  |  await admin.code.fill('T1');await admin.value.fill('10');await admin.expires.fill('2099-12-31');
  51  |  for(const width of [1280,390]){
  52  |   await page.setViewportSize({width,height:width===1280?800:844});
  53  |   const overlaps=await admin.form.locator('input,select').evaluateAll(es=>{
  54  |    const rs=es.map(e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,right:r.right,bottom:r.bottom};});
  55  |    return rs.flatMap((a,i)=>rs.slice(i+1).filter(b=>Math.min(a.right,b.right)-Math.max(a.x,b.x)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.y,b.y)>2).map(b=>({a,b})));
  56  |   });
  57  |   expect(overlaps,`overlap at viewport ${width}`).toEqual([]);
  58  |   await expect(admin.create).toBeVisible();
  59  |   const clipped=await admin.form.locator('input').evaluateAll(es=>es.filter(e=>e.type!=='date').map(e=>{
  60  |    const cs=getComputedStyle(e);const canvas=document.createElement('canvas');const ctx=canvas.getContext('2d');ctx.font=`${cs.fontSize} ${cs.fontFamily}`;
  61  |    const available=e.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
  62  |    const firstGlyph=ctx.measureText(e.value[0]||'0').width;
  63  |    return {placeholder:e.placeholder,available,firstGlyph};
  64  |   }).filter(x=>x.available<x.firstGlyph));
> 65  |   expect(clipped,`input cannot show even one glyph at viewport ${width}`).toEqual([]);
      |                                                                           ^ Error: input cannot show even one glyph at viewport 390
  66  |   // Temporary visual-QA capture, not a Passed screenshot attached to submission.
  67  |   await page.screenshot({path:`/tmp/hw03-admin-layout-${width}.png`});
  68  |  }
  69  | });
  70  | test('GUI-C-007: persistent labels and required markers',async({admin})=>{
  71  |  await expect(admin.form.locator('label')).toHaveCount(6);
  72  |  for(const label of await admin.form.locator('label').all())await expect(label).toContainText('*');
  73  | });
  74  | test('GUI-C-008: empty and whitespace code rejected',async({admin,adminApi},info)=>{
  75  |  await vector(admin,adminApi,info,'code','',false);
  76  |  await vector(admin,adminApi,info,'code','   ',false);
  77  | });
  78  | test('GUI-C-009: duplicate code rejected',async({admin,adminApi})=>{
  79  |  const c=await adminApi.seed();await admin.goto();await admin.fill(c);const reply=await admin.submit();
  80  |  expect(reply.status).toBeGreaterThanOrEqual(400);
  81  |  const rows=(await adminApi.list()).filter(x=>x.code===c.code);expect(rows).toHaveLength(1);
  82  |  await expect(admin.row(c.code)).toHaveCount(1);
  83  | });
  84  | test('GUI-C-010: type choices and keyboard selection',async({admin})=>{
  85  |  await expect(admin.type.getByRole('option')).toHaveText(['Phần trăm (%)','Số tiền cố định (₫)']);
  86  |  await admin.type.selectOption('percent');await admin.type.press('ArrowDown');await expect(admin.type).toHaveValue('fixed');
  87  |  await admin.type.press('Escape');await expect(admin.type).toHaveValue('fixed');
  88  | });
  89  | test('GUI-C-011: discount value boundaries',async({admin,adminApi},info)=>{
  90  |  for(const type of ['percent','fixed'])for(const value of [-1,0,1])await vector(admin,adminApi,info,'discount_value',value,value>0,{type});
  91  | });
  92  | test('GUI-C-012: minimum order boundaries',async({admin,adminApi},info)=>{
  93  |  for(const value of [-1,0,1])await vector(admin,adminApi,info,'min_order_amount',value,value>=0);
  94  | });
  95  | test('GUI-C-013: uses-per-user boundaries',async({admin,adminApi},info)=>{
  96  |  for(const value of [0,1,2])await vector(admin,adminApi,info,'max_uses_per_user',value,value>=1);
  97  | });
  98  | test('GUI-C-014: all mandatory fields reject empty values',async({admin,adminApi},info)=>{
  99  |  for(const field of ['discount_value','min_order_amount','expired_at','max_uses_per_user'])await vector(admin,adminApi,info,field,'',false);
  100 | });
  101 | test('GUI-C-015: leap date and invalid date picker values',async({admin},info)=>{
  102 |  await admin.expires.fill('2028-02-29');await expect(admin.expires).toHaveValue('2028-02-29');
  103 |  for(const invalid of ['2027-02-29','2026-04-31']){
  104 |   let nativeRejection='';
  105 |   try{await admin.expires.fill(invalid);}catch(e){if(!/Malformed value/.test(e.message))throw e;nativeRejection=e.message.split('\n')[0];}
  106 |   await expect(admin.expires).not.toHaveValue(invalid);
  107 |   await info.attach(`date-${invalid}`,{body:JSON.stringify({requested:invalid,value:await admin.expires.inputValue(),nativeRejection,scope:'Native date control rejection; not backend date validation'}),contentType:'application/json'});
  108 |  }
  109 | });
  110 | test('GUI-C-016: discount hint follows type',async({admin})=>{
  111 |  await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
  112 |  await admin.type.selectOption('fixed');await expect(admin.value).toHaveAttribute('placeholder',/Số tiền.*₫|Số tiền.*50000/);
  113 |  await admin.type.selectOption('percent');await expect(admin.value).toHaveAttribute('placeholder',/Giá trị %/);
  114 | });
  115 | test('GUI-C-017: form tab order',async({admin})=>{
  116 |  await admin.code.focus();
  117 |  for(const target of [admin.type,admin.value,admin.minimum,admin.expires]){await admin.page.keyboard.press('Tab');await expect(target).toBeFocused();}
  118 |  // The native date picker has multiple internal fields; leaving it may take several Tabs.
  119 |  let reached=false;
  120 |  for(let i=0;i<5;i++){await admin.page.keyboard.press('Tab');if(await admin.limit.evaluate(e=>e===document.activeElement)){reached=true;break;}}
  121 |  expect(reached).toBe(true);await admin.page.keyboard.press('Shift+Tab');await expect(admin.expires).toBeFocused();
  122 | });
  123 | test('GUI-C-018: create using Enter and click',async({admin,adminApi})=>{
  124 |  for(const method of ['enter','click']){const r=await create(admin,adminApi,{},method);expect(r.status).toBe(200);await expect(admin.row(r.data.code)).toHaveCount(1);}
  125 | });
  126 | test('GUI-C-019: coupons tab opens correct screen',async({admin})=>{
  127 |  await expect(admin.heading).toBeVisible();await expect(admin.create).toBeVisible();await expect(admin.page.getByRole('table')).toBeVisible();
  128 | });
  129 | test('GUI-C-020: active tab highlighted',async({admin})=>{
  130 |  await expect(admin.tab).toHaveClass(/text-blue-400/);
  131 |  await admin.page.getByText('Dashboard',{exact:true}).click();await expect(admin.tab).not.toHaveClass(/text-blue-400/);
  132 |  await admin.tab.click();await expect(admin.tab).toHaveClass(/text-blue-400/);
  133 | });
  134 | test('GUI-C-021: tab reachable by keyboard',async({admin,page})=>{
  135 |  await admin.page.getByText('Dashboard',{exact:true}).click();
  136 |  let reached=false;
  137 |  for(let i=0;i<18;i++){await page.keyboard.press('Tab');if(await admin.tab.evaluate(e=>e===document.activeElement)){reached=true;break;}}
  138 |  expect(reached,'Coupons nav must be keyboard focusable').toBe(true);
  139 |  await page.keyboard.press('Enter');await expect(admin.heading).toBeVisible();
  140 | });
  141 | test('GUI-C-022: navigating away does not mutate coupon data',async({admin,adminApi})=>{
  142 |  const before=await adminApi.list();const data=adminApi.fresh();await admin.fill(data);
  143 |  await admin.page.getByText('Dashboard',{exact:true}).click();await admin.tab.click();
  144 |  const after=await adminApi.list();expect(after).toEqual(before);await expect(admin.row(data.code)).toHaveCount(0);
  145 | });
  146 | test('GUI-C-023: successful create persists on reload',async({admin,adminApi})=>{
  147 |  for(const type of ['percent','fixed']){const r=await create(admin,adminApi,{type});expect(r.status).toBe(200);await admin.goto();await expect(admin.row(r.data.code)).toBeVisible();}
  148 | });
  149 | test('GUI-C-024: error understandable and above submit',async({admin,adminApi})=>{
  150 |  const duplicate=await adminApi.seed();await admin.goto();await admin.fill(duplicate);await admin.submit();
  151 |  const inline=admin.page.getByText(/mã.*tồn tại|trùng mã|không thể tạo/i).filter({visible:true});
  152 |  await expect(inline).toBeVisible();
  153 |  const error=await inline.boundingBox(),button=await admin.create.boundingBox();expect(error.bottom??error.y+error.height).toBeLessThanOrEqual(button.y);
  154 | });
  155 | test('GUI-C-025: delete can be cancelled or undone',async({admin,adminApi})=>{
  156 |  const c=await adminApi.seed();await admin.goto();await admin.row(c.code).getByRole('button',{name:'Xóa',exact:true}).click();
  157 |  const canConfirm=admin.events.dialogs.some(d=>d.type==='confirm');
  158 |  let undoOffered=false;
  159 |  if(!canConfirm){
  160 |   const undo=admin.page.getByRole('button',{name:/hoàn tác/i});undoOffered=(await undo.count())>0;
  161 |   if(undoOffered)await undo.click();
  162 |   else{
  163 |    await expect.poll(()=>admin.events.requests.some(r=>r.method==='DELETE'&&r.url.endsWith(`/${c.id}`))).toBe(true);
  164 |    await expect(admin.row(c.code)).toHaveCount(0);
  165 |   }
```