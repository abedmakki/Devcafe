/**
* Projects
* @namespace devcafe.Projects.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.projects.services')
    .factory('Projects', Projects);

  Projects.$inject = ['$http' , 'Upload'];

  /**
  * @namespace Projects
  * @returns {Factory}
  */
  function Projects($http , Upload) {
    var Projects = {
      all: all,
      assign: assign,
      // create: create,
      get: get,
      view_my_tasks: view_my_tasks,
      applyForJob: applyForJob,
      // comment: comment,
      changeLogo: changeLogo,
      createJob: createJob,
      viewRequest: viewRequest
      };

    return Projects;

    ////////////////////

    /**
    * @name all
    * @desc Get all Projects
    * @returns {Promise}
    * @memberOf devcafe.Projects.services.Projects
    */
    function all() {
      return $http.get('/projects/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf devcafe.Projects.services.Projects
    */
    // function create(title , description) {
    //   return $http.post('/projects/', {
    //     description: description,
    //     title: title,
    //     rating: 0,
    //     tags: []
    //   }).then(function() {
    //       window.location = '/projects';
    //     });
    // }

    /**
     * @name get
     * @desc Get the Projects of a given user
     * @param {string} username The username to get Projects for
     * @returns {Promise}
     * @memberOf devcafe.Projects.services.Projects
     */
    function get(id) {
      return $http.get('/projects/' + id + '/');
    }

    // function comment(id, text) {
    //   return $http.post('/projects/' + id + '/add_comment/', {
    //     text: text
    //   }).then(function() {
    //     window.location = '/projects';
    //   });
    // }

    function assign(contributor_id, title, description) {
      return $http.post('/projects/assign_task/' + contributor_id + '/', {
        title: title,
        description: description
        // issued_to: contributor_id,
        // project: id,
        // is_taken: false
      })
    }

    function view_my_tasks(id){
      return $http.get('/projects/' + id + '/view_my_tasks/');
    }


    function applyForJob(jobId){
      return $http.post('/projects/jobs/' + jobId + '/');
    }


    function changeLogo(files,$scope){
        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                Upload.upload({
                    url: '/projects/changelogo/',
                    file: file,
                    fields: {'projid': $scope.projId.id}
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                    $scope.logo.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
                }).success(function (data, status, headers, config) {
                    console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                    $scope.logo.result = data;
                    $( ".sjqclass").attr("disabled", 'disabled' )

                    $('#logo').on('hide.bs.modal', function (e) {
                        $( ".proj-logo").attr("ng-src", data.logo )
                        $( ".proj-logo").attr("src", data.logo )
                    })

                });
            }
        }
    }

function viewRequest(id){
      return $http.get('/projects/' + id + '/view_requests/');
    }

          function createJob(id , name, description) {
      return $http.post('/projects/'+id+'/create_job/', {
        name: name,
        description: description
      })
    }


  }
})();