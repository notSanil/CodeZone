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

