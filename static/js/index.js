

app.controller("detail", ['$scope', '$http', function ($scope, $http) {



$scope.submit=function(){
    details={
        'name': $scope.name,
        'email':$scope.email,
        'phone':$scope.mobile
    }
    console.log("---",$scope.name)
}

}]);
