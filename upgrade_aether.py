import os
import re

def upgrade_aether():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\aether.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_new = """
            const canvas = document.getElementById('aether-canvas'); if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const stats = document.getElementById('weather-stats');
            const searchInput = document.getElementById('weather-search');
            const flash = document.querySelector('.thunder-flash');
            
            function resize() {
                canvas.width = canvas.parentElement.clientWidth;
                canvas.height = canvas.parentElement.clientHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            let elements = [];
            let windStreaks = [];
            let currentCondition = 'clear';
            let targetCondition = 'clear';
            let isDay = 1;
            let windSpeed = 0;
            let fadeAlpha = 1.0;

            let stars = Array.from({length: 150}, () => ({
                x: Math.random() * 2000, y: Math.random() * 1000, 
                r: Math.random() * 1.5, speed: Math.random() * 0.3 + 0.05
            }));
            let clouds = Array.from({length: 12}, () => ({
                x: Math.random() * 2000, y: Math.random() * 400,
                speed: Math.random() * 0.2 + 0.1, size: 60 + Math.random() * 100
            }));

            class AtmoParticle {
                constructor() { this.reset(true); }
                reset(randomY=false) {
                    this.x = Math.random() * canvas.width * 1.5; 
                    this.y = randomY ? Math.random() * canvas.height : -30;
                    this.baseWindX = -(windSpeed * 0.4) - 0.2;
                    
                    if (currentCondition === 'rain' || currentCondition === 'thunder') {
                        this.vx = this.baseWindX - 1; 
                        this.vy = 10 + Math.random() * 6;
                        this.length = 16 + Math.random() * 16; 
                        this.alpha = Math.random() * 0.3 + 0.1;
                    } else if (currentCondition === 'snow') {
                        this.vx = this.baseWindX + (Math.random() - 0.5) * 1.2; 
                        this.vy = 1 + Math.random() * 2.5;
                        this.radius = 1.5 + Math.random() * 3; 
                        this.alpha = Math.random() * 0.5 + 0.2;
                    } else if (currentCondition === 'mist') {
                        this.vx = this.baseWindX + (Math.random() - 0.5) * 0.5; 
                        this.vy = 0.1 + Math.random() * 0.4;
                        this.radius = 3 + Math.random() * 4; 
                        this.alpha = Math.random() * 0.1;
                    } else {
                        this.vx = this.baseWindX + (Math.random() - 0.5) * 0.2; 
                        this.vy = 0.5 + Math.random() * 0.5;
                        this.radius = 0.8 + Math.random() * 1.5; 
                        this.alpha = Math.random() * 0.2;
                    }
                }
                update() {
                    this.x += this.vx; this.y += this.vy;
                    if (this.y > canvas.height || this.x < -50) this.reset();
                }
                draw() {
                    ctx.beginPath();
                    if (currentCondition === 'rain' || currentCondition === 'thunder') {
                        ctx.strokeStyle = isDay === 1 ? `rgba(140, 155, 180, ${this.alpha * fadeAlpha})` : `rgba(176, 161, 113, ${this.alpha * fadeAlpha})`;
                        ctx.lineWidth = 1.5; ctx.moveTo(this.x, this.y); 
                        ctx.lineTo(this.x + this.vx * 0.5, this.y + this.length); ctx.stroke();
                    } else {
                        ctx.fillStyle = currentCondition === 'snow' ? `rgba(240, 245, 255, ${this.alpha * fadeAlpha})` : `rgba(176, 161, 113, ${this.alpha * fadeAlpha})`;
                        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2); ctx.fill();
                    }
                }
            }

            class AirflowStreak {
                constructor() { this.reset(); }
                reset() { this.x = canvas.width + Math.random() * 200; this.y = Math.random() * canvas.height; this.speed = 6 + Math.random() * 8; this.length = 80 + Math.random() * 120; this.alpha = Math.random() * 0.08 + 0.02; }
                update() { this.x -= this.speed + (windSpeed * 0.2); if (this.x < -this.length) this.reset(); }
                draw() { ctx.beginPath(); ctx.strokeStyle = `rgba(255,255,255,${this.alpha * fadeAlpha})`; ctx.lineWidth = 1; ctx.moveTo(this.x, this.y); ctx.lineTo(this.x + this.length, this.y); ctx.stroke(); }
            }

            function triggerLightning() {
                if (currentCondition !== 'thunder') return;
                if (typeof AudioMatrix !== 'undefined') AudioMatrix.playThunder();
                if (flash) {
                    flash.style.opacity = isDay === 1 ? '0.4' : '0.7';
                    setTimeout(() => { flash.style.opacity = '0'; }, 50);
                    setTimeout(() => { if(Math.random() > 0.4) flash.style.opacity = '0.3'; setTimeout(() => { flash.style.opacity = '0'; }, 40); }, 100);
                }
            }
            setInterval(() => { if (currentCondition === 'thunder' && Math.random() > 0.4) triggerLightning(); }, 3500);

            function buildEnvironment(particleCount) {
                elements = []; windStreaks = [];
                for (let i = 0; i < particleCount; i++) elements.push(new AtmoParticle());
                if (windSpeed > 10 || currentCondition === 'wind') {
                    for (let i = 0; i < 20; i++) windStreaks.push(new AirflowStreak());
                }
            }

            function run() {
                if (currentCondition !== targetCondition) {
                    fadeAlpha -= 0.02;
                    if (fadeAlpha <= 0) {
                        currentCondition = targetCondition;
                        buildEnvironment(targetParticleCount);
                    }
                } else if (fadeAlpha < 1.0) {
                    fadeAlpha += 0.02;
                }

                let bgGrad = ctx.createLinearGradient(0, 0, 0, canvas.height);
                if (isDay === 1) {
                    if (['rain', 'thunder', 'snow'].includes(currentCondition)) {
                        bgGrad.addColorStop(0, '#101622'); bgGrad.addColorStop(1, '#05080f');
                    } else {
                        bgGrad.addColorStop(0, '#13233c'); bgGrad.addColorStop(1, '#050912');
                    }
                } else {
                    bgGrad.addColorStop(0, '#030408'); bgGrad.addColorStop(1, '#010102');
                }
                ctx.fillStyle = bgGrad; ctx.fillRect(0, 0, canvas.width, canvas.height);

                // Parallax Background
                if (isDay === 0) {
                    ctx.fillStyle = `rgba(255,255,255,${0.6 * fadeAlpha})`;
                    stars.forEach(s => {
                        s.x -= s.speed * (windSpeed * 0.05 + 0.1);
                        if (s.x < 0) s.x = canvas.width + 10;
                        ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI*2); ctx.fill();
                    });
                } else if (!['clear'].includes(currentCondition)) {
                    ctx.fillStyle = `rgba(255,255,255,${0.03 * fadeAlpha})`;
                    clouds.forEach(c => {
                        c.x -= c.speed * (windSpeed * 0.1 + 0.2);
                        if (c.x < -200) c.x = canvas.width + 200;
                        ctx.beginPath(); ctx.arc(c.x, c.y, c.size, 0, Math.PI*2); ctx.fill();
                    });
                }

                ctx.save();
                const nodeX = canvas.width - 120; const nodeY = 120;
                ctx.globalAlpha = (['rain', 'thunder'].includes(currentCondition) ? 0.15 : (currentCondition === 'mist' ? 0.3 : 1.0)) * fadeAlpha;

                if (isDay === 1) {
                    ctx.shadowBlur = 50; ctx.shadowColor = 'rgba(212, 175, 55, 0.6)';
                    let sunGrad = ctx.createRadialGradient(nodeX, nodeY, 2, nodeX, nodeY, 50);
                    sunGrad.addColorStop(0, 'rgba(255, 245, 210, 0.95)');
                    sunGrad.addColorStop(0.4, 'rgba(212, 175, 55, 0.4)');
                    sunGrad.addColorStop(1, 'rgba(212, 175, 55, 0)');
                    ctx.fillStyle = sunGrad; ctx.beginPath(); ctx.arc(nodeX, nodeY, 50, 0, Math.PI * 2); ctx.fill();
                } else {
                    ctx.shadowBlur = 40; ctx.shadowColor = 'rgba(255, 255, 255, 0.3)';
                    ctx.fillStyle = 'rgba(230, 235, 245, 0.9)';
                    ctx.beginPath(); ctx.arc(nodeX, nodeY, 22, 0, Math.PI * 2); ctx.fill();
                    ctx.shadowBlur = 0; ctx.fillStyle = ['rain','thunder','snow'].includes(currentCondition) ? '#05080f' : '#030408';
                    ctx.beginPath(); ctx.arc(nodeX - 8, nodeY - 6, 22, 0, Math.PI * 2); ctx.fill();
                }
                ctx.restore();

                windStreaks.forEach(s => { s.update(); s.draw(); });
                elements.forEach(p => { p.update(); p.draw(); });
                
                requestAnimationFrame(run);
            }

            let targetParticleCount = 40;
            async function fetchMetrics(lat, lon, city) {
                stats.innerText = "Querying live weather matrix...";
                try {
                    const res = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`);
                    const data = await res.json();
                    
                    const code = data.current_weather.weathercode;
                    isDay = data.current_weather.is_day !== undefined ? data.current_weather.is_day : 1; 
                    windSpeed = data.current_weather.windspeed || 0;

                    const prefix = isDay === 1 ? "DAY" : "NIGHT";
                    const windReadout = windSpeed > 15 ? ` // GALE_FORCE: ${windSpeed}KM/H` : ` // WIND: ${windSpeed}KM/H`;

                    if ([95, 96, 99].includes(code)) {
                        targetCondition = 'thunder'; targetParticleCount = 180;
                        stats.innerText = `LOC: ${city.toUpperCase()} // MATRIX: ${prefix}_ELECTROMAGNETIC_THUNDERSTORM${windReadout}`; 
                    } else if ([71, 73, 75, 77, 85, 86].includes(code)) {
                        targetCondition = 'snow'; targetParticleCount = 200;
                        stats.innerText = `LOC: ${city.toUpperCase()} // MATRIX: ${prefix}_CRYOSPHERIC_SNOWFALL${windReadout}`; 
                    } else if ([45, 48].includes(code)) {
                        targetCondition = 'mist'; targetParticleCount = 250;
                        stats.innerText = `LOC: ${city.toUpperCase()} // MATRIX: ${prefix}_CONDENSED_MIST_FIELD${windReadout}`; 
                    } else if ([51, 53, 55, 61, 63, 65, 80, 81, 82].includes(code)) {
                        targetCondition = 'rain'; targetParticleCount = 160;
                        stats.innerText = `LOC: ${city.toUpperCase()} // MATRIX: ${prefix}_LIQUID_PRECIPITATION_RAIN${windReadout}`; 
                    } else {
                        targetCondition = windSpeed > 18 ? 'wind' : 'clear'; targetParticleCount = 50;
                        stats.innerText = `LOC: ${city.toUpperCase()} // MATRIX: ${prefix}_METEOROLOGICAL_STABLE_CLEAR${windReadout}`; 
                    }
                } catch(e) {
                    targetCondition = 'clear'; isDay = 1; windSpeed = 0; targetParticleCount = 40;
                    stats.innerText = "LINK BACKUP RECOVERY NODE // AMBIENT DUST STATIC"; 
                }
                
                // If first run, set immediately
                if (currentCondition === 'clear' && elements.length === 0) {
                    currentCondition = targetCondition;
                    buildEnvironment(targetParticleCount);
                }
            }

            const searchContainer = document.querySelector('.aether-search-select-container');
            const dropdownMenu = document.getElementById('weather-dropdown-list');
            let debounceTimer = null;

            searchInput.addEventListener('click', (e) => {
                e.stopPropagation();
                if (dropdownMenu.children.length > 0) {
                    dropdownMenu.classList.add('show');
                    searchContainer.classList.add('active');
                }
            });

            searchInput.addEventListener('input', () => {
                const currentStr = searchInput.value.trim().toLowerCase();
                clearTimeout(debounceTimer);

                if (currentStr.length < 2) {
                    dropdownMenu.classList.remove('show');
                    searchContainer.classList.remove('active');
                    dropdownMenu.innerHTML = '';
                    return;
                }

                debounceTimer = setTimeout(async () => {
                    try {
                        const res = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(currentStr)}&count=6`);
                        const data = await res.json();
                        
                        dropdownMenu.innerHTML = '';

                        if (data.results && data.results.length > 0) {
                            data.results.forEach(city => {
                                const countryMarker = city.country_code ? ` [${city.country_code.toUpperCase()}]` : '';
                                const administrativeNode = city.admin1 ? `, ${city.admin1}` : '';
                                const fullLocationLabel = `${city.name}${administrativeNode}${countryMarker}`;

                                const itemNode = document.createElement('div');
                                itemNode.className = 'atmo-dropdown-item';
                                itemNode.textContent = fullLocationLabel;

                                itemNode.addEventListener('click', (e) => {
                                    e.stopPropagation();
                                    searchInput.value = city.name.toUpperCase();
                                    dropdownMenu.classList.remove('show');
                                    searchContainer.classList.remove('active');
                                    
                                    fetchMetrics(city.latitude, city.longitude, city.name);
                                });

                                dropdownMenu.appendChild(itemNode);
                            });

                            dropdownMenu.classList.add('show');
                            searchContainer.classList.add('active');
                        } else {
                            dropdownMenu.innerHTML = '<div class="atmo-dropdown-item" style="opacity:0.4; pointer-events:none;">NO ARCHIVE NODES MATCHED</div>';
                            dropdownMenu.classList.add('show');
                        }
                    } catch (err) {}
                }, 300);
            });

            document.addEventListener('click', () => {
                dropdownMenu.classList.remove('show');
                searchContainer.classList.remove('active');
            });

            searchInput.onkeydown = async (e) => {
                if (e.key === 'Enter' && searchInput.value.trim() !== '') {
                    const val = searchInput.value.trim();
                    dropdownMenu.classList.remove('show');
                    searchContainer.classList.remove('active');
                    
                    const firstSuggestion = dropdownMenu.querySelector('.atmo-dropdown-item:not([style*="pointer-events"])');
                    if (firstSuggestion) {
                        firstSuggestion.click();
                        return;
                    }

                    stats.innerText = "Resolving terminal coordinate telemetry...";
                    try {
                        const geo = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(val)}&count=1`);
                        const gData = await geo.json();
                        if (gData.results && gData.results.length > 0) {
                            fetchMetrics(gData.results[0].latitude, gData.results[0].longitude, gData.results[0].name);
                        } else { stats.innerText = "TELEMETRY ERROR: CODES UNRESOLVED"; }
                    } catch(err) { stats.innerText = "ROUTER NETWORK ERROR: CONNECTION REFUSED"; }
                }
            };

            fetchMetrics(10.52, 76.21, "Thrissur");
            run();
"""
    
    # Replace everything between <script>\n    (function() {\n and \n    })();\n</script>
    import re
    pattern = re.compile(r'<script>\s*\(function\(\) \{\s*(.*?)\s*\}\)\(\);\s*</script>', re.DOTALL)
    
    new_content = pattern.sub(f'<script>\n    (function() {{\n{js_new}\n    }})();\n</script>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
if __name__ == "__main__":
    upgrade_aether()
