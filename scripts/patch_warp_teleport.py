# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Warp Overlay HTML right before </body>
warp_overlay_html = '''
  <!-- HYPERSPACE ORBITAL RE-ENTRY OVERLAY -->
  <div id="warp-overlay" class="hidden fixed inset-0 z-50 bg-black/90 flex flex-col items-center justify-center pointer-events-none transition-opacity duration-700">
    <canvas id="warp-canvas" class="absolute inset-0 w-full h-full"></canvas>
    <div class="relative z-10 flex flex-col items-center space-y-3 text-center px-4">
      <div class="w-14 h-14 rounded-2xl bg-cyan-500/20 text-cyan-300 border border-cyan-400/50 flex items-center justify-center text-3xl shadow-2xl shadow-cyan-500/40 animate-pulse">
        🚀
      </div>
      <div class="space-y-1">
        <h2 class="text-xl md:text-3xl font-black text-white tracking-widest uppercase">
          Орбітальний Спуск • Гіперстрибок
        </h2>
        <p class="text-xs md:text-sm font-mono text-cyan-300 tracking-wider">
          ATMOSPHERIC RE-ENTRY • MID-ATLANTIC RIDGE INTERCEPT
        </p>
      </div>
      <div class="p-3 rounded-xl bg-slate-950/80 border border-cyan-500/40 font-mono text-xs text-emerald-400 flex items-center gap-4">
        <span>ALTITUDE: <b id="warp-alt">450,000 KM</b></span>
        <span>•</span>
        <span>VELOCITY: <b id="warp-mach">MACH 18.4</b></span>
        <span>•</span>
        <span>TARGET: <b id="warp-target">GULLFOSS</b></span>
      </div>
    </div>
  </div>
'''

if 'id="warp-overlay"' not in html:
    html = html.replace('</body>', warp_overlay_html + '\n</body>', 1)
    print("Injected #warp-overlay HTML.")

# 2. Add 'Телепортація 3D' and '10 Концептів' buttons to header navigation
old_nav_anchor = '<button onclick="openFactsModal()"'

warp_buttons = '''
      <button onclick="triggerHyperspaceDive()" class="px-3 py-1.5 rounded-lg bg-gradient-to-r from-cyan-500/25 to-blue-600/25 hover:from-cyan-500/40 hover:to-blue-600/40 text-cyan-200 border border-cyan-400/50 font-semibold flex items-center gap-1.5 shadow-md shadow-cyan-500/15 transition" title="Запустити орбітальний гіперстрибок та 3D спуск">
        <span>🚀</span> <span>Телепортація 3D</span>
      </button>

      <a href="iceland_guide_vision_lab.html" class="px-3 py-1.5 rounded-lg bg-gradient-to-r from-purple-500/20 to-pink-500/20 hover:from-purple-500/30 hover:to-pink-500/30 text-purple-300 border border-purple-500/40 font-semibold flex items-center gap-1.5 shadow-md shadow-purple-500/10 transition" title="10 Інноваційних Концептів Інтерфейсу Майбутнього">
        <span>🎨</span> <span>10 Концептів</span>
        <span class="text-[9px] px-1 py-0.2 rounded bg-purple-500/30 font-mono text-purple-200">WOW</span>
      </a>
'''

if 'triggerHyperspaceDive()' not in html:
    html = html.replace(old_nav_anchor, warp_buttons + '\n      ' + old_nav_anchor, 1)
    print("Added Warp & Vision Lab buttons to header nav.")

