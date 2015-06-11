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
      // like : like,
      rate: rate
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
        window.location = '/market';
      });
    }

    function rate(id, value) {
      return $http.post('/market/' + id + '/rate/', {
        value: value
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