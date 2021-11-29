
function ModeFunction(){
	var x=localStorage.getItem('modes');
	if(x==='Dark'){
		document.getElementById('mode').click();
        console.log("Fuck")}		
}

function MyFunction(){
    var r= document.querySelector(':root')
    if(document.getElementById('mode').value==='Light'){
        localStorage.setItem('modes', 'Dark');
        document.getElementById('mode').value='Dark';
        r.style.setProperty('--black', 'white');
        r.style.setProperty('--white', 'black');
        r.style.setProperty('--dark-blue', '#f1884e');
        r.style.setProperty('--orange', '#001333');
        r.style.setProperty('--orange2', 'red')
        document.getElementById('home').setAttribute('src','static/img/dashboard_images/Home_Dark.svg');
    }            
    else    
    {document.getElementById('mode').value='Light';
    localStorage.setItem('modes', 'Light');
    r.style.setProperty('--black', 'black');
    r.style.setProperty('--white', 'white');
    r.style.setProperty('--dark-blue', '#001333');
    r.style.setProperty('--orange', '#f1884e');
    r.style.setProperty('--orange2', '#f1884e');
    document.getElementById('home').setAttribute('src','static/img/dashboard_images/Home_Light.svg');
    }
    
}