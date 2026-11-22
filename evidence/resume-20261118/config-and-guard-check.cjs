const fs=require('node:fs');const os=require('node:os');const path=require('node:path');const assert=require('node:assert/strict');
const app='/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/frontend';const config=require(app+'/app.config.js');let passed=0;
for(const url of ['', 'http://validation.invalid', 'https://localhost', 'https://user:password@validation.invalid']){process.env.COMEIN_BUILD_ENV='production';process.env.EXPO_PUBLIC_BACKEND_URL=url;assert.throws(()=>config(),/HTTPS|credentials/);passed++;}
process.env.EXPO_PUBLIC_BACKEND_URL='https://validation.invalid';assert(config().plugins.some(p=>Array.isArray(p)&&p[0]==='./plugins/withReleaseSafety'&&p[1].production));passed++;
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'comein-guard-'));const filename=path.join(temp,'rules.json');process.env.CMD_GUARD_RULES=filename;const {loadRules}=require(app+'/scripts/cmd-guard/rules.js');assert.equal(loadRules().source,'baked');passed++;
fs.writeFileSync(filename,'invalid JSON');assert.throws(()=>loadRules(),/not valid JSON/);passed++;
fs.writeFileSync(filename,'{}');assert.throws(()=>loadRules(),/not a valid rule list/);passed++;
fs.writeFileSync(filename,JSON.stringify({'local command':{allowed:false}}));assert.equal(loadRules().source,'injected');passed++;
console.log(`${passed} PASS, 0 FAIL, 0 SKIPPED: production URL boundary and command guard fail-closed checks. No network requested.`);
