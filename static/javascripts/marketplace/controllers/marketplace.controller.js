/**
* MarketplaceController
* @namespace devcafe.marketplace.controllers
*/
(function () {
  'use strict';

  angular
  .module('devcafe.marketplace.controllers')
  .controller('MarketplaceController', MarketplaceController);

  MarketplaceController.$inject = ['$http', '$location','$scope', 'Upload', 'Market' , '$routeParams'];

  function MarketplaceController($http, $location, $scope, Upload, Market , $routeParams) {
    var vm = this;
    var createdAppId = null;

    /******* release from project **************/
    var projTitle =$routeParams.title;
    var projDesc =$routeParams.desc;
    if(projTitle!=null && projTitle.replace(/\s+/g, '')!='' && projTitle!=undefined){
        if(projDesc!=null && projDesc.replace(/\s+/g, '')!='' && projDesc!=undefined){
            vm.appname = projTitle;
            vm.description = projDesc;
        }
    }
    else{$location.path('/market')}
    /*****************************************/

    Market.all().success(function(data, status, headers, config) {
      $scope.apps = data;
    })


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
        $location.path('/market/post/new/upload');
      });

    }

    $scope.upload = function (pics, files) {
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
                });
              }
            }
          });
        }
      }
    }


    $scope.go = function(path)
    {
      $scope.pics = null;
      $scope.files = null;
      $location.path(path);
    };

  }
})();