function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }


function myFunction1(){
    document.getElementById("easytbl").style.display="block";
    document.getElementById("midtbl").style.display="none";
    document.getElementById("hardtbl").style.display="none";
    document.getElementById("insanetbl").style.display="none";
    document.getElementById("problvl").innerText="Easy";
}

function myFunction2(){
    document.getElementById("easytbl").style.display="none";
    document.getElementById("midtbl").style.display="block";
    document.getElementById("hardtbl").style.display="none";
    document.getElementById("insanetbl").style.display="none";
    document.getElementById("problvl").innerText="Medium";
}

function myFunction3(){
    document.getElementById("easytbl").style.display="none";
    document.getElementById("midtbl").style.display="none";
    document.getElementById("hardtbl").style.display="block";
    document.getElementById("insanetbl").style.display="none";
    document.getElementById("problvl").innerText="Hard";
}

function myFunction4(){
  document.getElementById("easytbl").style.display="none";
  document.getElementById("midtbl").style.display="none";
  document.getElementById("hardtbl").style.display="none";
  document.getElementById("insanetbl").style.display="block";
  document.getElementById("problvl").innerText="Insane";
}

  function toggle_function() {
  var r = document.querySelector(':root')
  if (document.getElementById('mode').innerText == 'Light') {
    document.getElementById('home-change').src = '/static/img/Home_dark.svg';
    document.getElementById('about-change').src = '/static/img/About_dark.svg';
    document.getElementById('logout-change').src = '/static/img/Logout_dark.svg';
    document.getElementById('mode').innerText = 'Dark';

    r.style.setProperty("--navyblue", "#eff3ff");
    r.style.setProperty("--lightblue", "#001333");
    r.style.setProperty("--greyblue", "#061d95");
  } 
  else {
    document.getElementById('mode').innerText = "Light";
    document.getElementById('home-change').src = '/static/img/Home.svg';
    document.getElementById('about-change').src = '/static/img/About.svg';
    document.getElementById('logout-change').src = '/static/img/Logout.svg';

    r.style.setProperty("--lightblue", "#eff3ff");
    r.style.setProperty("--navyblue", "#001333");
    r.style.setProperty("--greyblue", "#cbd2e1");
  }
  }

