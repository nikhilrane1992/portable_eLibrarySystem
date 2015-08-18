var eLabApp = angular.module('eLabApp', [
	'ngRoute',
	'eLabControllers'
	]);

eLabApp.config(['$routeProvider', function($routeProvider){
	$routeProvider.
	when('/books/:itemId', {
		templateUrl: '/partial_book/template/',
		controller: 'BookCtrl'
	}).
	otherwise({
		redirectTo: '/books/0'
	});
}]);
