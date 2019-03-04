const make_result = (data) => {
  $('#result').text("").append('<ul></ul>');
  for (const value of data) {
      $('<li>' + value.rank + ' : ' + value.title + ', score : ' + value.score + '</li>').appendTo('ul');
  }
};
$(function() {
$('#button').click(
  function() {
    let query = $('#query_form').val();
    console.log(query);
    $.ajax({
      url: './post',
      type: 'post',
      dataType: 'json',
      cache: false,
      contentType: 'application/json',
      data : JSON.stringify({text:query}),
     })
     .done(function( data, textStatus, jqXHR ) {
        make_result(data);
     })
     .fail(function( data, textStatus, jqXHR ) {
        alert('error');
     });
  }
);
});
