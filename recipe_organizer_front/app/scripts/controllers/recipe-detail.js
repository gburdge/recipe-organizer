'use strict';

/**
 * @ngdoc function
 * @name djangularFrontendApp.controller:RecipeDetailCtrl
 * @description
 * # RecipeDetailCtrl
 * Controller of the djangularFrontendApp
 */
angular.module('djangularFrontendApp')
    .controller('RecipeDetailCtrl', function ($scope, $routeParams, Restangular) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;

        });
    });
;
