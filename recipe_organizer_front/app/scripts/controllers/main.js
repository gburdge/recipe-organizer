'use strict';

/**
 * @ngdoc function
 * @name djangularFrontendApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the djangularFrontendApp
 */
angular.module('djangularFrontendApp')
    .controller('MainCtrl', function ($scope, Restangular) {
        Restangular.all('recipes/').getList().then(function (data) {
            $scope.recipes = data;
            console.log($scope.recipes);
        });
        $scope.awesomeThings = [
            'HTML5 Boilerplate',
            'AngularJS',
            'Karma'
        ];
    });
