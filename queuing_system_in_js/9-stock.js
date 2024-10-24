const express = require('express');
const app = express();
const port = 1245;

// Array containing the list of products
const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

// Function to get item by ID
function getItemById(id) {
    return listProducts.find(product => product.id === id);
}

// Route to return the list of products
app.get('/list_products', (req, res) => {
    const formattedProducts = listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
    }));
    res.json(formattedProducts);
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
