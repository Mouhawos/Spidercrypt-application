// script.js
document.addEventListener('DOMContentLoaded', () => {
    const apis = document.querySelectorAll('.api');

    const options = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                entry.target.classList.remove('visible');
            }
        });
    }, options);

    apis.forEach(api => {
        observer.observe(api);
    });
});
