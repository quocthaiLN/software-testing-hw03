# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: coupons.spec.mjs >> GUI-C-028: network load error is visible and recoverable
- Location: tools/gui/tests/coupons.spec.mjs:172:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByText(/lỗi.*tải|không thể.*tải|thử lại/i)
Expected: visible
Timeout: 3000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 3000ms
  - waiting for getByText(/lỗi.*tải|không thể.*tải|thử lại/i)

```

```yaml
- heading "EShop Admin" [level=1]
- list:
  - listitem: Dashboard
  - listitem: Danh mục
  - listitem: Sản phẩm
  - listitem: Mã Giảm Giá
  - listitem: Đơn hàng
  - listitem: Người dùng
  - listitem: Đăng xuất
- heading "Quản lý Mã Giảm Giá" [level=2]
- heading "Tạo mã giảm giá mới" [level=3]
- 'textbox "Mã coupon (VD: SAVE10)"'
- combobox:
  - option "Phần trăm (%)" [selected]
  - option "Số tiền cố định (₫)"
- 'spinbutton "Giá trị % (VD: 10)"'
- spinbutton "Đơn tối thiểu (₫)": "0"
- textbox:
  - /placeholder: Ngày hết hạn
- spinbutton "Số lần dùng tối đa/người": "1"
- button "Tạo mã"
- table:
  - rowgroup:
    - row "Mã Loại Giá trị Đơn tối thiểu Hết hạn Giới hạn/người Hành động":
      - columnheader "Mã"
      - columnheader "Loại"
      - columnheader "Giá trị"
      - columnheader "Đơn tối thiểu"
      - columnheader "Hết hạn"
      - columnheader "Giới hạn/người"
      - columnheader "Hành động"
  - rowgroup
```

# Test source

```ts
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
  157 |  expect(canConfirm||undoOffered,'confirm/cancel or undo offered').toBe(true);
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
> 176 |  await expect(page.getByText(/lỗi.*tải|không thể.*tải|thử lại/i)).toBeVisible();
      |                                                                   ^ Error: expect(locator).toBeVisible() failed
  177 |  await page.unroute('**/api/coupons');await admin.goto();await expect(page.getByRole('table')).toBeVisible();
  178 | });
  179 | 
```