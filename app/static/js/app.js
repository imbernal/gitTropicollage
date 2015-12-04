var TodoApp = angular.module("TodoApp" , ["ngResource"]).
    config(function($routeProvider){
        $routeProvider.
            when('/casas' , {controller: casa_index , templateUrl: 'casas/index.html'}).
            otherwise({ redirecto: '/' });
    });

var casa_index = function ($scope , $location) {
    $scope.test = "testing";
};