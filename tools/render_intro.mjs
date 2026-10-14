// 같은 시각 함수를 호출해 프레임을 만들고 ffmpeg로 30초 영상을 저장한다.
import {createRequire} from 'node:module';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {mkdir,writeFile} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.SOMI_PLAYWRIGHT_MODULE||'playwright');
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const origin=process.env.SOMI_PREVIEW_URL||'http://127.0.0.1:8765';
const qaOnly=process.argv.includes('--qa');
const output=process.env.SOMI_QA_OUTPUT||resolve(root,'../output/playwright/intro');
await mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true});
const report={formats:[],errors:[]};
try {
 for(const format of ['landscape','portrait']){
  const width=format==='landscape'?1920:1080,height=format==='landscape'?1080:1920;
  const page=await browser.newPage({viewport:{width,height},deviceScaleFactor:1});
  page.on('pageerror',e=>report.errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400)report.errors.push(`${r.status()} ${r.url()}`)});
  await page.goto(`${origin}/intro/?export=1&format=${format}`);
  await page.evaluate(()=>window.somiIntro.ready);
  const stage=page.locator('#viewport');
  for(const t of [0,1.5,3.6,4.6,5.7,7,10,14,17.5,20,22,24.5,26.8,29]){
   await page.evaluate(t=>window.somiIntro.renderAt(t),t);
   await stage.screenshot({path:resolve(output,`${format}-${t}.png`)});
  }
  // 다른 시각을 거쳐 되돌아와도 픽셀과 엔딩 정지 구간이 같아야 한다.
  const hash=async t=>{await page.evaluate(t=>window.somiIntro.renderAt(t),t);return createHash('sha256').update(await stage.screenshot()).digest('hex')};
  const deterministic=[];
  for(const t of [1.5,5.7,14,20,26.8]){const before=await hash(t);await hash(3.6);deterministic.push(before===await hash(t))}
  const hold=(await hash(27))===(await hash(29.9));
  if(!deterministic.every(Boolean)||!hold)throw new Error(`${format}: determinism/hold failed`);
  const buttons=Object.keys(await page.evaluate(()=>window.somiIntro.effects));
  for(const effect of buttons){await page.evaluate(effect=>{window.somiIntro.effects[effect]=false;window.somiIntro.renderAt(20)},effect);await page.evaluate(effect=>{window.somiIntro.effects[effect]=true},effect)}
  const stats=await page.evaluate(()=>{const times=[];for(let i=0;i<120;i++){const a=performance.now();window.somiIntro.renderAt(i/30);times.push(performance.now()-a)}times.sort((a,b)=>a-b);return {p95:times[Math.floor(times.length*.95)],max:times.at(-1)}});
  report.formats.push({format,width,height,deterministic,hold,renderMilliseconds:stats});
  if(!qaOnly){
   await page.evaluate(()=>window.somiIntro.renderAt(1.5));
   await stage.screenshot({path:resolve(root,`assets/intro/poster-${format}.jpg`),type:'jpeg',quality:90});
   const file=resolve(root,`assets/intro/somi-intro-${format}.mp4`);
   const ff=spawn('ffmpeg',['-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','mjpeg','-framerate','30','-i','pipe:0','-i',resolve(root,'assets/intro/soundtrack.mp3'),'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-r','30','-frames:v','900','-t','30','-c:a','aac','-b:a','128k','-movflags','+faststart','-map_metadata','-1',file],{stdio:['pipe','ignore','pipe']});
   let stderr='';ff.stderr.on('data',c=>stderr+=c);const finished=once(ff,'close');
   ff.stdin.on('error',e=>{stderr+=e.message});
   for(let frame=0;frame<900;frame++){
    await page.evaluate(t=>window.somiIntro.renderAt(t),frame/30);
    const jpeg=await stage.screenshot({type:'jpeg',quality:92});
    if(!ff.stdin.write(jpeg))await once(ff.stdin,'drain');
    if(frame%150===0)console.log(`${format}: ${frame}/900`);
   }
   ff.stdin.end();const [code]=await finished;if(code!==0)throw new Error(stderr);
   console.log(`${format}: completed 900 frames`);
  }
  await page.close();
 }
 if(report.errors.length)throw new Error(report.errors.join('\n'));
 await writeFile(resolve(output,qaOnly?'qa.json':'render-report.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify(report));
}finally{await browser.close()}
