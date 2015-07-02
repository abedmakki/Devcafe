(function () {
    'use strict';

    angular.module('devcafe', ['devcafe.routes', 'devcafe.config','devcafe.userapp', 'devcafe.layout', 'devcafe.ideas', 'devcafe.marketplace', 'devcafe.projects', 'devcafe.utils', 'devcafe.datepicker', 'devcafe.fileUpload' , 'devcafe.countrySelect' , 'devcafe.errorValidation' , 'angulike']);

    angular.module('devcafe.routes', ['ngRoute']);

    angular.module('devcafe.config', []);

    angular.module('devcafe').run(run);

    run.$inject = ['$http','$rootScope','$cookies'];

    function run($http , $rootScope , $cookies) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
        if(!!$cookies.authenticatedAccount){
            $rootScope.login=true;
        }else{$rootScope.login=false;}
        $rootScope.facebookAppId = '1585590368357539';
    }
}) ();