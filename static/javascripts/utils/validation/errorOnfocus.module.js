/**
 * Created by Abedmakki on 02/05/2015.
 */
(function () {
    'use strict';
    var errorValidation = angular
        .module('devcafe.errorValidation', []);
    errorValidation.directive('ngFocus', [function() {
        var FOCUS_CLASS = "ng-focused";
        return {
            restrict: 'A',
            require: 'ngModel',
            link: function(scope, element, attrs, ctrl) {
                ctrl.$focused = false;
                element.bind('focus', function(evt) {
                    element.addClass(FOCUS_CLASS);
                    element.parent('div').removeClass('has-error')
                    element.popover('hide')
                    scope.$apply(function() {ctrl.$focused = true;});
                }).bind('blur', function(evt) {
                    element.removeClass(FOCUS_CLASS);
                    if(ctrl.$invalid && ctrl.$dirty){
                        element.parent('div').addClass('has-error')
                        element.attr('data-toggle','popover');
                        element.attr('data-placement','bottom');
                        element.popover('show')
                    }
                    scope.$apply(function() {ctrl.$focused = false;});
                });
            }
        }
    }]);


})();