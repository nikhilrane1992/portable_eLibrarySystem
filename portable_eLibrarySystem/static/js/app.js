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
	when('/quiz/', {
		templateUrl: '/render_quiz_tab/',
		controller: 'QuizCtrl'
	}).
	otherwise({
		redirectTo: '/books/0'
	});
}]);
