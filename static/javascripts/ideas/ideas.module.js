(function () {
  'use strict';

  angular
    .module('devcafe.ideas', [
      'devcafe.ideas.controllers',
      'devcafe.ideas.directives',
      'devcafe.ideas.services'
    ]);

  angular
    .module('devcafe.ideas.controllers', []);

  angular
    .module('devcafe.ideas.directives', ['ngDialog']);

  angular
    .module('devcafe.ideas.services', []);
})();