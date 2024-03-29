(function () {
    'use strict';

    angular.module('devcafe', ['devcafe.routes', 'devcafe.config','devcafe.userapp', 'devcafe.layout', 'devcafe.ideas', 'devcafe.marketplace', 'devcafe.projects', 'devcafe.utils', 'devcafe.datepicker', 'devcafe.fileUpload' , 'devcafe.countrySelect' , 'devcafe.errorValidation']);

    angular.module('devcafe.routes', ['ngRoute']);

    angular.module('devcafe.config', []);

    angular.module('devcafe').run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
}) ();