(function () {
  'use strict';

  angular
    .module('devcafe.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/profile/', {    //na2es/profile/number . ":num" de s7.. eslam
      controller: 'ProfileController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/userapp/profile.html'
    }).when('/register/', {
      controller: 'RegisterController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/userapp/register.html'
        }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/userapp/login.html'
        }).otherwise('/');
  }
})();

