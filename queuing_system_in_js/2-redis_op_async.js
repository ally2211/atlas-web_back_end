import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.connect();

// Promisify the get function
const getAsync = promisify(client.get).bind(client);

// Function to set a new value in Redis
const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value);
  console.log(`Set ${schoolName} to ${value}`);
};

// Function to get a value from Redis and print it using async/await
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(value ? `${schoolName}: ${value}` : `${schoolName} not found`);
  } catch (error) {
    console.error('Error retrieving value:', error);
  }
};


// Example usage
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
