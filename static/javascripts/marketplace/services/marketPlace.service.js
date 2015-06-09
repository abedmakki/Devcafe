/**
* MarketPlace
* @namespace devcafe.MarketPlace.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.services')
    .factory('MarketPlace', MarketPlace);

  MarketPlace.$inject = ['$http'];

  /**
  * @namespace MarketPlace
  * @returns {Factory}
  */
  function MarketPlace($http) {
    var MarketPlace = {
      //bk end here
      // create: create,
      all: all
      };

    return MarketPlace;

    // function create(name, description, price, tags, image) {
    //   return $http.post('/market/', {
    //   name: name,
    //   description: description,
    //   price: price,
    //   tags: tags,
    //   image: image
    //   }).then(function() {
    //       window.location = '/market';
    //     });
    // }

    function all(){
      return $http.get('/market/');
    }

  }
})();