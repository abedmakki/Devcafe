/**
* ideasController
* @namespace devcafe.ideas.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.controllers')
    .controller('IdeasController', IdeasController);

  IdeasController.$inject = ['$http', '$location','$scope', '$rootScope', 'Ideas'];

  /**
  * @namespace ideasController
  */
  // function ideasController($scope) {
  //   var vm = this;

  //   vm.columns = [];

  //   activate();
  function IdeasController($http, $location, $scope, $rootScope, Ideas) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            vm.AddComment = AddComment;
            vm.LikeIdea = LikeIdea;
            Ideas.all().success(function(data, status, headers, config) {
              $scope.ideas = data;
            })

            $rootScope.$watch('searchQuery', function() {
              $scope.search = $rootScope.searchQuery;
            });

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf devcafe.ideas.controllers.ideasController
    */
    function activate() {
      $scope.$watchCollection(function () { return $scope.ideas; }, render);
      $scope.$watch(function () { return $(window).width(); }, render);
    }


    function AddComment(item, text) {
        var idea = item;
        console.log(item);
        console.log(text);
        Ideas.comment(idea, text);
    }

    var hasLiked = false;

    function LikeIdea(item) {
        var idea = item;
        console.log(item);
        Ideas.like(idea);
    }
  }
})();