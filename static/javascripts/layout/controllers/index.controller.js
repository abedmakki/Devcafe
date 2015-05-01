/**
* IndexController
* @namespace devcafe.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.layout.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$scope', 'Userapp', 'Ideas', 'Snackbar'];

  /**
  * @namespace IndexController
  */
  function IndexController($scope, Userapp, Ideas, Snackbar) {
    var vm = this;

    vm.isAuthenticated = Userapp.isAuthenticated();
    vm.idea = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf devcafe.layout.controllers.IndexController
    */
    function activate() {
      Ideas.all().then(ideaSuccessFn, ideaErrorFn);

      $scope.$on('idea.created', function (event, idea) {
        vm.idea.unshift(idea);
      });

      $scope.$on('idea.created.error', function () {
        vm.idea.shift();
      });


      /**
      * @name ideaSuccessFn
      * @desc Update idea array on view
      */
      function ideaSuccessFn(data, status, headers, config) {
        vm.ideas = data.data;
      }


      /**
      * @name ideaErrorFn
      * @desc Show snackbar with error
      */
      function ideaErrorFn(data, status, headers, config) {
        Snackbar.error(data.error);
      }
    }
  }
})();