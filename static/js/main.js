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

    // --- Premium Custom Cursor: Trailing "Ants" (Desktop Only) ---
    if (window.matchMedia("(pointer: fine)").matches) {
        const style = document.createElement('style');
        style.textContent = `
            body, a, button { cursor: none !important; }
            .custom-cursor-head {
                position: fixed; top: 0; left: 0; width: 10px; height: 10px; background: var(--color-accent); border-radius: 50%; pointer-events: none; z-index: 9999;
                transform: translate(-50%, -50%); transition: width 0.2s, height 0.2s;
            }
            .custom-cursor-ant {
                position: fixed; top: 0; left: 0; width: 6px; height: 6px; background: var(--color-accent); border-radius: 50%; pointer-events: none; z-index: 9998;
                transform: translate(-50%, -50%); transition: opacity 0.3s, background 0.3s;
            }
            .custom-cursor-ant.hover {
                background: white; opacity: 0.8 !important;
            }
            .custom-cursor-head.hover {
                width: 40px; height: 40px; background: transparent; border: 2px solid var(--color-accent);
            }
        `;
        document.head.appendChild(style);
        
        const head = document.createElement('div');
        head.className = 'custom-cursor-head';
        document.body.appendChild(head);
        
        const numAnts = 8;
        const ants = [];
        const positions = [];
        
        for (let i = 0; i < numAnts; i++) {
            const ant = document.createElement('div');
            ant.className = 'custom-cursor-ant';
            ant.style.opacity = 1 - (i * 0.1);
            document.body.appendChild(ant);
            ants.push(ant);
            positions.push({ x: -100, y: -100 });
        }
        
        let mouseX = -100, mouseY = -100;
        
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        const render = () => {
            // Update head
            head.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
            
            // Update ants (each ant follows the one in front of it)
            let prevX = mouseX;
            let prevY = mouseY;
            
            for (let i = 0; i < numAnts; i++) {
                positions[i].x += (prevX - positions[i].x) * 0.3;
                positions[i].y += (prevY - positions[i].y) * 0.3;
                
                ants[i].style.transform = `translate(${positions[i].x}px, ${positions[i].y}px)`;
                
                prevX = positions[i].x;
                prevY = positions[i].y;
            }
            
            requestAnimationFrame(render);
        };
        requestAnimationFrame(render);
        
        // Use event delegation for hover
        document.body.addEventListener('mouseover', (e) => {
            if (e.target.closest('a, button, input, textarea, [role="button"]')) {
                head.classList.add('hover');
                ants.forEach(ant => ant.classList.add('hover'));
            }
        });
        document.body.addEventListener('mouseout', (e) => {
            if (e.target.closest('a, button, input, textarea, [role="button"]')) {
                head.classList.remove('hover');
                ants.forEach(ant => ant.classList.remove('hover'));
            }
        });
    }
});
