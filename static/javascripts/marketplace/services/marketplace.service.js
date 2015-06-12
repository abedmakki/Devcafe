(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.services')
    .factory('Market', Market);

  Market.$inject = ['$http'];

 
  function Market($http) {
    var Market = {
      all: all,
      get: get,
      comment: comment,
      rate: rate,
      buy: buy
    };

    return Market;

   
    function all() {
      return $http.get('/market/');
    }

    function get(id) {
      return $http.get('/market/' + id + '/');
    }


    function comment(id, text) {
      return $http.post('/market/' + id + '/add_comment/', {
        text: text
      }).then(function() {
        window.location = '/market/'+ id;
      });
    }

    function rate(id, value) {
      return $http.post('/market/' + id + '/rate/', {
        value: value
      });
    }

    function buy(id) {
      return $http.post('/market/' + id + '/buy/', {
        // home_no: home_no,
        // phone_no: phone_no,
        // delivery_address: delivery_address,
        // delivery_time: delivery_time,
        home_no: "123456",
        phone_no: "654321",
        delivery_address: "sjfhfkfjk",
        delivery_time: "2015-07-20TZ12:50",
      });
    }
    // function like(id) {
    //   return $http.post('/market/' + id + '/like/', {
    //   }).then(function() {
    //     window.location = '/market';
    //   });
    // }
}

})();