
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

    function assignTask(id, contributor_id, title, description) {

    console.log($scope.projId.contributors.length);


    Projects.assign(contributor_id, title, description).success(function(data, status, headers, config) {
          for(var i = 0; i < $scope.projId.contributors.length; i++) {
            if ($scope.projId.contributors[i].id === contributor_id) {
              $scope.projId.contributors[i].tasks.push(data);
              $scope.vm.description = "";
              $scope.vm.title = "";            
            }
          }
        });

        }

  }


})();