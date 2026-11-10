// Disposable local demo data, never real user credentials.
export const demo={name:'HW03 GUI Login',password:'GuiDemo123!',wrong:'Incorrect123!'};
export const api='http://localhost:3000/api';
export const invalidInputs=[
  {name:'email missing',email:'',password:demo.password,invalid:1},
  {name:'password missing',email:'gui@example.test',password:'',invalid:1},
  {name:'both missing',email:'',password:'',invalid:2},
];
