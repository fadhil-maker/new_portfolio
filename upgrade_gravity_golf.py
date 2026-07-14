import os
import re

def upgrade_gg():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    js_new = """
            const canvas = document.getElementById('golf-canvas'); if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const winModal = document.getElementById('gg-win-screen');
            const strikeLabel = document.getElementById('gg-score');

            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = canvas.parentElement.clientHeight;

            let currentLevel = 1;
            let probesLeft = 5;
            let totalScore = 0;
            let calculateActive = true;
            let screenShake = 0;

            let targetNode = { x: canvas.width - 180, y: canvas.height / 2, r: 24 };
            let ballNode = { x: 120, y: canvas.height / 2, vx: 0, vy: 0, r: 6, launching: false };
            let dragControl = { active: false, startX: 0, startY: 0 };
            
            let probeTrail = [];
            let fullPathHistory = [];
            let ghostTrail = [];
            let burstParticles = [];
            let asteroids = [];
            let spaceCrystals = [];
            let repulsors = [];

            function generateLevelLayout() {
                probeTrail = [];
                fullPathHistory = [];
                burstParticles = [];
                ballNode.launching = false;
                ballNode.x = 120; ballNode.y = canvas.height / 2;
                ballNode.vx = 0; ballNode.vy = 0;

                targetNode.x = canvas.width * 0.5 + Math.random() * (canvas.width * 0.35);
                targetNode.y = canvas.height * 0.2 + Math.random() * (canvas.height * 0.6);

                asteroids = [];
                const hazardCount = Math.min(3, Math.floor(currentLevel / 2) + 1);
                for (let i = 0; i < hazardCount; i++) {
                    asteroids.push({
                        x: canvas.width * 0.35 + (i * 80),
                        y: Math.random() * canvas.height,
                        vx: 0,
                        vy: 1.5 + (currentLevel * 0.4) * (Math.random() > 0.5 ? 1 : -1),
                        r: 14 + Math.random() * 8
                    });
                }

                spaceCrystals = [];
                const crystalCount = 3;
                for (let i = 0; i < crystalCount; i++) {
                    const angle = (Math.PI * 2 / crystalCount) * i + Math.random();
                    const spawnDist = targetNode.r + 40 + Math.random() * 60;
                    spaceCrystals.push({
                        x: targetNode.x + Math.cos(angle) * spawnDist,
                        y: targetNode.y + Math.sin(angle) * spawnDist,
                        r: 5,
                        active: true
                    });
                }
                
                repulsors = [];
                if (currentLevel >= 3) {
                    const repCount = Math.min(3, currentLevel - 2);
                    for (let i=0; i<repCount; i++) {
                        repulsors.push({
                            x: canvas.width * 0.3 + Math.random() * (canvas.width * 0.4),
                            y: canvas.height * 0.2 + Math.random() * (canvas.height * 0.6),
                            r: 18 + Math.random() * 12,
                            angle: 0
                        });
                    }
                }
                
                updateHudReadout();
            }

            function updateHudReadout() {
                strikeLabel.innerHTML = `LVL ${currentLevel} &nbsp;&bull;&nbsp; PROBES: ${probesLeft} &nbsp;&bull;&nbsp; SCORE: ${totalScore}`;
            }

            class ShockwaveParticle {
                constructor(x, y, color) {
                    this.x = x; this.y = y;
                    this.vx = (Math.random() - 0.5) * 12;
                    this.vy = (Math.random() - 0.5) * 12;
                    this.alpha = 1.0; this.color = color || '#ffaa00';
                }
                process() { this.x += this.vx; this.y += this.vy; this.alpha -= 0.03; }
                draw() {
                    ctx.save(); ctx.globalAlpha = this.alpha; ctx.fillStyle = this.color;
                    ctx.beginPath(); ctx.arc(this.x, this.y, 4, 0, Math.PI*2); ctx.fill(); ctx.restore();
                }
            }

            function triggerTerminalOverlay(didWin) {
                calculateActive = false;
                document.querySelector('.golf-hud-overlay').style.opacity = '0';
                
                const titleNode = winModal.querySelector('h2');
                const descNode = winModal.querySelector('p');
                const actionBtn = document.getElementById('gg-restart-btn');

                if (didWin) {
                    if (typeof AudioMatrix !== 'undefined') AudioMatrix.playWin();
                    titleNode.innerText = "SINGULARITY CAPTURE CONFIRMED";
                    titleNode.style.color = "var(--neon-cyan)";
                    descNode.innerText = `Quantum core data stream stabilized. Bonus points credited to terminal score matrix.`;
                    actionBtn.innerText = "LAUNCH NEXT PROBE WAVE";
                } else {
                    if (typeof AudioMatrix !== 'undefined') AudioMatrix.playGameOver();
                    titleNode.innerText = "CRITICAL PROBE DEPLETION";
                    titleNode.style.color = "var(--neon-red)";
                    descNode.innerText = `All tracking modules lost to event horizons. Final Score secured: ${totalScore} XP.`;
                    actionBtn.innerText = "REBOOT GRAVITY FIELDS";
                }
                winModal.style.display = 'flex';
            }
            
            function applyGravity(x, y) {
                let dx = targetNode.x - x; let dy = targetNode.y - y;
                let rDist = Math.sqrt(dx*dx + dy*dy);
                let accelX = 0, accelY = 0;
                
                if (rDist > 1) {
                    let simAccel = (targetNode.r * 7.8) / (rDist * rDist);
                    accelX += (dx / rDist) * simAccel;
                    accelY += (dy / rDist) * simAccel;
                }
                
                repulsors.forEach(rep => {
                    let rdx = rep.x - x; let rdy = rep.y - y;
                    let rdist = Math.sqrt(rdx*rdx + rdy*rdy);
                    if (rdist > 1) {
                        let repAccel = -(rep.r * 8.5) / (rdist * rdist); // Negative gravity (push)
                        accelX += (rdx / rdist) * repAccel;
                        accelY += (rdy / rdist) * repAccel;
                    }
                });
                
                return { ax: accelX, ay: accelY };
            }

            function computePhysics() {
                if (!calculateActive) return;
                ctx.fillStyle = 'rgba(2, 2, 2, 0.3)'; ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.save();
                if (screenShake > 0) {
                    ctx.translate((Math.random() - 0.5) * screenShake, (Math.random() - 0.5) * screenShake);
                    screenShake *= 0.85; if (screenShake < 0.5) screenShake = 0;
                }

                // Draw Target
                ctx.beginPath(); ctx.fillStyle = '#ffaa00';
                ctx.shadowBlur = 25 + Math.sin(Date.now() * 0.005) * 5; ctx.shadowColor = '#ffaa00';
                ctx.arc(targetNode.x, targetNode.y, targetNode.r, 0, Math.PI*2); ctx.fill();
                ctx.restore();
                
                // Draw Repulsors
                repulsors.forEach(rep => {
                    rep.angle += 0.05;
                    ctx.save();
                    ctx.translate(rep.x, rep.y); ctx.rotate(rep.angle);
                    ctx.beginPath(); ctx.strokeStyle = '#ff007f'; ctx.lineWidth = 2;
                    ctx.shadowBlur = 15; ctx.shadowColor = '#ff007f';
                    ctx.rect(-rep.r/2, -rep.r/2, rep.r, rep.r);
                    ctx.stroke();
                    ctx.rotate(-rep.angle * 2);
                    ctx.rect(-rep.r/2 - 5, -rep.r/2 - 5, rep.r + 10, rep.r + 10);
                    ctx.stroke();
                    ctx.restore();
                });

                asteroids.forEach(ast => {
                    ast.y += ast.vy;
                    if (ast.y - ast.r < 0 || ast.y + ast.r > canvas.height) ast.vy *= -1;

                    ctx.beginPath(); ctx.fillStyle = '#3a3a3a'; ctx.strokeStyle = 'rgba(255,255,255,0.1)';
                    ctx.lineWidth = 1.5; ctx.arc(ast.x, ast.y, ast.r, 0, Math.PI*2); ctx.fill(); ctx.stroke();

                    if (ballNode.launching) {
                        let dX = ast.x - ballNode.x; let dY = ast.y - ballNode.y;
                        let dist = Math.sqrt(dX*dX + dY*dY);
                        if (dist < ast.r + ballNode.r) {
                            screenShake = 20;
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playError();
                            ghostTrail = [...fullPathHistory];
                            probesLeft--;
                            if (probesLeft <= 0) triggerTerminalOverlay(false);
                            else generateLevelLayout();
                        }
                    }
                });

                spaceCrystals.forEach(cry => {
                    if (!cry.active) return;
                    ctx.save(); ctx.shadowBlur = 10; ctx.shadowColor = 'var(--neon-cyan)';
                    ctx.beginPath(); ctx.fillStyle = 'var(--neon-cyan)';
                    ctx.arc(cry.x, cry.y, cry.r, 0, Math.PI*2); ctx.fill(); ctx.restore();

                    if (ballNode.launching) {
                        let dX = cry.x - ballNode.x; let dY = cry.y - ballNode.y;
                        if (Math.sqrt(dX*dX + dY*dY) < cry.r + ballNode.r + 5) {
                            cry.active = false;
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playTick();
                            totalScore += 250;
                            updateHudReadout();
                            for(let i=0; i<8; i++) burstParticles.push(new ShockwaveParticle(cry.x, cry.y, 'var(--neon-cyan)'));
                        }
                    }
                });

                if (ballNode.launching) {
                    let distanceX = targetNode.x - ballNode.x;
                    let distanceY = targetNode.y - ballNode.y;
                    let radiusDistance = Math.sqrt(distanceX*distanceX + distanceY*distanceY);

                    if (radiusDistance < targetNode.r + 3) {
                        if (typeof AudioMatrix !== 'undefined') AudioMatrix.playWin();
                        totalScore += (probesLeft * 50);
                        currentLevel++;
                        ghostTrail = [];
                        probesLeft = Math.min(7, probesLeft + 1);
                        screenShake = 15;
                        triggerTerminalOverlay(true);
                        return;
                    }
                    
                    repulsors.forEach(rep => {
                        let dX = rep.x - ballNode.x; let dY = rep.y - ballNode.y;
                        if (Math.sqrt(dX*dX + dY*dY) < rep.r + ballNode.r) {
                            screenShake = 25;
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playExplosion();
                            ghostTrail = [...fullPathHistory];
                            probesLeft--;
                            if (probesLeft <= 0) triggerTerminalOverlay(false);
                            else generateLevelLayout();
                        }
                    });

                    if (calculateActive) {
                        let gAccel = applyGravity(ballNode.x, ballNode.y);
                        ballNode.vx += gAccel.ax; ballNode.vy += gAccel.ay;
                        ballNode.x += ballNode.vx; ballNode.y += ballNode.vy;

                        probeTrail.push({ x: ballNode.x, y: ballNode.y });
                        fullPathHistory.push({ x: ballNode.x, y: ballNode.y });
                        if (probeTrail.length > 25) probeTrail.shift();

                        if (ballNode.x < -50 || ballNode.x > canvas.width+50 || ballNode.y < -50 || ballNode.y > canvas.height+50) {
                            if (typeof AudioMatrix !== 'undefined') AudioMatrix.playError();
                            screenShake = 10;
                            ghostTrail = [...fullPathHistory];
                            probesLeft--;
                            if (probesLeft <= 0) triggerTerminalOverlay(false);
                            else generateLevelLayout();
                        }
                    }
                }

                // Draw Ghost Trail
                if (ghostTrail.length > 0) {
                    ctx.beginPath();
                    ctx.setLineDash([2, 6]);
                    ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
                    ctx.lineWidth = 1;
                    ctx.moveTo(ghostTrail[0].x, ghostTrail[0].y);
                    for (let i = 1; i < ghostTrail.length; i++) {
                        ctx.lineTo(ghostTrail[i].x, ghostTrail[i].y);
                    }
                    ctx.stroke();
                    ctx.setLineDash([]);
                }

                probeTrail.forEach((pt, index) => {
                    ctx.beginPath(); ctx.fillStyle = `rgba(0, 229, 255, ${index / probeTrail.length})`;
                    ctx.arc(pt.x, pt.y, ballNode.r * (index / probeTrail.length), 0, Math.PI*2); ctx.fill();
                });

                burstParticles.forEach((part, pIdx) => {
                    part.process(); part.draw();
                    if (part.alpha <= 0) burstParticles.splice(pIdx, 1);
                });

                ctx.beginPath(); ctx.fillStyle = ballNode.launching ? '#00e5ff' : '#B0A171';
                ctx.arc(ballNode.x, ballNode.y, ballNode.r, 0, Math.PI*2); ctx.fill();

                if (dragControl.active && !ballNode.launching) {
                    let simX = ballNode.x; let simY = ballNode.y;
                    let simVx = (dragControl.startX - activeMouseX) * 0.11;
                    let simVy = (dragControl.startY - activeMouseY) * 0.11;
                    
                    for (let i = 0; i < 150; i++) {
                        let dX = targetNode.x - simX; let dY = targetNode.y - simY;
                        let rDist = Math.sqrt(dX*dX + dY*dY);
                        if (rDist < targetNode.r) {
                            ctx.beginPath(); ctx.fillStyle = '#ffaa00'; ctx.arc(simX, simY, 4, 0, Math.PI*2); ctx.fill();
                            break; 
                        }
                        
                        let broke = false;
                        repulsors.forEach(rep => {
                            let rx = rep.x - simX; let ry = rep.y - simY;
                            if (Math.sqrt(rx*rx + ry*ry) < rep.r) broke = true;
                        });
                        if (broke) {
                            ctx.beginPath(); ctx.fillStyle = '#ff007f'; ctx.arc(simX, simY, 6, 0, Math.PI*2); ctx.fill();
                            break;
                        }
                        
                        let gAccel = applyGravity(simX, simY);
                        simVx += gAccel.ax; simVy += gAccel.ay;
                        simX += simVx; simY += simVy;
                        
                        if (i % 3 === 0) {
                            ctx.beginPath(); 
                            ctx.fillStyle = `rgba(0, 229, 255, ${1 - i/150})`;
                            ctx.arc(simX, simY, Math.max(0.5, 3 - (i/40)), 0, Math.PI*2); 
                            ctx.fill();
                        }
                    }
                }
                
                if (screenShake > 0) ctx.restore();

                requestAnimationFrame(computePhysics);
            }

            canvas.onmousedown = (e) => {
                if (ballNode.launching || !calculateActive) return;
                dragControl.startX = e.clientX; dragControl.startY = e.clientY; dragControl.active = true;
            };

            canvas.addEventListener('touchstart', (e) => {
                if (ballNode.launching || !calculateActive) return;
                if (e.touches && e.touches.length > 0) {
                    dragControl.startX = e.touches[0].clientX; dragControl.startY = e.touches[0].clientY;
                    dragControl.active = true;
                }
            }, { passive: true });

            const emitAimTicks = () => {
                if (dragControl.active && !ballNode.launching && Math.random() > 0.84) {
                    if (typeof AudioMatrix !== 'undefined') AudioMatrix.playTick();
                }
            };
            window.addEventListener('mousemove', emitAimTicks);
            window.addEventListener('touchmove', emitAimTicks, { passive: true });

            const releaseLaunchEngine = () => {
                if (!dragControl.active) return; dragControl.active = false;
                ballNode.vx = (dragControl.startX - activeMouseX) * 0.11;
                ballNode.vy = (dragControl.startY - activeMouseY) * 0.11;
                ballNode.launching = true; 
                if (typeof AudioMatrix !== 'undefined') AudioMatrix.playPaperLaunch();
            };

            window.onmouseup = releaseLaunchEngine;
            window.addEventListener('touchend', releaseLaunchEngine, { passive: true });

            document.getElementById('gg-restart-btn').onclick = (e) => {
                e.preventDefault(); e.stopImmediatePropagation();

                if (probesLeft <= 0) {
                    currentLevel = 1; probesLeft = 5; totalScore = 0;
                }

                winModal.style.display = 'none';
                document.querySelector('.golf-hud-overlay').style.opacity = '1';

                if (!calculateActive) {
                    calculateActive = true;
                    generateLevelLayout();
                }
            };

            generateLevelLayout();
            computePhysics();
"""
    
    pattern = re.compile(r'<script>\s*\(function\(\) \{\s*(.*?)\s*\}\)\(\);\s*</script>', re.DOTALL)
    new_content = pattern.sub(f'<script>\n    (function() {{\n{js_new}\n    }})();\n</script>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
if __name__ == "__main__":
    upgrade_gg()
