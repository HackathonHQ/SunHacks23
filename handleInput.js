const fs = require('fs');
const path = require('path');
const AWS = require('aws-sdk');

// Assuming you have a button with id "submitBtn" and a form with id "inputForm" in your list.html file
const submitBtn = document.getElementById('submitBtn');
const inputForm = document.getElementById('inputForm');

submitBtn.addEventListener('click', (event) => {
    event.preventDefault(); // Prevents the form from submitting and refreshing the page

    const itemName = inputForm.elements.itemName.value;
    const itemPrice = inputForm.elements.itemPrice.value;
    const itemDescription = inputForm.elements.itemDescription.value;
    const itemImage = inputForm.elements.itemImage.files[0]; // Get the first file uploaded with the form

    const newItem = `${itemName}, ${itemPrice}, ${itemDescription}`;

    fs.writeFile(path.join(__dirname, 'newItem.txt'), newItem, (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log('New item added to file!');
    });

    const s3 = new AWS.S3();
    const params = {
        Bucket: 'your-bucket-name',
        Key: itemImage.name, // Use the original file name as the S3 object key
        Body: itemImage.data // Use the file data as the S3 object body
    };
    s3.upload(params, function(err, data) {
        if (err) {
            console.log("Error", err);
        } if (data) {
            console.log("Upload Success", data.Location);
        }
    });
});
