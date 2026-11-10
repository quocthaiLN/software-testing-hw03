export class LoginPage{
  constructor(page){
    this.page=page;
    // Source and intake show labels without label-for/input-id associations.
    // CSS fallback targets the two form inputs until semantic labels are available.
    this.email=page.locator('form input').nth(0);
    this.password=page.locator('form input').nth(1);
    this.submit=page.getByRole('button',{name:/Sign In|Đăng nhập/i});
    this.error=page.getByText('Đăng nhập thất bại. Vui lòng kiểm tra lại.',{exact:true});
  }
  async goto(){await this.page.goto('/login');}
  async fill(email,password){await this.email.fill(email);await this.password.fill(password);}
  async login(email,password,method='click'){
    await this.fill(email,password);
    const response=this.page.waitForResponse(r=>r.url().endsWith('/api/login')&&r.request().method()==='POST');
    if(method==='enter')await this.password.press('Enter');else await this.submit.click();
    return await response;
  }
}
