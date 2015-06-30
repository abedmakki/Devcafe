(function () {
  'use strict';

  angular
    .module('devcafe.projects', [
      'devcafe.projects.controllers',
      'devcafe.projects.services',
      'devcafe.projects.jobs'
    ]);

  angular
    .module('devcafe.projects.controllers', ['ngFileUpload']);

  angular
    .module('devcafe.projects.services', []);

  angular
    .module('devcafe.projects.jobs', []);
})();