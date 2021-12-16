// The API key is obtained from the openweathermap.org by signing up. The current plan is a free plan which allows 60 calls per minute.
// If a new key is created, it can be updated here

const api = {
  key: "735bb45f253e60888209648ad7929227",
  base: "https://api.openweathermap.org/data/2.5/"
}

// The below code adds a event listner to the input box
const searchbox = document.querySelector('.search-box');
searchbox.addEventListener('keypress', setQuery);

// The below code calls a function when enter key is pressed. Key code for enter key is 13.
function setQuery(evt) {
  if (evt.keyCode == 13) {
    getResults(searchbox.value);
  }
}

// Based on the city name (parameter) the API call is made to get results in a json format to weather.json
function getResults (query) {
  fetch(`${api.base}weather?q=${query}&units=metric&APPID=${api.key}`)
    .then(weather => {
      return weather.json();
    }).then(displayResults);
}

// Below function will extract weather info from the json data
function displayResults (weather) {
  let city = document.querySelector('.location .city');
  city.innerText = `${weather.name}, ${weather.sys.country}`;

  let now = new Date();
  let date = document.querySelector('.location .date');
  date.innerText = dateBuilder(now);

  let temp = document.querySelector('.current .temp');
  temp.innerHTML = `${Math.round(weather.main.temp)}<span>°c</span>`;

  let weather_el = document.querySelector('.current .weather');
  weather_el.innerText = weather.weather[0].main;

  let hilow = document.querySelector('.hi-low');
  hilow.innerText = `${Math.round(weather.main.temp_min)}°c / ${Math.round(weather.main.temp_max)}°c`;
}

// Below function is to style the Date in a better format
function dateBuilder (d) {
  let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  let day = days[d.getDay()];
  let date = d.getDate();
  let month = months[d.getMonth()];
  let year = d.getFullYear();

  return `${day} ${date} ${month} ${year}`;
}