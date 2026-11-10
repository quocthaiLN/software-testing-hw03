export class CheckoutPage{
 constructor(page){
  this.page=page;this.events={requests:[],responses:[],faults:[],fixtures:[]};this.pending=[];
  this.code=page.getByPlaceholder('Nhập mã giảm giá...');
  this.applyButton=page.getByRole('button',{name:/^Áp dụng$|^\.\.\.$/});
  this.saving=page.getByText(/^Tiết kiệm:/);this.final=page.getByText(/^Thành tiền:/);
  // The total label has no for/id association in the current SUT.
  this.total=page.locator('main input[type="number"]');
  this.error=page.getByText(/Mã giảm giá không tồn tại|Mã giảm giá đã hết hạn|Đơn hàng chưa đủ|Bạn đã sử dụng|Không thể áp dụng mã/);
  page.on('request',r=>{if(r.url().endsWith('/api/apply-coupon'))this.events.requests.push({observedAt:new Date().toISOString(),data:r.postDataJSON(),authorizationPresent:Boolean(r.headers().authorization)});});
  page.on('response',r=>{if(r.url().endsWith('/api/apply-coupon'))this.pending.push((async()=>this.events.responses.push({observedAt:new Date().toISOString(),status:r.status(),body:await r.json()}))());});
  page.on('requestfailed',r=>{if(r.url().endsWith('/api/apply-coupon'))this.events.faults.push({observedAt:new Date().toISOString(),error:r.failure()?.errorText});});
 }
 async prepare(product){
  // Full reload starts a fresh in-memory React cart; product is real backend fixture data.
  await this.page.goto('http://localhost:5173/');
  await this.page.getByRole('link',{name:/Chào,/}).waitFor({state:'visible'});
  await this.page.getByPlaceholder('Tìm kiếm...').fill(product.name);
  await this.page.getByRole('button',{name:'Tìm',exact:true}).click();
  // Product cards have no semantic group role; scope by the exact visible heading.
  const card=this.page.locator('div.border.rounded').filter({has:this.page.getByRole('heading',{name:product.name,exact:true})});
  await card.getByRole('button',{name:'Thêm vào giỏ',exact:true}).click();
  await this.page.getByRole('link',{name:'Giỏ hàng',exact:true}).click();
  await this.page.getByRole('button',{name:'Tiến hành thanh toán',exact:true}).click();
 }
 async apply(code){
  await this.code.fill(code);
  const pending=this.page.waitForResponse(r=>r.url().endsWith('/api/apply-coupon')&&r.request().method()==='POST');
  await this.applyButton.click();const r=await pending;
  return {status:r.status(),body:await r.json()};
 }
}
