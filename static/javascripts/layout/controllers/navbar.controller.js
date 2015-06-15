/**
* NavbarController
* @namespace devcafe.layout.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.layout.controllers')
        .controller('NavbarController', NavbarController);

        NavbarController.$inject = ['$scope', '$rootScope', 'Userapp'];

    /**
    * @namespace NavbarController
    */
    function NavbarController($scope, $rootScope, Userapp) {
        var vm = this;

        vm.logout = logout;

        $scope.$watch('search', function() {
            $rootScope.searchQuery = $scope.search;
        });
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
