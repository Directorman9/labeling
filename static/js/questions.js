main.controller('questionsCtrl',function($scope, $http, $window){  

  $scope.init = function() {
      $scope.get_questions();
      $scope.deletemsg = '';
      $scope.msg = ""
  };

  $scope.get_questions = function(){
        $http.get('/main/get_questions')
            .then(
                function successCallback(response) {
                    $scope.questions = response.data;
                },
                function errorCallback(response) {
                    $scope.errmsg = "system error, couldn't fetch questions, please contact hemed.";
                }
            );
  };

  $scope.save = function (){
       $scope.msg = "saving changes, please wait..."
       
       $http.post('/main/save_answers', $scope.questions)
            .then(
                function successCallback(response) {
                    $scope.msg = ""
                    $window.alert('Changes saved successfully')
                },
                function errorCallback(response) {
                    $scope.msg = ""
                    $window.alert('Error saving changes, contact hemed.');
                }
            );
  };

 
});
  



