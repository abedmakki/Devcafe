(function () {
  'use strict';

  angular
    .module('devcafe.userapp.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$scope', 'Userapp'];


  //na2es

  function ProfileController($location, $scope, userapp) {
    var vm = this;
    vm.getdata=getdata;


    function getdata() {
      userapp.getdata(1);
    }



}
})();
