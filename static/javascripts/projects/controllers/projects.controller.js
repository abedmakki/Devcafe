/**
* ProjectsController
* @namespace devcafe.projects.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.projects.controllers')
    .controller('ProjectsController', ProjectsController);

  ProjectsController.$inject = ['$http', '$location','$scope', '$rootScope', '$routeParams', 'Projects'];

  /**
  * @namespace ProjectsController
  */
  // function ProjectsController($scope) {
  //   var vm = this;

  //   vm.columns = [];

  //   activate();
  function ProjectsController($http, $location, $scope, $rootScope, $routeParams, Projects) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            var createdProjId = null;
            
            Projects.all().success(function(data, status, headers, config) {
              $scope.projects = data;
            })

            $rootScope.$watch('searchQuery', function() {
              $scope.search = $rootScope.searchQuery;
            });

          //   projects.get($routeParams.id).success(function(data, status, headers, config) {            
          //   $scope.projId = data;                                  
          // })

  }


  // function getProjectId(id) {
  //   console.log(id);
  //   Projects.get('projects/' + id + '/').success(function(data, status, headers, config) {
  //     $scope.projId = data;
  //     $location.url('projects/' + id);
  //     console.log(id);
  //   })
    
  // }

  
})();