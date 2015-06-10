(function () {
  'use strict';

  angular
  	.module('devcafe.ideas.controllers')
  	.controller('RatingIdeasController', RatingIdeasController);

  	RatingIdeasController.$inject = ['$http', '$location','$scope', 'Ideas'];
  	 
  	function RatingIdeasController($http, $location, $scope, Ideas) {
    // RatingIdeas.all().success(function(data, status, headers, config) {
    // $scope.rating = rating; 


    $scope.rateFunction = function(id, value) {
      Ideas.rate(id, value);
    };
    // })
    }
//starting here msh 3arfa
//http://www.angulartutorial.net/2014/03/rating-stars-in-angular-js-using.html

//feh dh kman
//http://codepen.io/TepigMC/pen/FIdHb


/////here
// $scope.rateFunction = function( rating )
// {
//        var _url = 'your service url';
 
//  var data = {
//    rating: rating
//  };
 
//  $http.post( _url, angular.toJson(data), {cache: false} )
//   .success( function( data )
//   {
//    success(data);
//   })
//   .error(function(data){
//     error(data);
//   });
 
// };





 })();