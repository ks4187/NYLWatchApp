var myAPIKey = 'a496197b748f1fe8fa154e0e6782ed43';

function iconFromWeatherId(weatherId) {
  if (weatherId < 600) {
    return 2;
  } else if (weatherId < 700) {
    return 3;
  } else if (weatherId > 800) {
    return 1;
  } else {
    return 0;
  }
}

/*function fetchWeather(latitude, longitude) {
  var req = new XMLHttpRequest();
  req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?' +
    'lat=' + latitude + '&lon=' + longitude + '&cnt=1&appid=' + myAPIKey, true);
  console.log('http://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude + '&cnt=1&appid=' + myAPIKey);
  req.onload = function () {
    //if (req.readyState === 4) {
      if (req.status === 200) {
        console.log(req.responseText);
        var response = JSON.parse(req.responseText);
        var temperature = Math.round(response.main.temp - 273.15);
        var icon = iconFromWeatherId(response.weather[0].id);
        var city = response.name;
        console.log('temp: ' + temperature);
        console.log('icon: ' + icon);
        console.log('city: ' + city);
        Pebble.sendAppMessage({
          'WEATHER_ICON_KEY': icon,
          'WEATHER_TEMPERATURE_KEY': temperature + '\xB0C',
          'WEATHER_CITY_KEY': city
        }, function() {
          console.log('Message sent successfully');
        }, function(e) {
          console.log('MEssage failed: ' + e);
        });
      //} else {
      //  console.log('Error');
      //}
    }
  };
  req.send(null);
}*/

function fetchWeather(latitude, longitude) {
  var req = new XMLHttpRequest();
  req.open('GET', 'https://ks4187.github.io/nylpay/api/payment_due.json', true);
  req.onload = function () {
    //if (req.readyState === 4) {
      if (req.status === 200) {
        console.log(req.responseText);
        var response = JSON.parse(req.responseText);
        /*var temperature = Math.round(response.main.temp - 273.15);
        var icon = iconFromWeatherId(response.weather[0].id);
        var city = response.name;
        console.log('temp: ' + temperature);
        console.log('icon: ' + icon);
        console.log('city: ' + city);*/
        Pebble.sendAppMessage({
          'WEATHER_ICON_KEY': 4,
          'WEATHER_TEMPERATURE_KEY': response.payment_date,
          'WEATHER_CITY_KEY': response.payment_message
        }, function() {
          console.log('Message sent successfully');
        }, function(e) {
          console.log('MEssage failed: ' + e);
        });
      //} else {
      //  console.log('Error');
      //}
    }
  };
  req.send(null);
}

function locationSuccess(pos) {
  var coordinates = pos.coords;
  fetchWeather(coordinates.latitude, coordinates.longitude);
}

function locationError(err) {
  console.warn('location error (' + err.code + '): ' + err.message);
  Pebble.sendAppMessage({
    'WEATHER_CITY_KEY': 'PREMIUM DUE',
    'WEATHER_TEMPERATURE_KEY': 'October 10th'
  });
}

var locationOptions = {
  'timeout': 15000,
  'maximumAge': 60000
};

Pebble.addEventListener('ready', function (e) {
  console.log('connect!' + e.ready);
  window.navigator.geolocation.getCurrentPosition(locationSuccess, locationError,
    locationOptions);
  console.log(e.type);
});

Pebble.addEventListener('appmessage', function (e) {
  window.navigator.geolocation.getCurrentPosition(locationSuccess, locationError,
    locationOptions);
  console.log(e.type);
  console.log(e.payload.temperature);
  console.log('message!');
});

Pebble.addEventListener('webviewclosed', function (e) {
  console.log('webview closed');
  console.log(e.type);
  console.log(e.response);
});
