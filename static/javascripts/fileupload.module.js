/**
 * Created by Abedmakki on 30/04/2015.
 */
(function () {
    'use strict';

var app = angular.module('devcafe.fileUpload', ['ngFileUpload']);

app.controller('uploadCtrl', ['$scope', 'Upload', function ($scope, Upload) {
    $scope.$watch('files', function () {
                if($scope.files==null || $scope.files==undefined || $scope.files==''){
            $( ".sjqclass").attr("disabled", 'disabled' )
        }
        else{
            $(".sjqclass").removeAttr( 'disabled' );
        }
    });

    $scope.upload = function (files) {
        if (files && files.length) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                Upload.upload({
                    url: '/users/uploadpicture/',
                    file: file
                }).progress(function (evt) {
                    var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                    console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                    $scope.files.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
                }).success(function (data, status, headers, config) {
                    console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
                    $scope.files.result = data;
                    $( ".sjqclass").attr("disabled", 'disabled' )

                    $('#profilePhotoModel').on('hide.bs.modal', function (e) {
                        $( ".profilepic").attr("ng-src", data.picture )
                        $( ".profilepic").attr("src", data.picture )
                    })

                });
            }
        }
    };


}])
    })();