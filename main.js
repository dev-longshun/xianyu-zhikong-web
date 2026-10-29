// 首屏按钮看得见时，顶栏的购买按钮先藏着
(function () {
  var nav = document.querySelector('.nav');
  var hero = document.getElementById('hero-actions');
  if (!('IntersectionObserver' in window)) { nav.classList.remove('hide-cta'); return; }
  new IntersectionObserver(function (entries) {
    nav.classList.toggle('hide-cta', entries[entries.length - 1].isIntersecting);
  }, { rootMargin: '-72px 0px 0px 0px' }).observe(hero);
})();

// 标签切换截图：点哪个标签换哪张图，淡出再淡入
(function () {
  var img = document.getElementById('stage-img');
  var name = document.getElementById('stage-name');
  var text = document.getElementById('stage-text');
  var tabs = document.querySelectorAll('.tabs button');

  // 预先把其它几张图拉下来，切换时不闪白
  tabs.forEach(function (tab) { new Image().src = 'img/' + tab.dataset.img + '.webp'; });

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      if (tab.getAttribute('aria-selected') === 'true') return;
      tabs.forEach(function (t) { t.setAttribute('aria-selected', t === tab ? 'true' : 'false'); });
      name.textContent = tab.textContent;
      text.textContent = tab.dataset.text;
      img.classList.add('fading');
      setTimeout(function () {
        img.src = 'img/' + tab.dataset.img + '.webp';
        img.alt = tab.textContent + '：' + tab.dataset.text;
        img.classList.remove('fading');
      }, 200);
    });
  });
})();
