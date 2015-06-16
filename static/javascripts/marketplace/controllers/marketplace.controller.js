/**
* MarketplaceController
* @namespace devcafe.marketplace.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.controllers')
    .controller('MarketplaceController', MarketplaceController);

  MarketplaceController.$inject = ['$http', '$location','$scope', 'Upload', 'Market'];

  function MarketplaceController($http, $location, $scope, Upload, Market) {
            var vm = this;
            // var appId = null;
            var createdAppId = null;
            // vm.Like = Like;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
                // $scope.$watch("rating", function(){
                //   console.log($scope.rating);
                // });
            })

            Market.tags().success(function(data, status, headers, config) {
                $scope.all_tags = data;
                // $scope.$watch("rating", function(){
                //   console.log($scope.rating);
                // });
            })

            $scope.$watch('files', function () {
                if($scope.files==null || $scope.files==undefined || $scope.files==''){
            $( ".sjqclass").attr("disabled", 'disabled' )
                }
                else{
                    $(".sjqclass").removeAttr( 'disabled' );
                }
            });


    $scope.rateFunction = function(id, value) {
      Market.rate(id, value);
    };

    $scope.Create = function(name, price, description, picture) {
      // console.log('upload');
      Market.create(name, price, description, picture).success(function(data, status, headers, config) {
        window.createdAppId = data.id;
        console.log('Created app ID: ' + window.createdAppId);
      });
      $location.path('/market/post/new/upload');
    }

    $scope.upload = function (files) {
        console.log('ID is: ' + window.createdAppId);
        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                Upload.upload({
                    url: '/market/' + window.createdAppId + '/upload/',
                    file: file
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                    $scope.files.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
                }).success(function (data, status, headers, config) {
                    console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                    $scope.files.result = data;
                    $( ".sjqclass").attr("disabled", 'disabled' )

                    $('#marketPhotoModel').on('hide.bs.modal', function (e) {
                        $( ".profilepic").attr("ng-src", data.picture )
                        $( ".profilepic").attr("src", data.picture )
                    })

                });
            }
        }
        // if (files && files.length) {
        //     for (var i = 0; i < files.length; i++) {
        //         var pic = files[i];
        //         Upload.upload({
        //             url: '/market/' + window.createdAppId + '/upload/',
        //             pic: pic
        //         }).progress(function (evt) {
        //             var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
        //             console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
        //             $scope.files.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
        //         }).success(function (data, status, headers, config) {
        //             console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
        //             $scope.files.result = data;
        //             $( ".sjqclass").attr("disabled", 'disabled' )

        //             $('#profilePhotoModel').on('hide.bs.modal', function (e) {
        //                 $( ".profilepic").attr("ng-src", data.picture )
        //                 $( ".profilepic").attr("src", data.picture )
        //             })

        //         });
        //     }
        // }
    };



  }
})();