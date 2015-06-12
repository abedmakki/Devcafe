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
    vm.AddComment = AddComment;
    vm.getDeliveryInfo = getDeliveryInfo;
    vm.Buy = Buy;
    // var appId = null;
    // vm.Like = Like;
    Market.get($routeParams.id).success(function(data, status, headers, config) {
      // console.log(data);
      $scope.appId = data;
      $scope.appIdRating = data.avg_rating;
      // console.log($scope.appId.avg_rating);
      // $scope.$watch("rating", function(){
      //   console.log($scope.rating);
      // });
      if (data.avg_rating === 0) {
        $scope.rating = 3;
      }
      else {
        $scope.rating = data.avg_rating;
      }
    })

    //get the current user
    $http.get('/users/profile/').success(function(data, status, headers, config) {
        $scope.user = data;
        // console.log($scope.user);
      })

    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };

    function AddComment(item, text) {
      var id = item;
      // console.log(item);
      // console.log(text);
      Market.comment(id, text);
    }

    function getDeliveryInfo(id) {
      $location.path('/market/' + id + '/buy');
      // console.log(id);
    }

    function Buy(id) {
      // console.log(item);
      // console.log(text);
      Market.buy(id);
    }

  }
})();