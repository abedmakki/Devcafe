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
    };

    return Market;

    ////////////////////

   
    function all() {
      return $http.get('/market/');
    }
  }
})();