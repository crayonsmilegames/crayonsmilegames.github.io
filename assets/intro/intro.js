const effects = { particles: true, scatter: true, kinetic: true, device: true, cursor: true, flip: true, flow: true, music: true, depth: true, sfx: true, timeline: true };
const $ = (id) => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const lerp = (a, b, t) => a + (b - a) * t;
const seeded = (n) => { const x = Math.sin(n * 78.233 + 4.21) * 43758.5453; return x - Math.floor(x); };
const stage = $('stage'), viewport = $('viewport');
const base = new URL('./', import.meta.url);
const canvas = $('particles'), ctx = canvas.getContext('2d');
let format = 'landscape', W = 1600, H = 900, time = 2, playing = false, lastWall = 0, speed = 1, delay = .06;
let analysis;
let points = [];
let audio;
let sound = false;
let assetReady = false;
let exporting = new URLSearchParams(location.search).has('export');
const english = document.documentElement.lang === 'en';
const scenes = [0, 1, 2, 3].map(i => $('scene-' + i));
const subtitles = ['놀이가 배움이 되는 시간', '한글 · 영어 · 이야기 · 색칠 · 퍼즐'];
const sceneNames = ['소미 키즈월드', '직접 골라요', '놀이의 세 걸음', '지금 만나보세요'];
const shots = ['../screenshots/한글놀이.png', '../screenshots/색칠놀이2.png', '../screenshots/동화책3.png'].map(p => new URL(p, base).href);
const labels = ['한글을 만나요', '마음껏 색칠해요', '이야기를 함께 읽어요'];
const kinetic = $('kinetic');
const letters = Array.from(subtitles[0], ch => { const span = document.createElement('span'); span.textContent = ch; kinetic.append(span); return span; });
const shared = $('shared-shot');
let flips = [];
const flowPaths = Array.from(document.querySelectorAll('.flow-line'));
const flowCards = Array.from(document.querySelectorAll('.flow-card'));
const spectrum = $('music-viz'), sctx = spectrum.getContext('2d');
const audioPath = () => new URL(effects.sfx ? 'soundtrack.mp3' : 'music.mp3', base).href;
function mask(text) {
    const c = document.createElement('canvas');
    c.width = W;
    c.height = H;
    const g = c.getContext('2d');
    g.font = `${format === 'portrait' ? 106 : 140}px SomiRound`;
    g.textAlign = 'center';
    g.textBaseline = 'middle';
    g.fillText(text, W / 2, format === 'portrait' ? 690 : 385, W - 110);
    const data = g.getImageData(0, 0, W, H).data;
    let area = 0;
    for (let i = 3; i < data.length; i += 4)
        if (data[i] > 128)
            area++;
    const spacing = Math.max(4, Math.sqrt(area / 3400));
    const found = [];
    for (let y = 0; y < H; y += spacing)
        for (let x = 0; x < W; x += spacing)
            if (data[(Math.floor(y) * W + Math.floor(x)) * 4 + 3] > 128)
                found.push(x, y);
    return new Float32Array(found);
}
function resize() {
    W = format === 'portrait' ? 900 : 1600;
    H = format === 'portrait' ? 1600 : 900;
    stage.classList.toggle('portrait', format === 'portrait');
    viewport.classList.toggle('portrait', format === 'portrait');
    stage.style.transform = `scale(${viewport.clientWidth / W})`;
    canvas.width = W;
    canvas.height = H;
    spectrum.width = W;
    spectrum.height = 40;
}
function opening(t) {
    ctx.clearRect(0, 0, W, H);
    const phase = clamp((t - 2.1) / .85), settle = ease((t - .1) / .9);
    const a = points[0], b = points[1], n = Math.max(a.length, b.length) / 2;
    const colors = ['#315b42', '#98552c', '#41678a', '#79538a'];
    if (!effects.particles) {
        ctx.fillStyle = '#3b4f36';
        ctx.font = `${format === 'portrait' ? 106 : 140}px SomiRound`;
        ctx.textAlign = 'center';
        ctx.fillText(t < 2.4 ? '소미 키즈월드' : '함께 놀아요', W / 2, format === 'portrait' ? 725 : 425);
    }
    for (let i = 0; effects.particles && i < n; i++) {
        const ia = (i % (a.length / 2)) * 2, ib = (i % (b.length / 2)) * 2, r = seeded(i);
        let x = lerp(a[ia], b[ib], ease(phase)), y = lerp(a[ia + 1], b[ib + 1], ease(phase));
        const burst = effects.scatter ? Math.sin(phase * Math.PI) * 95 : 0;
        x += Math.cos(r * 6.283) * burst;
        y += Math.sin(r * 6.283) * burst;
        x = lerp(r * W, x, settle);
        y = lerp(seeded(i + 782) * H, y, settle);
        ctx.fillStyle = colors[i % 4];
        ctx.beginPath();
        ctx.arc(x, y, format === 'portrait' ? 2.7 : 3, 0, Math.PI * 2);
        ctx.fill();
    }
    letters.forEach((el, i) => {
        const u = clamp((t - .65 - i * delay) / .7);
        const overshoot = 1 + Math.sin(u * Math.PI * 2) * Math.exp(-u * 4) * .22;
        el.style.opacity = String(effects.kinetic ? clamp(u * 3) : 1);
        el.style.transform = effects.kinetic ? `translateY(${(1 - ease(u)) * 42}px) scale(${overshoot},${1 / overshoot})` : 'none';
    });
}
// FLIP: 작은 배치 적용 → First 측정 → 전체 배치 적용 → Last 측정 → 역변환 캐시.
function measureFlip() {
    const screen = $('screen');
    const scale = viewport.clientWidth / W;
    flips = Array.from(document.querySelectorAll('.demo-card img')).map(card => {
        const first = card.getBoundingClientRect(), outer = screen.getBoundingClientRect();
        Object.assign(shared.style, { left: `${(first.left - outer.left) / scale}px`, top: `${(first.top - outer.top) / scale}px`, width: `${first.width / scale}px`, height: `${first.height / scale}px`, transform: 'none' });
        const small = shared.getBoundingClientRect();
        Object.assign(shared.style, { left: '0px', top: '0px', width: '100%', height: '100%', transform: 'none' });
        const large = shared.getBoundingClientRect();
        return { x: (small.left - large.left) / scale, y: (small.top - large.top) / scale, sx: small.width / large.width, sy: small.height / large.height };
    });
}
function measureFlow() {
    const scale = viewport.clientWidth / W, root = stage.getBoundingClientRect();
    const boxes = flowCards.map(c => c.getBoundingClientRect());
    flowPaths.forEach((p, i) => {
        const a = boxes[i], b = boxes[i + 1];
        const x1 = (format === 'portrait' ? a.left + a.width / 2 : a.right) - root.left;
        const y1 = (format === 'portrait' ? a.bottom : a.top + a.height / 2) - root.top;
        const x2 = (format === 'portrait' ? b.left + b.width / 2 : b.left) - root.left;
        const y2 = (format === 'portrait' ? b.top : b.top + b.height / 2) - root.top;
        p.setAttribute('d', `M${x1 / scale},${y1 / scale} L${x2 / scale},${y2 / scale}`);
        const length = p.getTotalLength();
        p.style.strokeDasharray = `${length} ${length}`;
    });
}
function demo(t) {
    const local = t - analysis.cuts[1];
    const active = clamp(Math.floor((t - analysis.clicks[0] + 1.2) / 4), 0, 2);
    const tap = analysis.clicks[active], delta = t - tap;
    const reveal = ease(delta / .85);
    const returning = active < 2 ? clamp((t - (analysis.clicks[active + 1] - 1.3)) / .3) : 0;
    const visible = delta >= 0 && returning === 0;
    const index = active | 0;
    if (shared.src !== shots[index])
        shared.src = shots[index];
    shared.style.opacity = visible ? '1' : '0';
    const f = flips[index];
    const u = effects.flip ? reveal : 1;
    shared.style.transform = `translate(${f.x * (1 - u)}px,${f.y * (1 - u)}px) scale(${lerp(f.sx, 1, u)},${lerp(f.sy, 1, u)})`;
    $('gallery').style.opacity = String(visible ? 1 - reveal : 1);
    // 작은 스크롤은 시간식으로 감속한다. 게임 이미지 자체에 가짜 플레이를 그리지 않는다.
    const scroll = effects.device ? 18 * (1 - Math.exp(-Math.max(0, local) * 3)) * Math.exp(-Math.max(0, local - 1) * 3) : 0;
    $('gallery').style.transform = `translateY(${-scroll}px)`;
    const tilt = effects.device ? Math.sin(local * .7) * 6 - 5 : 0;
    $('device').style.transform = `rotateY(${tilt}deg) rotateX(${effects.device ? 4 : 0}deg)`;
    $('device-shadow').style.transform = `translateX(${-tilt * 2}px) scaleX(${1 - Math.abs(tilt) * .006})`;
    $('glass').style.opacity = effects.device ? '.7' : '0';
    const screen = $('screen'), sw = screen.clientWidth, sh = screen.clientHeight;
    const arrival = ease((t - (tap - 1.1)) / .85);
    const targetX = (index + .5) / 3 * sw, targetY = sh * .46;
    const cx = lerp(sw * .1, targetX, arrival), cy = lerp(sh * .88, targetY, arrival) - Math.sin(arrival * Math.PI) * 65;
    const cursor = $('cursor');
    cursor.style.opacity = effects.cursor && delta < .5 ? '1' : '0';
    cursor.style.left = `${cx}px`;
    cursor.style.top = `${cy}px`;
    cursor.style.transform = `translate(-50%,-50%) scale(${1 - clamp(1 - Math.abs(delta) / .15) * .18})`;
    const r = $('ripple'), rp = clamp(delta / .65);
    r.style.left = `${targetX - 25}px`;
    r.style.top = `${targetY - 25}px`;
    r.style.transform = `scale(${.5 + rp * 2.4})`;
    r.style.opacity = effects.cursor && delta >= 0 && delta < .65 ? String(1 - rp) : '0';
    $('demo-caption').textContent = labels[index];
    $('sfx-caption').style.opacity = effects.sfx && delta >= 0 && delta < .55 ? '1' : '0';
}
function flow(t) {
    const local = t - analysis.cuts[2];
    flowCards.forEach((card, i) => { const u = effects.flow ? ease((local - i * 1.5) / .7) : 1; card.style.opacity = String(u); card.style.transform = `translateY(${(1 - u) * 35}px) scale(${.9 + .1 * u})`; card.style.borderColor = effects.flow && local > i * 1.5 && local < i * 1.5 + 1 ? '#e5a323' : '#d6ba89'; });
    flowPaths.forEach((path, i) => { const u = effects.flow ? ease((local - .8 - i * 1.5) / .8) : 1; path.style.strokeDashoffset = String(path.getTotalLength() * (1 - u)); path.setAttribute('marker-end', u > .97 ? 'url(#arrow)' : ''); });
    const dot = $('flow-dot'), progress = clamp((local - 1.5) / 4.5) * 2;
    const path = flowPaths[Math.min(1, Math.floor(progress))], p = path.getPointAtLength(path.getTotalLength() * (progress >= 2 ? 1 : progress % 1));
    dot.setAttribute('cx', String(p.x));
    dot.setAttribute('cy', String(p.y));
    dot.style.opacity = effects.flow && local > 1.5 && local < 6.4 ? '1' : '0';
}
const layers = Array.from({ length: 9 }, (_, i) => { const el = document.createElement('span'); el.textContent = '소미 키즈월드'; el.style.color = i === 8 ? '#385a38' : '#bfa679'; $('extruded').append(el); return el; });
function ending(t) {
    const local = t - analysis.cuts[3], u = ease(local / 1.1), bounce = Math.sin(clamp((local - .5) / 1.4) * Math.PI * 3) * Math.exp(-Math.max(0, local - .5) * 3) * 25;
    layers.forEach((el, i) => { el.style.transform = effects.depth ? `translate(${8 - i}px,${(8 - i) * 2}px) translateZ(${i}px)` : 'none'; el.style.opacity = effects.depth || i === 8 ? '1' : '0'; });
    $('extruded').style.transform = effects.depth ? `perspective(1200px) rotateX(${(1 - u) * -35}deg) rotateY(${(1 - u) * -14}deg) translateY(${(1 - u) * -100 + bounce}px)` : 'none';
    $('ending-logo').style.transform = effects.depth ? `translateY(${(1 - u) * -80}px) rotate(${(1 - u) * -16}deg) scale(${.85 + u * .15})` : 'none';
    $('ending-shine').style.transform = `translateX(${lerp(-W, W, ease((local - 1.3) / 1.3))}px)`;
    $('ending-shine').style.opacity = effects.depth && local > 1.3 && local < 2.6 ? '1' : '0';
}
function music(t) {
    sctx.clearRect(0, 0, W, 40);
    if (!effects.music)
        return;
    const frame = Math.min(899, Math.floor(t * 30)), row = analysis.bands[frame];
    row.forEach((level, i) => { sctx.fillStyle = ['#8baa76', '#cbb36e', '#bd9ec2', '#7da9bc'][i % 4]; sctx.fillRect(i * W / 32, 40 - level * 35, W / 32 - 6, level * 35); });
}
// 모든 장면을 절대 시간으로 복원한다. 27초부터는 시각 요소를 완전히 정지한다.
function renderAt(t) {
    time = clamp(t, 0, 30);
    if (!assetReady)
        return;
    const visual = Math.min(time, 27);
    const scene = visual < analysis.cuts[1] ? 0 : visual < analysis.cuts[2] ? 1 : visual < analysis.cuts[3] ? 2 : 3;
    scenes.forEach((s, i) => s.classList.toggle('active', i === scene));
    if (scene === 0)
        opening(visual);
    if (scene === 1)
        demo(visual);
    if (scene === 2)
        flow(visual);
    if (scene === 3)
        ending(visual);
    music(visual);
    $('seek').value = String(time);
    $('time').textContent = `${time.toFixed(1)} / 30.0`;
}
async function setFormat(value) {
    format = value;
    resize();
    points = [mask('소미 키즈월드'), mask('함께 놀아요')];
    $('device').style.transform = 'none';
    $('gallery').style.transform = 'none';
    flowCards.forEach(c => c.style.transform = 'none');
    measureFlip();
    measureFlow();
    renderAt(time);
    $('format').textContent = format === 'portrait' ? (english ? 'Landscape' : '가로로 보기') : (english ? 'Portrait' : '세로로 보기');
}
function pause() { playing = false; audio.pause(); $('play').textContent = english ? 'Play' : '재생'; }
async function play() {
    await ready;
    if (!effects.timeline)
        return;
    if (time >= 30)
        renderAt(0);
    playing = true;
    lastWall = performance.now();
    $('play').textContent = english ? 'Pause' : '일시정지';
    if (sound) {
        audio.currentTime = time;
        audio.playbackRate = speed;
        await audio.play().catch(() => { sound = false; updateSound(); });
    }
}
function updateSound() { $('sound').textContent = sound ? (english ? 'Sound on' : '소리 켬') : (english ? 'Sound off' : '소리 끔'); $('sound').setAttribute('aria-pressed', String(sound)); }
function tick(now) {
    if (playing) {
        const next = sound && !audio.paused ? audio.currentTime : time + (now - lastWall) / 1000 * speed;
        renderAt(next);
        if (next >= 29.999 || audio.ended)
            pause();
    }
    lastWall = now;
    requestAnimationFrame(tick);
}
const ready = (async () => {
    await document.fonts.load('100px SomiRound');
    await document.fonts.ready;
    analysis = await fetch(new URL('audio-analysis.json', base)).then(r => { if (!r.ok)
        throw new Error('audio analysis missing'); return r.json(); });
    audio = new Audio(audioPath());
    audio.preload = 'metadata';
    audio.volume = .6;
    await Promise.all(Array.from(stage.querySelectorAll('img')).map(img => img.decode()));
    if (exporting)
        document.documentElement.classList.add('export');
    const requested = new URLSearchParams(location.search).get('format');
    await setFormat(requested === 'portrait' || (!requested && innerWidth < 640) ? 'portrait' : 'landscape');
    assetReady = true;
    renderAt(2);
    $('load-status').textContent = '';
    $('studio').classList.toggle('enabled', new URLSearchParams(location.search).has('studio'));
    $('play').onclick = () => playing ? pause() : void play();
    $('restart').onclick = () => { pause(); renderAt(0); void play(); };
    $('sound').onclick = async () => { sound = !sound; updateSound(); if (!sound)
        audio.pause();
    else if (playing) {
        audio.currentTime = time;
        audio.playbackRate = speed;
        await audio.play().catch(() => { sound = false; updateSound(); });
    } };
    $('seek').oninput = e => { pause(); renderAt(Number(e.target.value)); audio.currentTime = time; };
    $('format').onclick = () => void setFormat(format === 'portrait' ? 'landscape' : 'portrait');
    $('delay').oninput = e => { delay = Number(e.target.value); renderAt(time); };
    $('speed').onchange = e => { speed = Number(e.target.value); audio.playbackRate = speed; };
    document.querySelectorAll('[data-effect]').forEach(input => input.onchange = () => {
        const key = input.dataset.effect;
        effects[key] = input.checked;
        if (key === 'sfx') {
            audio.pause();
            audio.src = audioPath();
            audio.playbackRate = speed;
            if (sound && playing) {
                audio.currentTime = time;
                void audio.play().catch(() => { sound = false; updateSound(); });
            }
        }
        if (key === 'timeline' && !input.checked)
            pause();
        renderAt(time);
    });
    document.addEventListener('visibilitychange', () => { if (document.hidden)
        pause(); });
    requestAnimationFrame(tick);
})();
const api = { ready, renderAt, setFormat, effects, get time() { return time; }, get analysis() { return analysis; } };
window.somiIntro = api;
new ResizeObserver(() => { resize(); if (assetReady) {
    $('device').style.transform = 'none';
    $('gallery').style.transform = 'none';
    flowCards.forEach(c => c.style.transform = 'none');
    measureFlip();
    measureFlow();
    renderAt(time);
} }).observe(viewport);
ready.catch(error => { $('load-status').textContent = '미리보기를 준비하지 못했습니다. 아래 MP4로 확인해 주세요.'; console.error(error); });
export {};
