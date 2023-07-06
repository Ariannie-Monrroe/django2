
// API 
function clima(latitud, longitud) {
    fetch("https://api.openweathermap.org/data/2.5/weather?lat="+ latitud + "&lon=" + longitud+ "&appid=da782411f0dd3e140c85a1c83494aa97")
    .then(response =>  response.json())
    .then(data => {
        console.log(data);
        let ubicacion = document.getElementById("ubicacion");
        ubicacion.innerHTML += "Ubicacion: " + data.name;

        let temperatura = document.getElementById("temperatura");
        let kelvin = 273.15;
        let celsius= data.main.temp - kelvin;
        temperatura.innerHTML = "Temperatura: " + Math.trunc(celsius) + "°"
    })
}

function ubi() {
    navigator.geolocation.getCurrentPosition(function(position){

        let latitud = position.coords.latitude;
        let longitud = position.coords.longitude;

        console.log(latitud, longitud);
        clima(latitud, longitud);
    })
}
