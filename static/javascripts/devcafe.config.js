(function () {
  'use strict';

  angular
    .module('devcafe.config')
    .config(config);

  config.$inject = ['$locationProvider' , '$httpProvider'];

  /**
  * @name config
  * @desc Enable HTML5 routing
  */
  function config($locationProvider ,$httpProvider) {
      $locationProvider.html5Mode(true);
      $locationProvider.hashPrefix('!');

      $httpProvider.interceptors.push(['$injector', function($injector) {
        var AuthInterceptor = {
                request: function (config) {
                    var Auth = $injector.get('Userapp');
                    var token = Auth.getAuthenticatedAccount();
                    if (token) {
                        config.headers['Authorization'] = 'Token ' + token;
                    }
                    return config;
                }
            }
            return AuthInterceptor;
    }]);

      $httpProvider.interceptors.push(['$q', function($q) {
        var UnauthorizedResponse = {
            responseError: function (response) {
                if (response.status == 401 ) {
                    window.location = '/login'
                }
                return $q.reject(response);
            }
        }
          return UnauthorizedResponse
    }]);


  }
})();
