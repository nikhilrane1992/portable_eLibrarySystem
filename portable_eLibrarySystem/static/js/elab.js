var eLabControllers = angular.module('eLabControllers', []);
eLabControllers.controller('BookCtrl', ['$scope', '$log', '$http', '$timeout', '$routeParams' , function($scope, $log, $http, $timeout, $routeParams){
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
    $scope.itemId = $routeParams.itemId
    $scope.loadContaint = function(tagObj){
    	$http.post('/elab/get/containt/', {tag_id:$scope.itemId}).
	    success(function(data, status, headers, config) {
	        console.log(data);
	        $scope.eLabContaint = data.containt_list;
	    }).
	    error(function(data, status, headers, config) {
	        console.log(data);
	    });
    }

}]);

eLabControllers.controller('QuizCtrl', ['$scope', '$log', '$http', '$timeout', '$routeParams' , function($scope, $log, $http, $timeout, $routeParams){
    $log.info('quiz controller loads');
    $scope.tagList = []
    $http.get('/elab/get/all/tags/').
    success(function(data, status, headers, config) {
        console.log(data);
        $scope.tagList = data.tag_list
    }).
    error(function(data, status, headers, config) {
        console.log(data);
    });

    $scope.progressBar = function(){
        $('#loadbar').show();
        $('#quiz').fadeOut();
        setTimeout(function(){
            $('#quiz').show();
            $('#loadbar').fadeOut();
           /* something else */
        }, 1500);
    }

}]);

eLabControllers.controller('QuizAdminCtrl', ['$scope', '$log', '$http', '$timeout', '$routeParams' , function($scope, $log, $http, $timeout, $routeParams){
    $log.info('Quiz admin controller loads');
    $scope.tagList = []
    $scope.question = '';
    $scope.optionType = '';
    $scope.option = '';
    $scope.optionList = [];
    $scope.rightWrong = 'Wrong';
    $scope.isRightValue = false;

    $scope.saveQuestion = function(){
        console.log({question:$scope.question, optionType:$scope.optionType, optionList: $scope.optionList});
        $http.post('/elab/save_question/', {question:$scope.question, optionType:$scope.optionType, optionList: $scope.optionList}).
        success(function(data, status, headers, config) {
            console.log(data);
            $scope.eLabContaint = data.containt_list;
        }).
        error(function(data, status, headers, config) {
            console.log(data);
        });
    }

    $scope.addOption = function(){
        if ($scope.option.length != 0){
            $scope.optionList.push({option: $scope.option, id:$scope.optionList.length+1, isRight: $scope.isRightValue})
            $scope.option = ''
            console.log($scope.optionList);
            $scope.rightWrong = 'Wrong';
            $(':checkbox').prop('checked', false);
            $scope.isRightValue = false;
        }
    }

    $scope.isRightWrong = function(){
        console.log($scope.rightWrong);
        if ($scope.rightWrong == 'Right'){
            $scope.rightWrong = 'Wrong';
            $(':checkbox').prop('checked', false);
            $scope.isRightValue = false;
        }else{
            $scope.rightWrong = 'Right';
            $(':checkbox').prop('checked', true);
            $scope.isRightValue = true;
        }
    }

}]);