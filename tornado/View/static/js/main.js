var websocket;


jQuery(document).ready(function() {

  // Open a websocket
  var host = 'ws://23.244.200.215:8000/socket';
  websocket = new WebSocket(host);

  websocket.onopen = function() {
    console.log('opened');
  }

  // Get each new tweet here
  websocket.onmessage = function(evt) {
    var tweet = JSON.parse(evt.data);
    add_tweet(tweet);
  }

});


function add_tweet(tweet) {
  // Clone a new div
  var topTweet = $('.tweet').eq(0);
  var newTweet = topTweet.clone();

  // Set user and tweet content or error data
  var user = ('@' + tweet['user']) || 'Ooops';
  var text = tweet['text'] || tweet['error'];

  newTweet.children('h4').text(user)
  newTweet.children('p').text(text);

  newTweet.insertBefore(topTweet);
}


function new_socket() {
  // Change a new keyword to monitor
  var hashtag = $('#hashtag').val();
  websocket.send(JSON.stringify({
    'hashtag': hashtag
  }));
}
