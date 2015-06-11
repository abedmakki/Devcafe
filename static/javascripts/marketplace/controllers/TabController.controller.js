
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('TabController', TabController);

  TabController.$inject = ['$http', '$location','$scope', 'Market'];

function TabController($http, $location, $scope, Market){
    this.tab = 1;

    this.setTab = function(newValue){
      this.tab = newValue;
    };

    this.isSet = function(tabName){
      return this.tab === tabName;
    };
 };

})();