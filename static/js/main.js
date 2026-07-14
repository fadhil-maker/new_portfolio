document.addEventListener('DOMContentLoaded', () => {
    // --- Dark/Light Mode Toggle ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
            } else {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
            }
        });
    }

    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                navbar.classList.add('py-2');
                navbar.classList.remove('py-4');
            } else {
                navbar.classList.add('py-4');
                navbar.classList.remove('py-2');
            }
        });
    }

    // --- Scroll Reveal Animations ---
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Optional: Stop observing once revealed
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal-up').forEach((el) => {
        revealObserver.observe(el);
    });

    // --- Premium Custom Cursor (Desktop Only) ---
    if (window.matchMedia("(pointer: fine)").matches) {
        const style = document.createElement('style');
        style.textContent = `
            body, a, button { cursor: none !important; }
            .custom-cursor-dot {
                position: fixed; top: 0; left: 0; width: 8px; height: 8px; background: var(--color-accent); border-radius: 50%; pointer-events: none; z-index: 9999;
                transition: width 0.2s, height 0.2s;
            }
            .custom-cursor-ring {
                position: fixed; top: 0; left: 0; width: 36px; height: 36px; border: 2px solid var(--color-accent); border-radius: 50%; pointer-events: none; z-index: 9998;
                transition: width 0.3s, height 0.3s, background 0.3s, opacity 0.3s, border-color 0.3s;
            }
            .custom-cursor-ring.hover {
                width: 56px; height: 56px; background: var(--color-accent); opacity: 0.15; border-color: transparent;
            }
            .custom-cursor-dot.hover {
                width: 0; height: 0;
            }
        `;
        document.head.appendChild(style);
        
        const dot = document.createElement('div');
        dot.className = 'custom-cursor-dot';
        const ring = document.createElement('div');
        ring.className = 'custom-cursor-ring';
        
        document.body.appendChild(dot);
        document.body.appendChild(ring);
        
        let mouseX = -100, mouseY = -100;
        let ringX = -100, ringY = -100;
        
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            dot.style.transform = `translate(${mouseX - 4}px, ${mouseY - 4}px)`;
        });
        
        const render = () => {
            ringX += (mouseX - ringX) * 0.15;
            ringY += (mouseY - ringY) * 0.15;
            ring.style.transform = `translate(${ringX - 18}px, ${ringY - 18}px)`;
            requestAnimationFrame(render);
        };
        requestAnimationFrame(render);
        
        // Use event delegation for hover
        document.body.addEventListener('mouseover', (e) => {
            if (e.target.closest('a, button, input, textarea, [role="button"]')) {
                ring.classList.add('hover');
                dot.classList.add('hover');
            }
        });
        document.body.addEventListener('mouseout', (e) => {
            if (e.target.closest('a, button, input, textarea, [role="button"]')) {
                ring.classList.remove('hover');
                dot.classList.remove('hover');
            }
        });
    }
});
