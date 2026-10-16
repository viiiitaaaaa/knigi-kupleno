// Последний ответ NotebookLM → markdown в window.__md; возвращает длину.
const bs=[...document.querySelectorAll('button')].filter(b=>/Копировать ответ/.test(b.getAttribute('aria-label')||''));
const b=bs[bs.length-1]; let c=b; while(c && !(c.innerText && c.innerText.length>3000)) c=c.parentElement;
function md(n,ind=''){ if(n.nodeType===3) return n.textContent; if(n.nodeType!==1) return ''; const t=n.tagName.toLowerCase(); const cl=(n.className||'').toString();
 if(['button','mat-icon','svg','style','script','follow-up'].includes(t) || /suggestions-container|follow-up/.test(cl)) return '';
 const kids=()=>[...n.childNodes].map(x=>md(x,ind)).join('');
 if(t==='pre') return '\n\n```'+(/mermaid|graph TD|graph LR/.test(n.innerText)?'mermaid':'')+'\n'+n.innerText.trim()+'\n```\n\n';
 if(/heading(\d)/.test(cl) && t==='div'){ const lv=+cl.match(/heading(\d)/)[1]; return '\n\n'+'#'.repeat(lv+1)+' '+kids().trim()+'\n\n'; }
 if(/^h[1-6]$/.test(t)) return '\n\n'+'#'.repeat(+t[1]+1)+' '+kids().trim()+'\n\n';
 if(t==='p') return '\n\n'+kids().trim()+'\n\n';
 if(t==='strong'||t==='b') return '**'+kids()+'**'; if(t==='em'||t==='i') return '*'+kids()+'*';
 if(t==='ul'||t==='ol') return '\n'+[...n.children].map((li,i)=>ind+(t==='ol'?(i+1)+'. ':'* ')+[...li.childNodes].map(x=>md(x,ind+'  ')).join('').trim()).join('\n')+'\n';
 if(t==='table'){const rows=[...n.querySelectorAll('tr')].map(r=>'| '+[...r.children].map(x=>x.innerText.trim().replace(/\n+/g,' ')).join(' | ')+' |'); if(rows.length) rows.splice(1,0,rows[0].replace(/[^|]+/g,' --- ')); return '\n\n'+rows.join('\n')+'\n\n';}
 if(t==='br') return '\n'; return kids(); }
window.__md=md(c).replace(/\n{3,}/g,'\n\n').trim(); window.__md.length
await Promise.race([navigator.clipboard.writeText(window.__md), new Promise((_,j)=>setTimeout(()=>j('timeout'),8000))]);
[window.__md.length, window.__md.slice(0,120), window.__md.slice(-150)]
