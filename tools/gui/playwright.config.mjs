import { defineConfig } from 'playwright/test';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { existsSync } from 'node:fs';

const here=path.dirname(fileURLToPath(import.meta.url));
const run=process.env.GUI_RUN_ID;
if(!run || !/^[A-Za-z0-9_-]+$/.test(run))throw new Error('Set GUI_RUN_ID to a unique run identifier');
const output=path.resolve(here,'../../submission/evidence/gui',run);
if(existsSync(output))throw new Error(`Evidence already exists for ${run}; choose a new GUI_RUN_ID`);
export default defineConfig({
  testDir:path.join(here,'tests'),
  outputDir:path.join(output,'artifacts'),
  timeout:65000,fullyParallel:false,workers:1,retries:0,
  reporter:[['list'],['json',{outputFile:path.join(output,'playwright-results.json')}]],
  use:{
    baseURL:'http://localhost:5173',
    headless:true,viewport:{width:1280,height:800},
    actionTimeout:5000,navigationTimeout:10000,
    screenshot:'only-on-failure',trace:'off',video:'off',
    launchOptions:{executablePath:'/usr/bin/microsoft-edge'},
  },
  expect:{timeout:3000},
});
