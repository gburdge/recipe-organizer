'use strict';

/**
 * @ngdoc function
 * @name djangularFrontendApp.controller:RecipeDetailCtrl
 * @description
 * # RecipeDetailCtrl
 * Controller of the djangularFrontendApp
 */
angular.module('djangularFrontendApp')
    .controller('RecipeDetailCtrl', function ($scope, $routeParams, Restangular, $location) {
        $scope.recipeId = $routeParams.recipeId;

        Restangular.one('recipes', $scope.recipeId).customGET().then(function (data) {
            $scope.recipe = data;
        });

        $scope.deleteRecipe = function () {
            var response = confirm("Are you sure you want to delete this recipe?");
            if (response == true) {
                Restangular.one('recipes', $scope.recipeId
            ).customDELETE().then(function () {
                    $location.path('/recipes');
                }, function () {
                    $scope.status = "The recipe couldn't be deleted";
                });
            }
        };
    });
;
