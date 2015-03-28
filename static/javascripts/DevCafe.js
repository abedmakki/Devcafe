(function () {
    'use strict';

    angular.module('DevCafe', ['DevCafe.routes', 'DevCafe.config', 'DevCafe.ideas']);
// 'DevCafe.controllers',

    angular.module('DevCafe.routes', ['ngRoute']);

    angular.module('DevCafe.config', []);

    // angular.module('DevCafe.controllers', []);

    angular.module('DevCafe').run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
}) ();
