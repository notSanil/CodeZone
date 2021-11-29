

function ModeFunction(){
	var x=localStorage.getItem('modes');
	if(x==='Dark'){
		document.getElementById('mode').click();}		
}

function toggle_function() {
    var r = document.querySelector(':root')
    if (document.getElementById('mode').innerText == 'Light') {
        localStorage.setItem('modes', 'Dark');
        document.getElementById('home-change').src = '/static/img/Home_dark.svg';
        document.getElementById('about-change').src = '/static/img/About_dark.svg';
        document.getElementById('logout-change').src = '/static/img/Logout_dark.svg';
        document.getElementById('mode').innerText = 'Dark';

        r.style.setProperty("--navyblue", "#eff3ff");
        r.style.setProperty("--lightblue", "#001333");
    } 
    else {
        document.getElementById('mode').innerText = "Light";
        document.getElementById('home-change').src = '/static/img/Home.svg';
        document.getElementById('about-change').src = '/static/img/About.svg';
        document.getElementById('logout-change').src = '/static/img/Logout.svg';
        localStorage.setItem('modes', 'Light');
        r.style.setProperty("--lightblue", "#eff3ff");
        r.style.setProperty("--navyblue", "#001333");
    }
}
