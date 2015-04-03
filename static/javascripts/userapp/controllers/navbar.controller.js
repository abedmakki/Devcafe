(function () {
  'use strict';

  angular
    .module('devcafe.userapp.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    /**
    * @name logout
    * @desc Log the user out
    * @memberOf devcafe.userapp.controllers.NavbarController
    */
    function logout() {
      Authentication.logout();
    }
  }
})();