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

  /* Set user and content of each tweet or error message */
  var user = tweet['user'] || 'Ooops';
  var text = tweet['text'] || tweet['error'];

  newTweet.children('p').text(text);
  newTweet.children('a').text(user)
  newTweet.children('a').attr('href', 'https://twitter.com/'+user);

  // set a random background color
  var colors = [
    '#A4D2A4',
    '#FF6699',
    '#FFFF66'
  ]
  var rand = Math.floor(Math.random() * 10) % colors.length;
  newTweet.css('background-color', colors[rand]);

  newTweet.insertBefore(topTweet);
}


function new_socket() {
  // Change a keyword to monitor
  var hashtag = $('#hashtag').val();
  websocket.send(JSON.stringify({
    'hashtag': hashtag
  }));
}
