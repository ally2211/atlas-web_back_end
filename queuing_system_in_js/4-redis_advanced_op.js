const redis = require('redis');
const client = redis.createClient();

client.on('error', (err) => {
    console.log('Error ' + err);
});

(async () => {
    // Connect to the Redis server
    await client.connect();
    console.log('Connected to Redis');

    // Create a hash using HSET
    await client.HSET('HolbertonSchools', 'Portland', '50');
    await client.HSET('HolbertonSchools', 'Seattle', '80');
    await client.HSET('HolbertonSchools', 'New York', '20');
    await client.HSET('HolbertonSchools', 'Bogota', '20');
    await client.HSET('HolbertonSchools', 'Cali', '40');
    await client.HSET('HolbertonSchools', 'Paris', '2');
    // Retrieve all fields and values of the hash
    const user = await client.HGETALL('HolbertonSchools');
    console.log(user);

    // Close the Redis connection
    await client.quit();
})();
