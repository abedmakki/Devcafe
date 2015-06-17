/**
* ProjectsController
* @namespace devcafe.projects.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.projects.controllers')
    .controller('ProjectsController', ProjectsController);

  ProjectsController.$inject = ['$http', '$location','$scope', '$rootScope', 'Projects'];

  /**
  * @namespace ProjectsController
  */
  // function ProjectsController($scope) {
  //   var vm = this;

  //   vm.columns = [];

  //   activate();
  function ProjectsController($http, $location, $scope, $rootScope, Projects) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            var createdProjId = null;
            
            Projects.all().success(function(data, status, headers, config) {
              $scope.projects = data;
            })

            $rootScope.$watch('searchQuery', function() {
              $scope.search = $rootScope.searchQuery;
            });


   


  }
})();