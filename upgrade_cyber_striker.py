import os
import re

def upgrade_striker():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_new = """
            const canvas = document.getElementById('striker-canvas'); if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const hud = document.getElementById('cs-score-readout');
            const gameOverScreen = document.getElementById('cs-terminal-screen');
            
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;

            let player = { x: canvas.width / 2, y: canvas.height - 100, w: 26, h: 26, shield: 3, weaponTier: 1 };
            let lasers = []; let enemyLasers = []; let enemies = []; let particles = []; let upgrades = []; let cosmicStars = [];
            let score = 0; let currentLevel = 1; let clockTicks = 0; let isSessionActive = true; let screenShake = 0;
            
            let boss = null;
            let bossSpawnedAt = 0;

            for (let i = 0; i < 60; i++) {
                cosmicStars.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, speed: 0.5 + Math.random() * 3, size: 1 + Math.random() * 2, color: Math.random() > 0.8 ? '#00e5ff' : '#ffffff' });
            }

            gameOverScreen.style.display = 'none';
            document.getElementById('cs-hud').style.opacity = '1';
            updateHudDisplay();

            function updateHudDisplay() {
                const shieldBar = player.shield > 0 ? "█".repeat(player.shield) : "NONE";
                hud.innerHTML = `LVL: ${currentLevel} &nbsp;&bull;&nbsp; SHIELDS: [ ${shieldBar} ] &nbsp;&bull;&nbsp; SCORE: ${String(score).padStart(4, '0')} XP`;
            }

            class LaserBolt {
                constructor(x, y, angleOffset = 0, isEnemy = false) {
                    this.x = x; this.y = y; this.r = isEnemy ? 4 : 3; 
                    this.vy = isEnemy ? 6 : -10;
                    this.vx = angleOffset;
                    this.isEnemy = isEnemy;
                }
                update() { this.x += this.vx; this.y += this.vy; }
                draw() {
                    ctx.save(); ctx.beginPath(); ctx.fillStyle = this.isEnemy ? '#ff007f' : '#00e5ff';
                    ctx.shadowBlur = 10; ctx.shadowColor = ctx.fillStyle;
                    ctx.arc(this.x, this.y, this.r, 0, Math.PI*2); ctx.fill(); ctx.restore();
                }
            }

            class CodeEnemy {
                constructor() {
                    this.w = 35; this.h = 35;
                    this.x = 40 + Math.random() * (canvas.width - 100); this.y = -40;
                    this.hp = Math.ceil(Math.random() * currentLevel * 1.5);
                    this.maxHp = this.hp;
                    this.vel = 1.0 + Math.random() * 1.5 + (currentLevel * 0.2);
                    this.angle = 0;
                    this.rotSpeed = (Math.random() - 0.5) * 0.1;
                    this.isHex = Math.random() > 0.5;
                }
                update() { this.y += this.vel; this.angle += this.rotSpeed; }
                draw() {
                    ctx.save();
                    ctx.translate(this.x + this.w/2, this.y + this.h/2);
                    ctx.rotate(this.angle);
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = this.maxHp > 2 ? '#ff007f' : '#ffaa00';
                    ctx.fillStyle = 'rgba(20, 10, 10, 0.8)';
                    
                    ctx.beginPath();
                    if (this.isHex) {
                        for (let i = 0; i < 6; i++) {
                            ctx.lineTo(this.w/2 * Math.cos(i * Math.PI / 3), this.h/2 * Math.sin(i * Math.PI / 3));
                        }
                    } else {
                        ctx.moveTo(0, -this.h/2); ctx.lineTo(this.w/2, this.h/2); ctx.lineTo(-this.w/2, this.h/2);
                    }
                    ctx.closePath();
                    ctx.fill(); ctx.stroke();
                    ctx.restore();
                    
                    // Health bar
                    let hpPercent = this.hp / this.maxHp;
                    ctx.fillStyle = 'rgba(255, 0, 127, 0.3)';
                    ctx.fillRect(this.x, this.y - 10, this.w, 4);
                    ctx.fillStyle = '#ff007f';
                    ctx.fillRect(this.x, this.y - 10, this.w * hpPercent, 4);
                }
            }

            class DreadnoughtBoss {
                constructor() {
                    this.w = 120; this.h = 80;
                    this.x = canvas.width / 2 - this.w / 2; this.y = -100;
                    this.hp = 50 + (currentLevel * 10);
                    this.maxHp = this.hp;
                    this.vx = 2;
                    this.entering = true;
                }
                update() {
                    if (this.entering) {
                        this.y += 1;
                        if (this.y >= 50) this.entering = false;
                    } else {
                        this.x += this.vx;
                        if (this.x < 20 || this.x + this.w > canvas.width - 20) this.vx *= -1;
                        
                        if (Math.random() < 0.05) {
                            enemyLasers.push(new LaserBolt(this.x + 20, this.y + this.h, 0, true));
                            enemyLasers.push(new LaserBolt(this.x + this.w - 20, this.y + this.h, 0, true));
                        }
                        if (Math.random() < 0.02) {
                            enemyLasers.push(new LaserBolt(this.x + this.w/2, this.y + this.h, (player.x - (this.x + this.w/2))/50, true));
                        }
                    }
                }
                draw() {
                    ctx.save();
                    ctx.translate(this.x, this.y);
                    ctx.fillStyle = '#111'; ctx.strokeStyle = '#ff007f'; ctx.lineWidth = 3;
                    ctx.shadowBlur = 20; ctx.shadowColor = '#ff007f';
                    
                    ctx.beginPath();
                    ctx.moveTo(0, 0); ctx.lineTo(this.w, 0); ctx.lineTo(this.w, this.h - 20);
                    ctx.lineTo(this.w/2 + 20, this.h); ctx.lineTo(this.w/2 - 20, this.h);
                    ctx.lineTo(0, this.h - 20); ctx.closePath();
                    ctx.fill(); ctx.stroke();
                    
                    // Core
                    ctx.fillStyle = '#ffaa00'; ctx.beginPath();
                    ctx.arc(this.w/2, this.h/2, 15 + Math.sin(Date.now() * 0.01)*3, 0, Math.PI*2);
                    ctx.fill();
                    ctx.restore();
                    
                    // Big Health Bar
                    let hpPercent = this.hp / this.maxHp;
                    ctx.fillStyle = 'rgba(255, 0, 127, 0.3)';
                    ctx.fillRect(this.x, this.y - 20, this.w, 8);
                    ctx.fillStyle = '#ff007f';
                    ctx.fillRect(this.x, this.y - 20, this.w * hpPercent, 8);
                }
            }

            class PowerNode {
                constructor(x, y) { this.x = x; this.y = y; this.r = 6; this.vy = 2; }
                update() { this.y += this.vy; }
                draw() {
                    ctx.save(); ctx.beginPath(); ctx.fillStyle = '#ffaa00';
                    ctx.shadowBlur = 15; ctx.shadowColor = '#ffaa00';
                    ctx.arc(this.x, this.y, this.r, 0, Math.PI*2); ctx.fill(); ctx.restore();
                }
            }

            class KineticParticle {
                constructor(x, y, color) {
                    this.x = x; this.y = y; this.vx = (Math.random() - 0.5) * 12; this.vy = (Math.random() - 0.5) * 12;
                    this.alpha = 1.0; this.color = color || '#ff4444';
                    this.r = Math.random() * 3 + 1;
                }
                update() { this.x += this.vx; this.y += this.vy; this.alpha -= 0.02; this.r *= 0.95; }
                draw() {
                    ctx.save(); ctx.globalAlpha = this.alpha; ctx.fillStyle = this.color;
                    ctx.beginPath(); ctx.arc(this.x, this.y, this.r, 0, Math.PI*2); ctx.fill();
                    ctx.restore();
                }
            }

            function triggerWeaponFire() {
                if (player.weaponTier === 1) {
                    lasers.push(new LaserBolt(player.x, player.y - 15));
                } else if (player.weaponTier === 2) {
                    lasers.push(new LaserBolt(player.x - 8, player.y - 10));
                    lasers.push(new LaserBolt(player.x + 8, player.y - 10));
                } else {
                    lasers.push(new LaserBolt(player.x, player.y - 15));
                    lasers.push(new LaserBolt(player.x - 12, player.y - 5, -3));
                    lasers.push(new LaserBolt(player.x + 12, player.y - 5, 3));
                }
                if (typeof AudioMatrix !== 'undefined') AudioMatrix.playTick();
            }

            function cycleRunner() {
                if (!isSessionActive) return;

                ctx.save();
                if (screenShake > 0) {
                    let dx = (Math.random() - 0.5) * screenShake;
                    let dy = (Math.random() - 0.5) * screenShake;
                    ctx.translate(dx, dy);
                    screenShake *= 0.88; if (screenShake < 0.4) screenShake = 0;
                }

                ctx.fillStyle = '#050505'; ctx.fillRect(0, 0, canvas.width, canvas.height);

                cosmicStars.forEach(s => {
                    s.y += s.speed; if (s.y > canvas.height) s.y = -5;
                    ctx.globalAlpha = s.speed / 3.5;
                    ctx.fillStyle = s.color;
                    ctx.fillRect(s.x, s.y, s.size, s.size);
                });
                ctx.globalAlpha = 1.0;

                clockTicks++;
                if (clockTicks % 12 === 0) triggerWeaponFire();
                
                if (currentLevel % 5 === 0 && bossSpawnedAt !== currentLevel && !boss && enemies.length === 0) {
                    boss = new DreadnoughtBoss();
                    bossSpawnedAt = currentLevel;
                }
                
                if (!boss && clockTicks % Math.max(20, 50 - currentLevel * 5) === 0) {
                    enemies.push(new CodeEnemy());
                }

                lasers.forEach((l, lIdx) => {
                    l.update(); l.draw();
                    if (l.y < -10) lasers.splice(lIdx, 1);
                });
                
                enemyLasers.forEach((l, lIdx) => {
                    l.update(); l.draw();
                    if (l.y > canvas.height + 10) enemyLasers.splice(lIdx, 1);
                    
                    let pDistX = Math.abs(l.x - player.x);
                    let pDistY = Math.abs(l.y - player.y);
                    if (pDistX < player.w/2 + 2 && pDistY < player.h/2 + 2) {
                        player.shield--; player.weaponTier = Math.max(1, player.weaponTier - 1);
                        screenShake = 15;
                        if (typeof AudioMatrix !== 'undefined') AudioMatrix.playError();
                        enemyLasers.splice(lIdx, 1);
                        updateHudDisplay();
                    }
                });

                upgrades.forEach((u, uIdx) => {
                    u.update(); u.draw();
                    let dX = u.x - player.x; let dY = u.y - player.y;
                    if (Math.sqrt(dX*dX + dY*dY) < u.r + player.w / 2) {
                        if (typeof AudioMatrix !== 'undefined') AudioMatrix.playWin();
                        player.weaponTier = Math.min(3, player.weaponTier + 1);
                        player.shield = Math.min(5, player.shield + 1);
                        score += 200; updateHudDisplay();
                        upgrades.splice(uIdx, 1);
                    } else if (u.y > canvas.height + 20) {
                        upgrades.splice(uIdx, 1);
                    }
                });

                if (boss) {
                    boss.update(); boss.draw();
                    
                    let pDistX = Math.abs(boss.x + boss.w/2 - player.x);
                    let pDistY = Math.abs(boss.y + boss.h/2 - player.y);
                    if (pDistX < (boss.w/2 + player.w/2) && pDistY < (boss.h/2 + player.h/2)) {
                        player.shield = 0; screenShake = 40;
                    }
                    
                    lasers.forEach((l, lIdx) => {
                        if (l.x >= boss.x && l.x <= boss.x + boss.w && l.y >= boss.y && l.y <= boss.y + boss.h) {
                            lasers.splice(lIdx, 1); boss.hp--;
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playTick();
                            for (let i = 0; i < 6; i++) particles.push(new KineticParticle(l.x, l.y, '#ff007f'));
                            
                            if (boss.hp <= 0) {
                                if (typeof AudioMatrix !== 'undefined') AudioMatrix.playExplosion();
                                score += 2000;
                                currentLevel++;
                                screenShake = 35;
                                updateHudDisplay();
                                for (let i = 0; i < 50; i++) particles.push(new KineticParticle(boss.x + boss.w/2, boss.y + boss.h/2, '#ffaa00'));
                                upgrades.push(new PowerNode(boss.x + boss.w/2, boss.y + boss.h/2));
                                boss = null;
                            }
                        }
                    });
                }

                enemies.forEach((e, eIdx) => {
                    e.update(); e.draw();

                    let pDistX = Math.abs(e.x + e.w/2 - player.x);
                    let pDistY = Math.abs(e.y + e.h/2 - player.y);
                    if (pDistX < (e.w/2 + player.w/2) && pDistY < (e.h/2 + player.h/2)) {
                        if (typeof AudioMatrix !== 'undefined') AudioMatrix.playError();
                        player.shield--; player.weaponTier = 1;
                        screenShake = 20;
                        enemies.splice(eIdx, 1);
                        updateHudDisplay();
                    }

                    lasers.forEach((l, lIdx) => {
                        if (l.x >= e.x && l.x <= e.x + e.w && l.y >= e.y && l.y <= e.y + e.h) {
                            lasers.splice(lIdx, 1); e.hp--;
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playTick();
                            for (let i = 0; i < 4; i++) particles.push(new KineticParticle(l.x, l.y, '#00e5ff'));
                            
                            if (e.hp <= 0) {
                                if (typeof AudioMatrix !== 'undefined') AudioMatrix.playExplosion();
                                score += 100;
                                currentLevel = Math.floor(score / 1200) + 1;
                                screenShake = 8;
                                updateHudDisplay();

                                if (Math.random() > 0.8) upgrades.push(new PowerNode(e.x + e.w/2, e.y + e.h/2));
                                for (let i = 0; i < 20; i++) particles.push(new KineticParticle(e.x + e.w/2, e.y + e.h/2, '#ff007f'));
                                enemies.splice(eIdx, 1);
                            }
                        }
                    });

                    if (e.y > canvas.height + 20) {
                        if (typeof AudioMatrix !== 'undefined') AudioMatrix.playError();
                        player.shield--; player.weaponTier = Math.max(1, player.weaponTier - 1);
                        screenShake = 12;
                        updateHudDisplay();
                        enemies.splice(eIdx, 1);
                    }
                });

                particles.forEach((p, pIdx) => {
                    p.update(); p.draw();
                    if (p.alpha <= 0) particles.splice(pIdx, 1);
                });

                ctx.save();
                ctx.translate(player.x, player.y);
                ctx.beginPath(); ctx.fillStyle = player.weaponTier === 3 ? '#ff007f' : '#B0A171';
                ctx.shadowBlur = 15; ctx.shadowColor = ctx.fillStyle;
                ctx.moveTo(0, -16); ctx.lineTo(-14, 14); ctx.lineTo(14, 14); ctx.closePath(); ctx.fill();
                
                ctx.fillStyle = Math.random() > 0.5 ? '#00e5ff' : '#ffffff';
                ctx.fillRect(-4, 15, 8, 4 + Math.random() * 8);
                ctx.restore();

                ctx.restore();

                if (player.shield <= 0) {
                    isSessionActive = false;
                    if (typeof AudioMatrix !== 'undefined') AudioMatrix.playGameOver();
                    gameOverScreen.style.display = 'flex';
                    document.getElementById('cs-hud').style.opacity = '0';
                } else {
                    requestAnimationFrame(cycleRunner);
                }
            }

            const trackFighterPosition = (clientX) => {
                const rect = canvas.getBoundingClientRect();
                let relativeX = clientX - rect.left;
                player.x = Math.max(20, Math.min(canvas.width - 20, relativeX));
            };

            window.addEventListener('mousemove', (e) => { if (isSessionActive) trackFighterPosition(e.clientX); });
            window.addEventListener('touchmove', (e) => {
                if (isSessionActive && e.touches.length > 0) trackFighterPosition(e.touches[0].clientX);
            }, { passive: true });

            const rebootActionBtn = document.getElementById('cs-restart-btn');
            rebootActionBtn.onclick = (e) => {
                e.preventDefault(); e.stopImmediatePropagation();
                isSessionActive = true; 
                player.shield = 3; player.weaponTier = 1;
                lasers = []; enemyLasers = []; enemies = []; particles = []; upgrades = []; boss = null;
                score = 0; currentLevel = 1; bossSpawnedAt = 0;
                gameOverScreen.style.display = 'none';
                document.getElementById('cs-hud').style.opacity = '1';
                updateHudDisplay();
                cycleRunner();
            };

            cycleRunner();
"""
    
    pattern = re.compile(r'<script>\s*\(function\(\) \{\s*(.*?)\s*\}\)\(\);\s*</script>', re.DOTALL)
    new_content = pattern.sub(f'<script>\n    (function() {{\n{js_new}\n    }})();\n</script>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
if __name__ == "__main__":
    upgrade_striker()
