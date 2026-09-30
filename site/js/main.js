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

  var ff=document.getElementById('fit-form');
  if(ff){
    var out=document.getElementById('fit-out'),setup=document.getElementById('fit-setup'),skill=document.getElementById('fit-skill');
    var L={pt:['Part time job Singapore','part-time-jobs-singapore.html'],wfh:['Work from home jobs Singapore','work-from-home-jobs-singapore.html'],
      rem:['Remote job Singapore','remote-jobs-singapore.html'],on:['Online jobs and online work from home','online-jobs-singapore.html'],
      fr:['Freelance jobs','freelance-jobs-singapore.html'],mm:['Make money at home: the main routes','make-money-at-home-singapore.html']};
    var pick=function(){
      if(!setup.value||!skill.value){out.hidden=true;return;}
      var r=[];
      if(setup.value==='site')r.push('pt');
      if(setup.value==='home')r.push('wfh');
      if(setup.value==='any')r.push('on');
      if(skill.value==='people')r.push(setup.value==='site'?'wfh':'pt');
      if(skill.value==='creative')r.push('fr');
      if(skill.value==='special')r.push('rem','fr');
      if(skill.value==='none')r.push('mm');
      var seen={},list=r.filter(function(k){if(seen[k])return false;seen[k]=1;return true;}).slice(0,3);
      out.innerHTML='<b>Good places to start</b><ul>'+list.map(function(k){return '<li><a href="'+L[k][1]+'">'+L[k][0]+' &rarr;</a></li>';}).join('')+'</ul>';
      out.hidden=false;};
    setup.addEventListener('change',pick);skill.addEventListener('change',pick);
  }

  var cf=document.getElementById('calc');
  if(cf){
    var t=document.getElementById('c-target'),r=document.getElementById('c-rate'),o=document.getElementById('c-out');
    var run=function(){var a=parseFloat(t.value),b=parseFloat(r.value);
      if(!(a>0)||!(b>0)){o.hidden=true;return;}
      var h=a/b/4.33;o.innerHTML='<b>About '+(Math.round(h*10)/10)+' hours a week</b><br>to reach $'+a+' a month at $'+b+' an hour, before tax and costs. A rough guide only; it is not a promise of income.';o.hidden=false;};
    t.addEventListener('input',run);r.addEventListener('input',run);
  }
})();
