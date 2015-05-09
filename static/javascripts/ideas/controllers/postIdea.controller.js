/**
* PostIdeaController
* @namespace devcafe.userapp.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.ideas.controllers')
        .controller('PostIdeaController', PostIdeaController);

    PostIdeaController.$inject = ['$location', '$scope', 'Userapp','Ideas'];

    /**
    * @namespace PostIdeaController
    */
    function PostIdeaController($location, $scope, Userapp , Ideas) {
        var vm = this;

        vm.PostIdea = PostIdea;
        
        activate();


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
