// 教程截图可用鼠标或键盘放大；关闭后焦点回到原图。
document.querySelectorAll('.guide-image a').forEach(function (link) {
  link.addEventListener('click', function (event) {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    var dialog = document.getElementById('image-viewer');
    if (!dialog || !dialog.showModal) return;
    event.preventDefault();
    var original = link.querySelector('img');
    var image = dialog.querySelector('img');
    image.src = link.href;
    image.alt = original.alt;
    dialog.querySelector('figcaption').textContent = original.alt;
    dialog.showModal();
    dialog.addEventListener('close', function () { link.focus(); }, { once: true });
  });
});
var viewer = document.getElementById('image-viewer');
if (viewer) {
  viewer.querySelector('button').addEventListener('click', function () { viewer.close(); });
  viewer.addEventListener('click', function (event) {
    if (event.target === viewer) viewer.close();
  });
}
