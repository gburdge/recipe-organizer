'use strict';

/**
 * @ngdoc function
 * @name recipeOrganizerFrontApp.controller:AddRecipeCtrl
 * @description
 * # AddRecipeCtrl
 * Controller of the recipeOrganizerFrontApp
 */
angular.module('djangularFrontendApp')
    .controller('AddRecipeCtrl', function ($scope, Restangular) {
        $scope.recipe = {};
        $scope.saveNewRecipe = function () {

            console.log($scope.recipe);

            Restangular.all('recipes').customPOST($scope.recipe).then(function () {
                $scope.status = alert("The recipe was successfully created!");
                $scope.recipe = {}

            }, function () {
                $scope.status = "The recipe couldn't be saved";
            });
        };
    });
