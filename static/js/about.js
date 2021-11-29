

function ModeFunction(){
	var x=localStorage.getItem('modes');
	if(x==='Dark'){
		document.getElementById('mode').click();}		
}
function toggle_function() {
    var r = document.querySelector(':root')
    if (document.getElementById('mode').innerText == 'Light') {
        localStorage.setItem('modes', 'Dark');
        document.getElementById('home-change').src = '/static/img/Home.svg';
        document.getElementById('about-change').src = '/static/img/About.svg';
        document.getElementById('logout-change').src = '/static/img/Logout.svg';
        document.getElementById('repo-change').src = '/static/img/about_pg_images/Repo_dark.svg';
        document.getElementById('full-pg-change').src = '/static/img/about_pg_images/about_dark_bg.svg';
        document.getElementById('git-change').src = "/static/img/about_pg_images/GitHub_dark.svg";
        document.getElementById('linkin-change').src = "/static/img/about_pg_images/LinkedIn_dark.svg";
        document.getElementById('git-change-1').src = "/static/img/about_pg_images/GitHub_dark.svg";
        document.getElementById('linkin-change-1').src = "/static/img/about_pg_images/LinkedIn_dark.svg";
        document.getElementById('git-change-2').src = "/static/img/about_pg_images/GitHub_dark.svg";
        document.getElementById('linkin-change-2').src = "/static/img/about_pg_images/LinkedIn_dark.svg";
        document.getElementById('git-change-3').src = "/static/img/about_pg_images/GitHub_dark.svg";
        document.getElementById('linkin-change-3').src = "/static/img/about_pg_images/LinkedIn_dark.svg";
        document.getElementById('git-change-4').src = "/static/img/about_pg_images/GitHub_dark.svg";
        document.getElementById('linkin-change-4').src = "/static/img/about_pg_images/LinkedIn_dark.svg";
        document.getElementById('mode').innerText = 'Dark';

        r.style.setProperty("--navyblue", "#eff3ff");
        r.style.setProperty("--lightblue", "#001333");
    } 
    else {
        localStorage.setItem('modes', 'Light');
        document.getElementById('mode').innerText = "Light";
        document.getElementById('home-change').src = '/static/img/Home_dark.svg';
        document.getElementById('about-change').src = '/static/img/About_dark.svg';
        document.getElementById('logout-change').src = '/static/img/Logout_dark.svg';
        document.getElementById('repo-change').src = '/static/img/about_pg_images/Repo_light.svg';
        document.getElementById('full-pg-change').src = '/static/img/about_pg_images/about_bg.svg';
        document.getElementById('git-change').src = "/static/img/about_pg_images/GitHub_light.svg";
        document.getElementById('linkin-change').src = "/static/img/about_pg_images/LinkedIn_light.svg";
        document.getElementById('git-change-1').src = "/static/img/about_pg_images/GitHub_light.svg";
        document.getElementById('linkin-change-1').src = "/static/img/about_pg_images/LinkedIn_light.svg";
        document.getElementById('git-change-2').src = "/static/img/about_pg_images/GitHub_light.svg";
        document.getElementById('linkin-change-2').src = "/static/img/about_pg_images/LinkedIn_light.svg";
        document.getElementById('git-change-3').src = "/static/img/about_pg_images/GitHub_light.svg";
        document.getElementById('linkin-change-3').src = "/static/img/about_pg_images/LinkedIn_light.svg";
        document.getElementById('git-change-4').src = "/static/img/about_pg_images/GitHub_light.svg";
        document.getElementById('linkin-change-4').src = "/static/img/about_pg_images/LinkedIn_light.svg";

        r.style.setProperty("--lightblue", "#eff3ff");
        r.style.setProperty("--navyblue", "#001333");
    }
}
