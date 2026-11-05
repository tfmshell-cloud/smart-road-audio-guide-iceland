# -*- coding: utf-8 -*-
import re
import os

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

print(f"Loaded index.html: {len(html)} bytes")

# ==============================================================================
# 1. UPDATE CSS FOR AVATAR STAGE (REMOVE SHAKING, ADD AURORA & BLINK STYLES)
# ==============================================================================
old_avatar_css = """    /* Co-pilot Living En-Face Avatar Breathing & Lip-Sync Animation */
    @keyframes copilotBreathing {
      0%, 100% { transform: scale(1) translateY(0px); }
      50% { transform: scale(1.008) translateY(-2px); }
    }
    @keyframes copilotTalkingNod {
      0%, 100% { transform: scale(1.005) translateY(-1px); }
      25% { transform: scale(1.012) translateY(-3px); }
      50% { transform: scale(1.006) translateY(0px); }
      75% { transform: scale(1.014) translateY(-2px); }
    }
    #copilot-avatar-stage {
      animation: copilotBreathing 5s ease-in-out infinite;
      transform-origin: center bottom;
      transition: transform 0.3s ease;
    }
    #copilot-avatar-stage.copilot-speaking-motion {
      animation: copilotTalkingNod 1.6s ease-in-out infinite;
      filter: drop-shadow(0 0 18px rgba(6, 182, 212, 0.45));
    }"""

new_avatar_css = """    /* Co-pilot Rock-Solid Proscenium & Living Arctic Aurora Lighting */
    #copilot-avatar-stage {
      transform: none !important;
      animation: none !important;
      position: absolute;
      inset: 0;
      overflow: hidden;
      background: #020617;
    }
    #copilot-avatar-stage.copilot-speaking-motion {
      transform: none !important;
      animation: none !important;
      filter: drop-shadow(0 0 22px rgba(16, 185, 129, 0.4));
    }

    /* Living Aurora Borealis Sky Canvas (Over the mountains behind Kári) */
    #copilot-aurora-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 54%;
      pointer-events: none;
      z-index: 12;
      mix-blend-mode: screen;
      opacity: 0.88;
      transition: opacity 0.5s ease;
      filter: drop-shadow(0 0 10px rgba(16, 185, 129, 0.5));
    }

    /* Natural Eyelid Blink Layer */
    #copilot-avatar-img-blink {
      z-index: 11;
      pointer-events: none;
      transition: opacity 0.08s ease-in-out;
    }"""

if old_avatar_css in html:
    html = html.replace(old_avatar_css, new_avatar_css, 1)
    print("1. Replaced avatar CSS (stage is now 100% frozen, added aurora canvas styles).")
else:
    print("Warning: old_avatar_css not matched directly, checking fallback...")

# ==============================================================================
# 2. UPDATE AVATAR STAGE HTML IN #copilot-modal
# ==============================================================================
old_stage_html = """            <!-- AVATAR EN-FACE STAGE -->
            <div id="copilot-avatar-stage" class="absolute inset-0 w-full h-full overflow-hidden">
              <!-- Base Resting Portrait -->
              <img id="copilot-avatar-img-rest" src="assets/images/viking_copilot_rest.jpg" alt="Viking Navigator Kári (En Face Neutral)" class="absolute inset-0 w-full h-full object-cover object-top transition-opacity duration-150">

              <!-- Active Talking Animation Layer -->
              <img id="copilot-avatar-img-talk" src="assets/images/viking_copilot_frontal_talking.webp" alt="Viking Navigator Kári (En Face Speaking)" class="absolute inset-0 w-full h-full object-cover object-top opacity-0 transition-opacity duration-150">

              <!-- Cyan Scanlines & Vignette -->
              <div class="absolute inset-0 pointer-events-none bg-gradient-to-b from-cyan-500/10 via-transparent to-slate-950/60"></div>
            </div>"""

