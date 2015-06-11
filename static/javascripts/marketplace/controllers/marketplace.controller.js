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
            vm.rating = rating;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
            })


  function AddComment(item, text) {
        var id = item;
        // console.log(item);
        // console.log(text);
        Market.comment(id, text);
    }

  function rating($http, $location, $scope, Market) {
    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };
    }

    

  }
})();