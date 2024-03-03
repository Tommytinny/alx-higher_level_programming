$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, character) {
      $('UL#list_movies').append('<li>' + character.title + '</li>');
    });
  });
});
