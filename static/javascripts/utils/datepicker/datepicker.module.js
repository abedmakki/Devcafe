/**
 * Created by Abedmakki on 30/04/2015.
 */
(function () {
    'use strict';

    var datepicker = angular
        .module('devcafe.datepicker', []);
        datepicker.directive('jqdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
             element.datepicker({
                 showOtherMonths: true,
                 dateFormat: "yy-mm-dd",
                 changeMonth: true,
                 changeYear: true,
                 maxDate: "-12M",
                 onSelect: function (date) {
                     scope.$apply(function () {
                         ngModelCtrl.$setViewValue(date);
                     });
                 }
             });
        }
    };
});

})();