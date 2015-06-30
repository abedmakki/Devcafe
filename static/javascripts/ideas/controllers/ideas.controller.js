/**
* ideasController
* @namespace devcafe.ideas.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.controllers')
    .controller('IdeasController', IdeasController);

  IdeasController.$inject = ['$http', '$location','$scope', '$rootScope', '$routeParams', 'Ideas'];

  /**
  * @namespace ideasController
  */
  function IdeasController($http, $location, $scope, $rootScope, $routeParams, Ideas) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            var createdProjId = null;
            vm.AddComment = AddComment;
            vm.LikeIdea = LikeIdea;
            vm.Realize = Realize;
            // vm.GetRealizeInfo = GetRealizeInfo;
            if ($routeParams.id) {
              Ideas.get($routeParams.id).success(function(data, status, headers, config) {
                $scope.item = data;
              })
            } else {
              Ideas.all().success(function(data, status, headers, config) {
                $scope.ideas = data;
              })
            };

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
        // console.log(item);
        // console.log(text);
        Ideas.comment(idea, text).success(function(data, status, headers, config) {
          for(var i = 0; i < $scope.ideas.length; i++) {
            if ($scope.ideas[i].id === item) {
              $scope.ideas[i].comments.push(data);
              console.log($scope.ideas[i].comments);
              $scope.ideas[i].name = "";
            }
          }
        });
        // document.getElementById('comment-form').reset();
        // $scope.reset();
        // $scope.item.name = "";
    }

    var hasLiked = false;

    function LikeIdea(item) {
        Ideas.like(item).success(function(data){
        var index = function(tid) {
            for (var i = 0, len = $scope.ideas.length; i < len; i++)
                if ($scope.ideas[i].id === tid)
                    return i;}
        $scope.ideas[index(item)].is_liked = data.op;
        $scope.ideas[index(item)].likes = data.count;
        })
    }


    // function Realize(item) {
    //     var id = item;
    //     // Ideas.realize(id);
    //     // $location.path('/projects/' + id + '/');
    //     }

    function Realize(title, description) {
      
      Ideas.realize(title, description).success(function(data, status, headers, config) {
        window.createdProjId = data.id;
        console.log('Created project ID: ' + window.createdProjId);
        $location.path('projects/' + window.createdProjId);
      });
      
      // $location.path('/projects/post/new');
    }
    


  }
})();