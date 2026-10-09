document.addEventListener('DOMContentLoaded', function () {
    const dateInput = document.querySelector('input[type="date"]');
    if (dateInput) {
        dateInput.min = new Date().toISOString().split('T')[0];
    }

    const menuLinks = document.querySelectorAll('.main-nav a');
    menuLinks.forEach(link => {
        link.addEventListener('click', () => document.body.classList.remove('nav-open'));
    });
});
