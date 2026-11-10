import {test as base,expect} from 'playwright/test';
import {CouponsPage} from '../pages/CouponsPage.mjs';
import {api} from '../test-data/users.mjs';
export const test=base.extend({
  adminApi:async({request},use,info)=>{
    const login=await request.post(`${api}/login`,{data:{email:'admin@eshop.com',password:'Admin123!'}});
    await expect(login).toBeOK();const {token}=await login.json();let n=0;
    const fresh=(overrides={})=>({code:`T1_${process.env.GUI_RUN_ID}_${info.testId.replace(/[^a-z0-9]/gi,'').slice(-8)}_${n++}`.toUpperCase(),type:'percent',discount_value:10,min_order_amount:0,expired_at:'2099-12-31',max_uses_per_user:1,...overrides});
    await use({token,fresh,
      list:async()=>{const r=await request.get(`${api}/coupons`,{headers:{Authorization:`Bearer ${token}`}});await expect(r).toBeOK();return await r.json();},
      seed:async(overrides={})=>{const data=fresh(overrides);const r=await request.post(`${api}/admin/coupons`,{data,headers:{Authorization:`Bearer ${token}`}});await expect(r).toBeOK();return {...data,...await r.json()};},
    });
  },
  admin:async({page,adminApi},use,info)=>{
    await page.addInitScript(token=>{if(location.origin==='http://localhost:5174')localStorage.setItem('adminToken',token);},adminApi.token);
    const admin=new CouponsPage(page);await admin.goto();await expect(admin.heading).toBeVisible();
    await use(admin);
    await info.attach('observed-ui',{body:JSON.stringify({itemId:info.title.match(/GUI-C-\d{3}/)?.[0],observedAt:new Date().toISOString(),url:page.url(),viewport:page.viewportSize(),browser:await page.context().browser().version(),visibleText:await page.locator('body').innerText(),inputs:await page.locator('form input,form select').evaluateAll(es=>es.map(e=>({tag:e.tagName,type:e.type,placeholder:e.getAttribute('placeholder'),value:e.value,required:e.required,valid:e.validity.valid}))),events:admin.events},null,2),contentType:'application/json'});
  },
});
export {expect};
