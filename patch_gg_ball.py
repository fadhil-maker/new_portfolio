import os

filepath = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_draw = """            ctx.beginPath(); ctx.fillStyle = ballNode.launching ? '#00e5ff' : '#00ff66';
            ctx.arc(ballNode.x, ballNode.y, ballNode.r, 0, Math.PI*2); ctx.fill();
            console.log('Ball Rendered at:', ballNode.x, ballNode.y, 'Launching:', ballNode.launching, 'Fill:', ctx.fillStyle);"""

if old_draw not in content:
    # try without console.log
    old_draw = """            ctx.beginPath(); ctx.fillStyle = ballNode.launching ? '#00e5ff' : '#00ff66';
            ctx.arc(ballNode.x, ballNode.y, ballNode.r, 0, Math.PI*2); ctx.fill();"""

new_draw = """
            // Failsafe coordinates
            if (isNaN(ballNode.x) || ballNode.x === 0) ballNode.x = Math.min(120, canvas.width * 0.2) || 120;
            if (isNaN(ballNode.y) || ballNode.y === 0) ballNode.y = canvas.height / 2 || 300;

            // Draw a massive glowing aura to guarantee it's visible
            ctx.beginPath(); 
            ctx.shadowBlur = 20; 
            ctx.shadowColor = ballNode.launching ? '#00e5ff' : '#00ff66';
            ctx.fillStyle = ballNode.launching ? '#00e5ff' : '#00ff66';
            ctx.arc(ballNode.x, ballNode.y, ballNode.r + 2, 0, Math.PI*2); 
            ctx.fill();
            ctx.shadowBlur = 0; // reset
            
            // Draw a bright white core
            ctx.beginPath();
            ctx.fillStyle = '#ffffff';
            ctx.arc(ballNode.x, ballNode.y, 3, 0, Math.PI*2);
            ctx.fill();
            
            // Add a radar pulse stroke
            ctx.beginPath();
            ctx.strokeStyle = ballNode.launching ? 'rgba(0, 229, 255, 0.5)' : 'rgba(0, 255, 102, 0.5)';
            ctx.lineWidth = 2;
            ctx.arc(ballNode.x, ballNode.y, ballNode.r + 8 + Math.sin(Date.now() * 0.005) * 4, 0, Math.PI*2);
            ctx.stroke();
"""

content = content.replace(old_draw, new_draw)

# Ensure calculateActive correctly resumes and ctx is safe
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ball rendering patched with massive glowing core!")
