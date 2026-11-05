# -*- coding: utf-8 -*-
import json

LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/iceland_guide_vision_lab.html"

html_content = '''<!DOCTYPE html>
<html lang="uk" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iceland Guide Vision Lab — 10 Футуристичних Концептів Інтерфейсу Майбутнього</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @keyframes warpSpeed {
      0% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.08); opacity: 1; }
      100% { transform: scale(1); opacity: 0.8; }
    }
    @keyframes hudScan {
      0% { top: 0%; opacity: 0.8; }
      50% { opacity: 0.4; }
      100% { top: 100%; opacity: 0.8; }
    }
    @keyframes auroraShift {
      0% { filter: hue-rotate(0deg); }
      50% { filter: hue-rotate(45deg); }
      100% { filter: hue-rotate(0deg); }
    }
    .hud-line {
      position: absolute;
      left: 0; right: 0; height: 1px;
      background: linear-gradient(90deg, transparent, rgba(6, 182, 212, 0.8), transparent);
      animation: hudScan 4s linear infinite;
    }
    .concept-card {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(8, 13, 24, 0.95) 100%);
      border: 1px solid rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(14px);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .concept-card:hover {
      border-color: rgba(6, 182, 212, 0.5);
      transform: translateY(-2px);
      box-shadow: 0 12px 30px -8px rgba(6, 182, 212, 0.25);
    }
    .concept-card.active {
      border-color: #06b6d4;
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.15) 0%, rgba(8, 13, 24, 0.98) 100%);
      box-shadow: 0 0 25px rgba(6, 182, 212, 0.35);
    }
    /* Biome Theme Overrides */
    body.theme-glacier {
      background: #020712;
      --accent: #38bdf8;
    }
    body.theme-obsidian {
      background: #0d0604;
      --accent: #f97316;
    }
    body.theme-moss {
      background: #040d08;
      --accent: #10b981;
    }
  </style>
</head>
<body class="bg-[#050811] text-[#f8fafc] font-sans min-h-screen overflow-x-hidden selection:bg-cyan-500 selection:text-black">

  <!-- TOP BAR -->
  <header class="border-b border-slate-800 bg-slate-950/80 backdrop-blur-xl sticky top-0 z-40 px-4 md:px-8 py-3 flex items-center justify-between">
    <div class="flex items-center space-x-3">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-cyan-500 to-emerald-500 flex items-center justify-center text-lg shadow-lg shadow-cyan-500/20">
        🚀
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-sm md:text-base font-black tracking-tight text-white">ICELAND VISION LAB</h1>
          <span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[10px] font-bold border border-cyan-500/30">10 КОНЦЕПТІВ МАЙБУТНЬОГО</span>
        </div>
        <p class="text-[11px] text-slate-400">Інтерактивна лабораторія надсучасних інтерфейсних парадигм для розумного аудіогіда</p>
      </div>
    </div>

    <!-- Navigation Back -->
    <div class="flex items-center gap-2">
      <a href="index.html" class="px-3.5 py-1.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs flex items-center gap-1.5 shadow-md shadow-cyan-600/30 transition">
        <span>🗺️</span> <span>Повернутися до 3D-Карти</span>
      </a>
      <a href="iceland_guide_encyclopedia.html" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition hidden sm:inline-flex">
        📚 Енциклопедія
      </a>
    </div>
  </header>

  <!-- MAIN INTERACTIVE STUDIO -->
  <main class="max-w-7xl mx-auto p-4 md:p-8 space-y-8">

    <!-- HERO INTRO BANNER -->
    <section class="relative rounded-3xl p-6 md:p-10 overflow-hidden border border-cyan-500/30 bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950/40 shadow-2xl">
      <div class="relative z-10 max-w-3xl space-y-4">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 font-mono text-xs">
          <span>⚡</span> <span>R&D EXPERIMENTAL LAB • BEYOND CONVENTIONAL WEB</span>
        </div>
        <h2 class="text-2xl md:text-4xl font-black text-white leading-tight">
          10 Інноваційних Концепцій, які Руйнують Уявлення про Туристичні Сайти
        </h2>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed">
          Традиційні веб-сайти з пласкими списками та кнопками відійшли в минуле. Для експедицій Ісландією потрібен досвід кінематографічного занурення: орбітальні гіперстрибки, голографічні вітрові HUD-дисплеї, живі симулятори стихій та аудіо-синестезія рельєфу. Випробуйте кожен концепт нижче в живому демо-режимі.
        </p>

        <div class="flex flex-wrap items-center gap-3 pt-2">
          <button onclick="activateConcept(0)" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold text-xs flex items-center gap-2 shadow-lg shadow-cyan-500/30 transition">
            <span>✨</span> <span>Запустити Орбітальний Спуск (Concept 1)</span>
          </button>
          <button onclick="playAllFXChime()" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center gap-1.5 transition">
            <span>🔊</span> <span>Звуковий синестезійний тест</span>
          </button>
        </div>
      </div>

      <!-- Holographic Background Elements -->
      <div class="absolute -right-16 -top-16 w-80 h-80 rounded-full bg-cyan-500/10 blur-3xl pointer-events-none"></div>
      <div class="absolute right-10 bottom-6 opacity-30 hidden lg:block">
        <span class="text-9xl font-mono font-black text-cyan-400/20 select-none">2035</span>
      </div>
    </section>

    <!-- LIVE DEMO STAGE (INTERACTIVE VIEWPORT) -->
    <section class="rounded-3xl border border-slate-800 bg-slate-950 overflow-hidden shadow-2xl relative">
      <div class="p-4 border-b border-slate-800 bg-slate-900/80 flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center space-x-2">
          <span class="w-3 h-3 rounded-full bg-cyan-400 animate-ping"></span>
          <span class="text-xs font-mono uppercase tracking-wider text-slate-400 font-bold">АКТИВНЕ ДЕМО:</span>
          <span id="demo-badge-title" class="text-xs font-bold text-cyan-300">01. Орбітальний Гіперстрибок (Orbital Re-Entry)</span>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="triggerActiveDemoAction()" id="btn-demo-action" class="px-3 py-1 rounded-lg bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300 text-xs font-bold border border-cyan-500/40 flex items-center gap-1 transition">
            <span>▶</span> <span id="btn-demo-action-text">Запустити дію</span>
          </button>
          <span id="demo-telemetry-badge" class="px-2 py-0.5 rounded bg-slate-800 text-slate-400 font-mono text-[10px]">FPS: 60 • WebGL Active</span>
        </div>
      </div>

      <!-- STAGE CANVAS & INTERACTIVE DISPLAY -->
      <div class="relative w-full h-[400px] md:h-[480px] bg-black overflow-hidden flex items-center justify-center" id="demo-stage-container">
        <canvas id="stage-canvas" class="absolute inset-0 w-full h-full"></canvas>
        <div class="hud-line pointer-events-none"></div>

        <!-- Dynamic Overlay Container -->
        <div id="stage-overlay" class="relative z-20 pointer-events-none flex flex-col items-center justify-center text-center p-6 space-y-3">
          <div class="text-4xl md:text-6xl" id="stage-icon">🛸</div>
          <h3 class="text-xl md:text-3xl font-black text-white" id="stage-title">Орбітальний Гіперстрибок</h3>
          <p class="text-xs md:text-sm text-cyan-300 font-mono max-w-lg" id="stage-desc">
            Натисніть кнопку нижче для симуляції спуску з орбіти Землі в каньйон Ґулльфосс зі звуковим бар'єром.
          </p>
          <div id="stage-telemetry" class="pt-2 font-mono text-[11px] text-emerald-400 flex items-center gap-4">
            <span>ALTITUDE: <b id="val-alt">450,000 KM</b></span>
            <span>MACH: <b id="val-mach">14.2</b></span>
            <span>TARGET: <b id="val-target">ÞINGVELLIR</b></span>
          </div>
        </div>
      </div>
    </section>

    <!-- 10 CONCEPTS GRID -->
    <section class="space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h3 class="text-lg md:text-xl font-black text-white flex items-center gap-2">
            <span>Каталог 10 Концепцій</span>
            <span class="text-xs font-normal text-slate-400">Оберіть концепт для запуску на інтерактивному стенді</span>
          </h3>
        </div>
        <span class="text-xs font-mono text-cyan-400">10 Готових Архітектур</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="concepts-grid">
        <!-- Rendered via JavaScript -->
      </div>
    </section>

  </main>

  <!-- MASTER LOGIC -->
  <script>
    const CONCEPTS = [
      {
        id: "orbital-reentry",
        num: "01",
        title: "Орбітальний Гіперстрибок (Orbital Re-Entry)",
        icon: "🛸",
        badge: "Deep Space Dive",
        shortDesc: "Спуск із космосу прямо в каньйон із переходом надзвукового бар'єра, гіперпросторовими лініями та симуляцією висоти.",
        fullDesc: "Сайт не відкривається нудною сторінкою: ви перебуваєте на орбіті на висоті 450 000 км, бачите всю планету та кільце Аврори, після чого камера на надзвуковій швидкості пронизує хмари і приземляється точно на потрібний POI.",
        actionText: "Здійснити Гіперстрибок",
        telemetry: { alt: "450,000 KM", mach: "14.2", target: "GULLFOSS" }
      },
      {
        id: "cyber-cockpit",
        num: "02",
        title: "Голографічний Вітровий HUD Cybertruck 2035",
        icon: "🛡️",
        badge: "AR Windshield",
        shortDesc: "Екран як лобове скло арктичного всюдихода з векторними зеленими/ціановими лініями, ризиком вітру та нахилом кузова.",
        fullDesc: "Користувач відчуває себе всередині броньованого авто майбутнього: на вітрове скло в реальному часі проєктуються кути нахилу, пориви вітру SafeTravel, дистанція до краю лави та приціл на гейзери.",
        actionText: "Активувати Тактичний HUD",
        telemetry: { alt: "12 M (Ground)", mach: "0.08", target: "KATLA VOLCANO" }
      },
      {
        id: "synesthesia-sound",
        num: "03",
        title: "Аудіо-Кінетична Синестезія Рельєфу",
        icon: "🔊",
        badge: "Sound Sculpting",
        shortDesc: "Звуки стихії формують геометрію: гуркіт водоспаду фізично деформує 3D-сітку ландшафту та хвилі частинок.",
        fullDesc: "Інтерфейс, у якому звук та зір нероздільні: голос гіда, гул підземної магми та шум вітру змушують вібрувати контури гір через Web Audio AnalyserNode в режимі реального часу.",
        actionText: "Запустити Звукову Деформацію",
        telemetry: { alt: "850 M", mach: "0.0", target: "SKÓGAFOSS" }
      },
      {
        id: "saga-chronosphere",
        num: "04",
        title: "Хроносфера Саг: Портал Часу (930 → 1783 → 2026)",
        icon: "⏳",
        badge: "Temporal Lens",
        shortDesc: "Часовий слайдер перемикає століття: від сучасних шосе до попелу Лакі 1783 року та хуторів вікінгів доби заселення.",
        fullDesc: "Переміщуючи важіль часу, користувач стирає асфальт і мотелі, бачачи перед собою криваво-червоний туман катастрофи Лакі або драккари та вогнища Альтингу в X столітті.",
        actionText: "Переміститися в 930 рік",
        telemetry: { alt: "115 M", mach: "TIME WARP", target: "ÞINGVELLIR 930 AD" }
      },
      {
        id: "shaman-elements",
        num: "05",
        title: "Шаманський Симулятор Стихій (Live Weather Physics)",
        icon: "❄️",
        badge: "Live Particle Physics",
        shortDesc: "Фізичний рушій заметілі, лавового свічення та рухомих шлейфів Аврори на основі реальних даних метеостанцій.",
        fullDesc: "Якщо у Віку зараз шторм 20 м/с, на вашому екрані миттєво здіймається реальна заметіль із частинками льоду, що заносить дорогу снігом та обмерзає по краях вікна.",
        actionText: "Зімітувати Буран та Аврору",
        telemetry: { alt: "250 M", mach: "WIND 24 M/S", target: "REYNISFJARA" }
      },
      {
        id: "icesar-tactical",
        num: "06",
        title: "Тактичний Центр Пошуку та Рятування (ICE-SAR Grid)",
        icon: "📡",
        badge: "SAR Command Grid",
        shortDesc: "Військово-рятувальна консоль із тепловізійними палітрами FLIR, дронами над розломами та маяками безпеки.",
        fullDesc: "Концепт для тих, хто вимагає граничного професіоналізму: тепловізори розпізнають тріщини в льодовиках, а рятувальні дрони передають відео з ущелин у прямому ефірі.",
        actionText: "Увімкнути Тепловізор FLIR",
        telemetry: { alt: "3,200 M (Drone)", mach: "0.2", target: "VATNAJÖKULL CREVASSE" }
      },
      {
        id: "biome-metamorphism",
        num: "07",
        title: "Біомний Метаморфізм Інтерфейсу (Ice / Basalt / Moss)",
        icon: "💎",
        badge: "Morphing Materials",
        shortDesc: "Кнопки з льоду тріскаються при кліку, обсидіан світиться тріщинами магми, а мох поглинає звук.",
        fullDesc: "Матеріали інтерфейсу живі: при наближенні до льодовиків вікна покриваються памороззю, біля вулканів лава пропікає рамки, а в зелених каньйонах екран дихає парою.",
        actionText: "Змінити Біом Матеріалу",
        telemetry: { alt: "40 M", mach: "0.0", target: "ELDHRAUN MOSS" }
      },
      {
        id: "binaural-telepathy",
        num: "08",
        title: "Бінауральний 3D Аудіо-Купол (Spatial Telepathy)",
        icon: "🎧",
        badge: "Binaural 360°",
        shortDesc: "Повний 360-градусний слуховий простір: поверніть камеру — і шепіт саги лунає з печери зліва, а річка реве праворуч.",
        fullDesc: "Звуковий купол відтворює реальне акустичне середовище печер та базальтових розломів з урахуванням ехолокації та реверберації субарктичного повітря.",
        actionText: "Тестувати Бінауральний 3D Звук",
        telemetry: { alt: "15 M", mach: "0.0", target: "GLJÚFRABÚI CAVE" }
      },
      {
        id: "neuro-viking-holo",
        num: "09",
        title: "Нейро-Голограма Штурмана Кáрі у 3D",
        icon: "🧙‍♂️",
        badge: "3D Hologram Avatar",
        shortDesc: "Жива тривимірна голограма досвідченого вікінга-рейнджера, яка реагує на голос і жести водія.",
        fullDesc: "Замість текстових ботів перед вами стоїть об'ємна проєкція Кáрі у високотехнологічному спорядженні, яка рукою вказує небезпечні ділянки на трасі та дає оперативні поради.",
        actionText: "Викликати Голограму Кáрі",
        telemetry: { alt: "COCKPIT HUD", mach: "ACTIVE", target: "PILOT KÁRI" }
      },
      {
        id: "fpv-drone-flyover",
        num: "10",
        title: "Безконтактний FPV-Дрон Політ крізь Каньйони",
        icon: "⚡",
        badge: "Cinematic FPV",
        shortDesc: "Кінематографічний політ на висоті 2 метрів над водоспадом та крізь арку Дірхолей із фізикою перевантажень.",
        fullDesc: "Режим повного занурення: натисніть одну кнопку, відкиньтеся на спинку крісла і спостерігайте за шаленим прольотом крізь базальтові арки з фізичним креном камери.",
        actionText: "Запустити FPV-Проліт",
        telemetry: { alt: "18 M", mach: "180 KM/H", target: "DYRHÓLAEY ARCH" }
      }
    ];

    let currentConceptIndex = 0;
    let canvasAnimationId = null;
    let audioCtx = null;

    // Web Audio Synthesizer
    function initAudio() {
      if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function playWarpSound() {
      initAudio();
      try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(80, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 1.2);
        osc.frequency.exponentialRampToValueAtTime(110, audioCtx.currentTime + 2.5);
        gain.gain.setValueAtTime(0.01, audioCtx.currentTime);
        gain.gain.linearRampToValueAtTime(0.12, audioCtx.currentTime + 0.8);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 2.5);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 2.5);
      } catch (e) {}
    }

    function playAllFXChime() {
      initAudio();
      try {
        [220, 330, 440, 660, 880].forEach((freq, idx) => {
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, audioCtx.currentTime + idx * 0.12);
          gain.gain.setValueAtTime(0.05, audioCtx.currentTime + idx * 0.12);
          gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + idx * 0.12 + 0.8);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start(audioCtx.currentTime + idx * 0.12);
          osc.stop(audioCtx.currentTime + idx * 0.12 + 0.8);
        });
      } catch (e) {}
    }

    // Canvas Visualizers
    function startCanvasSimulation(conceptId) {
      const canvas = document.getElementById('stage-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      canvas.width = canvas.parentElement.clientWidth;
      canvas.height = canvas.parentElement.clientHeight;

      if (canvasAnimationId) cancelAnimationFrame(canvasAnimationId);

      let step = 0;
      const particles = Array.from({ length: 90 }, () => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        z: Math.random() * canvas.width,
        sz: Math.random() * 2.5 + 1,
        speed: Math.random() * 4 + 2,
        color: Math.random() > 0.5 ? '#00f0ff' : '#10b981'
      }));

      function render() {
        step++;
        ctx.fillStyle = 'rgba(5, 8, 17, 0.25)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Render depending on concept
        if (conceptId === 'orbital-reentry') {
          // Warp stars towards center
          const cx = canvas.width / 2;
          const cy = canvas.height / 2;
          particles.forEach(p => {
            p.z -= p.speed * 2.5;
            if (p.z <= 0) p.z = canvas.width;
            const k = 180 / p.z;
            const px = (p.x - cx) * k + cx;
            const py = (p.y - cy) * k + cy;

            if (px >= 0 && px < canvas.width && py >= 0 && py < canvas.height) {
              const size = Math.max(1, (1 - p.z / canvas.width) * 5);
              ctx.fillStyle = p.color;
              ctx.beginPath();
              ctx.arc(px, py, size, 0, Math.PI * 2);
              ctx.fill();
            }
          });
        } else if (conceptId === 'cyber-cockpit') {
          // HUD grid & targeting reticle
          ctx.strokeStyle = 'rgba(6, 182, 212, 0.4)';
          ctx.lineWidth = 1;
          const cx = canvas.width / 2;
          const cy = canvas.height / 2;

          ctx.beginPath();
          ctx.arc(cx, cy, 90 + Math.sin(step * 0.05) * 8, 0, Math.PI * 2);
          ctx.stroke();

          ctx.beginPath();
          ctx.moveTo(cx - 120, cy); ctx.lineTo(cx + 120, cy);
          ctx.moveTo(cx, cy - 120); ctx.lineTo(cx, cy + 120);
          ctx.stroke();

          ctx.fillStyle = '#06b6d4';
          ctx.font = '10px monospace';
          ctx.fillText(`LOCK: [GULLFOSS GORGE] • AZ: 042° • DIST: 3.4 KM`, cx - 110, cy + 125);
        } else if (conceptId === 'shaman-elements') {
          // Aurora ribbons & blizzard particles
          const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
          grad.addColorStop(0, 'rgba(16, 185, 129, 0.05)');
          grad.addColorStop(0.5, 'rgba(6, 182, 212, 0.2)');
          grad.addColorStop(1, 'rgba(147, 51, 234, 0.1)');
          ctx.fillStyle = grad;

          ctx.beginPath();
          ctx.moveTo(0, canvas.height * 0.4);
          for (let x = 0; x <= canvas.width; x += 40) {
            const y = canvas.height * 0.35 + Math.sin((x + step * 4) * 0.015) * 45;
            ctx.lineTo(x, y);
          }
          ctx.lineTo(canvas.width, canvas.height);
          ctx.lineTo(0, canvas.height);
          ctx.fill();
        } else {
          // Generic glowing particle drift
          particles.forEach(p => {
            p.x += Math.cos(step * 0.02 + p.y) * 1.5;
            p.y += p.speed * 0.5;
            if (p.y > canvas.height) p.y = 0;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.sz, 0, Math.PI * 2);
            ctx.fill();
          });
        }

        canvasAnimationId = requestAnimationFrame(render);
      }

      render();
    }

    function activateConcept(idx) {
      currentConceptIndex = idx;
      const c = CONCEPTS[idx];
      if (!c) return;

      document.getElementById('demo-badge-title').textContent = `${c.num}. ${c.title}`;
      document.getElementById('stage-icon').textContent = c.icon;
      document.getElementById('stage-title').textContent = c.title;
      document.getElementById('stage-desc').textContent = c.fullDesc;
      document.getElementById('btn-demo-action-text').textContent = c.actionText;

      document.getElementById('val-alt').textContent = c.telemetry.alt;
      document.getElementById('val-mach').textContent = c.telemetry.mach;
      document.getElementById('val-target').textContent = c.telemetry.target;

      // Update active cards
      document.querySelectorAll('.concept-card').forEach((el, i) => {
        if (i === idx) {
          el.classList.add('active');
        } else {
          el.classList.remove('active');
        }
      });

      startCanvasSimulation(c.id);
    }

    function triggerActiveDemoAction() {
      const c = CONCEPTS[currentConceptIndex];
      playWarpSound();

      if (c.id === 'orbital-reentry') {
        alert("🚀 Симуляція орбітального спуску активована! Переходимо на 3D карту з гіперстрибком...");
        window.location.href = "index.html?warp=true";
      } else if (c.id === 'biome-metamorphism') {
        const themes = ['theme-glacier', 'theme-obsidian', 'theme-moss'];
        const randomTheme = themes[Math.floor(Math.random() * themes.length)];
        document.body.className = randomTheme + ' text-[#f8fafc] font-sans min-h-screen overflow-x-hidden';
      } else {
        const altElem = document.getElementById('val-alt');
        altElem.textContent = "SYNCHRONIZING...";
        setTimeout(() => {
          altElem.textContent = c.telemetry.alt;
        }, 1200);
      }
    }

    function renderConceptsGrid() {
      const grid = document.getElementById('concepts-grid');
      grid.innerHTML = '';

      CONCEPTS.forEach((c, idx) => {
        const card = document.createElement('div');
        card.className = `concept-card p-5 rounded-2xl cursor-pointer space-y-3 ${idx === 0 ? 'active' : ''}`;
        card.onclick = () => activateConcept(idx);

        card.innerHTML = `
          <div class="flex items-center justify-between gap-2">
            <span class="px-2.5 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[10px] font-bold border border-cyan-500/30">
              КОНЦЕПТ ${c.num} • ${c.badge}
            </span>
            <span class="text-xl">${c.icon}</span>
          </div>

          <h4 class="text-sm font-bold text-white group-hover:text-cyan-300 transition">${c.title}</h4>
          <p class="text-xs text-slate-300 leading-relaxed">${c.shortDesc}</p>

          <div class="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-cyan-400 font-semibold">
            <span>Запустити симуляцію →</span>
            <span class="font-mono text-[10px] text-slate-500">LIVE DEMO</span>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    // INIT
    window.addEventListener('DOMContentLoaded', () => {
      renderConceptsGrid();
      activateConcept(0);
    });

    window.addEventListener('resize', () => {
      startCanvasSimulation(CONCEPTS[currentConceptIndex].id);
    });
  </script>
</body>
</html>
'''

with open(LAB_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created {LAB_PATH} successfully.")
