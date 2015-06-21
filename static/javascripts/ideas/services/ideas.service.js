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
      get: get,
      comment: comment,
      rate: rate,
      like: like,
      realize: realize
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
    function create(title , description) {
      return $http.post('/ideas/', {
        description: description,
        title: title,
        rating: 0,
        tags: []
      }).then(function() {
          window.location = '/ideas';
      });
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

    function comment(id, text) {
      return $http.post('/ideas/' + id + '/add_comment/', {
        text: text
      });
    }


    function rate(id, value) {
      // return $http.post('/ideas/' + id + '/rate/', {
      //   value: value        
      // }).then(function() {
      //       window.location = '/ideas';
      // });
      return $http.post('/ideas/' + id + '/rate/', {
        value: value        
      });
    }


    function like(id) {
      return $http.post('/ideas/' + id + '/like/', {
      }).then(function() {
        window.location = '/ideas';
      });
    }


    // function realize(id) {
    //   //url here
    //   return $http.get('/project/' + id + '/', {
           
    //   });
    // }

    function realize(title, description) {
      //url here
      console.log(title);
      return $http.post('/projects/', {
        title: title,
        description: description        
      });
    }

  }
})();