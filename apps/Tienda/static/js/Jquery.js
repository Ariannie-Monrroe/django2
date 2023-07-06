// $(function() {
//     $("#formValidation").validate({
//         rules:{
//             email:{
//                 required: true
//             },
//             password:{
//                 required: true
//             }
//         },
//         messages: {
//             email:{
//                 required:"Este campo es obligatorio",
//             },
//             password:{
//                 required:"Este campo es obligatorio",
//                 minlength: "El min de caracteres es de 5",
//             }
//         }
//     })
// })

// const form1 = document.getElementById('form1');
// const username = document.getElementById('username');
// const email = document.getElementById('email');
// const password = document.getElementById('password');
// const password2 = document.getElementById('password2');

// form1.addEventListener('submit', e => {
//     e.preventDefault();

//     validateInputs();
// });

// const setError = (element, message) => {
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = message;
//     inputControl.classList.add('error');
//     inputControl.classList.remove('success')
// }

// const setSuccess = element => {
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = '';
//     inputControl.classList.add('success');
//     inputControl.classList.remove('error');
// };

// const isValidEmail = email => {
//     const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     return re.test(String(email).toLowerCase());
// }

// const validateInputs = () => {
//     const usernameValue = username.value.trim();
//     const emailValue = email.value.trim();
//     const passwordValue = password.value.trim();
//     const password2Value = password2.value.trim();

//     if(usernameValue === '') {
//         setError(username, 'Username es obligatorio');
//     } else {
//         setSuccess(username);
//     }

//     if(emailValue === '') {
//         setError(email, 'Email es obligatorio');
//     } else if (!isValidEmail(emailValue)) {
//         setError(email, 'Escribe un Email valido');
//     } else {
//         setSuccess(email);
//     }

//     if(passwordValue === '') {
//         setError(password, 'Contraseña es obligatoria');
//     } else if (passwordValue.length < 8 ) {
//         setError(password, 'Password must be at least 8 character.')
//     } else {
//         setSuccess(password);
//     }

//     if(password2Value === '') {
//         setError(password2, 'Confirma tu contraseña');
//     } else if (password2Value !== passwordValue) {
//         setError(password2, "Las contraseñas no coinciden");
//     } else {
//         setSuccess(password2);
//     }

// };
//dddddd341342134242134123
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
