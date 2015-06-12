/**
* MarketplaceController
* @namespace devcafe.marketplace.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('MarketplaceDetailController', MarketplaceDetailController);

  MarketplaceDetailController.$inject = ['$http', '$location','$scope', '$routeParams', 'Market'];

  function MarketplaceDetailController($http, $location, $scope, $routeParams, Market) {
    var vm = this;
    // vm.AddComment = AddComment;
    // vm.goToDetail = goToDetail;
    // var appId = null;
    // vm.Like = Like;
    Market.get($routeParams.id).success(function(data, status, headers, config) {
      // console.log(data);
      $scope.appId = data;
    })
  }
})();