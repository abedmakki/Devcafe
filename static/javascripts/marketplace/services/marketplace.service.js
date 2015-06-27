(function () {
  'use strict';

  angular
    .module('devcafe.marketplace.services')
    .factory('Market', Market);

  Market.$inject = ['$http'];

 
  function Market($http) {
    var Market = {
      all: all,
      get: get,
      create: create,
      comment: comment,
      rate: rate,
      buy: buy,
      tags: tags,
      view_transactions: view_transactions,
      view_my_apps: view_my_apps
    };

    return Market;

   
    function all() {
      return $http.get('/market/');
    }

    function get(id) {
      return $http.get('/market/' + id + '/');
    }

    function create(name, price, description, picture) {
      return $http.post('/market/', {
        name: name,
        description: description,
        price: price,
        tags: []
      });
    }

    function comment(id, text) {
      return $http.post('/market/' + id + '/add_comment/', {
        text: text
      })
    }

    function rate(id, value) {
      return $http.post('/market/' + id + '/rate/', {
        value: value
      });
    }

    function buy(id, firstname, lastname, email, address, ddate, mobile, hphone) {
      return $http.post('/market/' + id + '/buy/', {
        home_no: hphone,
        phone_no: mobile,
        delivery_address: address,
        delivery_time: ddate,
        // home_no: "123456",
        // phone_no: "654321",
        // delivery_address: "sjfhfkfjk",
        // delivery_time: "2015-07-20TZ12:50",
      });
    }

    function tags() {
      return $http.get('/general/tags/');
    }

    function view_transactions(){
      return $http.get('/market/view_transactions/');
    }

    function view_my_apps(){
      return $http.get('/market/view_my_apps/')
    }
    // function like(id) {
    //   return $http.post('/market/' + id + '/like/', {
    //   }).then(function() {
    //     window.location = '/market';
    //   });
    // }
}

})();