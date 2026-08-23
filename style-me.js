// Style Me — waitlist form (client-side only, no backend)
(function () {
  const form = document.getElementById('waitlist-form');
  const success = document.getElementById('waitlist-success');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    form.style.display = 'none';
    success.classList.add('show');
  });
})();
