import os

filepath = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\glyph-matrix.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to completely rewrite the HTML block for Glyph Matrix
new_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<canvas id="glyph-canvas" class="absolute inset-0 w-full h-full z-0 cursor-crosshair"></canvas>

<!-- Top HUD Controls -->
<div class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">
    <div class="bg-black/60 backdrop-blur-md border border-white/10 rounded-full px-4 py-2 flex items-center gap-2 pointer-events-auto shadow-xl">
        <button class="gm-style-btn active px-4 py-1 rounded-full text-xs font-mono transition-colors bg-[#00e5ff] text-black" data-style="dots">DOTS</button>
        <button class="gm-style-btn px-4 py-1 rounded-full text-xs font-mono text-white hover:text-[#00e5ff] transition-colors" data-style="symbols">MATRIX</button>
        <div class="w-px h-4 bg-white/20 mx-2"></div>
        <button id="gm-download-btn" class="px-4 py-1 rounded-full text-xs font-mono text-white hover:text-[#00e5ff] transition-colors flex items-center gap-1" style="display:none;">
            <i class="ph ph-download-simple"></i> SAVE
        </button>
    </div>
</div>

<!-- Upload Prompt Overlay -->
<div id="gm-upload-prompt" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6 transition-opacity duration-300">
    <h2 class="text-3xl md:text-5xl font-display font-black text-[#00e5ff] mb-4 tracking-wider">GLYPH MATRIX</h2>
    <p class="text-gray-300 font-mono text-sm md:text-lg mb-8 max-w-md">Upload an image to encode it into a digital matrix data stream.</p>
    <label for="matrix-image-upload" class="px-8 py-3 bg-[#00e5ff] text-black font-bold rounded-full hover:bg-[#00c2d6] transition-colors text-sm cursor-pointer inline-block">
        SELECT IMAGE
    </label>
    <input type="file" id="matrix-image-upload" class="hidden" accept="image/*">
</div>
{% endblock %}

{% block project_scripts %}
<script>
    (function() {
        const canvas = document.getElementById('glyph-canvas'); if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const fileInput = document.getElementById('matrix-image-upload');
        const promptOverlay = document.getElementById('gm-upload-prompt');
        const selectionButtons = document.querySelectorAll('.gm-style-btn');
        const downloadBtn = document.getElementById('gm-download-btn');
        
        ctx.imageSmoothingEnabled = false; 
        
        let cachedImg = null;
        let pixelBuffer = null;
        let sampleW = 0; let sampleH = 0;
        const cellSize = 7;
        const matrixGap = 1.5;
        
        let currentDisplayMode = 'dots'; 
        const symbolGlyphs = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\\\|()1{}[]?-_+~<>i!lI;:,"^`\\'. ';
        let currentAnimationLoopId = null;

        function renderMatrixLoop() {
            currentAnimationLoopId = requestAnimationFrame(renderMatrixLoop);

            if (!cachedImg || !pixelBuffer) {
                ctx.fillStyle = '#000000';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                return;
            }

            const hardwareFlicker = 0.94 + Math.random() * 0.09;

            ctx.fillStyle = '#000000';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            const centerX = sampleW / 2;
            const centerY = sampleH / 2;
            const maxRadius = Math.min(sampleW, sampleH) / 2 * 0.95;

            for (let y = 0; y < sampleH; y++) {
                for (let x = 0; x < sampleW; x++) {
                    const dx = x - centerX;
                    const dy = y - centerY;
                    if (Math.sqrt(dx*dx + dy*dy) > maxRadius) continue;

                    const bufferOffsetIdx = (y * sampleW + x) * 4;
                    const r = pixelBuffer[bufferOffsetIdx];
                    const g = pixelBuffer[bufferOffsetIdx + 1];
                    const b = pixelBuffer[bufferOffsetIdx + 2];

                    let luminosity = (0.2126 * r + 0.7152 * g + 0.0722 * b);
                    if (luminosity < 22) continue; 

                    let animatedLuminosity = luminosity * hardwareFlicker;
                    if (animatedLuminosity > 255) animatedLuminosity = 255;

                    const posX = x * cellSize;
                    const posY = y * cellSize;

                    if (currentDisplayMode === 'dots') {
                        ctx.fillStyle = `rgb(${animatedLuminosity}, ${animatedLuminosity}, ${animatedLuminosity})`;
                        ctx.fillRect(
                            posX + matrixGap / 2, 
                            posY + matrixGap / 2, 
                            cellSize - matrixGap, 
                            cellSize - matrixGap
                        );
                    } else {
                        const targetCharIdx = Math.floor(((255 - luminosity) / 255) * (symbolGlyphs.length - 1));
                        const singleSymbolChar = symbolGlyphs[targetCharIdx];
                        
                        ctx.fillStyle = `rgb(0, ${Math.min(255, animatedLuminosity + 40)}, 0)`;
                        ctx.font = `bold ${cellSize}px monospace`;
                        ctx.textAlign = 'center';
                        ctx.textBaseline = 'middle';
                        ctx.fillText(singleSymbolChar, posX + cellSize/2, posY + cellSize/2);
                    }
                }
            }
        }

        fileInput.onchange = (e) => {
            const file = e.target.files[0];
            if (!file) return;
            
            const reader = new FileReader();
            reader.onload = (event) => {
                cachedImg = new Image();
                cachedImg.onload = () => {
                    promptOverlay.style.opacity = '0';
                    setTimeout(() => { promptOverlay.style.display = 'none'; }, 300);
                    downloadBtn.style.display = 'flex';
                    
                    // Fixed resolution to fit within standard views, keeping detail
                    sampleW = 120;
                    const aspect = cachedImg.height / cachedImg.width;
                    sampleH = Math.floor(sampleW * aspect);
                    
                    canvas.width = sampleW * cellSize;
                    canvas.height = sampleH * cellSize;
                    
                    const memCanvas = document.createElement('canvas');
                    memCanvas.width = sampleW; memCanvas.height = sampleH;
                    const memCtx = memCanvas.getContext('2d');
                    memCtx.drawImage(cachedImg, 0, 0, sampleW, sampleH);
                    
                    pixelBuffer = memCtx.getImageData(0, 0, sampleW, sampleH).data;
                };
                cachedImg.src = event.target.result;
            };
            reader.readAsDataURL(file);
        };

        selectionButtons.forEach(btn => {
            btn.onclick = () => {
                selectionButtons.forEach(b => {
                    b.classList.remove('active', 'bg-[#00e5ff]', 'text-black');
                    b.classList.add('text-white');
                });
                btn.classList.add('active', 'bg-[#00e5ff]', 'text-black');
                btn.classList.remove('text-white');
                currentDisplayMode = btn.getAttribute('data-style');
            };
        });
        
        downloadBtn.onclick = () => {
            const link = document.createElement('a');
            link.download = `glyph-matrix-${Date.now()}.png`;
            link.href = canvas.toDataURL('image/png');
            link.click();
        };

        renderMatrixLoop();
    })();
</script>
{% endblock %}
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Glyph Matrix HTML and JS completely restored and download added!")
