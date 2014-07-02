'use strict';

describe('Controller: BlahCtrl', function () {

  // load the controller's module
  beforeEach(module('djangularFrontendApp'));

  var BlahCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BlahCtrl = $controller('BlahCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
