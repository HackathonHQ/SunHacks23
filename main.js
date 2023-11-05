// FILEPATH: /media/aryank/Tech AFOGA/TradeDaddy/main.js
const express = require('express');
const path = require('path');

const app = express();

app.use('/img', express.static(path.join(__dirname, 'img')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/logged_in', (req, res) => {
    res.sendFile(path.join(__dirname, 'logged_in.html'));
});

app.get('/listing/:query', (req, res) => {
    res.sendFile(path.join(__dirname, 'product_listing.html'));
});

app.get('/items/:item_id', (req, res) => {
    const { item_id } = req.params;
    const { q } = req.query;
    res.json({ item_id, q });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});
