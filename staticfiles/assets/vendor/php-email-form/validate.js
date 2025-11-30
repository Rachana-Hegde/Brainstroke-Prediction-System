/**
* PHP Email Form Validation - v3.9
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector('.php-email-form');
  const loadingDiv = document.querySelector('.loading');
  const sentMessage = document.querySelector('.sent-message');

  if (form) {
    form.addEventListener('submit', function () {
      loadingDiv.style.display = 'block';
      sentMessage.style.display = 'none';
    });
  }
});
