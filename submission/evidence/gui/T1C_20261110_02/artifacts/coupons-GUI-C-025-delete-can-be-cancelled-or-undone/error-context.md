# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: coupons.spec.mjs >> GUI-C-025: delete can be cancelled or undone
- Location: tools/gui/tests/coupons.spec.mjs:145:1

# Error details

```
Error: confirm/cancel or undo offered

expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false
```

# Page snapshot

```yaml
- generic [ref=f1e3]:
  - generic [ref=f1e4]:
    - heading "EShop Admin" [level=1] [ref=f1e5]
    - list [ref=f1e6]:
      - listitem [ref=f1e7] [cursor=pointer]: Dashboard
      - listitem [ref=f1e8] [cursor=pointer]: Danh mục
      - listitem [ref=f1e9] [cursor=pointer]: Sản phẩm
      - listitem [ref=f1e10] [cursor=pointer]: Mã Giảm Giá
      - listitem [ref=f1e11] [cursor=pointer]: Đơn hàng
      - listitem [ref=f1e12] [cursor=pointer]: Người dùng
      - listitem [ref=f1e13] [cursor=pointer]: Đăng xuất
  - generic [ref=f1e15]:
    - heading "Quản lý Mã Giảm Giá" [level=2] [ref=f1e16]
    - generic [ref=f1e17]:
      - heading "Tạo mã giảm giá mới" [level=3] [ref=f1e18]
      - generic [ref=f1e19]:
        - 'textbox "Mã coupon (VD: SAVE10)" [ref=f1e20]'
        - combobox [ref=f1e21]:
          - option "Phần trăm (%)" [selected]
          - option "Số tiền cố định (₫)"
        - 'spinbutton "Giá trị % (VD: 10)" [ref=f1e22]'
        - spinbutton "Đơn tối thiểu (₫)" [ref=f1e23]: "0"
        - textbox [ref=f1e24]:
          - /placeholder: Ngày hết hạn
        - spinbutton "Số lần dùng tối đa/người" [ref=f1e25]: "1"
      - button "Tạo mã" [ref=f1e26] [cursor=pointer]
    - table [ref=f1e27]:
      - rowgroup [ref=f1e28]:
        - row [ref=f1e29]:
          - columnheader "Mã" [ref=f1e30]
          - columnheader "Loại" [ref=f1e31]
          - columnheader "Giá trị" [ref=f1e32]
          - columnheader "Đơn tối thiểu" [ref=f1e33]
          - columnheader "Hết hạn" [ref=f1e34]
          - columnheader "Giới hạn/người" [ref=f1e35]
          - columnheader "Hành động" [ref=f1e36]
      - rowgroup [ref=f1e37]:
        - row [ref=f1e38]:
          - cell "SAVE10" [ref=f1e39]
          - cell "Phần trăm" [ref=f1e40]
          - cell "10%" [ref=f1e41]
          - cell "300,000 ₫" [ref=f1e42]
          - cell "2099-12-31" [ref=f1e43]
          - cell "1 lần" [ref=f1e44]
          - cell [ref=f1e45]:
            - button "Xóa" [ref=f1e46] [cursor=pointer]
        - row [ref=f1e47]:
          - cell "BIGBUY" [ref=f1e48]
          - cell "Cố định" [ref=f1e49]
          - cell "50,000 ₫" [ref=f1e50]
          - cell "500,000 ₫" [ref=f1e51]
          - cell "2099-12-31" [ref=f1e52]
          - cell "1 lần" [ref=f1e53]
          - cell [ref=f1e54]:
            - button "Xóa" [ref=f1e55] [cursor=pointer]
        - row [ref=f1e56]:
          - cell "VIP100" [ref=f1e57]
          - cell "Cố định" [ref=f1e58]
          - cell "100,000 ₫" [ref=f1e59]
          - cell "300,000 ₫" [ref=f1e60]
          - cell "2099-12-31" [ref=f1e61]
          - cell "2 lần" [ref=f1e62]
          - cell [ref=f1e63]:
            - button "Xóa" [ref=f1e64] [cursor=pointer]
        - row [ref=f1e65]:
          - cell "EXPIRED" [ref=f1e66]
          - cell "Phần trăm" [ref=f1e67]
          - cell "20%" [ref=f1e68]
          - cell "100,000 ₫" [ref=f1e69]
          - cell "Hết hạn" [ref=f1e70]
          - cell "1 lần" [ref=f1e71]
          - cell [ref=f1e72]:
            - button "Xóa" [ref=f1e73] [cursor=pointer]
        - row [ref=f1e74]:
          - cell "T1_T1C_20261110_02_C3CCC90C_0" [ref=f1e75]
          - cell "Phần trăm" [ref=f1e76]
          - cell "10%" [ref=f1e77]
          - cell "300,000 ₫" [ref=f1e78]
          - cell "2099-12-31" [ref=f1e79]
          - cell "1 lần" [ref=f1e80]
          - cell [ref=f1e81]:
            - button "Xóa" [ref=f1e82] [cursor=pointer]
        - row [ref=f1e83]:
          - cell "T1_T1C_20261110_02_C3CCC90C_1" [ref=f1e84]
          - cell "Cố định" [ref=f1e85]
          - cell "50,000 ₫" [ref=f1e86]
          - cell "500,000 ₫" [ref=f1e87]
          - cell "2099-12-31" [ref=f1e88]
          - cell "1 lần" [ref=f1e89]
          - cell [ref=f1e90]:
            - button "Xóa" [ref=f1e91] [cursor=pointer]
        - row [ref=f1e92]:
          - cell "T1_T1C_20261110_02_A02CA8AF_0" [ref=f1e93]
          - cell "Phần trăm" [ref=f1e94]
          - cell "10%" [ref=f1e95]
          - cell "123,000 ₫" [ref=f1e96]
          - cell "2099-12-31" [ref=f1e97]
          - cell "2 lần" [ref=f1e98]
          - cell [ref=f1e99]:
            - button "Xóa" [ref=f1e100] [cursor=pointer]
        - row [ref=f1e101]:
          - cell [ref=f1e102]
          - cell "Phần trăm" [ref=f1e103]
          - cell "10%" [ref=f1e104]
          - cell "0 ₫" [ref=f1e105]
          - cell "2099-12-31" [ref=f1e106]
          - cell "1 lần" [ref=f1e107]
          - cell [ref=f1e108]:
            - button "Xóa" [ref=f1e109] [cursor=pointer]
        - row [ref=f1e110]:
          - cell "T1_T1C_20261110_02_098BFA10_0" [ref=f1e111]
          - cell "Phần trăm" [ref=f1e112]
          - cell "10%" [ref=f1e113]
          - cell "0 ₫" [ref=f1e114]
          - cell "2099-12-31" [ref=f1e115]
          - cell "1 lần" [ref=f1e116]
          - cell [ref=f1e117]:
            - button "Xóa" [ref=f1e118] [cursor=pointer]
        - row [ref=f1e119]:
          - cell "T1_T1C_20261110_02_22873FFD_0" [ref=f1e120]
          - cell "Phần trăm" [ref=f1e121]
          - cell "-1%" [ref=f1e122]
          - cell "0 ₫" [ref=f1e123]
          - cell "2099-12-31" [ref=f1e124]
          - cell "1 lần" [ref=f1e125]
          - cell [ref=f1e126]:
            - button "Xóa" [ref=f1e127] [cursor=pointer]
        - row [ref=f1e128]:
          - cell "T1_T1C_20261110_02_22873FFD_1" [ref=f1e129]
          - cell "Phần trăm" [ref=f1e130]
          - cell "0%" [ref=f1e131]
          - cell "0 ₫" [ref=f1e132]
          - cell "2099-12-31" [ref=f1e133]
          - cell "1 lần" [ref=f1e134]
          - cell [ref=f1e135]:
            - button "Xóa" [ref=f1e136] [cursor=pointer]
        - row [ref=f1e137]:
          - cell "T1_T1C_20261110_02_22873FFD_2" [ref=f1e138]
          - cell "Phần trăm" [ref=f1e139]
          - cell "1%" [ref=f1e140]
          - cell "0 ₫" [ref=f1e141]
          - cell "2099-12-31" [ref=f1e142]
          - cell "1 lần" [ref=f1e143]
          - cell [ref=f1e144]:
            - button "Xóa" [ref=f1e145] [cursor=pointer]
        - row [ref=f1e146]:
          - cell "T1_T1C_20261110_02_22873FFD_3" [ref=f1e147]
          - cell "Cố định" [ref=f1e148]
          - cell "-1 ₫" [ref=f1e149]
          - cell "0 ₫" [ref=f1e150]
          - cell "2099-12-31" [ref=f1e151]
          - cell "1 lần" [ref=f1e152]
          - cell [ref=f1e153]:
            - button "Xóa" [ref=f1e154] [cursor=pointer]
        - row [ref=f1e155]:
          - cell "T1_T1C_20261110_02_22873FFD_4" [ref=f1e156]
          - cell "Cố định" [ref=f1e157]
          - cell "0 ₫" [ref=f1e158]
          - cell "0 ₫" [ref=f1e159]
          - cell "2099-12-31" [ref=f1e160]
          - cell "1 lần" [ref=f1e161]
          - cell [ref=f1e162]:
            - button "Xóa" [ref=f1e163] [cursor=pointer]
        - row [ref=f1e164]:
          - cell "T1_T1C_20261110_02_22873FFD_5" [ref=f1e165]
          - cell "Cố định" [ref=f1e166]
          - cell "1 ₫" [ref=f1e167]
          - cell "0 ₫" [ref=f1e168]
          - cell "2099-12-31" [ref=f1e169]
          - cell "1 lần" [ref=f1e170]
          - cell [ref=f1e171]:
            - button "Xóa" [ref=f1e172] [cursor=pointer]
        - row [ref=f1e173]:
          - cell "T1_T1C_20261110_02_019F2B15_0" [ref=f1e174]
          - cell "Phần trăm" [ref=f1e175]
          - cell "10%" [ref=f1e176]
          - cell "-1 ₫" [ref=f1e177]
          - cell "2099-12-31" [ref=f1e178]
          - cell "1 lần" [ref=f1e179]
          - cell [ref=f1e180]:
            - button "Xóa" [ref=f1e181] [cursor=pointer]
        - row [ref=f1e182]:
          - cell "T1_T1C_20261110_02_019F2B15_1" [ref=f1e183]
          - cell "Phần trăm" [ref=f1e184]
          - cell "10%" [ref=f1e185]
          - cell "0 ₫" [ref=f1e186]
          - cell "2099-12-31" [ref=f1e187]
          - cell "1 lần" [ref=f1e188]
          - cell [ref=f1e189]:
            - button "Xóa" [ref=f1e190] [cursor=pointer]
        - row [ref=f1e191]:
          - cell "T1_T1C_20261110_02_019F2B15_2" [ref=f1e192]
          - cell "Phần trăm" [ref=f1e193]
          - cell "10%" [ref=f1e194]
          - cell "1 ₫" [ref=f1e195]
          - cell "2099-12-31" [ref=f1e196]
          - cell "1 lần" [ref=f1e197]
          - cell [ref=f1e198]:
            - button "Xóa" [ref=f1e199] [cursor=pointer]
        - row [ref=f1e200]:
          - cell "T1_T1C_20261110_02_94682DFC_1" [ref=f1e201]
          - cell "Phần trăm" [ref=f1e202]
          - cell "10%" [ref=f1e203]
          - cell "0 ₫" [ref=f1e204]
          - cell "2099-12-31" [ref=f1e205]
          - cell "1 lần" [ref=f1e206]
          - cell [ref=f1e207]:
            - button "Xóa" [ref=f1e208] [cursor=pointer]
        - row [ref=f1e209]:
          - cell "T1_T1C_20261110_02_94682DFC_2" [ref=f1e210]
          - cell "Phần trăm" [ref=f1e211]
          - cell "10%" [ref=f1e212]
          - cell "0 ₫" [ref=f1e213]
          - cell "2099-12-31" [ref=f1e214]
          - cell "2 lần" [ref=f1e215]
          - cell [ref=f1e216]:
            - button "Xóa" [ref=f1e217] [cursor=pointer]
        - row [ref=f1e218]:
          - cell "T1_T1C_20261110_02_50195D20_1" [ref=f1e219]
          - cell "Phần trăm" [ref=f1e220]
          - cell "10%" [ref=f1e221]
          - cell "₫" [ref=f1e222]
          - cell "2099-12-31" [ref=f1e223]
          - cell "1 lần" [ref=f1e224]
          - cell [ref=f1e225]:
            - button "Xóa" [ref=f1e226] [cursor=pointer]
        - row [ref=f1e227]:
          - cell "T1_T1C_20261110_02_50195D20_3" [ref=f1e228]
          - cell "Phần trăm" [ref=f1e229]
          - cell "10%" [ref=f1e230]
          - cell "0 ₫" [ref=f1e231]
          - cell "2099-12-31" [ref=f1e232]
          - cell "1 lần" [ref=f1e233]
          - cell [ref=f1e234]:
            - button "Xóa" [ref=f1e235] [cursor=pointer]
        - row [ref=f1e236]:
          - cell "T1_T1C_20261110_02_753A5AB7_0" [ref=f1e237]
          - cell "Phần trăm" [ref=f1e238]
          - cell "10%" [ref=f1e239]
          - cell "0 ₫" [ref=f1e240]
          - cell "2099-12-31" [ref=f1e241]
          - cell "1 lần" [ref=f1e242]
          - cell [ref=f1e243]:
            - button "Xóa" [ref=f1e244] [cursor=pointer]
        - row [ref=f1e245]:
          - cell "T1_T1C_20261110_02_753A5AB7_1" [ref=f1e246]
          - cell "Phần trăm" [ref=f1e247]
          - cell "10%" [ref=f1e248]
          - cell "0 ₫" [ref=f1e249]
          - cell "2099-12-31" [ref=f1e250]
          - cell "1 lần" [ref=f1e251]
          - cell [ref=f1e252]:
            - button "Xóa" [ref=f1e253] [cursor=pointer]
        - row [ref=f1e254]:
          - cell "T1_T1C_20261110_02_2D1045AB_0" [ref=f1e255]
          - cell "Phần trăm" [ref=f1e256]
          - cell "10%" [ref=f1e257]
          - cell "0 ₫" [ref=f1e258]
          - cell "2099-12-31" [ref=f1e259]
          - cell "1 lần" [ref=f1e260]
          - cell [ref=f1e261]:
            - button "Xóa" [ref=f1e262] [cursor=pointer]
        - row [ref=f1e263]:
          - cell "T1_T1C_20261110_02_2D1045AB_1" [ref=f1e264]
          - cell "Cố định" [ref=f1e265]
          - cell "10 ₫" [ref=f1e266]
          - cell "0 ₫" [ref=f1e267]
          - cell "2099-12-31" [ref=f1e268]
          - cell "1 lần" [ref=f1e269]
          - cell [ref=f1e270]:
            - button "Xóa" [ref=f1e271] [cursor=pointer]
        - row [ref=f1e272]:
          - cell "T1_T1C_20261110_02_706320A9_0" [ref=f1e273]
          - cell "Phần trăm" [ref=f1e274]
          - cell "10%" [ref=f1e275]
          - cell "0 ₫" [ref=f1e276]
          - cell "2099-12-31" [ref=f1e277]
          - cell "1 lần" [ref=f1e278]
          - cell [ref=f1e279]:
            - button "Xóa" [ref=f1e280] [cursor=pointer]
```

