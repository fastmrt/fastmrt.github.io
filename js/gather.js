function submitForm() {
    var name = $('#name').val();
    var email = $('#email').val();
    var institution = $('#institution').val();
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
          institution: institution
        }
      }),
      success: function(result) {
        alert('Form submit successfully!');
      },
      error: function(xhr, status, error) {
        alert('Form submission failed: ' + error);
      }
    });
  }