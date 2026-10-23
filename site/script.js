const prompt=document.getElementById('prompt'),status=document.getElementById('copy-status'),copy=document.getElementById('copy');
// Localized pages override prompts and status text via data-* attributes; Chinese stays the default.
const prompts={codex:prompt?.dataset.codex||'使用 $create-miniature-world，把这张商品图做成微缩摄影，创意由你决定，给我两个不同且成立的创意各一张。',claude:prompt?.dataset.claude||'/create-miniature-world 把这张商品图做成微缩摄影，给我两个不同且成立的创意；没有生图工具就给对应提示词。'};
if(prompt&&status){
  for(const button of document.querySelectorAll('[data-host]'))button.addEventListener('click',()=>{if(!prompts[button.dataset.host])return;for(const b of document.querySelectorAll('[data-host]'))b.setAttribute('aria-pressed',String(b===button));prompt.textContent=prompts[button.dataset.host];status.textContent='';});
  copy?.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(prompt.textContent);status.textContent=copy.dataset.done||'已复制。安装后，在新任务中粘贴并上传商品图。';}catch{const range=document.createRange();range.selectNodeContents(prompt);const selection=window.getSelection();selection?.removeAllRanges();selection?.addRange(range);status.textContent=copy?.dataset.fallback||'请复制已选中的指令文字。';}});
}
const dialog=document.getElementById('lightbox'),photo=document.getElementById('lightbox-image'),caption=document.getElementById('lightbox-caption');
if(dialog&&photo&&caption){
  let opener=null;
  const close=dialog.querySelector('.close');
  for(const button of document.querySelectorAll('[data-image]'))button.addEventListener('click',()=>{opener=button;photo.src=button.dataset.image;photo.alt=button.dataset.alt||button.querySelector('img')?.alt||dialog.dataset.altFallback||'微缩摄影案例';caption.textContent=button.dataset.caption||'';dialog.showModal();close?.focus();});
  close?.addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>{opener?.focus();opener=null;});
  // Native dialog handles Escape and modal focus containment; close restores the trigger.
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
}
