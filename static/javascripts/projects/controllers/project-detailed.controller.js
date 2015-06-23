
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

    // //get the current user
    // $http.get('/users/profile/').success(function(data, status, headers, config) {
    //     $scope.user = data;
    //     // console.log($scope.user);
    //   })
    function assignTask(id, contributor_id, title, description) {
    // console.log(id);
    console.log(contributor_id);
    // $scope.Projects.description = "";
    // $scope.Projects.title = "";
    Projects.assign(contributor_id, title, description)
    // .success(function(data, status, headers, config) {
    //       // for(var i = 0; i < $scope.ideas.length; i++) {
    //         if ($scope.ideas[i].id === item) {
    //           $scope.ideas[i].comments.push(data);
    //           console.log($scope.ideas[i].comments);
    //           $scope.ideas[i].name = "";
    //         }
    //       // }
    //     });

        }

  }


})();