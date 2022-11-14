(function () {
    'use strict';

    angular.module('summarizer_web_app.demo', ['ngRoute'])
        .controller('SummarizerController', ['$scope', '$http', '$location', SummarizerController]);


    function SummarizerController($scope, $http, $location) {
        $scope.add = function (list, title) {
            var card = {
                list: list.id,
                title: title
            };
            $http.post('summarizer_web_app/cards/', card).then(function (response) {
                    list.cards.push(response.data);
                },
                function () {
                    alert('Could not create card')
                });
        };

        $scope.logout = function () {
            $http.get('/auth_api/logout/').then(function (){
                $location.url('/login')
            })
        }

        $scope.data = [];
        $http.get('/summarizer_web_app/lists/').then(function (response) {
            $scope.data = response.data;
        },
        function (){
            alert('Not authenticated please authenticate by clicking log in below')
        });
    }
}());