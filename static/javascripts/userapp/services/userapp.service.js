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
            edit: edit,
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
                address: address,
                picture: null
            }).then(function() {
                window.location = '/login';
            });
        }

        
        function edit(id, username, first_name, last_name, birth_date, password, country, email, address) {
            // console.log("services");
            return $http.patch('/users/' + id + '/', {
                username: username,
                first_name: first_name,
                last_name: last_name,
                birth_date: birth_date,
                password: password,
                country: country,
                email: email,
                address: address,
                picture: null
            }).then(function() {
                window.location = '/profile';
            });
        }
        //end here


        function login(username, password , remember , scp) {
            return $http.post('/rest-auth/login/', {
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);

            function loginSuccessFn(data, status, headers, config) {
                if(remember){
                    setCookie('authenticatedAccount' , data.data.key , 20)
                }
                else{
                    Userapp.setAuthenticatedAccount(data.data.key);
                }
                Userapp.setAccId(data.data.user);
                window.location = '/';
            }

            function loginErrorFn(data, status, headers, config) {
                //alert('login faild')
                scp.error=data.data.non_field_errors
            }
        }


        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }
            return $cookies.authenticatedAccount;
        }

        function setCookie(cname, cvalue, exdays) {
                        var d = new Date();
                        d.setTime(d.getTime() + (exdays*24*60*60*1000));
                        var expires = "expires="+d.toUTCString();
                        document.cookie = cname + "="+ cvalue + "; " + expires;
                    }
        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }


        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = account;
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
            setCookie('authenticatedAccount' , '',-1);
            delete $cookies.authenticatedAccount;
            setCookie('accId' , '',-1);
            delete $cookies.accId;
        }

        function setAccId(account) {
            $cookies.accId = account;
        }

        function getAccId() {
            if (!$cookies.accId) {
                return;
            }
            else if ($cookies.accId === 'undefined') {
                return;
            }
            return $cookies.accId;
        }
    }

})();
