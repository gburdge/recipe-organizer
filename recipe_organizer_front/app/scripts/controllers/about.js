'use strict';

/**
 * @ngdoc function
 * @name djangularFrontendApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the djangularFrontendApp
 */
angular.module('djangularFrontendApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
