/**
* Projects
* @namespace devcafe.Projects.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.projects.services')
    .factory('Projects', Projects);

  Projects.$inject = ['$http'];

  /**
  * @namespace Projects
  * @returns {Factory}
  */
  function Projects($http) {
    var Projects = {
      all: all,
      assign: assign,
      // create: create,
      get: get
      // comment: comment,
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


  }
})();