const redis = require('redis');
const client = redis.createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

(async () => {
    // Connect to the Redis server
    await client.connect();
    console.log('Connected to Redis');

    // Subscribe to the channel "holberton school"
    await client.subscribe('holberton school', (message) => {
        console.log(`Received message: ${message}`);

        // If the message is "KILL_SERVER", unsubscribe and quit
        if (message === 'KILL_SERVER') {
            console.log('KILL_SERVER received. Unsubscribing and quitting...');
            client.unsubscribe('holberton school');
            client.quit();
        }
    });

    console.log('Subscribed to channel "holberton school"');
})();