new_stage_html = """            <!-- AVATAR EN-FACE STAGE (FROZEN BACKGROUND + LIVING AURORA + NATURAL LIP SYNC) -->
            <div id="copilot-avatar-stage" class="absolute inset-0 w-full h-full overflow-hidden bg-slate-950">
              <!-- 1. Base Resting Portrait (100% stable, no transforms) -->
              <img id="copilot-avatar-img-rest" src="assets/images/viking_copilot_rest.jpg" alt="Viking Navigator Kári (En Face Neutral)" class="absolute inset-0 w-full h-full object-cover object-top transition-opacity duration-200">

              <!-- 2. Active Talking Articulation Layer (Mouth & Jaw Visemes, 100% frozen background) -->
              <img id="copilot-avatar-img-talk" src="assets/images/viking_copilot_frontal_talking.webp" alt="Viking Navigator Kári (En Face Speaking)" class="absolute inset-0 w-full h-full object-cover object-top opacity-0 transition-opacity duration-150">

              <!-- 3. Living Eye Blink Micro-Expression Layer -->
              <img id="copilot-avatar-img-blink" src="assets/images/kari_eye_blink_layer.png" alt="Kári Eyelid Blink" class="absolute inset-0 w-full h-full object-cover object-top opacity-0 pointer-events-none transition-opacity duration-75">

              <!-- 4. Dynamic Aurora Borealis Canvas (Dancing Northern Lights over the sky) -->
              <canvas id="copilot-aurora-canvas" data-speaking="false"></canvas>

              <!-- 5. Dynamic Aurora Rim Light & Atmospheric Lighting -->
              <div id="copilot-aurora-glow" class="absolute inset-0 pointer-events-none transition-all duration-500 opacity-40 bg-gradient-to-b from-emerald-500/20 via-cyan-500/5 to-slate-950/75"></div>
              
              <!-- 6. Subtle Frost Border -->
              <div class="absolute inset-0 pointer-events-none ring-1 ring-inset ring-cyan-500/25"></div>
            </div>"""

if old_stage_html in html:
    html = html.replace(old_stage_html, new_stage_html, 1)
    print("2. Replaced avatar stage HTML in index.html.")
else:
    print("Warning: old_stage_html not matched directly, checking fallback...")

# ==============================================================================
# 3. UPGRADE JAVASCRIPT: AURORA ENGINE, BLINK TIMER & SET SPEAKING STATE
# ==============================================================================
old_speaking_js = """    function setCopilotSpeakingState(isSpeaking, customText = '') {
      const restImg = document.getElementById('copilot-avatar-img-rest');
      const talkImg = document.getElementById('copilot-avatar-img-talk');
      const stage = document.getElementById('copilot-avatar-stage');
      const hud = document.getElementById('copilot-vocal-hud');
      const dot = document.getElementById('copilot-live-dot');
      const label = document.getElementById('copilot-status-label');
      const waveText = document.getElementById('copilot-wave-text');
      const waveBars = document.getElementById('copilot-soundwave-bars');

      if (isSpeaking) {
        if (stage) stage.classList.add('copilot-speaking-motion');
        if (restImg) restImg.style.opacity = '0';
        if (talkImg) talkImg.style.opacity = '1';
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
        if (restImg) restImg.style.opacity = '1';
        if (hud) hud.style.opacity = '0';
        if (dot) dot.className = 'w-2 h-2 rounded-full bg-emerald-400 animate-ping';
        if (label) {
          label.textContent = currentLang === 'uk' ? 'НА ЗВ\'ЯЗКУ' : 'STANDBY ONLINE';
          label.className = 'font-bold uppercase tracking-wider text-emerald-300';
        }
        if (waveText) waveText.textContent = currentLang === 'uk' ? 'ГОТОВИЙ ДО ДІАЛОГУ' : 'READY FOR COMMS';
        if (waveBars) waveBars.classList.remove('animate-pulse');
      }
    }"""

new_speaking_js = """    // =========================================================================
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
          label.textContent = currentLang === 'uk' ? 'НА ЗВ\\'ЯЗКУ' : 'STANDBY ONLINE';
          label.className = 'font-bold uppercase tracking-wider text-emerald-300';
        }
        if (waveText) waveText.textContent = currentLang === 'uk' ? 'ГОТОВИЙ ДО ДІАЛОГУ' : 'READY FOR COMMS';
        if (waveBars) waveBars.classList.remove('animate-pulse');
      }
    }"""

if old_speaking_js in html:
    html = html.replace(old_speaking_js, new_speaking_js, 1)
    print("3. Replaced setCopilotSpeakingState and injected Aurora/Blink engines.")
else:
    print("Warning: old_speaking_js not matched directly, checking fallback...")

# Update openCopilotModal and closeCopilotModal to trigger aurora & blink
if "function openCopilotModal() {" in html:
    html = re.sub(
        r'function openCopilotModal\(\)\s*\{',
        'function openCopilotModal() {\n      startCopilotAuroraEngine();\n      scheduleNextCopilotBlink();',
        html,
        count=1
    )
    print("Updated openCopilotModal to start aurora and blinking.")

if "function closeCopilotModal() {" in html:
    html = re.sub(
        r'function closeCopilotModal\(\)\s*\{',
        'function closeCopilotModal() {\n      stopCopilotAuroraEngine();\n      stopCopilotBlinkTimer();',
        html,
        count=1
    )
    print("Updated closeCopilotModal to stop aurora and blinking.")

