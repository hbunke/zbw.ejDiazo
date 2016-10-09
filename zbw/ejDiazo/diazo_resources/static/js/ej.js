//Hendrik Bunke
//ZBW - Leibniz Information Centre for Economics

"use strict";
var showjumbo = document.getElementById('showjumbo');
var hidejumbo = document.getElementById('hidejumbo');
var jumbotron = document.getElementById('ejumbo');
var loggo = document.getElementById('loggo');
$(jumbotron).show();
$(showjumbo).hide();

if (jumbotron) {
    $(loggo).hide()
}

$(showjumbo).on('click', function() {
    show_jumbo();

});

$(hidejumbo).on('click', function() {
    hide_jumbo();
});

function show_jumbo() {
    $(jumbotron).show();
    $(showjumbo).hide();
    $(hidejumbo).show();
    $(loggo).hide();
}

function hide_jumbo() {
    $(jumbotron).hide();
    $(showjumbo).show();
    $(hidejumbo).hide();
    $(loggo).show();
}
