function submitForm() {
    var name = $('#name').val();
    var email = $('#email').val();
    var message = $('#message').val();
    var token = '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';
    $.ajax({
      url: 'https://api.github.com/repos/fastmrt/fastmrt.github.io/dispatches',
      type: 'POST',
      headers: {
        'Accept': 'application/vnd.github.everest-preview+json',
        'Authorization': 'Bearer ' + token
      },
      data: JSON.stringify({
        event_type: 'form_submission',
        client_payload: {
          name: name,
          email: email,
          message: message
        }
      }),
      success: function(result) {
        alert('Form submitted successfully!');
      },
      error: function(xhr, status, error) {
        alert('Form submission failed: ' + error);
      }
    });
  }