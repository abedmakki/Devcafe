(function () {
  'use strict';

  angular
    .module('devcafe.marketplace', [
      'devcafe.marketplace.controllers',
      'devcafe.marketplace.services',
      'devcafe.marketplace.directives'
    ]);

  angular
    .module('devcafe.marketplace.controllers', []);

  angular
    .module('devcafe.marketplace.services', ['ngCookies']);

  angular
    .module('devcafe.marketplace.directives', []);
})();
