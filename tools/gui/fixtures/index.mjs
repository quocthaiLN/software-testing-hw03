import {test as base,expect} from 'playwright/test';
import {LoginPage} from '../pages/LoginPage.mjs';
import {api,demo} from '../test-data/users.mjs';

export const test=base.extend({
  login:async({page},use)=>{const login=new LoginPage(page);await login.goto();await use(login);},
  makeUser:async({request},use,testInfo)=>{
    let n=0;
    await use(async()=>{
      const email=`t1-${process.env.GUI_RUN_ID}-${testInfo.testId.replace(/[^a-z0-9]/gi,'').slice(-12)}-${n++}@example.test`;
      const response=await request.post(`${api}/register`,{data:{...demo,email}});
      await expect(response).toBeOK();
      return {email,password:demo.password};
    });
  },
});
export {expect};
