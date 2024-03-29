
(function () {
  'use strict';

  angular
    .module('devcafe.projects.controllers')
    .controller('ProjectDetailedController', ProjectDetailedController);

  ProjectDetailedController.$inject = ['$http', '$location','$scope', '$routeParams', 'Projects'];

  function ProjectDetailedController($http, $location, $scope, $routeParams, Projects) {
    var vm = this;

     // Projects.all().success(function(data, status, headers, config) {
     //          $scope.projects = data;
     //        })

     Projects.get($routeParams.id).success(function(data, status, headers, config) {
      // console.log($routeParams.id);
      // console.log(data);
      $scope.projId = data;

    })

    // //get the current user
    // $http.get('/users/profile/').success(function(data, status, headers, config) {
    //     $scope.user = data;
    //     // console.log($scope.user);
    //   })

  }
})();