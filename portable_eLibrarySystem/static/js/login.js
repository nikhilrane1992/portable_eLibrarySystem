var loginApp = angular.module('loginApp', []);
loginApp.controller('loginAppCtrl', function($scope, $log, $http){
	$log.info('Login controller loads');
	$scope.username = '';
	$scope.password = '';
	$scope.errormsg = '';

	$scope.login = function(){
		$http.post('/auth/', {username:$scope.username, password:$scope.password}).
        success(function(data, status, headers, config) {
            console.log(data);
            if (data.status){
                window.location = data.redirectUrl;
            }else{
                $log.info($scope.errormsg);
                $scope.errormsg = data.validation;
                $log.info($scope.errormsg);
            }
        }).
        error(function(data, status, headers, config) {
            console.log(data);
        });
	}
});
