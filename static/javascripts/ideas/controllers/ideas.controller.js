/**
* ideasController
* @namespace devcafe.ideas.controllers
*/
(function () {
  'use strict';

  angular
    .module('devcafe.ideas.controllers')
    .controller('IdeasController', IdeasController);

  IdeasController.$inject = ['$http', '$location','$scope', 'Ideas'];

  /**
  * @namespace ideasController
  */
  // function ideasController($scope) {
  //   var vm = this;

  //   vm.columns = [];

  //   activate();
  function IdeasController($http, $location, $scope, Ideas) {
            //var userid = Userapp.getAccId();      //we don't need it any more
            var vm = this;
            vm.AddComment = AddComment;
            vm.LikeIdea = LikeIdea;
            Ideas.all().success(function(data, status, headers, config) {
                $scope.ideas = data;
            })

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


    /**
    * @name calculateNumberOfColumns
    * @desc Calculate number of columns based on screen width
    * @returns {Number} The number of columns containing ideas
    * @memberOf devcafe.ideas.controllers.ideasControllers
    */
    function calculateNumberOfColumns() {
      var width = $(window).width();

      if (width >= 1200) {
        return 4;
      } else if (width >= 992) {
        return 3;
      } else if (width >= 768) {
        return 2;
      } else {
        return 1;
      }
    }


    /**
    * @name approximateShortestColumn
    * @desc An algorithm for approximating which column is shortest
    * @returns The index of the shortest column
    * @memberOf devcafe.ideas.controllers.ideasController
    */
    function approximateShortestColumn() {
      var scores = vm.columns.map(columnMapFn);

      return scores.indexOf(Math.min.apply(this, scores));


      /**
      * @name columnMapFn
      * @desc A map function for scoring column heights
      * @returns The approximately normalized height of a given column
      */
      function columnMapFn(column) {
        var lengths = column.map(function (element) {
          return element.content.length;
        });

        return lengths.reduce(sum, 0) * column.length;
      }


      /**
      * @name sum
      * @desc Sums two numbers
      * @params {Number} m The first number to be summed
      * @params {Number} n The second number to be summed
      * @returns The sum of two numbers
      */
      function sum(m, n) {
        return m + n;
      }
    }


    /**
    * @name render
    * @desc Renders ideas into columns of approximately equal height
    * @param {Array} current The current value of `vm.ideas`
    * @param {Array} original The value of `vm.ideas` before it was updated
    * @memberOf devcafe.ideas.controllers.ideasController
    */
    function render(current, original) {
      if (current !== original) {
        vm.columns = [];

        for (var i = 0; i < calculateNumberOfColumns(); ++i) {
          vm.columns.push([]);
        }

        for (var i = 0; i < current.length; ++i) {
          var column = approximateShortestColumn();

          vm.columns[column].push(current[i]);
        }
      }
    }
  }
})();