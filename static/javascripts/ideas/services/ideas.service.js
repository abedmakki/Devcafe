/**
* ideas
* @namespace devcafe.ideas.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.services')
    .factory('ideas', ideas);

  ideas.$inject = ['$http'];

  /**
  * @namespace ideas
  * @returns {Factory}
  */
  function ideas($http) {
    var ideas = {
      all: all,
      create: create,
      get: get
    };

    return ideas;

    ////////////////////

    /**
    * @name all
    * @desc Get all ideas
    * @returns {Promise}
    * @memberOf devcafe.ideas.services.ideas
    */
    function all() {
      return $http.get('/ideas/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf devcafe.ideas.services.ideas
    */
    function create(content) {
      return $http.post('/ideas/', {
        content: content
      });
    }

    /**
     * @name get
     * @desc Get the ideas of a given user
     * @param {string} username The username to get ideas for
     * @returns {Promise}
     * @memberOf devcafe.ideas.services.ideas
     */
    function get(username) {
      return $http.get('/users/:id' + username + '/ideas/');
    }
  }
})();