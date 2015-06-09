/**
* MarketPlaceController
* @namespace devcafe.MarketPlace.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('MarketPlaceController', MarketPlaceController);

  MarketPlaceController.$inject = ['$http', '$location','$scope', 'MarketPlace'];

  function MarketPlaceController($http, $location, $scope, MarketPlace) {
    var vm = this;
  };

})();