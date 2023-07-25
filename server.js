// Server-side (Node.js with Express)

const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/send-email', (req, res) => {
  const { recipient, subject, body } = req.body;

  // Create a Nodemailer transporter
  const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: 'gyasisamuelkobina22@gmail.com', // Replace with your Gmail email address
      pass: 'Power4026', // Replace with your Gmail password
    },
  });

  // Set up email data
  const mailOptions = {
    from: 'your-email@gmail.com',
    to: recipient,
    subject: subject,
    text: body,
  };

  // Send the email
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('Error sending email:', error);
      res.status(500).send('Error sending email');
    } else {
      console.log('Email sent:', info.response);
      res.status(200).send('Email sent successfully');
    }
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on http://localhost:${port}`);
});
