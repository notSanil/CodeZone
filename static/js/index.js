localStorage.setItem('modes', document.getElementById('mode').value);

function ModeFunction(){
	var x=localStorage.getItem('modes');
	if(x==='Dark'){
		document.getElementById('mode').click();}		
}



function MyFunction(){
  var r= document.querySelector(':root')
  if(document.getElementById('mode').value==='Light'){
	  localStorage.setItem('modes', 'Dark');
      document.getElementById('mode').value='Dark';
      r.style.setProperty('--black', 'white');
      r.style.setProperty('--white', 'black');
      document.getElementById('div3').style.backgroundImage="url('static/img/index_images/Landing_Dark.gif')";
  }            
  else    
  {localStorage.setItem('modes', 'Light');
  document.getElementById('mode').value='Light';
  r.style.setProperty('--black', 'black');
  r.style.setProperty('--white', 'white');
  document.getElementById('div3').style.backgroundImage="url('static/img/index_images/Landing.gif')"
  }
  
}