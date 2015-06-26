
(function () {
  'use strict';

  angular
  .module('devcafe.projects.controllers')
  .controller('ProjectDetailedController', ProjectDetailedController);

  ProjectDetailedController.$inject = ['$http', '$location', '$scope', '$routeParams', 'Projects'];

  function ProjectDetailedController($http, $location, $scope, $routeParams, Projects) {
    var vm = this;
    vm.assignTask = assignTask;
    vm.changeLogo = changeLogo;
    var progress_ratio = 0;
    vm.createJob = createJob;
    vm.resolveRequest = resolveRequest;


    Projects.get($routeParams.id).success(function(data, status, headers, config) {
      $scope.projId = data;
      progress();
    })

    Projects.view_my_tasks($routeParams.id).success(function(data, status, headers, config) {
      $scope.mytasks = data;
    })

    Projects.viewRequest($routeParams.id).success(function(data, status, headers, config) {
      $scope.requests = data;
    })


    function assignTask(contributor_id, title, description) {

      // console.log($scope.projId.contributors.length);


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

    function progress(){
        var tasks_num = $scope.projId.project_tasks.length;
        var done_num = 0;
        if (tasks_num === 0){
          $scope.progress_ratio = 0;
        }
        else{
        for (var i = 0; i < tasks_num; i++){
          if ($scope.projId.project_tasks[i].is_done === true){
            done_num++;
          }
        }
        $scope.progress_ratio = Math.floor((done_num/tasks_num)*100);
      }
    }
      /**** Change Logo ****/
      $scope.$watch('logo', function () {
          if($scope.logo==null || $scope.logo==undefined || $scope.logo==''){
              $( ".sjqclass").attr("disabled", 'disabled' )
          }
          else{
              $(".sjqclass").removeAttr( 'disabled' );
          }
      });
      function changeLogo(logo){
          Projects.changeLogo(logo , $scope)
        }

    /**********************/

    /**** Create Job ****/
    function createJob(){
      Projects.createJob($routeParams.id , $scope.jName , $scope.jDesc).success(function(){
        $('#CreateJob').modal('hide');
        $.notify("Congratulation\nsuccess adding a new job",{ position:"bottom right" ,className:"success"});
      })
    }

    $('#CreateJob').on('hide.bs.modal', function (e) {
      $scope.creJob.$setPristine();
      $scope.jName=null;$scope.jDesc=null;
      $('#job-name').focus()
    })
    /**********************/

    /**** Resolve Job's request ****/
    function resolveRequest(reqID,yn){
      Projects.resolveRequest(reqID,yn).success(function(){
        $.notify("Congratulation\nsuccess accepting a new contributer for job",{ position:"bottom right" ,className:"success"});
      }).error(function(){
        $.notify("Sorry\nError in accepting a new contributer for job",{ position:"bottom right" });
      })
    }
    /**********************/


  }


})();
