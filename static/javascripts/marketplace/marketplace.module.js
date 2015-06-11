(function () {
  'use strict';

  angular
    .module('devcafe.marketplace', [
      'devcafe.marketplace.controllers',
      'devcafe.marketplace.services'
    ]);

  angular
    .module('devcafe.marketplace.controllers', []);

  angular
    .module('devcafe.marketplace.services', ['ngCookies']);
})();
