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

    var vm = this;
    vm.edit = edit;



    function edit(email, username, password, firstname, lastname, birthdate, country, address) {
      var id = $scope.user.id;
      Userapp.edit(id, username, firstname, lastname, birthdate, password, country,
        email, address);
    }
  }

})();
