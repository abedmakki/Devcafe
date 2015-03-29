(function () {
  'use strict';

  angular
    .module('devcafe.userapp.services')
    .factory('Userapp', Userapp);

  Userapp.$inject = ['$cookies', '$http'];

  /**
  * @namespace userapp
  * @returns {Factory}
  */
  function Userapp($cookies, $http) {
    /**
    * @name userapp
    * @desc The Factory to be returned
    */
    var Userapp = {
      getdata: getdata
    };

    return Userapp;


    function getdata(number) {
        return $http.get('/users/:number/').then(getdataSuccessFn, getdataErrorFn);

        function getdataSuccessFn(data, status, headers, config) {
            console.log('Successfully Attached!');

            //store data f model

            // window.location = '/';
        }

        function getdataErrorFn(data, status, headers, config) {
            console.error('Epic failure!');
        }
    }
  }
})();
