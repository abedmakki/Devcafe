/**
* idea
* @namespace devcafe.idea.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.services')
    .factory('idea', idea);

  idea.$inject = ['$http'];

  /**
  * @namespace idea
  * @returns {Factory}
  */
  function idea($http) {
    var idea = {
      all: all,
      create: create,
      get: get
    };

    return idea;

    ////////////////////

    /**
    * @name all
    * @desc Get all idea
    * @returns {Promise}
    * @memberOf devcafe.idea.services.idea
    */
    function all() {
      return $http.get('/ideas/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf devcafe.idea.services.idea
    */
    function create(title , content) {
      return $http.post('/ideas/', {
        content: content,
        title: title,
        tags: null,
        rate:null
      }).then(function() {
                window.location = '/idea';
            });;
    }

    /**
     * @name get
     * @desc Get the idea of a given user
     * @param {string} username The username to get idea for
     * @returns {Promise}
     * @memberOf devcafe.idea.services.idea
     */
    function get(id) {
      return $http.get('/ideas/' + id + '/');
    }
  }
})();