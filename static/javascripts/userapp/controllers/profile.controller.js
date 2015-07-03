(function () {
  'use strict';

  angular
  .module('devcafe.userapp.controllers')
  .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$http', '$location', '$scope', 'Userapp','Market','Projects','$anchorScroll','$timeout'];

  function ProfileController($http, $location, $scope, Userapp,Market,Projects,$anchorScroll,$timeout) {
    $http.get('/users/profile/').success(function(data, status, headers, config) {
      $scope.user = data;
    })

    Market.view_transactions().success(function(data, status, headers, config) {
          $scope.transactions = data;
        if ($scope.transactions.length==0) $scope.transactions=false;
      })
    Market.view_my_apps().success(function(data, status, headers, config){
          $scope.my_apps = data;
        if ($scope.my_apps.length==0) $scope.my_apps=false;
      })

    Projects.getMyProjects().success(function(data){
        $scope.myProjects = data;
        if ($scope.myProjects.length==0) $scope.myProjects=false;
    })

      var vm = this;
    vm.edit = edit;
    vm.scrolto = scrolto;
    vm.getDateTime = getDateTime;


    function edit(email, username, password, firstname, lastname, birthdate, country, address) {
      var id = $scope.user.id;
      Userapp.edit(id, username, firstname, lastname, birthdate, password, country,
        email, address);
    }

    function scrolto(id){
        $timeout(function() {
            $location.hash(id);
            $anchorScroll();
        },300);
    }

      function getDateTime(datetime){
          var dd= new Date(datetime)
          return $.datepicker.formatDate("dd/mm/yy", dd)+' '+$.datepicker.formatTime('hh:mm TT', {hour: dd.getHours(), minute: dd.getMinutes(), timezone: '+2000' })
      }



  }

})();
