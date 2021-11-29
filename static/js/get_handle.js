
function ModeFunction() {
    var x = localStorage.getItem('modes');
    if (x == 'Dark') {
        document.getElementById('mode').click();
    }
}

function toggle_function() {
    var r = document.querySelector(':root')
    if (document.getElementById('mode').innerText == 'Light') {
        localStorage.setItem('modes', 'Dark');
        document.getElementById('mode').innerText = 'Dark';

        r.style.setProperty("--navyblue", "#eff3ff");
        r.style.setProperty("--lightblue", "#001333");
        r.style.setProperty("--grey", "#45546e");
    } 
    else {
        document.getElementById('mode').innerText = "Light";

        localStorage.setItem('modes', 'Light');
        r.style.setProperty("--lightblue", "#eff3ff");
        r.style.setProperty("--navyblue", "#001333");
        r.style.setProperty("--grey", "#c3c3c3");
    }
}
