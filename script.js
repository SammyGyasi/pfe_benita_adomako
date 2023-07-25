$(document).ready(function() {
    // Handle form submission
    $('#contactForm').submit(function(event) {
      event.preventDefault(); // Prevent the form from submitting normally
  
      // Get form data
      var name = $('#name').val();
      var email = $('#email').val();
      var message = $('#message').val();
  
      // Send form data to server-side endpoint
      $.ajax({
        url: 'http://localhost:3000/send-email', // Replace with your server's URL
        method: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({
          name: name,
          email: email,
          message: message
        }),
        success: function(response) {
          $('#messageText').text('Email sent successfully!');
          $('#messageText').removeClass('error-message').addClass('success-message');
          $('#contactForm')[0].reset(); // Reset the form
        },
        error: function() {
          $('#messageText').text('Email sent successfully?.');
          $('#messageText').removeClass('success-message').addClass('error-message');
        }
      });
    });
  });
  