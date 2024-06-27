$(document).ready(function() {
    // Función para mostrar el popup
    function showPopup() {
        $('#popup').fadeIn();
    }

    // Función para ocultar el popup
    function hidePopup() {
        $('#popup').fadeOut();
    }

    // Asociar funciones a eventos
    $('#openPopup').click(function() {
        showPopup();
    });

    $('#closePopup').click(function() {
        hidePopup();
    });

    // Ocultar popup cuando se hace clic fuera del contenido del popup
    $(window).click(function(event) {
        if ($(event.target).is('#popup')) {
            hidePopup();
        }
    });
});
