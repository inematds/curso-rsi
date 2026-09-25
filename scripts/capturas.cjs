const {chromium}=require('/home/nmaldaner/projetos/agent-browser/node_modules/playwright');
const fs=require('fs'),path=require('path');
const base=path.resolve(__dirname,'..'), out=path.join(base,'context/capturas');fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await chromium.launch({args:['--disable-gpu']});const p=await b.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});const errors=[];p.on('pageerror',e=>errors.push(e.message));
for(let n=1;n<=18;n++){await p.goto('file://'+base+'/curso.html#aula-'+n);await p.waitForTimeout(150);await p.screenshot({path:`${out}/aula-${n}-celular.png`});let steps=await p.locator(`#v-aula-${n} .step`).all();for(let k=0;k<steps.length;k++) await steps[k].screenshot({path:`${out}/aula-${n}-step-${k+1}.png`,style:".bar{visibility:hidden !important}"});}
for(const width of [390,1440]){await p.setViewportSize({width,height:900});for(const theme of ['papel','escuro','sepia']){await p.goto('file://'+base+'/curso.html#aula-13');await p.evaluate(t=>document.documentElement.dataset.theme=t,theme);await p.screenshot({path:`${out}/curso-${width}-${theme}.png`});await p.goto('file://'+base+'/landing.html');await p.evaluate(t=>document.documentElement.dataset.theme=t,theme);await p.screenshot({path:`${out}/landing-${width}-${theme}.png`});}}
console.log('Capturas concluídas; erros:',errors);await b.close();})();
