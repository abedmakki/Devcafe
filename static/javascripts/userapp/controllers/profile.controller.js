(function () {
    'use strict';

    angular
        .module('devcafe.userapp.controllers')
        .controller('ProfileController', ProfileController);

    ProfileController.$inject = ['$http', '$location', '$scope', 'Userapp'];


    

        function ProfileController($http, $location, $scope, Userapp) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            $http.get('/users/profile/').success(function(data, status, headers, config) {
                $scope.user = data;
        })

            var vm = this;
            vm.edit = edit;


    
        function edit(email, username, password, firstname, lastname, birthdate, country, address) {
            // console.log($scope.user.id);
            var id = $scope.user.id;
            
            // if(email == "")
            //     email = $scope.user.email;
            // if(username == "")
            //     username = $scope.user.username;
            // // if(password == "")
            // //     password = $scope.user.password;
            // if(firstname == "")
            //     firstname = $scope.user.first_name;
            // if(lastname == "")
            //     lastname = $scope.user.last_name;
            // if(country == "")
            //     country = $scope.user.country;
            // if(address == "")
            //     address = $scope.user.address;
            // if(birthdate == "")
            //     birthdate = $scope.user.birth_date;
            // console.log($scope.user.address);
            // console.log($scope.user.birthdate);
            // console.log($scope.user.country);
            


            Userapp.edit(id, username, firstname, lastname, birthdate, password, country,
         email, address);
        }
    }
    
})();
