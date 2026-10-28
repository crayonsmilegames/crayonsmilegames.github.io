'use strict';
// Preserve public links to sections of the former single-product homepage.
(() => {
  const hash = location.hash;
  const legacy = ['home', 'features', 'voice-recording', 'screenshots', 'storybooks', 'faq', 'download', 'updates', 'app-guide'];
  const isHome = location.pathname === '/' || location.pathname === '/en/';
  if (isHome && legacy.includes(hash.slice(1))) {
    const prefix = location.pathname === '/en/' ? '/en' : '';
    location.replace(prefix + '/games/somi-kids-world/' + hash);
  }
})();
