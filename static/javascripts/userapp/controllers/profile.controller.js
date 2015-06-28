(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['$http', '$location', '$scope', 'Userapp'];

        function ProfileController($http, $location, $scope, Userapp) {
            $http.get('/users/profile/').success(function(data, status, headers, config) {
                $scope.user = data;
        })
    }
})();
