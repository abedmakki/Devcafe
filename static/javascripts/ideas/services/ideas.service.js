/**
* Ideas
* @namespace devcafe.Ideas.services
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.services')
    .factory('Ideas', Ideas);

  Ideas.$inject = ['$http'];

  /**
  * @namespace Ideas
  * @returns {Factory}
  */
  function Ideas($http) {
    var Ideas = {
      all: all,
      create: create,
      get: get
    };

    return Ideas;

    ////////////////////

    /**
    * @name all
    * @desc Get all Ideas
    * @returns {Promise}
    * @memberOf devcafe.Ideas.services.Ideas
    */
    function all() {
      return $http.get('/ideas/');
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf devcafe.Ideas.services.Ideas
    */
    function create(title , content) {
      return $http.post('/ideas/', {
        content: content,
        title: title,
        tags: null,
        rate:null
      }).then(function() {
                window.location = '/ideas';
            });;
    }

    /**
     * @name get
     * @desc Get the Ideas of a given user
     * @param {string} username The username to get Ideas for
     * @returns {Promise}
     * @memberOf devcafe.Ideas.services.Ideas
     */
    function get(id) {
      return $http.get('/ideas/' + id + '/');
    }
  }
})();