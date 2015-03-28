/**
* Posts
* @namespace thinkster.posts.services
*/
(function () {
  'use strict';

  angular
    .module('DevCafe.ideas.services')
    .factory('Ideas', Ideas);

  Ideas.$inject = ['$http'];

  /**
  * @namespace Posts
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
    * @desc Get all Posts
    * @returns {Promise}
    * @memberOf thinkster.posts.services.Posts
    */
    function all() {
      return $http.get('/ideas/').success(function(data) {
        $scope.artists = data;
      });
    }


    /**
    * @name create
    * @desc Create a new Post
    * @param {string} content The content of the new Post
    * @returns {Promise}
    * @memberOf thinkster.posts.services.Posts
    */
    function create(content) {
      return $http.post('/ideas/', {
        content: content
      });
    }

    /**
     * @name get
     * @desc Get the Posts of a given user
     * @param {string} username The username to get Posts for
     * @returns {Promise}
     * @memberOf thinkster.posts.services.Posts
     */
    // function get(username) {
    //   return $http.get('/api/v1/accounts/' + username + '/posts/');
    // }
  }
})();
