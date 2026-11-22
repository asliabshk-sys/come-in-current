const fs=require('node:fs');const assert=require('node:assert/strict');
const {chromium}=require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const e='/workspace/come-in-current/evidence/resume-20261118';
(async()=>{
 const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});const checks=[],errors=[];
 try{
  const page=await browser.newPage();page.on('pageerror',e=>errors.push(e.message));
  const visible=id=>page.locator(`[data-testid="${id}"]:visible`);
  await page.goto('http://localhost:3000/',{waitUntil:'networkidle',timeout:60000});
  await visible('chand-home-entry').waitFor();assert.equal(await page.locator('[data-testid="request-anything-card"]').count(),0);checks.push('CHAND entry present; obsolete Request Anything card absent');
  for(const id of ['online-shops-card','offline-shops-card','restaurant-mode-card','home-services-card'])await visible(id).waitFor();checks.push('All four existing discovery modes retained');
  await visible('chand-home-entry').click();await page.waitForURL(u=>u.pathname==='/chand'&&!u.searchParams.has('voice'));
  await visible('chand-message-input').waitFor();checks.push('Primary assistant entry opens existing editable CHAND route');
  await page.goto('http://localhost:3000/',{waitUntil:'networkidle'});await visible('header-voice-search').click();
  await page.waitForURL(u=>u.pathname==='/chand'&&u.searchParams.get('voice')==='1');await visible('chand-message-input').waitFor();
  await page.waitForFunction(()=>document.activeElement?.getAttribute('data-testid')==='chand-message-input');checks.push('Home microphone opens CHAND voice typing and focuses input');
  assert(!(await page.locator('body').innerText()).includes('Speech recognition is not configured for this app.'));checks.push('No unconditional obsolete voice-unavailable alert');
  assert.equal(errors.length,0);fs.writeFileSync(e+'/home-chand-browser.json',JSON.stringify({ok:true,checks,pageErrors:errors,scope:'Web route/focus behavior only; no native microphone permission or provider request attempted'},null,2));console.log(JSON.stringify({ok:true,checks:checks.length,pageErrors:errors.length}));
 }finally{await browser.close()}
})().catch(e=>{console.error(e.message);process.exitCode=1});
