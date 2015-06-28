(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('ViewAnotherProfileController', ViewAnotherProfileController);

    ViewAnotherProfileController.$inject = ['$http', '$location', '$scope', '$routeParams', '$cookies', 'Userapp'];
        function ViewAnotherProfileController($http, $location, $scope, $routeParams, $cookies, Userapp) {
            var userId = $routeParams.id;
            $http.get('/users/' + userId + '/').success(function(data, status, headers, config) {
                $scope.user = data;
                if (userId === $cookies.accId) {
                    $scope.otherProfile = false;
                } else {
                    $scope.otherProfile = true;
                };
        }).error(function(data, status, headers, config) {
            console.log('Account does not exist');
            $location.path('/');
        })
    }
})();
