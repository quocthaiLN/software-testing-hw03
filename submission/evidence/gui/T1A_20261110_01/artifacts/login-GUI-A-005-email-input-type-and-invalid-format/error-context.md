# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: login.spec.mjs >> GUI-A-005: email input type and invalid format
- Location: tools/gui/tests/login.spec.mjs:32:1

# Error details

```
Error: expect(locator).toHaveAttribute(expected) failed

Locator:  locator('form input').first()
Expected: "email"
Received: "text"
Timeout:  3000ms

Call log:
  - Expect "toHaveAttribute" with timeout 3000ms
  - waiting for locator('form input').first()
    10 × locator resolved to <input value="" required="" type="text" class="w-full border p-2 rounded"/>
       - unexpected value "text"

```

```yaml
- textbox
```

# Test source

```ts
  1   | import {test,expect} from '../fixtures/index.mjs';
  2   | import {demo,invalidInputs} from '../test-data/users.mjs';
  3   | 
  4   | test.afterEach(async({page,browser},info)=>{
  5   |   const observation={
  6   |     itemId:info.title.match(/GUI-A-\d{3}/)?.[0],
  7   |     observedAt:new Date().toISOString(),
  8   |     browser:await browser.version(),os:process.platform,
  9   |     viewport:page.viewportSize(),url:page.url(),
  10  |     visibleText:await page.locator('body').innerText(),
  11  |     // The text is raw observation, not a student-written bug description.
  12  |     inputs:await page.locator('form input').evaluateAll(els=>els.map(e=>({type:e.type,required:e.required,valid:e.validity.valid,focused:e===document.activeElement}))),
  13  |   };
  14  |   await info.attach('observed-ui',{body:JSON.stringify(observation,null,2),contentType:'application/json'});
  15  | });
  16  | 
  17  | test('GUI-A-001: title describes login',async({page,login})=>{
  18  |   await expect(page.getByRole('heading').first()).toHaveText(/đăng nhập/i);
  19  | });
  20  | test('GUI-A-002: exactly one h1',async({page,login})=>{
  21  |   await expect(page.getByRole('heading',{level:1})).toHaveCount(1);
  22  | });
  23  | test('GUI-A-003: Vietnamese form labels',async({page,login})=>{
  24  |   await expect(page.locator('form')).toContainText('Email');
  25  |   await expect(login.submit).toHaveText(/đăng nhập/i);
  26  | });
  27  | test('GUI-A-004: positive action blue',async({login})=>{
  28  |   const color=await login.submit.evaluate(e=>getComputedStyle(e).backgroundColor);
  29  |   const rgb=color.match(/\d+/g).map(Number);
  30  |   expect(rgb[2]>rgb[0]&&rgb[2]>rgb[1]).toBe(true);
  31  | });
  32  | test('GUI-A-005: email input type and invalid format',async({login,page})=>{
> 33  |   await expect(login.email).toHaveAttribute('type','email');
      |                             ^ Error: expect(locator).toHaveAttribute(expected) failed
  34  |   await login.fill('not-an-email',demo.password);
  35  |   await login.submit.click();
  36  |   await expect(page.locator('form input:invalid')).toHaveCount(1);
  37  |   await expect(page).toHaveURL(/\/login$/);
  38  | });
  39  | test('GUI-A-006: password masked',async({login})=>{
  40  |   await login.password.fill(demo.password);
  41  |   await expect(login.password).toHaveAttribute('type','password');
  42  | });
  43  | test('GUI-A-007: required field markers',async({page,login})=>{
  44  |   await expect(page.locator('form label').nth(0)).toContainText('*');
  45  |   await expect(page.locator('form label').nth(1)).toContainText('*');
  46  | });
  47  | test('GUI-A-008: blank required fields rejected',async({page,login},info)=>{
  48  |   for(const v of invalidInputs){
  49  |     await test.step(v.name,async()=>{
  50  |       await login.fill(v.email,v.password);await login.submit.click();
  51  |       await expect(page).toHaveURL(/\/login$/);
  52  |       await expect(page.locator('form input:invalid')).toHaveCount(v.invalid);
  53  |     });
  54  |   }
  55  | });
  56  | test('GUI-A-009: replace and edit field values',async({login,page})=>{
  57  |   await login.fill('first@example.test','First123!');
  58  |   await page.context().grantPermissions(['clipboard-read','clipboard-write'],{origin:'http://localhost:5173'});
  59  |   await login.email.press('ControlOrMeta+A');await login.email.press('Backspace');
  60  |   await page.evaluate(()=>navigator.clipboard.writeText('second@example.test'));
  61  |   await login.email.press('ControlOrMeta+V');
  62  |   await login.password.press('ControlOrMeta+A');await login.password.press('Backspace');
  63  |   await page.evaluate(value=>navigator.clipboard.writeText(value),demo.password);
  64  |   await login.password.press('ControlOrMeta+V');
  65  |   await expect(login.email).toHaveValue('second@example.test');
  66  |   await expect(login.password).toHaveValue(demo.password);
  67  | });
  68  | test('GUI-A-010: natural top-down tab order',async({page,login})=>{
  69  |   await page.keyboard.press('Tab');
  70  |   await expect(page.getByRole('link',{name:'EShop',exact:true})).toBeFocused();
  71  |   await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Giỏ hàng',exact:true})).toBeFocused();
  72  |   await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Đăng nhập',exact:true})).toBeFocused();
  73  |   await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Đăng ký',exact:true})).toBeFocused();
  74  |   await page.keyboard.press('Tab');await expect(login.email).toBeFocused();
  75  |   await page.keyboard.press('Tab');await expect(login.password).toBeFocused();
  76  | });
  77  | test('GUI-A-011: support links navigate by mouse and keyboard',async({page,login})=>{
  78  |   for(const method of ['click','enter']){
  79  |     await login.goto();
  80  |     const forgot=page.getByRole('link',{name:'Quên mật khẩu?'});
  81  |     if(method==='click')await forgot.click();else await forgot.press('Enter');
  82  |     await expect(page).toHaveURL(/\/forgot-password$/);
  83  |     await login.goto();
  84  |     const register=page.getByRole('link',{name:'Đăng ký ngay'});
  85  |     if(method==='click')await register.click();else await register.press('Enter');
  86  |     await expect(page).toHaveURL(/\/register$/);
  87  |   }
  88  | });
  89  | test('GUI-A-012: successful login by click and enter',async({page,login,makeUser})=>{
  90  |   for(const method of ['click','enter']){
  91  |     await page.evaluate(()=>localStorage.clear());await login.goto();
  92  |     const user=await makeUser();await login.login(user.email,user.password,method);
  93  |     await expect(page).toHaveURL('http://localhost:5173/');
  94  |     await expect(page.getByRole('link',{name:/Chào,/})).toBeVisible();
  95  |   }
  96  | });
  97  | test('GUI-A-013: safe generic authentication error',async({login,makeUser})=>{
  98  |   const user=await makeUser();await login.login(user.email,demo.wrong);
  99  |   await expect(login.error).toBeVisible();const existing=await login.error.innerText();
  100 |   await login.login(`absent-${process.env.GUI_RUN_ID}@example.test`,demo.wrong);
  101 |   await expect(login.error).toHaveText(existing);
  102 | });
  103 | test('GUI-A-014: error above submit',async({login,makeUser})=>{
  104 |   const user=await makeUser();await login.login(user.email,demo.wrong);
  105 |   await expect(login.error).toBeVisible();
  106 |   const error=await login.error.boundingBox();const button=await login.submit.boundingBox();
  107 |   expect(error.y+error.height).toBeLessThanOrEqual(button.y);
  108 | });
  109 | test('GUI-A-015: lock threshold at three consecutive failures',async({page,login,makeUser},info)=>{
  110 |   const observations=[];
  111 |   for(const count of [1,2,3]){
  112 |     await page.evaluate(()=>localStorage.clear());await login.goto();
  113 |     const user=await makeUser();
  114 |     for(let i=0;i<count;i++)await login.login(user.email,demo.wrong);
  115 |     const response=await login.login(user.email,user.password);
  116 |     observations.push({wrongAttempts:count,correctLoginStatus:response.status(),observedAt:new Date().toISOString()});
  117 |     if(count<3)await expect.soft(page,`after ${count} wrong attempts`).toHaveURL('http://localhost:5173/');
  118 |     else await expect.soft(page).toHaveURL(/\/login$/);
  119 |   }
  120 |   await info.attach('threshold-observations',{body:JSON.stringify(observations,null,2),contentType:'application/json'});
  121 | });
  122 | test('GUI-A-016: login recovers after 30-second lock',async({page,login,makeUser},info)=>{
  123 |   const user=await makeUser();
  124 |   for(let i=0;i<3;i++)await login.login(user.email,demo.wrong);
  125 |   const started=Date.now();
  126 |   const before=await login.login(user.email,user.password);
  127 |   await expect(login.error).toBeVisible();
  128 |   // Poll the specified elapsed-time condition, not a fixed Playwright sleep.
  129 |   await expect.poll(()=>Date.now()-started,{timeout:35000,intervals:[1000]}).toBeGreaterThanOrEqual(31000);
  130 |   const after=await login.login(user.email,user.password);
  131 |   await info.attach('lock-duration-observations',{body:JSON.stringify({
  132 |     firstCheckAt:new Date(started).toISOString(),elapsedMs:Date.now()-started,
  133 |     beforeStatus:before.status(),afterStatus:after.status(),
```