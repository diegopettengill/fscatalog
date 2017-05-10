/**
 * Created by Diego Pettengill Fernandes on 23/04/2017.
 */

$(document).ready(function(){

    //Form validation, thanks jQuery Validate :D
    $(".validate").validate();

    //Mask money
    $('.mask-money').maskMoney();

});

// Auth functions

// Gplus signIn
function onSignIn(googleUser) {

    console.log("chamou");
    //console.log(authResult);

    var profile = googleUser.getBasicProfile();

    var id_token = googleUser.getAuthResponse().id_token;
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    console.log('Token: ' +id_token); // This is null if the 'email'

    if (googleUser) {

        $.ajax({
            type: 'POST',
            url: '/login/gplus',
            processData: false,
            data: {token: id_token},
            contentType: 'application/octet-stream; charset=utf-8',
            success: function (result) {

                console.log(result);
                // // Handle or verify the server response if necessary.
                // if (result) {
                //     $('#result').html('Login Successful!</br>' + result + '</br>Redirecting...')
                //     setTimeout(function () {
                //         window.location.href = "/";
                //     }, 4000);
                //
                // } else if (authResult['error']) {
                //     console.log('There was an error: ' + authResult['error']);
                // } else {
                //     $('#result').html('Failed to make a server-side call. Check your configuration and console.');
                // }
            }

        });
    }
}
