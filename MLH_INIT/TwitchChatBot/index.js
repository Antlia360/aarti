const tmi = require('tmi.js');

const options={
    options:{
        debug:true,
    },
    connection: {
         cluster:'aws',
        reconnect:'true',

    },
    identity:{
        username: 'BotBot',
        password:'WRITE YOUR PASSWORD',
    },
    channels:['NAME OF THE CHANNEL YOU WNAT TO CONNECT WITH'],
};

const client = new tmi.client(options);

client.connect();

client.on('connected',(address, port) => {
    client.action('NAME OF THE CHANNEL YOU WNAT TO CONNECT WITH','Hello, BotBot is now connected');
});