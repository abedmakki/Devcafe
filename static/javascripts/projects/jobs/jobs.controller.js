/**
 * Created by Abedmakki on 30/06/2015.
 */

(function () {
  'use strict';

  angular
    .module('devcafe.projects.jobs')
    .controller('JobsController', JobsController);

  JobsController.$inject = ['$http', '$location','$scope', '$rootScope', '$routeParams', '$timeout', 'Projects'];

  /**
  * @namespace JobsController
  */
  function JobsController($http, $location, $scope, $rootScope, $routeParams, $timeout, Projects) {
            var vm = this;

            $scope.options = [
                {name:'freelancer'  , value:'freelancer'},
                {name:'full-time'  , value:'fulltime'},
                {name:'part-time'  , value:'parttime'},
                {name:'volunteer'  , value:'volunteer'}
            ]

            $http.get('/projects/jobs/').success(function(data){
                $scope.jobs = data
                console.log($scope.jobs)
            })
  }
})();