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
    }).when('/', {
        controller: 'IndexController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/layout/index.html'
    }).when('/ideas', {
        controller: 'IdeasController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/ideas/ideas.html'
    }).when('/market', {
        controller: 'MarketplaceController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/market-view.html'
    }).when('/market/:id', {
        controller: 'MarketplaceDetailController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/shop-app-page.html'
    }).when('/market/:id/buy', {
        controller: 'MarketplaceDetailController',
        controllerAs: 'vm',
        templateUrl: 'static/templates/marketplace/payment-page.html'
    }).otherwise('/')
}
})();

