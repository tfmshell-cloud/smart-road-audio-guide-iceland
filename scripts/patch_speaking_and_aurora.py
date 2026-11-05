# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

start_marker = "function setCopilotSpeakingState(isSpeaking, customText = '') {"
end_marker = "function onCopilotSpeechFinished() {"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    raise Exception(f"Could not locate setCopilotSpeakingState markers ({start_idx}, {end_idx})")

new_speaking_and_aurora_code = """// =========================================================================
    // LIVING AURORA BOREALIS CANVASES ENGINE (NIGHT SKY BEHIND KÁRI)
    // =========================================================================
    let copilotAuroraAnimId = null;
    let copilotAuroraCanvas = null;
    let copilotAuroraCtx = null;
    let auroraStars = [];
    let copilotBlinkTimer = null;

    function initCopilotAuroraCanvas() {
      copilotAuroraCanvas = document.getElementById('copilot-aurora-canvas');
      if (!copilotAuroraCanvas) return;
      copilotAuroraCtx = copilotAuroraCanvas.getContext('2d');
      
      auroraStars = [];
      for (let i = 0; i < 30; i++) {
        auroraStars.push({
          x: Math.random(),
          y: Math.random() * 0.85,
          radius: 0.6 + Math.random() * 1.2,
          twinkleSpeed: 0.03 + Math.random() * 0.05
        });
      }
    }

    function startCopilotAuroraEngine() {
      if (!copilotAuroraCanvas) initCopilotAuroraCanvas();
      if (!copilotAuroraCanvas || !copilotAuroraCtx) return;
      if (copilotAuroraAnimId) cancelAnimationFrame(copilotAuroraAnimId);

      const cvs = copilotAuroraCanvas;
      const ctx = copilotAuroraCtx;
      
      const rect = cvs.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      cvs.width = Math.max(260, Math.round((rect.width || 280) * dpr));
      cvs.height = Math.max(160, Math.round((rect.height || 180) * dpr));

      let t = 0;

      function renderAurora() {
        t += 0.022;
        const w = cvs.width;
        const h = cvs.height;
        ctx.clearRect(0, 0, w, h);

        const isSpeaking = cvs.dataset.speaking === 'true';
        const speedMult = isSpeaking ? 1.45 : 1.0;
        const lumMult = isSpeaking ? 1.35 : 1.0;

        // 1. Draw twinkling northern stars
        for (let i = 0; i < auroraStars.length; i++) {
          const s = auroraStars[i];
          const starAlpha = Math.abs(Math.sin(t * s.twinkleSpeed * 10 + i)) * 0.65 + 0.35;
          ctx.beginPath();
          ctx.arc(s.x * w, s.y * h, s.radius * dpr, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(224, 242, 254, ${starAlpha})`;
          ctx.fill();
        }

        // 2. Draw Aurora Ribbon 1: Vivid Arctic Emerald (Primary dancing curtain)
        drawAuroraRibbon(ctx, w, h, {
          baseY: h * 0.32,
          amplitude: 26 * dpr,
          freq: 0.009 / dpr,
          time: t * speedMult * 0.85,
          colorStops: [
            [0.0, 'rgba(16, 185, 129, 0.0)'],
            [0.35, `rgba(52, 211, 153, ${0.48 * lumMult})`],
            [0.72, `rgba(5, 150, 105, ${0.28 * lumMult})`],
            [1.0, 'rgba(5, 150, 105, 0.0)']
          ]
        });

        // Ribbon 2: Electric Arctic Cyan (Harmonic wavy curtain)
        drawAuroraRibbon(ctx, w, h, {
          baseY: h * 0.22,
          amplitude: 20 * dpr,
          freq: 0.013 / dpr,
          time: t * speedMult * 1.1 + 2.4,
          colorStops: [
            [0.0, 'rgba(6, 182, 212, 0.0)'],
            [0.4, `rgba(34, 211, 238, ${0.52 * lumMult})`],
            [0.78, `rgba(14, 116, 144, ${0.22 * lumMult})`],
            [1.0, 'rgba(14, 116, 144, 0.0)']
          ]
        });

        // Ribbon 3: Polar Amethyst / Violet (High altitude fringe)
        drawAuroraRibbon(ctx, w, h, {
          baseY: h * 0.14,
          amplitude: 15 * dpr,
          freq: 0.007 / dpr,
          time: t * speedMult * 0.65 + 4.8,
          colorStops: [
            [0.0, 'rgba(168, 85, 247, 0.0)'],
            [0.45, `rgba(192, 132, 252, ${0.36 * lumMult})`],
            [0.82, `rgba(126, 34, 206, ${0.16 * lumMult})`],
            [1.0, 'rgba(126, 34, 206, 0.0)']
          ]
        });

        copilotAuroraAnimId = requestAnimationFrame(renderAurora);
      }

      function drawAuroraRibbon(ctx, w, h, opts) {
        ctx.save();
        ctx.beginPath();
        const step = 8;
        ctx.moveTo(0, h);

        for (let x = 0; x <= w + step; x += step) {
          const y = opts.baseY 
            + Math.sin(x * opts.freq + opts.time) * opts.amplitude
            + Math.cos(x * opts.freq * 2.2 - opts.time * 0.75) * (opts.amplitude * 0.38);
          if (x === 0) ctx.lineTo(0, y);
          else ctx.lineTo(x, y);
        }

        ctx.lineTo(w, h);
        ctx.closePath();

        const grad = ctx.createLinearGradient(0, Math.max(0, opts.baseY - opts.amplitude), 0, h);
        opts.colorStops.forEach(([pos, color]) => grad.addColorStop(pos, color));
        ctx.fillStyle = grad;
        ctx.fill();
        ctx.restore();
      }

      renderAurora();
    }

    function stopCopilotAuroraEngine() {
      if (copilotAuroraAnimId) {
        cancelAnimationFrame(copilotAuroraAnimId);
        copilotAuroraAnimId = null;
      }
    }

    // Natural Human Eye Blinking Routine
    function scheduleNextCopilotBlink() {
      if (copilotBlinkTimer) clearTimeout(copilotBlinkTimer);
      const delay = 3400 + Math.random() * 2400;
      copilotBlinkTimer = setTimeout(() => {
        const blinkImg = document.getElementById('copilot-avatar-img-blink');
        if (blinkImg) {
          blinkImg.style.opacity = '1';
          setTimeout(() => {
            blinkImg.style.opacity = '0';
            scheduleNextCopilotBlink();
          }, 115);
        } else {
          scheduleNextCopilotBlink();
        }
      }, delay);
    }

    function stopCopilotBlinkTimer() {
      if (copilotBlinkTimer) {
        clearTimeout(copilotBlinkTimer);
        copilotBlinkTimer = null;
      }
    }

    // =========================================================================
    // SPEAKING STATE CONTROLLER (NATURAL ARTICULATION & AURORA INTENSITY)
    // =========================================================================
    function setCopilotSpeakingState(isSpeaking, customText = '') {
      const restImg = document.getElementById('copilot-avatar-img-rest');
      const talkImg = document.getElementById('copilot-avatar-img-talk');
      const stage = document.getElementById('copilot-avatar-stage');
      const hud = document.getElementById('copilot-vocal-hud');
      const dot = document.getElementById('copilot-live-dot');
      const label = document.getElementById('copilot-status-label');
      const waveText = document.getElementById('copilot-wave-text');
      const waveBars = document.getElementById('copilot-soundwave-bars');
      const auroraCvs = document.getElementById('copilot-aurora-canvas');
      const auroraGlow = document.getElementById('copilot-aurora-glow');

      if (isSpeaking) {
        if (stage) stage.classList.add('copilot-speaking-motion');
        // Do not hide restImg so feathered mouth blends seamlessly without flicker
        if (talkImg) talkImg.style.opacity = '1';
        if (auroraCvs) auroraCvs.dataset.speaking = 'true';
        if (auroraGlow) {
          auroraGlow.style.opacity = '0.85';
          auroraGlow.className = 'absolute inset-0 pointer-events-none transition-all duration-500 opacity-85 bg-gradient-to-b from-emerald-400/35 via-cyan-400/15 to-slate-950/75';
        }
        if (hud) hud.style.opacity = '1';
        if (dot) dot.className = 'w-2 h-2 rounded-full bg-cyan-400 animate-ping';
        if (label) {
          label.textContent = currentLang === 'uk' ? 'ШТУРМАН ПРОМОВЛЯЄ' : 'NAVIGATOR BRIEFING';
          label.className = 'font-bold uppercase tracking-wider text-cyan-300';
        }
        if (waveText) waveText.textContent = currentLang === 'uk' ? 'ГОЛОСОВИЙ БРИФІНГ...' : 'SPEAKING DISPATCH...';
        if (waveBars) waveBars.classList.add('animate-pulse');
      } else {
        if (stage) stage.classList.remove('copilot-speaking-motion');
        if (talkImg) talkImg.style.opacity = '0';
        if (auroraCvs) auroraCvs.dataset.speaking = 'false';
        if (auroraGlow) {
          auroraGlow.style.opacity = '0.4';
          auroraGlow.className = 'absolute inset-0 pointer-events-none transition-all duration-500 opacity-40 bg-gradient-to-b from-emerald-500/20 via-cyan-500/5 to-slate-950/75';
        }
        if (hud) hud.style.opacity = '0';
        if (dot) dot.className = 'w-2 h-2 rounded-full bg-emerald-400 animate-ping';
        if (label) {
          label.textContent = currentLang === 'uk' ? "НА ЗВ'ЯЗКУ" : 'STANDBY ONLINE';
          label.className = 'font-bold uppercase tracking-wider text-emerald-300';
        }
        if (waveText) waveText.textContent = currentLang === 'uk' ? 'ГОТОВИЙ ДО ДІАЛОГУ' : 'READY FOR COMMS';
        if (waveBars) waveBars.classList.remove('animate-pulse');
      }
    }

    """

html = html[:start_idx] + new_speaking_and_aurora_code + html[end_idx:]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Injected setCopilotSpeakingState and Aurora Engine successfully!")
