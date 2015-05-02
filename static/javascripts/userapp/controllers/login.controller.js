/**
* LoginController
* @namespace devcafe.userapp.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Userapp'];

    /**
    * @namespace LoginController
    */
    function LoginController($location, $scope, Userapp) {
        var vm = this;

        vm.login = login;

        activate();

        /**
        * @name activate
        * @desc Actions to be performed when this controller is instantiated
        * @memberOf devcafe.userapp.controllers.LoginController
        */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Userapp.isAuthenticated()) {
              $location.url('/');
            }
        }

        /**
        * @name login
        * @desc Log the user in
        * @memberOf devcafe.userapp.controllers.LoginController
        */
        function login() {
            Userapp.login(vm.username, vm.password , vm.remember , $scope);
        }
    }
})();
