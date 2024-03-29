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
            var createdAppId = null;
            Market.all().success(function(data, status, headers, config) {
                $scope.apps = data;
            })

           $scope.$watch(function () {
            return $location.path();
            }, function(value) {
                if ($location.path() === '/market/post/new/upload' && createdAppId === null) {
                    $location.path('/market');
                };

            });

            Market.tags().success(function(data, status, headers, config) {
                $scope.all_tags = data;
            })

            $scope.$watch('pics', function () {
                if($scope.pics==null || $scope.pics==undefined || $scope.pics==''){
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
      Market.create(name, price, description, picture).success(function(data, status, headers, config) {
        window.createdAppId = data.id;
        console.log('Created app ID: ' + window.createdAppId);
      });
      $location.path('/market/post/new/upload');
    }

    $scope.upload = function (pics, files) {
        console.log('ID is: ' + window.createdAppId);
        if (pics && pics.length) {
            for (var i = 0; i < pics.length; i++) {
                var file = pics[i];
                Upload.upload({
                    url: '/market/' + window.createdAppId + '/upload/',
                    file: file
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                    $scope.pics.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
                }).success(function (data, status, headers, config) {
                    console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                    $scope.pics.result = data;
                    $( ".sjqclass").attr("disabled", 'disabled' )

                    $('#marketPhotoModel').on('hide.bs.modal', function (e) {
                        $( ".profilepic").attr("ng-src", data.picture )
                        $( ".profilepic").attr("src", data.picture )
                    })

                });
            }
        }

        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                Upload.upload({
                    url: '/market/' + window.createdAppId + '/upload_file/',
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
    };



  }
})();