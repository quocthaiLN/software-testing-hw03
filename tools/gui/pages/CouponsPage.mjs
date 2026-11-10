export class CouponsPage{
  constructor(page){
    this.page=page;this.events={dialogs:[],requests:[],faults:[]};this.confirm='dismiss';
    this.tab=page.getByText('Mã Giảm Giá',{exact:true});
    this.heading=page.getByRole('heading',{name:'Quản lý Mã Giảm Giá',exact:true});
    this.form=page.locator('form');
    this.code=page.getByPlaceholder('Mã coupon (VD: SAVE10)');
    this.type=page.getByRole('combobox');
    this.value=page.getByPlaceholder(/Giá trị % \(VD: 10\)|Số tiền \(VD: 50000\)/);
    this.minimum=page.getByPlaceholder('Đơn tối thiểu (₫)');
    this.expires=page.getByPlaceholder('Ngày hết hạn');
    this.limit=page.getByPlaceholder('Số lần dùng tối đa/người');
    this.create=page.getByRole('button',{name:'Tạo mã',exact:true});
    page.on('dialog',async d=>{
      this.events.dialogs.push({type:d.type(),message:d.message(),observedAt:new Date().toISOString()});
      if(d.type()==='confirm'&&this.confirm==='accept')await d.accept();else await d.dismiss();
    });
    page.on('response',r=>{
      if(/\/api\/(admin\/)?coupons/.test(r.url()))this.events.requests.push({method:r.request().method(),url:r.url(),status:r.status(),observedAt:new Date().toISOString()});
    });
    page.on('requestfailed',r=>this.events.faults.push({url:r.url(),error:r.failure()?.errorText,observedAt:new Date().toISOString()}));
  }
  async goto(){await this.page.goto('http://localhost:5174');await this.tab.click();}
  row(code){
    // Whitespace-only cell names are normalized by accessibility APIs.
    if(code.trim()==='')return this.page.locator('tbody tr').filter({has:this.page.locator('td:first-child').filter({hasText:new RegExp(`^\\s{${code.length}}$`)})});
    return this.page.getByRole('row').filter({has:this.page.getByRole('cell',{name:code,exact:true})});
  }
  async fill(data){
    await this.code.fill(data.code);await this.type.selectOption(data.type);
    await this.value.fill(String(data.discount_value));await this.minimum.fill(String(data.min_order_amount));
    await this.expires.fill(data.expired_at);await this.limit.fill(String(data.max_uses_per_user));
  }
  async submit(method='click'){
    const valid=await this.form.evaluate(e=>e.checkValidity());
    if(!valid){if(method==='enter')await this.code.press('Enter');else await this.create.click();return {clientBlocked:true,status:null};}
    const pending=this.page.waitForResponse(r=>r.url().endsWith('/api/admin/coupons')&&r.request().method()==='POST');
    if(method==='enter')await this.code.press('Enter');else await this.create.click();
    const response=await pending;return {clientBlocked:false,status:response.status(),body:await response.json()};
  }
}
