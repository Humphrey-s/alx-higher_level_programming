#!/usr/bin/node
$('DIV#toggle_header').bind('click', function () {
  $('header').toggleClass('red green');
});
