// Deals & Sales — client-side filter logic
(function () {
  const grid = document.getElementById('deal-grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.deal-card'));
  const noResults = document.getElementById('no-results');
  const chips = Array.from(document.querySelectorAll('.chip'));

  let statusFilter = 'all';
  let tierFilter = 'all';

  function applyFilters() {
    let visibleCount = 0;
    cards.forEach((card) => {
      const status = card.getAttribute('data-status');
      const tier = card.getAttribute('data-tier');
      const statusMatch = statusFilter === 'all' || status === statusFilter;
      const tierMatch = tierFilter === 'all' || tier === tierFilter;
      const show = statusMatch && tierMatch;
      card.style.display = show ? '' : 'none';
      if (show) visibleCount++;
    });
    noResults.style.display = visibleCount === 0 ? 'block' : 'none';
  }

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      const type = chip.getAttribute('data-filter-type');
      const value = chip.getAttribute('data-filter');

      // Deactivate siblings of the same filter type
      chips
        .filter((c) => c.getAttribute('data-filter-type') === type)
        .forEach((c) => c.classList.remove('active'));
      chip.classList.add('active');

      if (type === 'status') statusFilter = value;
      if (type === 'tier') tierFilter = value;

      applyFilters();
    });
  });

  applyFilters();
})();
