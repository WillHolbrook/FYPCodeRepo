(function (){
    'use strict';

    angular.module('summarizer_web_app.demo')
        .config(['$routeProvider', config])
        .run(['$http', run]);

    function config($routeProvider){

        $routeProvider
            .when('/', {
                templateUrl: '/static/html/scrumboard.html',
                controller: 'SummarizerController'
            })
            .when('/login', {
                templateUrl: 'static/html/login.html',
                controller: 'LoginController'
            })
            .otherwise('/')
    }

    function run($http) {
        $http.defaults.xsrfCookieName = 'csrftoken'
        $http.defaults.xsrfHeaderName = 'X-CSRFToken'
    }
})();