# 3. Add Hyperspace Dive JavaScript Engine
js_warp_engine = '''
    // ==========================================
    // HYPERSPACE ORBITAL DIVE TELEPORTATION ENGINE
    // ==========================================
    let isWarping = false;

    function triggerHyperspaceDive(targetPoiId = 'gullfoss') {
      if (isWarping) return;
      isWarping = true;

      const overlay = document.getElementById('warp-overlay');
      const canvas = document.getElementById('warp-canvas');
      if (!overlay || !canvas) return;

      overlay.classList.remove('hidden');
      overlay.style.opacity = '1';

      // Play Sound
      playAmbientGlacierTone();
      try {
        if (webAudioCtx) {
          const osc = webAudioCtx.createOscillator();
          const gain = webAudioCtx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(60, webAudioCtx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(840, webAudioCtx.currentTime + 1.2);
          osc.frequency.exponentialRampToValueAtTime(120, webAudioCtx.currentTime + 2.4);
          gain.gain.setValueAtTime(0.01, webAudioCtx.currentTime);
          gain.gain.linearRampToValueAtTime(0.15, webAudioCtx.currentTime + 0.9);
          gain.gain.exponentialRampToValueAtTime(0.001, webAudioCtx.currentTime + 2.4);
          osc.connect(gain);
          gain.connect(webAudioCtx.destination);
          osc.start();
          osc.stop(webAudioCtx.currentTime + 2.4);
        }
      } catch (e) {}

      // Fast Warp Canvas Stars
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const stars = Array.from({ length: 140 }, () => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        z: Math.random() * canvas.width,
        color: Math.random() > 0.4 ? '#00f0ff' : '#10b981'
      }));

      let startTs = Date.now();
      const duration = 2200;

      function renderWarp() {
        const elapsed = Date.now() - startTs;
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        const cx = canvas.width / 2;
        const cy = canvas.height / 2;

        stars.forEach(s => {
          s.z -= 18;
          if (s.z <= 0) s.z = canvas.width;
          const k = 220 / s.z;
          const px = (s.x - cx) * k + cx;
          const py = (s.y - cy) * k + cy;
          const sz = Math.max(1, (1 - s.z / canvas.width) * 6);

          ctx.fillStyle = s.color;
          ctx.beginPath();
          ctx.arc(px, py, sz, 0, Math.PI * 2);
          ctx.fill();
        });

        // Altitude counter countdown
        const frac = Math.min(1, elapsed / duration);
        const altKm = Math.floor(450000 * (1 - frac) + 1.2);
        const machVal = (18.4 * (1 - frac * 0.9)).toFixed(1);
        const altElem = document.getElementById('warp-alt');
        const machElem = document.getElementById('warp-mach');
        if (altElem) altElem.textContent = `${altKm.toLocaleString()} KM`;
        if (machElem) machElem.textContent = `MACH ${machVal}`;

        if (elapsed < duration) {
          requestAnimationFrame(renderWarp);
        } else {
          // Camera zoom into target POI
          const target = POIS.find(p => p.id === targetPoiId) || POIS[0];
          if (map && target) {
            map.flyTo({
              center: [target.lng, target.lat],
              zoom: 14.5,
              pitch: 62,
              bearing: 40,
              speed: 2.2,
              curve: 1.2,
              essential: true
            });
          }

          // Fade out overlay
          overlay.style.opacity = '0';
          setTimeout(() => {
            overlay.classList.add('hidden');
            isWarping = false;
            // Open POI modal with slight delay for dramatic effect
            setTimeout(() => {
              openPoiModal(target.id);
            }, 500);
          }, 700);
        }
      }

      renderWarp();
    }
'''

if "function triggerHyperspaceDive(" not in html:
    html = html.replace("window.setNavMode = setNavMode;", js_warp_engine + "\n    window.triggerHyperspaceDive = triggerHyperspaceDive;\n    window.setNavMode = setNavMode;", 1)
    print("Added triggerHyperspaceDive JS function.")

# 4. Check url params on load for ?warp=true
url_check = '''
      // Check for ?warp=true in query string
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('warp') === 'true') {
        setTimeout(() => {
          triggerHyperspaceDive('gullfoss');
        }, 600);
      }
'''
if "urlParams.get('warp') === 'true'" not in html:
    html = html.replace("renderPoiList();\n    });", "renderPoiList();\n" + url_check + "    });", 1)
    print("Added ?warp=true auto-trigger on DOM load.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved index.html successfully with Warp Engine.")
