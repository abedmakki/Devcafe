/**
* ProjectsController
* @namespace devcafe.projects.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.projects.controllers')
    .controller('ProjectsController', ProjectsController);

  ProjectsController.$inject = ['$http', '$location','$scope', '$rootScope', '$routeParams', '$timeout', 'Projects'];

  /**
  * @namespace ProjectsController
  */
  function ProjectsController($http, $location, $scope, $rootScope, $routeParams, $timeout, Projects) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            vm.startProject = startProject;
            var createdProjId = null;
            // var applyForJob = applyForJob;
            $scope.islogged = $rootScope.login
            
            Projects.all().success(function(data, status, headers, config) {
              $scope.projects = data;
            })

            $rootScope.$watch('searchQuery', function() {
              $scope.search = $rootScope.searchQuery;
            });

            $scope.applyForJob = function(jobId){
              // console.log(jobId);
              Projects.applyForJob(jobId);
            }


            function startProject(){
                Projects.startProject($scope.ptitle,$scope.pDesc).success(function(data){
                    var createdProjId = data.id;
                    // $('#StartProj').modal('toggle');
                    // $('#modal').modal('toggle');
                    // $('#exampleModalLabel').modal('toggle');
                    $timeout(function() {                      
                      $location.path('/projects/'+createdProjId+'/');
                    }, 500);
                })
            }
  }
})();