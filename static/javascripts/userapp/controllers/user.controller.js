angular.module("devcafe.userapp.controllers").controller("UserCtrl", 
	['$scope','$location', 'Facebook',
        function($scope, $location, Facebook /*we will write this factory next*/){
        
        $scope.login_fb = function(){
           Facebook.login().then(function(response){
               //this is where we'll contact backend. for now just log response 
               console.log(response);
           });
        }
}]);