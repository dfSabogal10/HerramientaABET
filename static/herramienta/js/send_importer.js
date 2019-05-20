/**
 * Created by dark on 31/03/18.
 */
/**
 * Created by dark on 6/03/18.
 */
/**
 * Created by dark on 31/03/18.
 */
/**
 * Created by dark on 6/03/18.
 */

/**
 * Created by dark on 31/03/18.
 */
/**
 * Created by dark on 6/03/18.
 */
window.data = [];
$(document).ready(function () {
    console.log("dadaasasas");
    // bind form using 'ajaxForm'
    window.id_file=0;
    var options = {
        //beforeSubmit:  showRequest,  // pre-submit callback
        success:       respuesta  // post-submit callback

        // other available options:
        //url:       url         // override for form's 'action' attribute
        //type:      type        // 'get' or 'post', override for form's 'method' attribute
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type)
        //clearForm: true        // clear all form fields after successful submit
        //resetForm: true        // reset the form after successful submit

        // $.ajax options can be used here too, for example:
        //timeout:   3000
    };

    // bind form using 'ajaxForm'
    //$('#form').ajaxForm(options);
    $('#form').submit(function() {
        // inside event callbacks 'this' is the DOM element so we first
        // wrap it in a jQuery object and then invoke ajaxSubmit
        $(this).ajaxSubmit(options);

        // !!! Important !!!
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});
// pre-submit callback
function showRequest(formData, jqForm, options) {
    // formData is an array; here we use $.param to convert it to a string to display it
    // but the form plugin does this for you automatically when it submits the data
    var queryString = $.param(formData);

    // jqForm is a jQuery object encapsulating the form element.  To access the
    // DOM element for the form do this:
    // var formElement = jqForm[0];

    alert('About to submit: \n\n' + queryString);

    // here we could return false to prevent the form from being submitted;
    // returning anything other than false will allow the form submit to continue
    return true;
}

// post-submit callback
function respuesta(responseText, statusText, xhr, $form)  {
    if(responseText.respuesta != undefined){
        if(responseText.respuesta){
            window.id_file = responseText.mensaje;
            var datos = responseText.data;
            var value ="";
            for(var i=0; i < datos.length; i++){
                value+= "<option value=\""+datos[i].row+"\">"+datos[i].nombre+"</option>";
            }
            window.data = datos;
            $("#datos").html("");
            $("#datos").append(value);
            $('.selectpicker').addClass('col-lg-12').selectpicker('setStyle');
            $('.selectpicker').selectpicker('refresh');
            $('#myModal').modal('show');
        }else{
            $('#myAlert').modal('show');
        }
    }else{
        $('#myAlert').modal('show');
    }
}
/*
window.data = [];
$(document).ready(function () {
    console.log("dadaasasas");
    // bind form using 'ajaxForm'
    window.id_file=0;
    var options = {
        //beforeSubmit:  showRequest,  // pre-submit callback
        success:       respuesta  // post-submit callback

        // other available options:
        //url:       url         // override for form's 'action' attribute
        //type:      type        // 'get' or 'post', override for form's 'method' attribute
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type)
        //clearForm: true        // clear all form fields after successful submit
        //resetForm: true        // reset the form after successful submit

        // $.ajax options can be used here too, for example:
        //timeout:   3000
    };

    // bind form using 'ajaxForm'
    //$('#form').ajaxForm(options);
    $('#form').submit(function() {
        // inside event callbacks 'this' is the DOM element so we first
        // wrap it in a jQuery object and then invoke ajaxSubmit
        $(this).ajaxSubmit(options);

        // !!! Important !!!
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});
// pre-submit callback
function showRequest(formData, jqForm, options) {
    // formData is an array; here we use $.param to convert it to a string to display it
    // but the form plugin does this for you automatically when it submits the data
    var queryString = $.param(formData);

    // jqForm is a jQuery object encapsulating the form element.  To access the
    // DOM element for the form do this:
    // var formElement = jqForm[0];

    alert('About to submit: \n\n' + queryString);

    // here we could return false to prevent the form from being submitted;
    // returning anything other than false will allow the form submit to continue
    return true;
}

// post-submit callback
function respuesta(responseText, statusText, xhr, $form)  {
    if(responseText.respuesta != undefined){
        if(responseText.respuesta){
            window.id_file = responseText.mensaje;
            var datos = responseText.data;
            var value ="";
            for(var i=0; i < datos.length; i++){
                value+= "<option value=\""+datos[i].row+"\">"+datos[i].nombre+"</option>";
            }
            window.data = datos;
            $("#datos").html("");
            $("#datos").append(value);
            $('.selectpicker').addClass('col-lg-12').selectpicker('setStyle');
            $('.selectpicker').selectpicker('refresh');
            $('#myModal').modal('show');
        }else{
            $('#myAlert').modal('show');
        }
    }else{
        $('#myAlert').modal('show');
    }
}
/*
$(document).ready(function () {
    console.log("dadaasasas");
    // bind form using 'ajaxForm'
    window.id_file=0;
    var options = {
        //beforeSubmit:  showRequest,  // pre-submit callback
        success:       respuesta  // post-submit callback

        // other available options:
        //url:       url         // override for form's 'action' attribute
        //type:      type        // 'get' or 'post', override for form's 'method' attribute
        //dataType:  null        // 'xml', 'script', or 'json' (expected server response type)
        //clearForm: true        // clear all form fields after successful submit
        //resetForm: true        // reset the form after successful submit

        // $.ajax options can be used here too, for example:
        //timeout:   3000
    };

    // bind form using 'ajaxForm'
    //$('#form').ajaxForm(options);
    $('#form').submit(function() {
        // inside event callbacks 'this' is the DOM element so we first
        // wrap it in a jQuery object and then invoke ajaxSubmit
        $(this).ajaxSubmit(options);

        // !!! Important !!!
        // always return false to prevent standard browser submit and page navigation
        return false;
    });
});
// pre-submit callback
function showRequest(formData, jqForm, options) {
    // formData is an array; here we use $.param to convert it to a string to display it
    // but the form plugin does this for you automatically when it submits the data
    var queryString = $.param(formData);

    // jqForm is a jQuery object encapsulating the form element.  To access the
    // DOM element for the form do this:
    // var formElement = jqForm[0];

    alert('About to submit: \n\n' + queryString);

    // here we could return false to prevent the form from being submitted;
    // returning anything other than false will allow the form submit to continue
    return true;
}

// post-submit callback
function respuesta(responseText, statusText, xhr, $form)  {
    console.log('esp esdsdsd');
    console.log(responseText);
    if(responseText.respuesta != undefined){
        if(responseText.respuesta){
            window.id_file = responseText.mensaje;
            var datos = responseText.data;
            var value ="";
            for(var i=0; i < datos.length; i++){
                value+= "<option value=\""+datos[i].row+"\">"+datos[i].nombre+"</option>";
            }
            console.log(value);
            $("#datos").html("");
            $("#datos").append(value);
            $('.selectpicker').addClass('col-lg-12').selectpicker('setStyle');
            $('.selectpicker').selectpicker('refresh');
            $('#myModal').modal('show');
        }else{
            $('#myAlert').modal('show');
        }
    }else{
        $('#myAlert').modal('show');
    }
}*/