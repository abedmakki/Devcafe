(function () {
  'use strict';

  angular
    .module('devcafe.userapp.controllers')
    .controller('ProfileController', function($scope, $http) {
      $http.get('/users/28/').success(function(data, status, headers, config) {
        $scope.user = data;
      });
    });



  // angular
  //   .module('devcafe.userapp.controllers')
  //   .controller('ProfileController', ProfileController);

//   ProfileController.$inject = ['$location', '$scope', 'Userapp'];


//   //na2es

//   function ProfileController($location, $scope, userapp) {
//     var vm = this;
//     vm.getdata=getdata;


//     function getdata() {
//       Userapp.getdata(1);
//     }



// }
})();
