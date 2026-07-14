import type { Metadata } from "next";
import { Inter, Outfit } from "next/font/google";
import "./globals.css";
import Script from "next/script";import { Heart } from "@phosphor-icons/react/dist/ssr/Heart";
import { List } from "@phosphor-icons/react/dist/ssr/List";
import { Moon } from "@phosphor-icons/react/dist/ssr/Moon";
import { Sparkle } from "@phosphor-icons/react/dist/ssr/Sparkle";
import { Sun } from "@phosphor-icons/react/dist/ssr/Sun";
import { X } from "@phosphor-icons/react/dist/ssr/X";


const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const outfit = Outfit({
  variable: "--font-outfit",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Muhammed Fadhil EH | Full Stack Developer",
  description: "Portfolio of Muhammed Fadhil EH, a Full Stack Developer specializing in crafting sleek, user-focused digital experiences.",
  openGraph: {
    title: "Muhammed Fadhil EH | Full Stack Developer",
    description: "Portfolio of Muhammed Fadhil EH, a Full Stack Developer specializing in crafting sleek, user-focused digital experiences.",
    url: "https://muhammedfadhil.vercel.app",
    type: "website",
    images: [
      {
        url: "https://muhammedfadhil.vercel.app/media/profile/hero.jpg",
        width: 1200,
        height: 630,
        alt: "Muhammed Fadhil EH - Full Stack Developer",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Muhammed Fadhil EH | Full Stack Developer",
    description: "Portfolio of Muhammed Fadhil EH, a Full Stack Developer specializing in crafting sleek, user-focused digital experiences.",
  },
  keywords: ["Muhammed Fadhil EH", "Full Stack Developer", "Web Developer", "Portfolio", "ShanuDigiCore", "Django", "React", "Next.js"],
  robots: "index, follow",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${outfit.variable} scroll-smooth dark`} suppressHydrationWarning>
      <head>
        <Script
          id="theme-script"
          strategy="beforeInteractive"
          dangerouslySetInnerHTML={{
            __html: `
              if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                  document.documentElement.classList.add('dark');
              } else {
                  document.documentElement.classList.remove('dark');
              }
            `,
          }}
        />
        <meta name="theme-color" content="#0a0a0a" />
      </head>
      <body className="relative flex min-h-screen flex-col overflow-x-hidden pt-24 selection:bg-[var(--color-accent)] selection:text-black">
        <nav className="fixed top-6 left-1/2 -translate-x-1/2 w-[90%] max-w-2xl z-50 transition-all duration-300" id="navbar">
          <div className="md:animate-liquid px-6 py-4 rounded-full flex items-center justify-between shadow-[0_8px_32px_rgba(0,0,0,0.1),inset_0_1px_2px_rgba(255,255,255,0.4)] dark:shadow-[0_8px_32px_rgba(0,0,0,0.3),inset_0_1px_1px_rgba(255,255,255,0.1)] border border-white/30 dark:border-white/10 bg-white/20 dark:bg-black/20 backdrop-blur-lg backdrop-saturate-200">
            <a href="#" className="flex items-center gap-2 group">
              <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-gray-900 to-gray-600 dark:from-white dark:to-gray-400 font-outfit tracking-tight">Fadhil.</span>
            </a>
            <div className="flex items-center gap-4">
              <div className="hidden md:flex items-center gap-6 text-base font-semibold">
                <a href="#about" className="hover:text-[var(--color-accent)] transition-colors flex items-center gap-1"><Sparkle className="text-xs opacity-50" weight="fill" /> About</a>
                <a href="#experience" className="hover:text-[var(--color-accent)] transition-colors flex items-center gap-1"><Sparkle className="text-xs opacity-50" weight="fill" /> Experience</a>
                <a href="#works" className="hover:text-[var(--color-accent)] transition-colors flex items-center gap-1"><Sparkle className="text-xs opacity-50" weight="fill" /> Works</a>
                <a href="#contact" className="hover:text-[var(--color-accent)] transition-colors flex items-center gap-1"><Sparkle className="text-xs opacity-50" weight="fill" /> Contact</a>
              </div>
              <button id="theme-toggle" className="p-2 rounded-full border-2 border-transparent hover:border-black dark:hover:border-white bg-gray-100 dark:bg-gray-800 transition-all hover:-translate-y-0.5" aria-label="Toggle Dark Mode">
                <Sun className="text-lg hidden dark:block" weight="fill" />
                <Moon className="text-lg block dark:hidden" weight="fill" />
              </button>
              {/* Mobile Menu Button */}
              <button id="mobile-menu-btn" aria-label="Toggle Mobile Menu" className="md:hidden p-2 rounded-full border-2 border-transparent hover:border-black dark:hover:border-white bg-gray-100 dark:bg-gray-800 transition-all hover:-translate-y-0.5">
                  <List className="text-lg menu-icon" weight="fill" />
                  <X className="text-lg hidden close-icon" weight="fill" />
              </button>
            </div>
          </div>
          {/* Mobile Menu Dropdown */}
          <div id="mobile-menu" className="hidden md:hidden absolute top-full left-0 right-0 mt-4 p-6 rounded-[2rem] flex-col gap-6 text-2xl font-bold shadow-[0_8px_32px_rgba(0,0,0,0.1),inset_0_1px_2px_rgba(255,255,255,0.4)] dark:shadow-[0_8px_32px_rgba(0,0,0,0.3),inset_0_1px_1px_rgba(255,255,255,0.1)] border border-white/30 dark:border-white/10 bg-white/20 dark:bg-black/20 backdrop-blur-lg backdrop-saturate-200 transition-all">
              <a href="#about" className="hover:text-black dark:hover:text-white transition-colors mobile-link flex items-center gap-3 text-black dark:text-white drop-shadow-sm"><Sparkle className="text-xl text-black dark:text-white" weight="fill" /> About</a>
              <a href="#experience" className="hover:text-black dark:hover:text-white transition-colors mobile-link flex items-center gap-3 text-black dark:text-white drop-shadow-sm"><Sparkle className="text-xl text-black dark:text-white" weight="fill" /> Experience</a>
              <a href="#works" className="hover:text-black dark:hover:text-white transition-colors mobile-link flex items-center gap-3 text-black dark:text-white drop-shadow-sm"><Sparkle className="text-xl text-black dark:text-white" weight="fill" /> Works</a>
              <a href="#mini-projects" className="hover:text-black dark:hover:text-white transition-colors mobile-link flex items-center gap-3 text-black dark:text-white drop-shadow-sm"><Sparkle className="text-xl text-black dark:text-white" weight="fill" /> Experiments</a>
              <a href="#contact" className="hover:text-black dark:hover:text-white transition-colors mobile-link flex items-center gap-3 text-black dark:text-white drop-shadow-sm"><Sparkle className="text-xl text-black dark:text-white" weight="fill" /> Contact</a>
          </div>
        </nav>
        {children}
        <footer className="py-8 text-center text-sm text-gray-500 dark:text-gray-400 border-t border-gray-200 dark:border-gray-800 mt-auto">
          <div className="mx-auto max-w-7xl px-6">
              <p>&copy; {new Date().getFullYear()} | Made with <Heart className="text-red-500 mx-1" weight="fill" /> by Fadhil</p>
          </div>
        </footer>
        <Script
          id="interactive-scripts"
          strategy="afterInteractive"
          dangerouslySetInnerHTML={{
            __html: `
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
                      }
                  });
              }, observerOptions);
              document.querySelectorAll('.reveal-up').forEach((el) => {
                  revealObserver.observe(el);
              });

              // --- Mobile Menu Toggle ---
              const menuBtn = document.getElementById('mobile-menu-btn');
              const mobileMenu = document.getElementById('mobile-menu');
              if (menuBtn && mobileMenu) {
                  const menuIcon = menuBtn.querySelector('.menu-icon');
                  const closeIcon = menuBtn.querySelector('.close-icon');
                  
                  menuBtn.addEventListener('click', () => {
                      mobileMenu.classList.toggle('hidden');
                      mobileMenu.classList.toggle('flex');
                      menuIcon.classList.toggle('hidden');
                      closeIcon.classList.toggle('hidden');
                  });

                  document.querySelectorAll('.mobile-link').forEach(link => {
                      link.addEventListener('click', () => {
                          mobileMenu.classList.add('hidden');
                          mobileMenu.classList.remove('flex');
                          menuIcon.classList.remove('hidden');
                          closeIcon.classList.add('hidden');
                      });
                  });
              }

              // --- Premium Custom Cursor (Desktop Only) ---
              if (window.matchMedia("(pointer: fine)").matches) {
                  const style = document.createElement('style');
                  style.textContent = \`
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
                  \`;
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
                      dot.style.transform = \`translate(\${mouseX - 4}px, \${mouseY - 4}px)\`;
                  });
                  
                  const render = () => {
                      ringX += (mouseX - ringX) * 0.15;
                      ringY += (mouseY - ringY) * 0.15;
                      ring.style.transform = \`translate(\${ringX - 18}px, \${ringY - 18}px)\`;
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
            `
          }}
        />
      </body>
    </html>
  );
}
