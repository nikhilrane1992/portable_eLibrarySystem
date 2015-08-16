var eLabApp = angular.module('eLabApp', [])
eLabApp.controller('eLabCtrl', function($scope, $log, $http, $timeout){
	$log.info('eLab controller loads');
	$scope.tagList = []
	$http.get('/elab/get/all/tags/').
    success(function(data, status, headers, config) {
        console.log(data);
        $scope.tagList = data.tag_list
    }).
    error(function(data, status, headers, config) {
        console.log(data);
    });

    $scope.init =  function() {
    	$scope.loadContaint($scope.tagList[0]);
    };

    $timeout($scope.init,1000);


    $scope.eLabContaint = []
    $scope.loadContaint = function(tagObj){
    	$http.post('/elab/get/containt/', {tag_id:tagObj.id}).
	    success(function(data, status, headers, config) {
	        console.log(data);
	        $scope.eLabContaint = data.containt_list
	    }).
	    error(function(data, status, headers, config) {
	        console.log(data);
	    });
    }
});