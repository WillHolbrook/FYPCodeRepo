(function () {
        'use strict';

        angular.module('summarizer_web_app.demo', [])
            .controller('SummarizerController', ['$scope', SummarizerController]);

        function SummarizerController($scope) {
            $scope.add = function (list, title) {
                var card = {
                    title: title
                };

                list.cards.push(card);
            }

            $scope.data = [
                {
                    name: 'Django demo',
                    cards: [
                        {
                            title: 'Create models'
                        },
                        {
                            title: 'card 2'
                        },
                        {
                            title: 'card 3'
                        }
                    ]
                },
                {
                    name: 'Angular Demo',
                    cards: [
                        {
                            title: 'basic controller setup'
                        },
                        {
                            title: 'dunno why im using angular tho'
                        }
                    ]
                }
            ]
        }
    }());