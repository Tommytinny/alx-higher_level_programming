document.addEventListener('DOMContentLoaded', function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const helloTransl = data.hello;
    $('DIV#hello').text(helloTransl);
  });
});
