document.getElementById('loginForm').addEventListener('submit', function(event) {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var emailError = document.getElementById('emailError');
    var passwordError = document.getElementById('passwordError');
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    var passwordPattern = /^(?=.*\d).{8,}$/;

    if (!emailPattern.test(username)) {
      emailError.style.display = 'block';
      event.preventDefault(); // Prevenir el envío del formulario si la validación falla
    } else {
      emailError.style.display = 'none';
    }

    if (!passwordPattern.test(password)) {
      passwordError.style.display = 'block';
      event.preventDefault(); // Prevenir el envío del formulario si la validación falla
    } else {
      passwordError.style.display = 'none';
    }
  });

