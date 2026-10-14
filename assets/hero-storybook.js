'use strict';
(() => {
  const figure = document.querySelector('.hero-screen-wrap.hero-art');
  if (!figure || !Element.prototype.animate) return;
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const image = figure.querySelector('img');
  const scene = document.createElement('div');
  scene.className = 'storybook-scene';
  const viewport = document.createElement('div');
  viewport.className = 'scene-viewport';
  image.before(scene);
  scene.append(viewport);
  viewport.append(image);
  for (const name of ['scene-sun', 'scene-light', 'scene-dust']) {
    const layer = document.createElement('span');
    layer.className = name;
    layer.setAttribute('aria-hidden', 'true');
    viewport.append(layer);
  }
  const dust = viewport.querySelector('.scene-dust');
  // Deliberate, repeatable positions frame the face rather than covering it.
  const points = [[9,60],[17,38],[26,74],[36,88],[8,86],[29,28],[81,22],[92,35],[88,68],[72,83],[94,86],[18,91],[39,45],[76,9],[57,90],[6,24],[90,13],[32,61]];
  points.forEach(([x,y], i) => {
    const particle = document.createElement('i');
    particle.style.cssText = `--x:${x}%;--y:${y}%;--size:${i%3===0?15:4+i%3}px;--delay:${i*85}ms;--drift:${i%2?12:-9}px`;
    dust.append(particle);
  });
  const replay = document.createElement('button');
  replay.className = 'scene-replay';
  replay.type = 'button';
  replay.innerHTML = '<span aria-hidden="true">✦</span> 그림에 햇살 더하기';
  scene.append(replay);
  let visible = false;
  let introduced = false;
  let cleanup;

  function resetTilt() {
    scene.classList.remove('scene-hover');
    for (const key of ['--rx','--ry','--dx','--dy']) scene.style.removeProperty(key);
  }
  function stop() {
    clearTimeout(cleanup);
    scene.classList.remove('scene-lit');
    resetTilt();
    scene.getAnimations({subtree:true}).forEach(animation => animation.cancel());
  }
  function play() {
    if (motion.matches || !visible || document.hidden) return;
    clearTimeout(cleanup);
    scene.classList.remove('scene-lit');
    // Restart a bounded CSS timeline on explicit input; no permanent render loop.
    void scene.offsetWidth;
    scene.classList.add('scene-lit');
    cleanup = setTimeout(() => scene.classList.remove('scene-lit'), 4600);
  }
  function sync() {
    replay.disabled = motion.matches;
    stop();
  }
  replay.addEventListener('click', play);
  scene.addEventListener('pointerenter', event => {
    if (event.pointerType === 'mouse' && !motion.matches) play();
  });
  scene.addEventListener('pointermove', event => {
    if (event.pointerType !== 'mouse' || motion.matches || !visible) return;
    // Pointer-driven only; CSS interpolates the bounded transform between inputs.
      const rect = viewport.getBoundingClientRect();
      const x = Math.max(-.5,Math.min(.5,(event.clientX-rect.left)/rect.width-.5));
      const y = Math.max(-.5,Math.min(.5,(event.clientY-rect.top)/rect.height-.5));
      scene.classList.add('scene-hover');
      scene.style.setProperty('--rx', (-y*7)+'deg');
      scene.style.setProperty('--ry', (x*8)+'deg');
      scene.style.setProperty('--dx', (-x*5)+'px');
      scene.style.setProperty('--dy', (-y*5)+'px');
  }, {passive:true});
  scene.addEventListener('pointerleave', resetTilt);
  scene.addEventListener('pointercancel', resetTilt);
  document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
  motion.addEventListener('change', sync);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      if (!visible) stop();
      else if (!introduced) { introduced = true; image.decode().then(play).catch(() => {}); }
    }, {threshold:.2}).observe(scene);
  } else {
    visible = true;
    image.decode().then(play).catch(() => {});
  }
  sync();
})();
