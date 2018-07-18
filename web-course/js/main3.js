function alertMe(){
    alert("Me");
}

$(document).ready(function(){
    // alert("Loaded");

    var el = document.getElementById('text');

    console.log("EL in Vanilla JS:", el);

    console.log("EL in jQuery:", $(el));

    // document.getElementById('go-button').addEventListener('click', alertMe);
    $('#go-button').on('mouseenter',function(){
        alert("Fantastic job clicking that button!");
    });
    // document.getElementById('text').innerHTML = "This is my text";
    // $('#text').html("This is now my text");

    // document.getElementsByClassName('my-input').value = "Value of input";
    // $('.my-input').val("New input Val");
});
