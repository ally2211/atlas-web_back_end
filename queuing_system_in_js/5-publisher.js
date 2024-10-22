const redis = require('redis');
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

async function publishMessage(message, time) {
    // Wait for the specified time
    setTimeout(async () => {
        console.log(`About to send ${message}`);

        // Publish the message to the "holberton school" channel
        await client.publish('holberton school', message);
    }, time);
}

// Connect to the Redis server
client.connect().then(() => {
    console.log('Publisher connected to Redis');
});

// Example usage
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);