(function () {
  'use strict';

  angular
    .module('DevCafe.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/idea', {
      controller: 'IdeasController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/ideas.html'
    }).otherwise('/');
  }
})();
