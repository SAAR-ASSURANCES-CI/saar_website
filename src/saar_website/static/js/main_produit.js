     // Toggle Accordion
function toggleAccordion(header) {
    const content = header.nextElementSibling;
    const allContents = document.querySelectorAll('.accordion-content');
    
    // Fermer toutes les autres sections
    allContents.forEach(item => {
        if (item !== content) {
            item.classList.remove('active');
        }
    });

    // Ouvrir/Fermer la section courante
    content.classList.toggle('active');
}

// Smooth scrolling pour les ancres
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Observer pour animation au scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Appliquer l'animation aux cards
document.querySelectorAll('.feature-card, .plan-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});
