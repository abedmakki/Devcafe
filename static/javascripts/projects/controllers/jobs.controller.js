/**
 * Created by Abedmakki on 30/06/2015.
 */

(function () {
    'use strict';

    angular
        .module('devcafe.projects.jobs')
        .controller('JobsController', JobsController);

    JobsController.$inject = ['$http', '$location','$scope', 'Projects','$timeout'];

    /**
     * @namespace JobsController
     */
    function JobsController($http, $location, $scope, Projects,$timeout) {
        var vm = this;
        vm.details = details;
        vm.applyForJob = applyForJob;
        vm.getUser = getUser;
        vm.getProj = getProj;

        /***** get all jobs ****************/
        $http.get('/projects/jobs/').success(function(data){
            $scope.jobs = data
        })
        /**********************************/

        /***** show job details ***********/
        function details(id){
            //alert('details')
            var index = function(tid) {
                for (var i = 0, len = $scope.jobs.length; i < len; i++)
                    if ($scope.jobs[i].id === tid)
                        return i;}
            $scope.jobDet =$scope.jobs[index(id)]
            var dt = getJobDateTime($scope.jobDet.time_posted)
            $scope.jobDateTime = dt
            $('#JobModal').modal('show')
        }
        /*********************************/

        /*$scope.$watch('jobDet', function () {
            if($scope.jobDet!=null){$(".jdetail").hide().show(1000)}
            else{$(".jdetail").hide()}
        });*/
        /*********************************/

        /******** Apply for job **********/
        function applyForJob(jobId , pid){
            Projects.applyForJob(jobId).success(function(data){
                $('#JobModal').modal('hide');
                $timeout(function() {
                    $location.path('/projects/' + pid)
                },500);
                $.notify("Congratulation\nsuccess applying for job\nthis is the project's page\nNow wait project manager to accept",{ position:"bottom right" ,className:"success",autoHideDelay: 8000});
            })
        }
        /*********************************/

        function getJobDateTime(datetime){
                var dd= new Date(datetime)
                return $.datepicker.formatDate("dd/mm/yy", dd)+' '+$.datepicker.formatTime('hh:mm TT', {hour: dd.getHours(), minute: dd.getMinutes(), timezone: '+2000' })
            }
        /*********************************/

        function getUser(uid ,e){
            if(e){e.stopPropagation()}
            try{$('#JobModal').modal('hide');}catch (e){console.log(e)}
            $timeout(function() {
                $location.path('/users/' + uid)
            },500);
        }

        function getProj(pid){
            $('#JobModal').modal('hide');
            $timeout(function() {
                $location.path('/projects/' + pid)
            }, 500);
        }
    }
})();