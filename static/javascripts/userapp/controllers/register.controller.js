(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Userapp'];

    /**
    * @namespace RegisterController
    */
    function RegisterController($location, $scope, Userapp) {
        var vm = this;

        vm.register = register;

        activate();

        /**
        * @name activate
        * @desc Actions to be performed when this controller is instantiated
        * @memberOf devcafe.authentication.controllers.RegisterController
        */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Userapp.isAuthenticated()) {
                $location.url('/');
            }
        }

        /**
        * @name register
        * @desc Register a new user
        * @memberOf devcafe.authentication.controllers.RegisterController
        */
        function register() {
            Userapp.register(vm.username, vm.firstname, vm.lastname, vm.birthdate, vm.password, vm.country,
                             vm.email, vm.address);
        }
    }
})();



