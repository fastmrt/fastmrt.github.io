import javax.mail.*;
import javax.mail.internet.*;

// Get form data
String name = request.getParameter("name");
String email = request.getParameter("email");
// String message = request.getParameter("message");

// Set up SMTP
String host = "smtp.gmail.com";
int port = 587;
String username = System.getenv("FASTMRT_EMAIL");
String password = System.getenv("FASTMRT_EMAIL_PASSWORD");
Properties props = new Properties();
props.put("mail.smtp.auth", "true");
props.put("mail.smtp.starttls.enable", "true");
props.put("mail.smtp.host", host);
props.put("mail.smtp.port", port);
Session session = Session.getInstance(props, new Authenticator() {
  protected PasswordAuthentication getPasswordAuthentication() {
    return new PasswordAuthentication(username, password);
  }
});

// Create email message
String subject = "Subject of your email";
String body = "Dear " + name + ",\n\n" + "test, test";
Message emailMessage = new MimeMessage(session);
emailMessage.setFrom(new InternetAddress(username));
emailMessage.setRecipient(Message.RecipientType.TO, new InternetAddress(email));
emailMessage.setSubject(subject);
emailMessage.setText(body);

// Send email
Transport.send(emailMessage);