(() => {
  const quotes = document.querySelector('#quotes');
  const avg = document.querySelector('#avg');
  const rate = document.querySelector('#rate');
  if (!quotes || !avg || !rate) return;

  const eur = value => new Intl.NumberFormat('it-IT', {
    style: 'currency', currency: 'EUR', maximumFractionDigits: 0
  }).format(Number.isFinite(value) ? value : 0);

  const render = () => {
    const count = Math.max(0, Number(quotes.value) || 0);
    const average = Math.max(0, Number(avg.value) || 0);
    const pct = Math.min(100, Math.max(0, Number(rate.value) || 0)) / 100;
    document.querySelector('#pipelineValue').textContent = eur(count * average);
    document.querySelector('#quoteValue').textContent = (count * pct).toLocaleString('it-IT', { maximumFractionDigits: 1 });
    document.querySelector('#testValue').textContent = eur(count * average * pct);
  };

  [quotes, avg, rate].forEach(el => el.addEventListener('input', render));
  render();
})();
