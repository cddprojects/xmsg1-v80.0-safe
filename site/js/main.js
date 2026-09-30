(function(){
  var btn=document.querySelector('.menu-btn'),list=document.getElementById('nav-list');
  if(btn&&list){btn.addEventListener('click',function(){
    var o=list.classList.toggle('open');btn.setAttribute('aria-expanded',o);});}

  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  }else{document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');});}

  var chips=document.querySelectorAll('.chip[data-filter]');
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===c);});
    var f=c.dataset.filter;
    document.querySelectorAll('.post[data-cat]').forEach(function(p){
      p.hidden=!(f==='all'||p.dataset.cat===f);});});});

  var s=document.getElementById('glossary-search');
  if(s){s.addEventListener('input',function(){
    var q=s.value.trim().toLowerCase(),n=0;
    document.querySelectorAll('.term').forEach(function(t){
      var m=t.textContent.toLowerCase().indexOf(q)>-1;t.hidden=!m;if(m)n++;});
    document.getElementById('glossary-empty').hidden=n>0;});}

  var chk=document.getElementById('scam-check');
  if(chk){
    var out=document.getElementById('scam-result');
    var update=function(){
      var n=chk.querySelectorAll('input:checked').length,h,p,c='result';
      if(n===0){out.hidden=true;return;}
      if(n===1){c+=' warn';h='One red flag. Slow down.';p='Verify the company independently before sharing anything. Look it up on ACRA and the official MyCareersFuture listing.';}
      else{c+=' bad';h=n+' red flags. Treat this as likely a scam.';p='Stop replying. Do not send money, IDs, bank or Singpass details. Call the ScamShield helpline 1799 if unsure, and report to the Police if you lost money.';}
      out.className=c;out.hidden=false;out.querySelector('h3').textContent=h;out.querySelector('p').textContent=p;};
    chk.addEventListener('change',update);
  }

  var f=document.getElementById('contact-form');
  if(f){f.addEventListener('submit',function(e){
    e.preventDefault();var ok=true;
    f.querySelectorAll('[required]').forEach(function(i){
      var err=i.parentElement.querySelector('.err'),bad=!i.value.trim()||(i.type==='email'&&!/^\S+@\S+\.\S+$/.test(i.value));
      err.textContent=bad?(i.type==='email'?'Please enter a valid email.':'This field is required.'):'';
      i.setAttribute('aria-invalid',bad);if(bad)ok=false;});
    if(ok){f.hidden=true;document.getElementById('form-ok').hidden=false;document.getElementById('form-ok').focus();}
  });}
})();
