function onEntry(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
        entry.target.classList.add('AnimOriginal');
        }
    });
    }

function setupAnimations() {
    const options = { 
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(onEntry, options);
    const animatedElements = document.querySelectorAll('.AnimLeft, .AnimRight , .AnimTop');

    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

window.addEventListener('load', setupAnimations);