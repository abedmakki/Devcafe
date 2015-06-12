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
            vm.AddComment = AddComment;
            vm.goToDetail = goToDetail;
            var appId = null;
            // vm.Like = Like;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
            })


    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };

    function goToDetail(id) {
      // $scope.appDetail = product;
      Market.get(id).success(function(data, status, headers, config) {
        // console.log(id);
        $location.path('/market/' + id);
        $scope.appId = data;
        // console.log(appId);
      })
      // console.log("HELLO");
    }

  }
})();