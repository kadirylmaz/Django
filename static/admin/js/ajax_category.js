jQuery(function ($) {
    var category_form = $('#category-form');

    var success_msg = 'Your enquiry has been successfully submitted';

    var general_error_msg = 'Some of the information submitted is incorrect';

    $(category_form).submit(function (event) {
        event.preventDefault();

        var error = false;

        if ($('#category-name').val() == "") {
            var error_msg = "Please enter a category name";
            error = true;
        }
        $('#btnSave').click(function () {
            var category_name = $('#category-name').val();

            $.ajax({
                type: 'POST',
                url: '/blog_post/admin_category_add/',
                data: {
                    'category-name': category_name.val()
                },
                dataType: 'json',
                success: function (returnData) {
                    var returnJSONobj = returnData;
                    var status = (returnJSONobj.category_status);
                    if (status == 0) {
                        $('#error-message').slideUp();
                        $('.category-input').val('');
                        $('#success-message').slideDown();
                        $('#success-message').text(succes_msg);
                    }
                    else if (status == 1) {
                        $('#error-message').slideDown();
                        $('#error-message p').text(general_error_msg);
                    }
                }
            })
        })

    }
else
    {
        $('#error-message').slideDown();
        $('#error-message p').text(error_msg);
    }

});

})
;

// var app = angular.module('myApp', []);
// app.controller('categoryCtrl',function ($scope,$http) {
//     $http.get("/admin/category/admin_category_index/").then(function (response) {
//         $scope.myData = response.data.records;
//         console.log(response);
//     })
// })