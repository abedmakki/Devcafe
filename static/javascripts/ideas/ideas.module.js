(function () {
  'use strict';

  angular
    .module('DevCafe.ideas', [
      'DevCafe.ideas.controllers',
      'DevCafe.ideas.services'
    ]);

  angular
    .module('DevCafe.ideas.controllers', []);

  angular
    .module('DevCafe.ideas.services', ['ngCookies']);
})();
