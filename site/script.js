const prompts={codex:'使用 $create-miniature-world，把这张商品图做成微缩摄影。先给三个有明显区别的创意，不要立即生图。',claude:'/create-miniature-world 把这张商品图做成微缩摄影。先给三个有明显区别的创意，不要立即生图。'};
const prompt=document.getElementById('prompt'),status=document.getElementById('copy-status');
for(const button of document.querySelectorAll('[data-host]'))button.addEventListener('click',()=>{for(const b of document.querySelectorAll('[data-host]'))b.setAttribute('aria-pressed',String(b===button));prompt.textContent=prompts[button.dataset.host];status.textContent='';});
document.getElementById('copy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(prompt.textContent);status.textContent='已复制。安装后，在新任务中粘贴并上传商品图。';}catch{const range=document.createRange();range.selectNodeContents(prompt);const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent='请复制已选中的指令文字。';}});
const dialog=document.getElementById('lightbox'),photo=document.getElementById('lightbox-image'),caption=document.getElementById('lightbox-caption');
for(const button of document.querySelectorAll('[data-image]'))button.addEventListener('click',()=>{photo.src=button.dataset.image;photo.alt=button.dataset.alt||button.querySelector('img')?.alt||'微缩摄影案例';caption.textContent=button.dataset.caption;dialog.showModal();});
dialog.querySelector('.close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
