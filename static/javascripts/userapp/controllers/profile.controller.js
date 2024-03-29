(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['$http', '$location', '$scope', 'Userapp'];


      //na2es

        function ProfileController($http, $location, $scope, Userapp) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            $http.get('/users/profile/').success(function(data, status, headers, config) {
                $scope.user = data;
        })
    }
})();
