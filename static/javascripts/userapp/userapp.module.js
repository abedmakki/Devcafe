(function () {
  'use strict';

  angular
    .module('devcafe.userapp', [
      'devcafe.userapp.controllers',
      'devcafe.userapp.services'
    ]);

  angular
    .module('devcafe.userapp.controllers', []);

  angular
    .module('devcafe.userapp.services', ['ngCookies']);
})();
