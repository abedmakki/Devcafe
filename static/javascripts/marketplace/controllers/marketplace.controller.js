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
            var appId = null;
            // vm.Like = Like;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
            })


  function AddComment(item, text) {
        var id = item;
        // console.log(item);
        // console.log(text);
        Market.comment(id, text);
    }

  $scope.rateFunction = function(id, value) {
    Market.rate(id, value);
  };


    // function Like(item) {
    //     var id = item;
    //     console.log(item);
    //     Market.like(id);
    // }

    function goToDetail(product) {
      // $scope.appDetail = product;
      Market.get(product).success(function(data, status, headers, config) {
        $location.path('/market/' + product);
        appId = data;
        console.log(appId);
      })
    }

  }
})();