(function () {
  'use strict';

  angular
    .module('devcafe.viewideas.controllers')
    .controller('viewideasController', viewideasController);

  viewideasController.$inject = ['$location', '$routeParams', 'Posts', 'viewideas', 'Snackbar'];

  /**
  * @namespace viewideasController
  */
  function viewideasController($location, $routeParams, Posts, viewideas, Snackbar) {
    var vm = this;

    vm.viewideas = undefined;
    vm.posts = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf devcafe.viewideas.controllers.viewideasController
    */
    function activate() {
      var idea = $routeParams.idea.substr(1);

      viewideas.get(idea).then(viewideasSuccessFn, viewideasErrorFn);
      Posts.get(idea).then(postsSuccessFn, postsErrorFn);

      /**
      * @name viewideasSuccessviewideas
      * @desc Update `viewideas` on viewmodel
      */
      function viewideasSuccessFn(data, status, headers, config) {
        vm.viewideas = data.data;
      }


      /**
      * @name viewideasErrorFn
      * @desc Redirect to index and show error Snackbar
      */
      function viewideasErrorFn(data, status, headers, config) {
        $location.url('/');
        Snackbar.error('That idea does not exist.');
      }


      /**
        * @name postsSucessFn
        * @desc Update `posts` on viewmodel
        */
      function postsSuccessFn(data, status, headers, config) {
        vm.posts = data.data;
      }


      /**
        * @name postsErrorFn
        * @desc Show error snackbar
        */
      function postsErrorFn(data, status, headers, config) {
        Snackbar.error(data.data.error);
      }
    }
  }
})();