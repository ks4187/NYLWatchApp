function fetchWeather(latitude, longitude) {
  var req = new XMLHttpRequest();
  req.open('GET', 'https://ks4187.github.io/nylpay/api/payment_due.json', true);
  req.onload = function () {
    //if (req.readyState === 4) {
      if (req.status === 200) {
        console.log(req.responseText);
        var response = JSON.parse(req.responseText);
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
    'WEATHER_CITY_KEY': 'Loc Unavailable',
    'WEATHER_TEMPERATURE_KEY': 'N/A'
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
