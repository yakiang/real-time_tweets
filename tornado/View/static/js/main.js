var websocket;


jQuery(document).ready(function() {

  var host = 'ws://23.244.200.215:8000/socket';
  websocket = new WebSocket(host);

  websocket.onopen = function() {
    console.log('opened');
  }

  websocket.onmessage = function(evt) {
    var tweet = JSON.parse(evt.data);
    add_tweet(tweet);
  }

});


function add_tweet(tweet) {
  var topTweet = $('.tweet').eq(0);
  var newTweet = topTweet.clone();

  var user = ('@' + tweet['user']) || 'Ooops';
  var text = tweet['text'] || tweet['error'];
  console.log(user);
  console.log(text);

  newTweet.children('h4').text(user)
  newTweet.children('p').text(text);
  newTweet.insertBefore(topTweet);
}


function new_socket() {
  var hashtag = $('#hashtag').val();

  websocket.send(JSON.stringify({
    'hashtag': hashtag
  }));
}
