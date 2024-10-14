## Node JS
Let's break this down step by step and explain how to achieve each point:

### 1. **Running JavaScript Using Node.js**

To run JavaScript code using Node.js:

- First, install Node.js from the official website [Node.js](https://nodejs.org).
- Once installed, you can create a simple JavaScript file (`app.js`), and run it with the following command in your terminal:

```javascript
// app.js
console.log("Hello, World!");
```

To execute it:
```bash
node app.js
```

### 2. **Using Node.js Modules**

Node.js has built-in modules, such as `fs` for file system operations, `http` for server creation, etc. You can require these modules using the `require()` function.

For example:
```javascript
const fs = require('fs');  // File system module
```

### 3. **Using a Specific Node.js Module to Read Files**

To read files using the `fs` (file system) module:

```javascript
const fs = require('fs');

// Reading a file asynchronously
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});
```

### 4. **Using `process` to Access Command Line Arguments and the Environment**

The `process` object in Node.js gives you access to command-line arguments and the environment:

- **Command-line arguments** are stored in `process.argv`. The first two elements are the path to the Node.js executable and the file being executed, so you can access arguments starting from index 2.

```javascript
// Accessing command line arguments
const args = process.argv.slice(2);
console.log("Arguments:", args);
```

- **Environment variables** can be accessed using `process.env`.

```javascript
// Accessing environment variables
console.log("Environment Variables:", process.env.MY_VARIABLE);
```

### 5. **Create a Small HTTP Server Using Node.js**

To create a basic HTTP server using the `http` module:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!');
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
```

### 6. **Create a Small HTTP Server Using Express.js**

To create a simple server with Express.js:

1. First, install Express.js:
    ```bash
    npm install express
    ```

2. Then, create an `express_server.js` file:

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(3000, () => {
    console.log('Express server running at http://localhost:3000/');
});
```

Run the server:
```bash
node express_server.js
```

### 7. **Create Advanced Routes with Express.js**

You can define routes with parameters and query strings in Express:

```javascript
const express = require('express');
const app = express();

// Route with URL parameter
app.get('/user/:id', (req, res) => {
    res.send(`User ID: ${req.params.id}`);
});

// Route with query parameters
app.get('/search', (req, res) => {
    const { query } = req.query;
    res.send(`Search Query: ${query}`);
});

app.listen(3000, () => {
    console.log('Advanced Express server running at http://localhost:3000/');
});
```

### 8. **Use ES6 with Node.js Using Babel-Node**

1. Install Babel for transpiling ES6+ code:
    ```bash
    npm install @babel/core @babel/cli @babel/preset-env @babel/node
    ```

2. Create a Babel configuration file (`.babelrc`):
    ```json
    {
      "presets": ["@babel/preset-env"]
    }
    ```

3. Write an ES6+ file (`app_es6.js`):

```javascript
const greet = () => {
    console.log("Hello from ES6+!");
};

greet();
```

4. Run the code using Babel:
    ```bash
    npx babel-node app_es6.js
    ```

### 9. **Use Nodemon for Faster Development**

Nodemon automatically restarts the Node.js application when file changes are detected.

1. Install Nodemon:
    ```bash
    npm install -g nodemon
    ```

2. Run your application using Nodemon:
    ```bash
    nodemon app.js
    ```

### 10. **Create a Function Named `displayMessage` that Prints to STDOUT**

To create a simple function `displayMessage` that prints a string argument to `STDOUT`:

```javascript
function displayMessage(message) {
    console.log(message);
}

// Example usage
displayMessage("Hello, this is a message!");
```

---
