(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['$http', '$location', '$scope', 'Userapp'];


      //na2es

        function ProfileController($http, $location, $scope, Userapp) {
            $http.get('/users/profile/').success(function(data, status, headers, config) {
                $scope.user = data;
        })
            
            var userid = Userapp.getAccId();
            $http.get('/users/' + userid + '/').success(function(data, status, headers, config) {
            $scope.user = data;
        });
            
            var vm = this;
            vm.edit = edit;

            activate();

            function activate() {
                // If the user is authenticated, they should not be here.
                if (!Userapp.isAuthenticated()) {
                    $location.url('/');
                }
            }

            function edit() {
                Userapp.edit(vm.username, vm.firstname, vm.lastname, vm.birthdate, vm.password, vm.country,
                                 vm.email, vm.address);
            }

        });

    }
})();
