function open_socket() {
  var host = 'ws://23.244.200.215:8000/socket';
  var websocket = new WebSocket(host);

  websocket.onopen = function() {
  }

  WebSocket.onmessage = function(evt) {
  }
}

function add() {
  var topTweet = $('.tweet').eq(0);
  var newTweet = topTweet.clone();
  newTweet.children('p').text('this is a new one');
  newTweet.insertBefore(topTweet);
}
