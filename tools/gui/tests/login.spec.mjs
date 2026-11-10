import {test,expect} from '../fixtures/index.mjs';
import {demo,invalidInputs} from '../test-data/users.mjs';

test.afterEach(async({page,browser},info)=>{
  const observation={
    itemId:info.title.match(/GUI-A-\d{3}/)?.[0],
    observedAt:new Date().toISOString(),
    browser:await browser.version(),os:process.platform,
    viewport:page.viewportSize(),url:page.url(),
    visibleText:await page.locator('body').innerText(),
    // The text is raw observation, not a student-written bug description.
    inputs:await page.locator('form input').evaluateAll(els=>els.map(e=>({type:e.type,required:e.required,valid:e.validity.valid,focused:e===document.activeElement}))),
  };
  await info.attach('observed-ui',{body:JSON.stringify(observation,null,2),contentType:'application/json'});
});

test('GUI-A-001: title describes login',async({page,login})=>{
  await expect(page.getByRole('heading').first()).toHaveText(/đăng nhập/i);
});
test('GUI-A-002: exactly one h1',async({page,login})=>{
  await expect(page.getByRole('heading',{level:1})).toHaveCount(1);
});
test('GUI-A-003: Vietnamese form labels',async({page,login})=>{
  await expect(page.locator('form')).toContainText('Email');
  await expect(login.submit).toHaveText(/đăng nhập/i);
});
test('GUI-A-004: positive action blue',async({login})=>{
  const color=await login.submit.evaluate(e=>getComputedStyle(e).backgroundColor);
  const rgb=color.match(/\d+/g).map(Number);
  expect(rgb[2]>rgb[0]&&rgb[2]>rgb[1]).toBe(true);
});
test('GUI-A-005: email input type and invalid format',async({login,page})=>{
  await expect(login.email).toHaveAttribute('type','email');
  await login.fill('not-an-email',demo.password);
  await login.submit.click();
  await expect(page.locator('form input:invalid')).toHaveCount(1);
  await expect(page).toHaveURL(/\/login$/);
});
test('GUI-A-006: password masked',async({login})=>{
  await login.password.fill(demo.password);
  await expect(login.password).toHaveAttribute('type','password');
});
test('GUI-A-007: required field markers',async({page,login})=>{
  await expect(page.locator('form label').nth(0)).toContainText('*');
  await expect(page.locator('form label').nth(1)).toContainText('*');
});
test('GUI-A-008: blank required fields rejected',async({page,login},info)=>{
  for(const v of invalidInputs){
    await test.step(v.name,async()=>{
      await login.fill(v.email,v.password);await login.submit.click();
      await expect(page).toHaveURL(/\/login$/);
      await expect(page.locator('form input:invalid')).toHaveCount(v.invalid);
    });
  }
});
test('GUI-A-009: replace and edit field values',async({login,page})=>{
  await login.fill('first@example.test','First123!');
  await page.context().grantPermissions(['clipboard-read','clipboard-write'],{origin:'http://localhost:5173'});
  await login.email.press('ControlOrMeta+A');await login.email.press('Backspace');
  await page.evaluate(()=>navigator.clipboard.writeText('second@example.test'));
  await login.email.press('ControlOrMeta+V');
  await login.password.press('ControlOrMeta+A');await login.password.press('Backspace');
  await page.evaluate(value=>navigator.clipboard.writeText(value),demo.password);
  await login.password.press('ControlOrMeta+V');
  await expect(login.email).toHaveValue('second@example.test');
  await expect(login.password).toHaveValue(demo.password);
});
test('GUI-A-010: natural top-down tab order',async({page,login})=>{
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link',{name:'EShop',exact:true})).toBeFocused();
  await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Giỏ hàng',exact:true})).toBeFocused();
  await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Đăng nhập',exact:true})).toBeFocused();
  await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Đăng ký',exact:true})).toBeFocused();
  await page.keyboard.press('Tab');await expect(login.email).toBeFocused();
  await page.keyboard.press('Tab');await expect(login.password).toBeFocused();
});
test('GUI-A-011: support links navigate by mouse and keyboard',async({page,login})=>{
  for(const method of ['click','enter']){
    await login.goto();
    const forgot=page.getByRole('link',{name:'Quên mật khẩu?'});
    if(method==='click')await forgot.click();else await forgot.press('Enter');
    await expect(page).toHaveURL(/\/forgot-password$/);
    await login.goto();
    const register=page.getByRole('link',{name:'Đăng ký ngay'});
    if(method==='click')await register.click();else await register.press('Enter');
    await expect(page).toHaveURL(/\/register$/);
  }
});
test('GUI-A-012: successful login by click and enter',async({page,login,makeUser})=>{
  for(const method of ['click','enter']){
    await page.evaluate(()=>localStorage.clear());await login.goto();
    const user=await makeUser();await login.login(user.email,user.password,method);
    await expect(page).toHaveURL('http://localhost:5173/');
    await expect(page.getByRole('link',{name:/Chào,/})).toBeVisible();
  }
});
test('GUI-A-013: safe generic authentication error',async({login,makeUser})=>{
  const user=await makeUser();await login.login(user.email,demo.wrong);
  await expect(login.error).toBeVisible();const existing=await login.error.innerText();
  await login.login(`absent-${process.env.GUI_RUN_ID}@example.test`,demo.wrong);
  await expect(login.error).toHaveText(existing);
});
test('GUI-A-014: error above submit',async({login,makeUser})=>{
  const user=await makeUser();await login.login(user.email,demo.wrong);
  await expect(login.error).toBeVisible();
  const error=await login.error.boundingBox();const button=await login.submit.boundingBox();
  expect(error.y+error.height).toBeLessThanOrEqual(button.y);
});
test('GUI-A-015: lock threshold at three consecutive failures',async({page,login,makeUser},info)=>{
  const observations=[];
  for(const count of [1,2,3]){
    await page.evaluate(()=>localStorage.clear());await login.goto();
    const user=await makeUser();
    for(let i=0;i<count;i++)await login.login(user.email,demo.wrong);
    const response=await login.login(user.email,user.password);
    observations.push({wrongAttempts:count,correctLoginStatus:response.status(),observedAt:new Date().toISOString()});
    if(count<3)await expect.soft(page,`after ${count} wrong attempts`).toHaveURL('http://localhost:5173/');
    else await expect.soft(page).toHaveURL(/\/login$/);
  }
  await info.attach('threshold-observations',{body:JSON.stringify(observations,null,2),contentType:'application/json'});
});
test('GUI-A-016: login recovers after 30-second lock',async({page,login,makeUser},info)=>{
  const user=await makeUser();
  for(let i=0;i<3;i++)await login.login(user.email,demo.wrong);
  const started=Date.now();
  const before=await login.login(user.email,user.password);
  await expect(login.error).toBeVisible();
  // Poll the specified elapsed-time condition, not a fixed Playwright sleep.
  await expect.poll(()=>Date.now()-started,{timeout:35000,intervals:[1000]}).toBeGreaterThanOrEqual(31000);
  const after=await login.login(user.email,user.password);
  await info.attach('lock-duration-observations',{body:JSON.stringify({
    firstCheckAt:new Date(started).toISOString(),elapsedMs:Date.now()-started,
    beforeStatus:before.status(),afterStatus:after.status(),
  },null,2),contentType:'application/json'});
  await expect(page).toHaveURL('http://localhost:5173/');
});
