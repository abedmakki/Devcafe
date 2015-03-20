var myApp = angular.module('myApp', []);

myApp.controller('MyController', ['$scope', '$http', function($scope, $http) {
  $http.get('ideas/').success(function(data) {
    $scope.artists = data;
  });
}]);

