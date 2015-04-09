/**
* IndexController
* @namespace devcafe.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Userapp', 'ideas', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Userapp, ideas, Snackbar) {
    var vm = this;

    vm.isAuthenticated = Userapp.isAuthenticated();
    vm.ideas = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf devcafe.layout.controllers.IndexController
    */
    function activate() {
      ideas.all().then(ideasSuccessFn, ideasErrorFn);

      $scope.$on('idea.created', function (event, idea) {
        vm.ideas.unshift(idea);
      });

      $scope.$on('idea.created.error', function () {
        vm.ideas.shift();
      });


      /**
      * @name ideasSuccessFn
      * @desc Update ideas array on view
      */
      function ideasSuccessFn(data, status, headers, config) {
        vm.ideas = data.data;
      }


      /**
      * @name ideasErrorFn
      * @desc Show snackbar with error
      */
      function ideasErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();