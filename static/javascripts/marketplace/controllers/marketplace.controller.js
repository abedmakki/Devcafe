/**
* MarketplaceController
* @namespace devcafe.marketplace.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('MarketplaceController', MarketplaceController);

  MarketplaceController.$inject = ['$http', '$location','$scope', 'Market'];

  function MarketplaceController($http, $location, $scope, Market) {
            var vm = this;
            var appId = null;
            // vm.Like = Like;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
                // $scope.$watch("rating", function(){
                //   console.log($scope.rating);
                // });
            })


    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };


  }
})();