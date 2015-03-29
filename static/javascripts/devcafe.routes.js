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
    }).otherwise('/');
  }
})();
