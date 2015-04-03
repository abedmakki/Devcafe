/**
* NavbarController
* @namespace devcafe.layout.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.layout.controllers')
        .controller('NavbarController', NavbarController);

        NavbarController.$inject = ['$scope', 'Userapp'];

    /**
    * @namespace NavbarController
    */
    function NavbarController($scope, Userapp) {
        var vm = this;

        vm.logout = logout;

        /**
        * @name logout
        * @desc Log the user out
        * @memberOf devcafe.layout.controllers.NavbarController
        */
        function logout() {
            Userapp.logout();
        }
    }
})();
