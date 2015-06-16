(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('ViewTransactionsController', ViewTransactionsController);

  ViewTransactionsController.$inject = ['$http','$location','$scope','Market'];

  function ViewTransactionsController($http, $location, $scope, Market) {
            //var vm = this;

            Market.view_transactions().success(function(data, status, headers, config) {
              $scope.transactions = data;
            })
            Market.view_my_apps().success(function(data, status, headers, config){
              $scope.my_apps = data;
            })
  }
})();