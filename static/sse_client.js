var queue = [];
var interval = setInterval(function(){addItem()}, 1000);

function addItem(){
  if(queue.length > 0){
    var item = queue[0];
    queue.shift();
    $('#output').append(item);
  }
}

$(document).ready(

  function() {

    var sse = new EventSource('/my_event_source');
    console.log('blah');

    sse.onmessage = function(event) {

      console.log('A message has arrived!');
      var list_item = '<li>' + event.data + '</li>';
      console.log(list_item);
      queue.push(list_item);
    };
})
