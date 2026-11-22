const {chromium}=require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'); const assert=require('node:assert/strict');
const root='/workspace/come-in-current/evidence/session-20261117';
const accounts=JSON.parse(fs.readFileSync('/workspace/come-in-tools/continuation-test-accounts.json','utf8'));
const env=Object.fromEntries(fs.readFileSync('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/.env','utf8').split('\n').filter(l=>l&&!l.startsWith('#')).map(l=>{let i=l.indexOf('=');return[l.slice(0,i),l.slice(i+1)]}));
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const checks=[],errors=[];
 try{
  const publicContext=await browser.newContext();const p=await publicContext.newPage();p.on('pageerror',e=>errors.push(e.message));
  await p.goto('http://localhost:3000/',{waitUntil:'networkidle',timeout:60000});
  await p.locator('[data-testid="restaurant-mode-card"]:visible').waitFor({timeout:30000});
  await p.screenshot({path:root+'/home.png',fullPage:false});console.log('check',checks.length+1);checks.push('public shopping home renders');
  await p.locator('[data-testid="restaurant-mode-card"]:visible').click();await p.locator('[data-testid="restaurant-back-to-shopping"]:visible').waitFor({timeout:20000});
  await p.screenshot({path:root+'/restaurant.png',fullPage:false});console.log('check',checks.length+1);checks.push('Restaurant Mode navigation and isolated shell render');
  await p.locator('[data-testid="restaurant-back-to-shopping"]:visible').click();await p.locator('[data-testid="restaurant-mode-card"]:visible').waitFor();console.log('check',checks.length+1);checks.push('Restaurant return navigation preserves Shopping home');await publicContext.close();
  for(const [role,next,path,expected] of [
   ['CUSTOMER','/orders','/delivery-partner',/Delivery Partner/i],
   ['SELLER','/seller/products','/seller/support',/Seller Support/i],
   ['RESTO','/restaurant/dashboard','/restaurant/orders',/Restaurant|Orders/i],
   ['ADMIN','/admin','/admin-delivery-partners',/Delivery Partner|applications/i]
  ]){
   const context=await browser.newContext();const page=await context.newPage();page.on('pageerror',e=>errors.push(role+': '+e.message));
   await page.goto('http://localhost:3000/auth?next='+encodeURIComponent(next),{waitUntil:'networkidle',timeout:60000});
   await page.locator('[data-testid="auth-email"]:visible').fill(role==='ADMIN'?env.ADMIN_EMAIL:'continuation.'+role.toLowerCase()+'@comein-preview.com');
   await page.locator('[data-testid="auth-password"]:visible').fill(role==='ADMIN'?env.ADMIN_PASSWORD:accounts[role]);
   await page.locator('[data-testid="auth-submit"]:visible').click();
   await page.waitForURL(url=>!url.pathname.startsWith('/auth'),{timeout:20000});
   await page.waitForLoadState('networkidle');
   assert(!(await page.locator('body').innerText()).includes('Please sign in'));
   console.log('check',checks.length+1);checks.push(role+' real UI login and '+next+' render');
   await page.goto('http://localhost:3000'+path,{waitUntil:'networkidle',timeout:30000});
   const text=await page.locator('body').innerText();assert(expected.test(text),role+' route failed to render');
   assert(!text.includes('Maximum update depth exceeded'));
   console.log('check',checks.length+1);checks.push(role+' authenticated '+path+' render');await context.close();
  }
  assert.equal(errors.length,0,'Unhandled browser errors: '+errors.join('; '));
  fs.writeFileSync(root+'/browser-smoke.json',JSON.stringify({ok:true,checks,pageErrors:errors,scope:'Real web login/navigation/render smoke; no native devices or external provider calls'},null,2));
  console.log(JSON.stringify({ok:true,checks:checks.length,pageErrors:errors.length}));
 }finally{await browser.close()}
})().catch(error=>{console.error(error.message);process.exitCode=1});
