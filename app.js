// LuxeFind shared app behavior — theme toggle, mobile nav, footer year, active nav highlight

(function () {
  // ---- Theme toggle ----
  const root = document.documentElement;
  const toggle = document.querySelector('[data-theme-toggle]');
  let theme = matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
  root.setAttribute('data-theme', theme);

  const sunIcon =
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>';
  const moonIcon =
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 14.5A8.5 8.5 0 1 1 9.5 3.5a7 7 0 0 0 11 11z"/></svg>';

  function paintToggle() {
    if (!toggle) return;
    toggle.innerHTML = theme === 'dark' ? sunIcon : moonIcon;
    toggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  }
  paintToggle();

  if (toggle) {
    toggle.addEventListener('click', () => {
      theme = theme === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', theme);
      paintToggle();
    });
  }

  // ---- Mobile nav ----
  const mobileToggle = document.querySelector('[data-mobile-nav-toggle]');
  const mobilePanel = document.querySelector('[data-mobile-nav-panel]');
  if (mobileToggle && mobilePanel) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = mobilePanel.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  // ---- Footer year (static freshness note is separate) ----
  const yearEls = document.querySelectorAll('[data-year]');
  yearEls.forEach((el) => (el.textContent = '2026'));
})();
