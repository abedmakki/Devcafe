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
            login: login,
            register: register,
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate,
            getAccId: getAccId,
            setAccId: setAccId,
            logout: logout
        };

        return Userapp;


         function register(username, first_name, last_name, birth_date, password, country, email, address) {
            return $http.post('/users/', {
                username: username,
                first_name: first_name,
                last_name: last_name,
                birth_date: birth_date,
                password: password,
                country: country,
                email: email,
                address: address
            });
        }


        function login(username, password) {
            return $http.post('/rest-auth/login/', {
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

            function loginSuccessFn(data, status, headers, config) {
                Userapp.setAuthenticatedAccount(data.data.key);
                Userapp.setAccId(data.data.user);
                window.location = '/';
            }

            function loginErrorFn(data, status, headers, config) {
                console.error('Login failure!');
            }
        }


        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }
            return JSON.parse($cookies.authenticatedAccount);
        }


        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }


        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }


        function logout() {
            return $http.post('/rest-auth/logout/')
            .then(logoutSuccessFn, logoutErrorFn);


            function logoutSuccessFn(data, status, headers, config) {
                Userapp.unauthenticate();
                window.location = '/';
            }


            function logoutErrorFn(data, status, headers, config) {
                console.error('Logout failure!');
            }
        }

        function unauthenticate() {
            delete $cookies.authenticatedAccount;
            delete $cookies.accId;
        }

        function setAccId(account) {
            $cookies.accId = JSON.stringify(account);
        }

        function getAccId() {
            if (!$cookies.accId) {
                return;
            }
            else if ($cookies.accId === 'undefined') {
                return;
            }
            return JSON.parse($cookies.accId);
        }
    }

})();
