$(document).ready(function(){
    var $myForm = $('.my-ajax-form')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        var $endpoint = $myForm.attr("data-url") || window.location.href
        console.log($endpoint)
        console.log($formData)
        $.ajax({
            method: "POST",
            url: $endpoint,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })

        function handleFormSuccess(data, textStatus, jqXHR){
        $('#result').empty();
        // console.log(data)
        // console.log(textStatus)
        // console.log(jqXHR)
        $myForm[0].reset() // reset form data
        $('#result').append("<p>Записано</p>")
    }

        function handleFormError(jqXHR, textStatus, errorThrown){
            console.log(jqXHR)
            console.log(textStatus)
            console.log(errorThrown)
        }
    })
   })