function MyFunction(){
  var r= document.querySelector(':root')
  if(document.getElementById('mode').value==='Light'){
      document.getElementById('mode').value='Dark';
      r.style.setProperty('--black', 'white');
      r.style.setProperty('--white', 'black');
      document.getElementById('div3').style.backgroundImage="url('static/img/index_images/Landing_Dark.gif')";
  }            
  else    
  {document.getElementById('mode').value='Light';
  r.style.setProperty('--black', 'black');
  r.style.setProperty('--white', 'white');
  document.getElementById('div3').style.backgroundImage="url('static/img/index_images/Landing.gif')"
  }
  
}