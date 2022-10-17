main.config(function ($routeProvider) {

    $routeProvider
    /*.when("/", {
        templateUrl : function($routeParams){
            if ($routeParams.role == 0)              
                return "/static/htmls/admin/admin-feeds.html"
            else
                return "/static/htmls/community/cmfeeds.html"
        }
    })*/
    .when("/", {
        templateUrl : "/static/htmls/questions.html"
    })
    .when("/questions", {
        templateUrl: "/static/htmls/questions.html"
    })
    .otherwise({
        redirectTo : "/static/htmls/questions.html"
    })
 });
