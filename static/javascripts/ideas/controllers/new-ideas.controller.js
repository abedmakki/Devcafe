/**
* NewideaController
* @namespace devcafe.ideas.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.controllers')
    .controller('NewideaController', NewideaController);

  NewideaController.$inject = ['$rootScope', '$scope', 'Userapp', 'Snackbar', 'ideas'];

  /**
  * @namespace NewideaController
  */
  function NewideaController($rootScope, $scope, Userapp, Snackbar, ideas) {
    var vm = this;

    vm.submit = submit;

    /**
    * @name submit
    * @desc Create a new idea
    * @memberOf devcafe.ideas.controllers.NewideaController
    */
    function submit() {
      $rootScope.$broadcast('idea.created', {
        content: vm.content,
        author: {
          username: Userapp.getAuthenticatedAccount().username
        }
      });

      $scope.closeThisDialog();

      ideas.create(vm.content).then(createideaSuccessFn, createideaErrorFn);


      /**
      * @name createideaSuccessFn
      * @desc Show snackbar with success message
      */
      function createideaSuccessFn(data, status, headers, config) {
        Snackbar.show('Success! idea created.');
      }


      /**
      * @name createideaErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createideaErrorFn(data, status, headers, config) {
        $rootScope.$broadcast('idea.created.error');
        Snackbar.error(data.error);
      }
    }
  }
})();