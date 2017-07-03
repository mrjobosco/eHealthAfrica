/**
 * Created by joey on 03/07/2017.
 */
angular.module('survey.templates',['ngRoute'])
.config([
'$routeProvider', function ($routeProvider) {
        $routeProvider.
            when('/templates', {
                templateUrl: 'templates/templates.html',
                controller: 'TemplatesCtrl'
        });
    }

])
    .controller('TemplatesCtrl', [$scope, function () {
        console.log('TemplateCrtl Init')
    }]);
