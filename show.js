var app = angular.module('app', []);
app.controller('cntrl', function ($scope) {
    $scope.content = { like: 0, dislike: 0 }

    $scope.like = function (content) {
        content.like++;
    }
    $scope.dislike = function (content) {
        content.dislike++;
    }

});