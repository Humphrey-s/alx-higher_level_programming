#!/usr/bin/node

$('header').css('color', 'green');

$('DIV#red_header').bind('click', function () {
  $('header').addClass('red');
});
