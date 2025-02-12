## Redis basic

To get started with Redis for basic operations and using it as a simple cache:

### 1. **Setting up Redis**

#### Install Redis

- On Ubuntu/Debian: `sudo apt-get install redis-server`
- On macOS: `brew install redis`
- On Windows: Use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) and follow the Ubuntu steps.

Start Redis with:

```bash
redis-server
```

### 2. **Basic Redis Operations**

To interact with Redis, use the Redis CLI:

```bash
redis-cli
```

#### Key-Value Operations

- **Set a key**: `SET mykey "Hello, Redis!"`
- **Get a key**: `GET mykey`
- **Delete a key**: `DEL mykey`
- **Check if a key exists**: `EXISTS mykey`
- **Expire a key**: `EXPIRE mykey 10` (the key will expire after 10 seconds)

### 3. **Using Redis as a Simple Cache**

A cache is used to store frequently accessed data temporarily to improve performance.

#### Basic Cache Example

Let’s say we want to cache the result of a database query:

1. **First, check if the value exists in Redis**:

   ```bash
   GET user:1234
   ```

2. **If it doesn’t exist**:

   - Fetch the data from the database.
   - Store the result in Redis with an expiration time:

   ```bash
   SETEX user:1234 3600 "user data here"  # This key will expire in 1 hour (3600 seconds)
   ```

3. **Subsequent requests** will get the data directly from Redis:
   ```bash
   GET user:1234
   ```

### 4. **Example Code: Basic Redis Cache in Python**

To integrate Redis with Python, you'll need the `redis` package:

```bash
pip install redis
```

Here’s a basic example using Redis as a cache:

```python
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def get_user_data(user_id):
    # Check cache first
    cached_data = r.get(f"user:{user_id}")
    if cached_data:
        return cached_data.decode('utf-8')

    # Simulate fetching data from the database
    user_data = f"Data for user {user_id}"

    # Store in cache with a 1-hour expiration
    r.setex(f"user:{user_id}", 3600, user_data)

    return user_data

# Usage
user_id = 1234
data = get_user_data(user_id)
print(data)
```

In this example, the `get_user_data` function first checks Redis to see if the user data is already cached. If it’s not cached, it simulates fetching the data, stores it in Redis with a 1-hour expiration (`SETEX`), and then returns the data.

This is how Redis can be used as a simple and efficient caching layer in your applications!
