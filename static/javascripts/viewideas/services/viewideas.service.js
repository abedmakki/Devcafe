(function () {
  'use strict';

  angular
    .module('devcafe.viewideas.services')
    .factory('viewideas', viewideas);

  viewideas.$inject = ['$http'];

  /**
  * @namespace viewidea
  */
  function viewideas($http) {
    /**
    * @name viewidea
    * @desc The factory to be returned
    * @memberOf devcafe.viewideas.services.viewidea
    */
    var viewideas = {
      destroy: destroy,
      get: get,
      update: update
    };

    return viewideas;

    /////////////////////

    /**
    * @name destroy
    * @desc Destroys the given viewidea
    * @param {Object} viewidea The viewidea to be destroyed
    * @returns {Promise}
    * @memberOf devcafe.viewideas.services.viewidea
    */
    function destroy(viewideas) {
      return $http.delete('/ideas/' + viewideas.id + '/');
    }


    /**
    * @name get
    * @desc Gets the viewidea for user with username `username`
    * @param {string} username The username of the user to fetch
    * @returns {Promise}
    * @memberOf devcafe.viewideas.services.viewidea
    */
    function get(username) {
      return $http.get('/ideas/' + username + '/');
    }


    /**
    * @name update
    * @desc Update the given viewidea
    * @param {Object} viewidea The viewidea to be updated
    * @returns {Promise}
    * @memberOf devcafe.viewideas.services.viewidea
    */
    function update(viewideas) {
      return $http.put('/ideas/' + viewidea.username + '/', viewideas);
    }
  }
})();