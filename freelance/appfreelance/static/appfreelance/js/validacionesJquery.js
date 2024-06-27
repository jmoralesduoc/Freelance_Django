$(document).ready(function() {
    $("#resetForm").on("submit", function(event) {
        event.preventDefault();
        var email = $("#email").val();
        var newPassword = $("#newPassword").val();
        var confirmPassword = $("#confirmPassword").val();
        var message = "";

        // Validar el formato del correo electrónico
        if (!validateEmail(email)) {
            message = "Por favor, ingrese un correo electrónico válido.";
            $("#message").text(message);
            return;
        }

        // Validar la longitud de la nueva contraseña
        if (newPassword.length < 8) {
            message = "La nueva contraseña debe tener al menos 8 caracteres.";
            $("#message").text(message);
            return;
        }

        // Validar que la contraseña tenga al menos una letra y un número
        if (!validatePassword(newPassword)) {
            message = "La contraseña debe contener al menos una letra y un número.";
            $("#message").text(message);
            return;
        }

        // Validar que las contraseñas coincidan
        if (newPassword !== confirmPassword) {
            message = "Las contraseñas no coinciden.";
            $("#message").text(message);
            return;
        }

        // Si todas las validaciones pasan, se puede enviar el formulario.
        message = "Contraseña restablecida con éxito.";
        $("#message").css("color", "green").text(message);
    });

    function validateEmail(email) {
        var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return re.test(email);
    }

    function validatePassword(password) {
        var re = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
        return re.test(password);
    }
});

