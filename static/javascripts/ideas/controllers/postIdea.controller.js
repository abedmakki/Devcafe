/**
* PostIdeaController
* @namespace devcafe.userapp.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.ideas.controllers')
        .controller('PostIdeaController', PostIdeaController);

    PostIdeaController.$inject = ['$location', '$scope', 'Userapp','idea'];

    /**
    * @namespace PostIdeaController
    */
    function PostIdeaController($location, $scope, Userapp , idea) {
        var vm = this;

        vm.PostIdea = PostIdea;
        
        activate();

        /**
        * @name activate
        * @desc Actions to be performed when this controller is instantiated
        * @memberOf devcafe.userapp.controllers.PostIdeaController
        */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Userapp.isAuthenticated()) {
              $location.url('/');
            }
        }

        /**
        * @name PostIdea
        * @desc Log the user in
        * @memberOf devcafe.userapp.controllers.PostIdeaController
        */
        function PostIdea() {
            Ideas.create(vm.title , vm.content);
        }
    }
})();
