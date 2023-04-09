
function runModel(){
    let preg = document.getElementById('preg').value;
    let gluc = document.getElementById('gluc').value;
    let blood = document.getElementById('blood').value;
    let skin = document.getElementById('skin').value;
    let ins = document.getElementById('ins').value;
    let bmi = document.getElementById('bmi').value;
    let dpf = document.getElementById('dpf').value;
    let age = document.getElementById('age').value;
    let vals = [preg, gluc, blood, skin, ins, bmi, dpf, age]
    let url = `/predict`

    fetch(url).then(response => response.json())
    .then(json => {console.log(json);
    document.getElementById('results').innerHTML = JSON.stringify(json)});
};