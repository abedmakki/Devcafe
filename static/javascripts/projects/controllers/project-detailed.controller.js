
(function () {
  'use strict';

  angular
  .module('devcafe.projects.controllers')
  .controller('ProjectDetailedController', ProjectDetailedController);

  ProjectDetailedController.$inject = ['$http', '$location','$scope', '$routeParams', 'Projects'];

  function ProjectDetailedController($http, $location, $scope, $routeParams, Projects) {
    var vm = this;
    vm.assignTask = assignTask;


    Projects.get($routeParams.id).success(function(data, status, headers, config) {
      $scope.projId = data;
    })

    Projects.view_my_tasks($routeParams.id).success(function(data, status, headers, config) {
      $scope.mytasks = data;
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