import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

client.connect();
// Function to set a new value in Redis
const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value);
  console.log(`Set ${schoolName} to ${value}`);
};

// Function to get a value from Redis and print it
const displaySchoolValue = async (schoolName) => {
  const value = await client.get(schoolName);
  console.log(value ? `${schoolName}: ${value}` : `${schoolName} not found`);
};
// Example usage
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
