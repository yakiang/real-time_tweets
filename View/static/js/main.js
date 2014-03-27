function open_socket() {
  var host = 'ws://23.244.200.215:8000/socket';
  var websocket = new WebSocket(host);

  websocket.onopen = function() {
    console.log('===');
  }

  WebSocket.onmessage = function(evt) {
  }
}
