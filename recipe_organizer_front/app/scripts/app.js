'use strict';

/**
 * @ngdoc overview
 * @name djangularFrontendApp
 * @description
 * # djangularFrontendApp
 *
 * Main module of the application.
 */
angular
    .module('djangularFrontendApp', [
        'ngAnimate',
        'ngCookies',
        'ngResource',
        'ngRoute',
        'ngSanitize',
        'ngTouch',
        'restangular'
    ])
    .config(function ($routeProvider, RestangularProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .when('/about', {
                templateUrl: 'views/about.html',
                controller: 'AboutCtrl'
            })
            .when('/recipes/:recipeId', {
                templateUrl: 'views/recipe-detail.html',
                controller: 'RecipeDetailCtrl'
            })
                .when('/add-recipe', {
                templateUrl: 'views/add-recipe.html',
                controller: 'AddRecipeCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
        RestangularProvider.setBaseUrl('http://localhost:8001');
    });
