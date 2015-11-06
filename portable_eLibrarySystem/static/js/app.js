var eLabApp = angular.module('eLabApp', [
	'ngRoute',
	'eLabControllers',
	'ui-notification'
	]);

eLabApp.config(['$routeProvider', 'NotificationProvider', function($routeProvider, NotificationProvider){
	NotificationProvider.setOptions({
		delay: 3000,
		startTop: 20,
		startRight: 10,
		verticalSpacing: 20,
		horizontalSpacing: 20,
		positionX: 'right',
		positionY: 'top'
	});


	$routeProvider.
	when('/books/:itemId', {
		templateUrl: '/partial_book/template/',
		controller: 'BookCtrl'
	}).
	when('/quiz/', {
		templateUrl: '/render_quiz_tab/',
		controller: 'QuizCtrl'
	}).
	when('/quiz/admin/', {
		templateUrl: '/elab/quiz_admin_page/',
		controller: 'QuizAdminCtrl'
	}).
	otherwise({
		redirectTo: '/books/0'
	});
}]);
