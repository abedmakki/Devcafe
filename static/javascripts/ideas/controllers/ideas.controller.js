(function () {
  'use strict';

  angular
    .module('DevCafe.ideas.controllers')
    .controller('IdeasController', IdeasController);

  IdeasController.$inject = ['$scope'];

  /**
  * @namespace PostsController
  */
 function IdeasController($location, $scope, Ideas) {
    // var vm = this;

    // vm.login = login;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.authentication.controllers.LoginController
    */
    function activate() {
      Ideas.all();
    });
      // $http.get('ideas/').success(function(data) {
      // $scope.artists = data;
      }
    }

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.posts.controllers.PostsController
    */
    // function activate() {
    //   $scope.$watchCollection(function () { return $scope.posts; }, render);
    //   $scope.$watch(function () { return $(window).width(); }, render);
    // }
}) ();
