/**
* ideas
* @namespace devcafe.ideas.directives
*/
(function () {
    'use strict';

    angular
        .module('devcafe.ideas.directives')
        .directive('ideas', ideas);

    /**
    * @namespace ideas
    */
    function ideas() {
        /**
        * @name directive
        * @desc The directive to be returned
        * @memberOf devcafe.ideas.directives.ideas
        */
        var directive = {
            controller: 'ideasController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                ideas: '='
            },
            templateUrl: '/static/templates/ideas/ideas.html'
        };

        return directive;
    }
    })();
