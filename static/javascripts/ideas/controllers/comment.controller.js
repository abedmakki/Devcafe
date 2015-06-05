/**
* CommentController
* @namespace devcafe.userapp.controllers
*/
(function () {
    'use strict';

    angular
        .module('devcafe.ideas.controllers')
        .controller('CommentController', CommentController);

    CommentController.$inject = ['$location', '$scope', 'Userapp','Ideas'];

    /**
    * @namespace CommentController
    */
    function CommentController($location, $scope, Userapp , Ideas) {
        var vm = this;

        vm.AddComment = AddComment;
        
        idea = $scope.item;
        /**
        * @name AddComment
        * @desc Add a Comment to and existing Idea
        * @memberOf devcafe.ideas.controllers.CommentController
        */
        function AddComment(idea, text) {
            Ideas.comment(vm.text);
        }
    }
})();
