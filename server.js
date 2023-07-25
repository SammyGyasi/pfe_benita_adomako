const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors'); // Import the cors module
const app = express();
const port = 3000; // Replace with your desired port number

app.use(express.json());
app.use(cors()); // Enable CORS

// Create a route to handle the email sending
app.post('/send-email', (req, res) => {
  const { name, email, message } = req.body;

  console.log('Received data:', name, email, message);

  // Create a Nodemailer transporter using your email service provider's credentials
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'gyasisamuelkobina22@gmail.com',
      pass: 'hpwdczghjbabrswt'
    }
  });

  // Define the email options
  const mailOptions = {
    from: 'your-email@gmail.com',
    to: 'adomakobenita@gmail.com', // Replace with your email address
    subject: 'New Contact Form Submission From Explore Ghana',
    text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
  };

  // Send the email
  transporter.sendMail(mailOptions, function(error, info) {
    if (error) {
      console.error(error);
      res.status(500).send('Failed to send email');
    } else {
      console.log('Email sent: ' + info.response);
      res.sendStatus(200);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