# Test source

```ts
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
  134 |  const after=await adminApi.list();expect(after).toEqual(before);await expect(admin.row(data.code)).toHaveCount(0);
  135 | });
  136 | test('GUI-C-023: successful create persists on reload',async({admin,adminApi})=>{
  137 |  for(const type of ['percent','fixed']){const r=await create(admin,adminApi,{type});expect(r.status).toBe(200);await admin.goto();await expect(admin.row(r.data.code)).toBeVisible();}
  138 | });
  139 | test('GUI-C-024: error understandable and above submit',async({admin,adminApi})=>{
  140 |  const duplicate=await adminApi.seed();await admin.goto();await admin.fill(duplicate);await admin.submit();
  141 |  const inline=admin.page.getByText(/mã.*tồn tại|trùng mã|không thể tạo/i).filter({visible:true});
  142 |  await expect(inline).toBeVisible();
  143 |  const error=await inline.boundingBox(),button=await admin.create.boundingBox();expect(error.bottom??error.y+error.height).toBeLessThanOrEqual(button.y);
  144 | });
  145 | test('GUI-C-025: delete can be cancelled or undone',async({admin,adminApi})=>{
  146 |  const c=await adminApi.seed();await admin.goto();await admin.row(c.code).getByRole('button',{name:'Xóa',exact:true}).click();
  147 |  const canConfirm=admin.events.dialogs.some(d=>d.type==='confirm');
  148 |  let undoOffered=false;
  149 |  if(!canConfirm){
  150 |   const undo=admin.page.getByRole('button',{name:/hoàn tác/i});undoOffered=(await undo.count())>0;
  151 |   if(undoOffered)await undo.click();
  152 |   else{
  153 |    await expect.poll(()=>admin.events.requests.some(r=>r.method==='DELETE'&&r.url.endsWith(`/${c.id}`))).toBe(true);
  154 |    await expect(admin.row(c.code)).toHaveCount(0);
  155 |   }
  156 |  }
> 157 |  expect(canConfirm||undoOffered,'confirm/cancel or undo offered').toBe(true);
      |                                                                   ^ Error: confirm/cancel or undo offered
  158 |  await expect(admin.row(c.code)).toBeVisible();
  159 | });
  160 | test('GUI-C-026: delete only target coupon and persist',async({admin,adminApi})=>{
  161 |  const a=await adminApi.seed(),b=await adminApi.seed();await admin.goto();admin.confirm='accept';
  162 |  await admin.row(a.code).getByRole('button',{name:'Xóa',exact:true}).click();await expect(admin.row(a.code)).toHaveCount(0);
  163 |  await admin.goto();await expect(admin.row(a.code)).toHaveCount(0);await expect(admin.row(b.code)).toBeVisible();
  164 |  const stored=(await adminApi.list()).find(c=>c.code===b.code);expect(stored.discount_value).toBe(b.discount_value);
  165 | });
  166 | test('GUI-C-027: empty-state UI using isolated empty API fixture',async({admin,page},info)=>{
  167 |  await page.route('**/api/coupons',r=>r.fulfill({status:200,contentType:'application/json',body:'[]'}));
  168 |  await admin.goto();await expect(page.getByRole('table').locator('tbody tr')).toHaveCount(0);
  169 |  await info.attach('fixture-mode',{body:JSON.stringify({mode:'Controlled API empty response; no backend data deleted',response:[]}),contentType:'application/json'});
  170 |  await expect(page.getByText(/chưa có mã|không có mã|danh sách.*trống/i)).toBeVisible();
  171 | });
  172 | test('GUI-C-028: network load error is visible and recoverable',async({admin,page},info)=>{
  173 |  await page.route('**/api/coupons',r=>r.abort('failed'));
  174 |  await info.attach('fixture-mode',{body:JSON.stringify({mode:'Transport fault injection: GET /api/coupons aborted; create/delete variants not reached if load assertion fails'}),contentType:'application/json'});
  175 |  await admin.goto();
  176 |  await expect(page.getByText(/lỗi.*tải|không thể.*tải|thử lại/i)).toBeVisible();
  177 |  await page.unroute('**/api/coupons');await admin.goto();await expect(page.getByRole('table')).toBeVisible();
  178 | });
  179 | 
```