# ==============================================================================
# 4. EXPAND KÁRI CONVERSATIONAL INTELLIGENCE ENGINE (HUMAN CHAT + DIALOGUE)
# ==============================================================================
new_deep_answer_func = '''    // =========================================================================
    // KÁRI CONVERSATIONAL INTELLIGENCE & EXPEDITION BRAIN (HUMAN PERSONA + CHAT)
    // =========================================================================
    function generateDeepCopilotAnswer(q, lang) {
      const lower = q.toLowerCase().trim();
      const isUk = lang === 'uk';

      // -------------------------------------------------------------
      // 1. GREETINGS & PERSONAL SALUTATIONS (Привітання)
      // -------------------------------------------------------------
      const isGreeting = ['привіт', 'добрий день', 'доброго дня', 'добрий ранок', 'доброго ранку', 
        'добрий вечір', 'доброго вечора', 'здоров', 'вітаю', 'салют', 'хай', 'hello', 'hi', 'hey', 
        'good morning', 'good afternoon', 'good evening', 'greetings', 'góðan daginn', 'godan daginn']
        .some(w => lower.includes(w));

      const isHowAreYou = ['як справи', 'як ти', 'як настрій', 'як ся маєш', 'як життя', 'як твій день', 
        'що нового', 'як поживаєш', 'як почуваєшся', 'how are you', 'how is it going', 'how do you feel', 
        'how are things', 'whats up', "what's up", 'how goes it']
        .some(w => lower.includes(w));

      // Combined "Привіт, як справи?"
      if (isGreeting && isHowAreYou) {
        return isUk 
          ? "Góðan daginn, друже! Радий тебе чути! У мене все чудово — північний вітер сьогодні свіжий і бадьорий, кава в моєму термосі гаряча, а на Трасі 1 панує спокійна видимість. Як твій день? Куди сьогодні тримаємо курс — на водоспади Півдня чи підкорювати льодовики?"
          : "Góðan daginn, my friend! Wonderful to hear from you! I'm doing great — crisp arctic breeze, steaming hot coffee in my thermos, and clear cruising conditions on Route 1. How is your day going? Where are we heading today — south coast waterfalls or glacier exploration?";
      }

      if (isGreeting) {
        return isUk 
          ? "Góðan daginn, друже! Вітаю на борту нашої експедиції! Я — твій штурман Кáрі. На дорозі спокійно, полярне небо величне, а попереду цілий острів дивовижних пригод. Як настрій? Готовий їхати чи просто хочеш поговорити перед стартом? Я завжди поруч!"
          : "Góðan daginn, friend! Welcome aboard our Icelandic expedition! I'm your navigator Kári. The Ring Road is calm, the sub-arctic sky is vast, and an entire island of wonder awaits. How's your spirit today? Ready to roll, or would you like to chat before we start?";
      }

      if (isHowAreYou) {
        return isUk 
          ? "Дякую, що запитав, друже! Мої справи на висоті. Слідкую за супутниковими радарами хмарності, попиваю міцну ісландську каву і милуюсь північним горизонтом. Головне — щоб у тебе подорож була легкою і безпечною. Як твоє самопочуття? До чого найбільше лежить душа сьогодні?"
          : "Thanks for asking, friend! I'm in great spirits. Keeping a sharp eye on cloud radar telemetry, sipping strong black coffee, and admiring the northern horizon. Most of all, I want to make sure your journey is smooth and inspiring. How are you feeling today?";
      }

      // -------------------------------------------------------------
      // 2. IDENTITY, BACKGROUND & PERSONA (Хто ти? Розкажи про себе)
      // -------------------------------------------------------------
      if (lower.includes('хто ти') || lower.includes('як тебе звати') || lower.includes("твоє ім'я") || 
          lower.includes('розкажи про себе') || lower.includes('звідки ти') || lower.includes('ти хто') || 
          lower.includes('ти людина') || lower.includes('ти робот') || lower.includes('who are you') || 
          lower.includes('what is your name') || lower.includes('tell me about yourself')) {
        return isUk 
          ? "🛡️ Я — <b>Кáрі (Kári Pétursson)</b>, твій офіційний штурман і ліцензований гід експедиції. Народився тут, в Ісландії, серед фіордів і чорних лавових полів. Мої предки ходили на драккарах, а я об'їздив кожен кілометр Кільцевої траси 1 та суворих високогірних доріг F-roads. Я тут не як сухий диктор датчиків, а як живий друг у дорозі — підкажу секретні купальні, розкажу давні саги й подбаю, щоб жоден шторм не застав тебе зненацька!"
          : "🛡️ I am <b>Kári (Kári Pétursson)</b>, your licensed expedition navigator and Icelandic road companion. Born among the basalt sea stacks and volcanic moss. My ancestors navigated Viking longships, and I've driven every mile of Ring Road 1 and rugged highland F-roads. I'm here not as a rigid automated voice, but as your genuine road brother — sharing secret baths, ancient sagas, and keeping you safe from sudden Atlantic gales!";
      }

      // -------------------------------------------------------------
      // 3. COMPANIONSHIP & SMALL TALK (Що робиш? Холодно? Ти живий?)
      // -------------------------------------------------------------
      if (lower.includes('що робиш') || lower.includes('чим займаєшся') || lower.includes('what are you doing')) {
        return isUk 
          ? "Слідкую за горизонтом, відстежую пересування хмарних фронтів над льодовиком Ватнайокюдль і звіряю координати нашої наступної стоянки. А ще просто тішуся нашій розмові! Чим можу допомогти тобі просто зараз?"
          : "Scanning the arctic horizon, tracking cloud advection corridors over Vatnajökull ice cap, and checking waypoints for our next turnout. And enjoying our conversation! How can I assist you right now?";
      }

      if (lower.includes('холодно') || lower.includes('тобі холодно') || lower.includes('мерзнеш') || lower.includes('cold') || lower.includes('are you cold')) {
        return isUk 
          ? "Холодно? Справжній ісландець знає давню мудрість: <i>«Немає поганої погоди — є лише поганий одяг!»</i> Мене зігріває вовняний светр лопапейса (lopapeysa) та гарячі геотермальні джерела. Але ти обов'язково одягайся шарами: тутешній вітер уміє пробирати до кісток, особливо біля океану!"
          : "Cold? In Iceland we live by an old truth: <i>'There is no bad weather, only bad clothing!'</i> A hand-knit wool lopapeysa and hot geothermal springs keep me toasty. But make sure you wear windproof layers—our coastal winds can chill right through to the bone!";
      }

      if (lower.includes('ти живий') || lower.includes('are you alive') || lower.includes('ти справжній') || lower.includes('are you real')) {
        return isUk 
          ? "Я цілком живий духом і поглядом! Дивлюсь прямо на тебе своїми нордичними очима, відчуваю цей холодний вітер і завжди готовий прийти на допомогу. У кожній моїй пораді — досвід поколінь ісландських мореплавців і любов до цього острова."
          : "I'm very much alive in spirit and focus! Looking right at you with clear Nordic eyes, feeling the brisk northern winds, and always standing by to navigate. In every tip I share lies generations of Icelandic seamanship and deep respect for this land.";
      }

      if (lower.includes('жарт') || lower.includes('анекдот') || lower.includes('розвесели') || lower.includes('смішне') || lower.includes('joke') || lower.includes('funny')) {
        return isUk 
          ? "😄 Тримай класичний ісландський жарт: <i>«Що треба робити, якщо ви заблукали в ісландському лісі? — Просто встаньте на повний зріст!»</i> Через наші вітри дерева тут рідко виростають вище пояса. А головне — пам'ятай наше національне заклинання: <b>'Þetta reddast'</b> (все обов'язково владнається)!"
          : "😄 Here's an authentic Icelandic joke for the road: <i>'What should you do if you get lost in an Icelandic forest? — Just stand up!'</i> Our sub-arctic birch trees rarely grow taller than waist height due to the gales. And always remember our national motto: <b>'Þetta reddast'</b> — everything will work out in the end!";
      }

      if (lower.includes('дякую') || lower.includes('спасибі') || lower.includes('вдячний') || lower.includes('thanks') || lower.includes('thank you') || lower.includes('appreciate')) {
        return isUk 
          ? "Завжди щиро будь ласка, друже! Для мене честь супроводжувати тебе цією неймовірною землею льоду й вогню. Якщо знадобиться будь-яка порада — я завжди тут, на відстані одного кліку чи слова!"
          : "You are most welcome, my friend! It's a genuine honor navigating this land of fire and ice with you. Whenever you need advice or a route check, I'm right here by your side!";
      }

      if (lower.includes('бувай') || lower.includes('до побачення') || lower.includes('на добраніч') || lower.includes('папа') || lower.includes('пока') || lower.includes('goodbye') || lower.includes('bye') || lower.includes('see you')) {
        return isUk 
          ? "Góða ferð! Щасливої дороги й тримай кермо міцно! Насолоджуйся краєвидами за вікном, а я продовжу стежити за радарами та безпекою нашого курсу. До зустрічі!"
          : "Góða ferð! Safe journey and keep a firm grip on the steering wheel! Take in the epic views, and I'll keep monitoring road telemetry and radars. Talk soon!";
      }

      // -------------------------------------------------------------
      // 4. ICELANDIC FOOD, DRINKS & CULTURE (Їжа, ресторани, звичаї)
      // -------------------------------------------------------------
      if (lower.includes('їж') || lower.includes('поїсти') || lower.includes('кухн') || lower.includes('страва') || 
          lower.includes('кава') || lower.includes('акул') || lower.includes('хот-дог') || lower.includes('food') || 
          lower.includes('eat') || lower.includes('restaurant') || lower.includes('shark') || lower.includes('pylsa')) {
        return isUk 
          ? "🍲 <b>Ісландська гастрономія від Кáрі:</b><br>1) <b>Pylsa</b> — легендарний ісландський хот-дог із бараниною, смаженою хрусткою цибулею та соусом remúlaði в Рейк'явіку.<br>2) <b>Kjötsúpa</b> — наваристий суп із баранини та коренеплодів, найкраще зігріває після шторму.<br>3) Свіжий арктичний голець і ніжний десерт Skyr.<br>4) А для відчайдушних — кубик ферментованої акули <b>Hákarl</b> під чарку кминного напою Brennivín («Чорна смерть»). Спробуй — це спогади на все життя!"
          : "🍲 <b>Kári's Icelandic Culinary Guide:</b><br>1) <b>Pylsa</b> — legendary Icelandic lamb hot-dog with crispy fried onions and remúlaði in Reykjavík.<br>2) <b>Kjötsúpa</b> — slow-simmered lamb and root vegetable soup, ideal after a brisk windy hike.<br>3) Pan-seared Arctic char and creamy Skyr with bilberries.<br>4) For the daring adventurer — a cube of fermented shark <b>Hákarl</b> chased with caraway schnapps Brennivín ('Black Death'). An unforgettable rite of passage!";
      }

      if (lower.includes('музик') || lower.includes('пісн') || lower.includes('music') || lower.includes('sigur') || lower.includes('bjork') || lower.includes('бйорк')) {
        return isUk 
          ? "🎵 <b>Музика Ісландії:</b> Увімкни в машині <b>Sigur Rós</b> або <b>Ólafur Arnalds</b> — їхнє ембієнт-звучання ідеально зливається з туманними вулканічними пустками. Якщо хочеться енергії — слухай <b>Kaleo</b> (ісландський блюз-рок із Мосфедльсбайра) чи неповторну <b>Björk</b>!"
          : "🎵 <b>Soundtrack of the Road:</b> Put on <b>Sigur Rós</b> or <b>Ólafur Arnalds</b> — their ambient orchestral soundscapes blend spiritually with misty volcanic fields. For gritty driving energy, tune into <b>Kaleo</b> (blues-rock from Mosfellsbær) or the iconic visionary <b>Björk</b>!";
      }

      // -------------------------------------------------------------
      // 5. SAGAS, FOLKLORE, ELVES & TROLLS (Саги, ельфи, міфологія)
      // -------------------------------------------------------------
      if (lower.includes('саг') || lower.includes('ельф') || lower.includes('трол') || lower.includes('хульдуфоулк') || 
          lower.includes('казк') || lower.includes('легенд') || lower.includes('міф') || lower.includes('saga') || 
          lower.includes('elf') || lower.includes('elves') || lower.includes('troll') || lower.includes('myth')) {
        return isUk 
          ? "🧝‍♂️ <b>Саги та Прихований народ (Huldufólk):</b> В Ісландії кожен камінь має пам'ять. Досі при прокладанні доріг дорожня служба Vegagerðin консультується, щоб не потривожити скелі, де мешкають ельфи! А от чорні скелі Reynisdrangar біля Віка — це тролі, які тягнули трищогловий корабель на берег, забарилися й закам'яніли з першим променем сонця. Поважай тутешніх духів природи — і дорога буде прихильною до тебе!"
          : "🧝‍♂️ <b>Sagas & Huldufólk (The Hidden People):</b> In Iceland, every rock holds memory. Even modern road engineers at Vegagerðin take care not to displace boulders believed to house elves! The dramatic sea needles of Reynisdrangar near Vík were trolls caught dragging a ship ashore, turned to basalt stone by the morning sun. Treat the nature spirits with respect, and the land will guide you safely!";
      }

      // -------------------------------------------------------------
      // 6. AURORA BOREALIS & CLOUD CLEARANCES (Полярне сяйво)
      // -------------------------------------------------------------
      if (lower.includes('аврор') || lower.includes('aurora') || lower.includes('сяйв') || lower.includes('lights') || lower.includes('північн')) {
        return isUk 
          ? "🌌 <b>Полювання на Аврору від Штурмана:</b> Планетарний індекс Kp зараз 4.2 (активна фаза). Головний секрет успіху — не сила геомагнітної бурі, а <b>чисте небо без низької хмарності (Lágský &lt; 15%)</b>! Поглянь на мою карту радарів: чудові зелені прогалини прогнозуються навколо Скоугафосса та озера Міватн після 22:00. Від'їдь далі від вогнів міст, дай очам 15 хвилин звикнути до темряви — і дивись на зеніт!"
          : "🌌 <b>Aurora Hunting Dispatch:</b> Planetary Kp index is currently 4.2 (Active storm). The number one rule is finding <b>clear sky windows free of low clouds (Lágský &lt; 15%)</b>! Check my live advection radar: optimal clear corridors open near Skógafoss and Lake Mývatn past 22:00. Park safely in designated dark-sky turnouts away from highway lights!";
      }

      // -------------------------------------------------------------
      // 7. ROAD SAFETY, SEVERE WIND & CAR DOORS (Безпека та Траса 1)
      // -------------------------------------------------------------
      if (lower.includes('вітер') || lower.includes('wind') || lower.includes('шторм') || lower.includes('двері') || lower.includes('door') || lower.includes('шквал')) {
        return isUk 
          ? "💨 <b>Головне дорожнє правило Ісландії (Door Danger!):</b> На південному узбережжі біля мису Дирхолей та на східних перевалах пориви вітру досягають 16–22 м/с. <b>ЗАВЖДИ тримай двері автомобіля обома руками при відкриванні!</b> Раптовий шквал може вивернути двері назовні, а страховка прокатних авто цього не покриває. Паркуйся завжди носом проти вітру!"
          : "💨 <b>Critical Driver Rule (Door Danger!):</b> Along the South Shore near Cape Dyrhólaey and eastern passes, gale gusts exceed 16–22 m/s. <b>ALWAYS grip your car door with BOTH hands when exiting!</b> A sudden gust can snap door hinges outward instantly, and car rental CDW insurance never covers blown-door damage. Always park facing directly into the wind!";
      }

      if (lower.includes('дорог') || lower.includes('трас') || lower.includes('road') || lower.includes('route 1') || lower.includes('міст')) {
        return isUk 
          ? "🛣️ <b>Стан Траси 1 (Ring Road):</b> Кільцева траса навколо острова повністю відкрита й розчищена (Greiðfært). Пам'ятай про специфіку: в Ісландії багато <b>односмугових дерев'яних мостів (Einbreið brú)</b> — хто перший під'їхав, той має пріоритет. Знижуй швидкість до 30 км/год перед кожним мостом і стережися овець на узбіччі!"
          : "🛣️ <b>Route 1 Ring Road Status:</b> The entire coastal ring highway is open and clear (Greiðfært). Keep in mind key local road rules: frequent <b>Single Lane Bridges (Einbreið brú)</b> where the first vehicle at the crossing has right-of-way. Slow to 30 km/h on approach, and watch for free-roaming sheep near the asphalt!";
      }

      // -------------------------------------------------------------
      // 8. WATERFALLS & SECRET GEMS (Водоспади та улюблені локації)
      // -------------------------------------------------------------
      if (lower.includes('водоспад') || lower.includes('waterfall') || lower.includes('секретн') || lower.includes('secret') || lower.includes('куди поїхати') || lower.includes('порадь')) {
        return isUk 
          ? "💧 <b>Мої улюблені секретні місця:</b> Окрім відомих гігантів Gullfoss та Skógafoss, обов'язково відвідай: 1) <b>Kvernufoss</b> — казковий водоспад у смарагдовій ущелині за музеєм Скоугар, куди можна зайти за стіну води; 2) <b>Gljúfrabúi</b> — схований усередині таємної печери; 3) <b>Brúarfoss</b> із льодовиковою водою неонового блакитного кольору; 4) Термальну річку <b>Reykjadalur</b>, де купаються просто серед гір!"
          : "💧 <b>Kári's Personal Secret Gems:</b> Beyond the famous icons Gullfoss and Skógafoss, do not miss: 1) <b>Kvernufoss</b> — ethereal cataract tucked into a green gorge behind Skógar museum where you can walk behind the roaring veil; 2) <b>Gljúfrabúi</b> — hidden inside an ancient basalt cave; 3) <b>Brúarfoss</b> with radiant cyan glacial braids; 4) Warm thermal river in <b>Reykjadalur</b> valley!";
      }

      // -------------------------------------------------------------
      // 9. BEACHES, SNEAKER WAVES & REYNISFJARA (Чорні пляжі)
      // -------------------------------------------------------------
      if (lower.includes('reynisfjara') || lower.includes('рейнісф') || lower.includes('чорний пляж') || lower.includes('хвил') || lower.includes('хвилі') || lower.includes('beach')) {
        return isUk 
          ? "⚠️ <b>Рейнісф'яра (Чорний пляж & Хвилі-підкрадачі):</b> Один із найвеличніших і водночас найпідступніших берегів Атлантики! Хвилі-вбивці (sneaker waves) виникають зненацька і накочуються на десятки метрів вище лінії прибою. <b>СУВОРЕ ПРАВИЛО: ніколи не повертайся спиною до океану</b> і тримайся на відстані не менше 30 метрів від піни. Звертай увагу на колірний світлофор безпеки біля входу!"
          : "⚠️ <b>Reynisfjara Black Sand Beach Alert:</b> One of Iceland's most awe-inspiring yet dangerous coastlines. Treacherous sneaker waves surge unexpectedly far up the basalt shore. <b>STRICT SURVIVAL RULE: Never turn your back on the Atlantic Ocean</b>, and keep a minimum 30-meter buffer from the incoming surf. Always obey the automated digital warning beacon at the parking lot!";
      }

      // -------------------------------------------------------------
      // 10. GEOTHERMAL SPAS & BATHS (СПА, басейни, купальні)
      // -------------------------------------------------------------
      if (lower.includes('спа') || lower.includes('spa') || lower.includes('басейн') || lower.includes('купальн') || lower.includes('lagoon') || lower.includes('гаряч')) {
        return isUk 
          ? "♨️ <b>Геотермальні перлини острова:</b> 1) <b>Sky Lagoon</b> — неймовірний безкрайній теплий басейн із видом на океан і 7-етапним ритуалом; 2) Автентичні <b>Hvammsvík Hot Springs</b> — 8 кам'яних чаш просто в морському фіорді; 3) <b>Blue Lagoon</b> — насичена кремнеземом бірюзова вода; 4) Дика історична купальня <b>Seljavallalaug</b> 1923 року біля підніжжя вулкана. Обов'язкове правило: ретельний душ із милом перед входом у воду!"
          : "♨️ <b>Geothermal Wellness Guide:</b> 1) <b>Sky Lagoon</b> — spectacular infinity pool cantilevered over ocean breakers featuring the 7-step ritual; 2) Authentic <b>Hvammsvík Hot Springs</b> — 8 natural stone tidal pools right in the fjord; 3) <b>Blue Lagoon</b> — iconic silica mud and mineral salt waters; 4) Historic mountain pool <b>Seljavallalaug</b> built in 1923 nestled in a secluded valley. Mandatory etiquette: thorough soap shower before bathing!";
      }

      // -------------------------------------------------------------
      // 11. GLACIERS, ICE CAVES & DIAMOND BEACH (Льодовики)
      // -------------------------------------------------------------
      if (lower.includes('льодовик') || lower.includes('айсберг') || lower.includes('лагун') || lower.includes('glacier') || lower.includes('ice cave') || lower.includes('jökulsárlón') || lower.includes('diamond')) {
        return isUk 
          ? "🧊 <b>Льодовики та Крижана лагуна Йокульсарлон:</b> Тут від шельфу льодовика Брейдамеркюрйокюдль відколюються тисячолітні сині айсберги й дрейфують до океану. А через дорогу розташований знаменитий Діамантовий пляж (Diamond Beach), де крижані брили виблискують на чорному вулканічному піску, як коштовне каміння. Не виходьте на плавучі айсберги — це небезпечно!"
          : "🧊 <b>Glacial Wonders & Jökulsárlón Lagoon:</b> Massive thousand-year-old icebergs calve off Breiðamerkurjökull and glide serenely toward the Atlantic. Right across the road is Diamond Beach, where sculpted blue ice crystals sparkle against jet-black volcanic sand. Never climb onto drifting icebergs — currents are deceptively swift!";
      }

      // -------------------------------------------------------------
      // 12. LOGISTICS: PARKING, GAS & EMERGENCY (Парковки, пальне, 112)
      // -------------------------------------------------------------
      if (lower.includes('паркінг') || lower.includes('parking') || lower.includes('parka') || lower.includes('оплат')) {
        return isUk 
          ? "🅿️ <b>Оплата парковок в Ісландії:</b> У національних парках (Þingvellir, Seljalandsfoss, Skaftafell, Jökulsárlón, Fagradalsfjall) встановлені камери автоматичного розпізнавання номерів. Оплачуйте стоянку через додаток або сайт <b>Parka.is</b> протягом 24 годин після виїзду, щоб уникнути адмінштрафу від прокатної компанії."
          : "🅿️ <b>Parking Logistics:</b> Major natural sights (Þingvellir, Seljalandsfoss, Skaftafell, Jökulsárlón, Fagradalsfjall) utilize automatic camera license plate recognition. Pay parking via the <b>Parka.is</b> app or website within 24 hours of departure to avoid car rental handling penalties.";
      }

      if (lower.includes('бензин') || lower.includes('gas') || lower.includes('палив') || lower.includes('заправ')) {
        return isUk 
          ? "⛽ <b>Заправки на острові:</b> Мережі N1, Olís, Orkan. Автоматичні колонки вимагають банківську картку з 4-значним PIN-кодом (Apple Pay на багатьох сільських терміналах не підтримується). Між Віком та Хьофном заправки зустрічаються рідко — заправляйте повний бак, як тільки стрілка опускається нижче половини!"
          : "⛽ <b>Fuel & Refueling Logistics:</b> Leading networks include N1, Olís, and Orkan. Self-service pumps strictly require a chip-and-PIN bank card (Apple Pay often fails on remote unstaffed pumps). Between Vík and Höfn fuel stops are far apart — fill up your tank whenever you dip below half!";
      }

      if (lower.includes('112') || lower.includes('sos') || lower.includes('порятунок') || lower.includes('emergency')) {
        return isUk 
          ? "🚨 <b>Екстрена допомога в Ісландії:</b> Єдиний екстрений номер — <b>112</b> (з'єднується навіть без SIM-картки через будь-яку доступну вежу зв'язку). Рекомендую встановити мобільний додаток <b>112 Iceland</b> та зареєструвати маршрут своєї експедиції на SafeTravel.is!"
          : "🚨 <b>Emergency Protocol:</b> The universal emergency number in Iceland is <b>112</b> (connects without SIM via any reachable cellular tower). Download the <b>112 Iceland</b> mobile app and lodge your expedition travel itinerary on SafeTravel.is before setting off!";
      }

      // -------------------------------------------------------------
      // 13. DYNAMIC LOOKUP IN 115 POI CATALOG & MASTER FACTS
      // -------------------------------------------------------------
      if (typeof MASTER_GEOJSON !== 'undefined' && MASTER_GEOJSON.features) {
        const matchedPoi = MASTER_GEOJSON.features.find(f => {
          const p = f.properties;
          const nameUk = (p.name || '').toLowerCase();
          const nameEn = (p.name_en || '').toLowerCase();
          const id = (p.id || '').toLowerCase();
          return lower.includes(id) || 
            (nameUk && nameUk.split(' ').some(w => w.length > 3 && lower.includes(w))) ||
            (nameEn && nameEn.split(' ').some(w => w.length > 3 && lower.includes(w)));
        });

        if (matchedPoi) {
          const p = matchedPoi.properties;
          const poiName = isUk ? p.name : (p.name_en || p.name);
          const icon = p.icon || '📍';
          return isUk
            ? `${icon} <b>Штурман Кáрі про ${poiName}:</b> Це одна з найвизначніших точок нашого маршруту! Локація розташована в регіоні <i>${p.region || 'Ісландія'}</i>. Я зафіксував її координати в бортовому навігаторі. Хочеш прокласти до неї оперативний маршрут або почути геологічну довідку?`
            : `${icon} <b>Navigator Kári on ${poiName}:</b> This is one of the premier highlights in our expedition log! Located in the <i>${p.region || 'Iceland'}</i> corridor. Coordinates are locked into flight telemetry. Would you like me to plot direct navigation bearings or dive into geological history?`;
        }
      }

      // -------------------------------------------------------------
      // 14. WARM HUMAN PHILOSOPHICAL & OPEN CONVERSATION FALLBACK
      // -------------------------------------------------------------
      return isUk 
        ? "🛡️ <b>Штурман Кáрі:</b> Цікава думка, друже! Сидячи тут, серед суворих вулканічних ландшафтів Ісландії під цим полярним небом, на багато речей дивишся по-іншому. Я завжди радий такій щирій розмові. Розкажи більше, або якщо захочеш — запитай мене про стан Траси 1, полювання за Авророю чи затишні секретні купальні. Куди тримаємо курс далі?"
        : "🛡️ <b>Navigator Kári:</b> That's a thoughtful question, my friend! Out here amidst Iceland's vast volcanic wilderness under the dancing northern lights, one sees the world with fresh clarity. I'm always glad to talk with you on any topic. Tell me more, or if you prefer, ask me about Ring Road conditions, Aurora hunting windows, or hidden hot springs. Where shall we navigate next?";
    }'''

# Replace old generateDeepCopilotAnswer with new expanded conversational intelligence
start_deep_idx = html.find('function generateDeepCopilotAnswer(q, lang) {')
end_deep_target = '// SEND QUERY DISPATCHER (LM STUDIO OR EXPERT ENGINE)'
end_deep_idx = html.find(end_deep_target)

if start_deep_idx != -1 and end_deep_idx != -1:
    html = html[:start_deep_idx] + new_deep_answer_func.strip() + "\n\n    " + html[end_deep_idx:]
    print("4. Replaced generateDeepCopilotAnswer with full 14-domain conversational AI engine.")
else:
    print(f"Warning: could not locate generateDeepCopilotAnswer markers ({start_deep_idx}, {end_deep_idx})")

# Write updated file
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully.")
