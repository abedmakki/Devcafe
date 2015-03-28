(function () {
  'use strict';

  angular
    .module('DevCafe.controllers')
    .controller('MyController', MyController);

    MyController.$inject = ['$scope', '$http']


function MyController($scope, $http) {
    $http.get('ideas/').success(function(data) {
    $scope.artists = data;
  });
}

}) ();
