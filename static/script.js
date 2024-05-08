function fetchData() {
    
    fetch('/moisture_data')
    .then((moisture_value) => {
        return moisture_value.text();
    }).then((moisture_value) => {
        document.getElementById("soilMoisture").innerHTML = `${moisture_value}%`;
    }).catch(error => console.error('Error fetching data:', error));
    
    fetch('/temperature_data')
    .then((temperature_value) => {
        return temperature_value.text();
    }).then((temperature_value) => {
        document.getElementById("temperature_C").innerHTML = `${temperature_value}°c`;
        document.getElementById("temperature_F").innerHTML = `${(temperature_value * 9 / 5) + 32}°F`;
    }).catch(error => console.error('Error fetching data:', error));
    
    fetch('/humidity_data')
    .then((humidity_value) => {
        return humidity_value.text();
    }).then((humidity_value) => {
        document.getElementById("humidity").innerHTML = `${humidity_value}%`;
    }).catch(error => console.error('Error fetching data:', error));
}

setInterval(fetchData,10000);

let btn1 = document.getElementById("Mode_Switch");
let btn2 = document.getElementById("Pump");
let state = false;

function switch_mode() {
    state =!state
    if (state == true) {
        btn2.disabled=state;
        //Api req
    }
    else {
        btn2.disabled=state;
        //Api req
    }
}
btn1.addEventListener("click",switch_mode)