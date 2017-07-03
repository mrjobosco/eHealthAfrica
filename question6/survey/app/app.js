'use strict';

// Declare app level module which depends on views, and components
angular.module('survey', [
  'ngRoute',
  'survey.view1',
  'survey.view2',
  'survey.templates'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider.otherwise({redirectTo: '/templates'});
}]);
