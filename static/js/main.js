function leadForm() {
  return {
    email: '',
    loading: false,
    submit() {
      if (!this.email || !this.email.includes('@')) return;
      this.loading = true;
      fetch('/api/lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: this.email,
          source: 'final_cta',
        }),
      })
        .then((r) => r.json())
        .then((data) => {
          this.loading = false;
          if (data.ok) {
            alert('Спасибо! Мы свяжемся в ближайшее время — на ' + this.email);
            this.email = '';
          } else {
            alert('Похоже, email некорректный. Попробуй ещё раз.');
          }
        })
        .catch(() => {
          this.loading = false;
          alert('Что-то пошло не так. Напиши нам на hello@mentortrack.io');
        });
    },
  };
}

document.querySelectorAll('a[href^="#"]').forEach((a) => {
  a.addEventListener('click', (e) => {
    const id = a.getAttribute('href');
    if (id.length <= 1) return;
    const target = document.querySelector(id);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
