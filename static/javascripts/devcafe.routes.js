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
    $routeProvider.when('/profile', {
        controller: 'ProfileController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/userapp/profile.html'
    }).when('/users/:id', {
        controller: 'ViewAnotherProfileController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/userapp/profile.html'
    }).when('/register', {
        controller: 'RegisterController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/userapp/register.html'
    }).when('/editprofile', {
        controller: 'ProfileController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/userapp/edit.html'
    }).when('/login', {
        controller: 'LoginController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/userapp/login.html'
    }).when('/', {
        controller: 'IdeasController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/ideas/ideas.html'
    }).when('/ideas', {
        controller: 'IdeasController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/ideas/ideas.html'
    }).when('/ideas/:id', {
        controller: 'IdeasController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/ideas/idea-detail.html'
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
    }).when('/market/:id/buy/deliveryinfo', {
        controller: 'MarketplaceDetailController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/market-required-info-application.html'
    }).when('/market/post/new', {
        controller: 'MarketplaceController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/upload-page-info.html'
    }).when('/market/post/new/upload', {
        controller: 'MarketplaceController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/upload-app-files.html'
    }).when('/view_transactions', {
        controller: 'ViewTransactionsController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/marketplace/view-transactions.html'
    }).when('/projects', {
        controller: 'ProjectsController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/projects/projects-view.html'
    }).when('/projects/:id', {
        controller: 'ProjectDetailedController',
        controllerAs: 'vm',
        templateUrl: '/static/templates/projects/project-detailed-page.html'
    }).otherwise('/ideas')
}
})();

