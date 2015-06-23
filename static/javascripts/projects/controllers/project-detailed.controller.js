
(function () {
  'use strict';

  angular
    .module('devcafe.projects.controllers')
    .controller('ProjectDetailedController', ProjectDetailedController);

  ProjectDetailedController.$inject = ['$http', '$location','$scope', '$routeParams', 'Projects'];

  function ProjectDetailedController($http, $location, $scope, $routeParams, Projects) {
    var vm = this;
    vm.assignTask = assignTask;

     // Projects.all().success(function(data, status, headers, config) {
     //          $scope.projects = data;
     //        })

     Projects.get($routeParams.id).success(function(data, status, headers, config) {
      // console.log($routeParams.id);
      // console.log(data);
      $scope.projId = data;

    })
     Projects.view_my_tasks($routeParams.id).success(function(data, status, headers, config) {
              $scope.mytasks = data;
            })

    // //get the current user
    // $http.get('/users/profile/').success(function(data, status, headers, config) {
    //     $scope.user = data;
    //     // console.log($scope.user);
    //   })
    function assignTask(id, contributor_id, title, description) {      
      Projects.assign(id, contributor_id, title, description);
        }

  }


})();