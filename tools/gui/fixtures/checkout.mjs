import {test as adminBase,expect} from './admin.mjs';
import {CheckoutPage} from '../pages/CheckoutPage.mjs';
import {api,demo} from '../test-data/users.mjs';
import {execFileSync} from 'node:child_process';
import {createHmac} from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export const test=adminBase.extend({
 shop:async({page,request,adminApi},use,info)=>{
  const suffix=info.testId.replace(/[^a-z0-9]/gi,'').slice(-10);
  const email=`t1b-${process.env.GUI_RUN_ID}-${suffix}@example.test`;
  await expect(await request.post(`${api}/register`,{data:{name:'HW03 Coupon UI',email,password:demo.password}})).toBeOK();
  const login=await request.post(`${api}/login`,{data:{email,password:demo.password}});await expect(login).toBeOK();
  const {user,token}=await login.json();let n=0;
  await page.addInitScript(token=>{if(location.origin==='http://localhost:5173')localStorage.setItem('token',token);},token);
  const ui=new CheckoutPage(page);
  const prepare=async total=>{
   const categories=await(await request.get(`${api}/categories`)).json();
   const product={name:`T1B_${process.env.GUI_RUN_ID}_${suffix}_${n++}`,price:total,description:'Disposable coupon-boundary fixture',imageUrl:'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="1" height="1"/>',category_id:categories[0].id};
   const res=await request.post(`${api}/products`,{data:product,headers:{Authorization:`Bearer ${adminApi.token}`}});await expect(res).toBeOK();
   const created={...product,...await res.json()};await ui.prepare(created);
   await expect(page).toHaveURL(/\/checkout$/);await expect(ui.total).toHaveValue(String(total));
   return created;
  };
  const seedCoupon=async(overrides={})=>adminApi.seed({type:'fixed',discount_value:50000,min_order_amount:0,max_uses_per_user:2,...overrides});
  const inactive=async()=>{
   const c=await seedCoupon();
   if(!c.code.startsWith('T1_'))throw new Error('Refuse changing a non-fixture coupon');
   const db=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../../../eshop-sut/backend/database.sqlite');
   execFileSync('python3',['-c','import sqlite3,sys; c=sqlite3.connect(sys.argv[1], timeout=5); q=c.execute("UPDATE coupons SET is_active=0 WHERE id=? AND code=?",(int(sys.argv[2]),sys.argv[3])); assert q.rowcount==1; c.commit()',db,String(c.id),c.code]);
   expect((await adminApi.list()).find(x=>x.id===c.id).is_active).toBe(0);return c;
  };
  const usage=async(coupon,count)=>{for(let i=0;i<count;i++)await expect(await request.post(`${api}/coupon-usage`,{data:{coupon_id:coupon.id},headers:{Authorization:`Bearer ${token}`}})).toBeOK();};
  // Public demo signing key from the supplied SUT, never a real service credential.
  const b64=x=>Buffer.from(JSON.stringify(x)).toString('base64url');
  const unsigned=`${b64({alg:'HS256',typ:'JWT'})}.${b64({id:user.id,role:'user',exp:1})}`;
  const expired=`${unsigned}.${createHmac('sha256','super_secret_key_that_should_not_be_here').update(unsigned).digest('base64url')}`;
  await use({ui,prepare,seedCoupon,inactive,usage,user,expired});
  await Promise.all(ui.pending);
  await info.attach('observed-ui',{body:JSON.stringify({itemId:info.title.match(/GUI-B-\d{3}/)?.[0],observedAt:new Date().toISOString(),url:page.url(),viewport:page.viewportSize(),browser:await page.context().browser().version(),visibleText:await page.locator('body').innerText(),events:ui.events},null,2),contentType:'application/json'});
 },
});
export {expect};
