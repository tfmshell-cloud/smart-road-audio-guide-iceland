# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. ADD CSS FOR CO-PILOT SPEAKING MICRO-ANIMATION
# ---------------------------------------------------------------------------
vocal_css = '''
    /* Co-pilot Speaking Micro-Vocal Pulse Illusion */
    #copilot-video.copilot-speaking {
      filter: contrast(1.05) brightness(1.04) drop-shadow(0 0 16px rgba(6, 182, 212, 0.5));
      animation: vocalPulse 0.18s infinite alternate ease-in-out;
    }
    @keyframes vocalPulse {
      0% { transform: scale(1.0) translateY(0); }
      100% { transform: scale(1.014) translateY(-1px); }
    }
'''

if "#copilot-video.copilot-speaking" not in html:
    html = html.replace("</style>", vocal_css + "\n  </style>", 1)
    print("Added vocalPulse CSS animation.")

# ---------------------------------------------------------------------------
# 2. REPLACE #copilot-modal WITH 9:16 VIDEO AVATAR LAYOUT
# ---------------------------------------------------------------------------
start_idx = html.find('<div id="copilot-modal"')
end_idx = html.find('<!-- MODAL 2: NOTEBOOKLM & AUDIO PRODUCTION STUDIO -->')

if start_idx == -1 or end_idx == -1:
    raise Exception("Could not find copilot modal start or end")

new_copilot_html = '''<div id="copilot-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-2 sm:p-4 md:p-6">
    <div class="glass-panel w-full max-w-7xl lg:w-[94vw] xl:w-[92vw] max-h-[82vh] md:max-h-[72vh] rounded-2xl border border-emerald-500/40 overflow-hidden shadow-2xl flex flex-col bg-slate-950/95 backdrop-blur-2xl">
      <!-- Cockpit Header -->
      <div class="px-5 py-3 border-b border-slate-800 bg-gradient-to-r from-emerald-950/60 via-slate-900 to-slate-900 flex items-center justify-between shrink-0">
        <div class="flex items-center space-x-3">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-500 to-cyan-500 flex items-center justify-center text-lg shadow-lg shadow-emerald-500/25">
            🛡️
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h3 class="text-sm font-bold text-white flex items-center gap-2">
                <span>Штурман-Копілот: Командний Центр Експедиції</span>
                <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono text-[10px] font-bold border border-emerald-500/30">AI RANGER • 9:16 LIVE</span>
              </h3>
            </div>
            <p class="text-[11px] text-slate-400">Синхронізовано з радарами SafeTravel.is • Vegagerðin • Veðurstofa Íslands • NOAA</p>
          </div>
        </div>
        <button onclick="closeCopilotModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm transition">✕</button>
      </div>

      <!-- Cockpit Content: Left 9:16 Video Avatar + Right Telemetry & Interactive Chat -->
      <div class="p-4 md:p-5 overflow-y-auto flex-1 flex flex-col md:flex-row gap-4.5 text-xs">
        
        <!-- LEFT: 9:16 PROPORTIONATE VIDEO AVATAR CARD -->
        <div class="w-full md:w-[280px] lg:w-[310px] shrink-0 flex flex-col">
          <div class="relative w-full aspect-[9/16] max-h-[480px] rounded-2xl overflow-hidden border border-cyan-400/50 shadow-2xl bg-slate-900 flex flex-col justify-between">
            
            <!-- Video Player (Autoplay Loop Muted with Poster Fallback) -->
            <video id="copilot-video" autoplay loop muted playsinline poster="assets/images/viking_copilot.jpg" class="absolute inset-0 w-full h-full object-cover transition-transform duration-300">
              <source src="assets/videos/viking_copilot.mp4" type="video/mp4">
              <img src="assets/images/viking_copilot.jpg" alt="Viking Navigator Kári" class="w-full h-full object-cover">
            </video>

            <!-- Top Overlay: Live Status Pill -->
            <div class="relative z-10 p-3 flex items-center justify-between pointer-events-none">
              <div id="copilot-live-pill" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-950/75 backdrop-blur-md border border-emerald-400/50 text-[10px] text-emerald-300 font-mono shadow-md">
                <span id="copilot-live-dot" class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span id="copilot-status-label" class="font-bold uppercase tracking-wider">НА ЗВ'ЯЗКУ</span>
              </div>
              <span class="px-2 py-0.5 rounded bg-slate-950/70 backdrop-blur-md text-cyan-300 font-mono text-[9px] border border-cyan-400/30">
                9:16 CAM
              </span>
            </div>

            <!-- Center Speaking Visualizer HUD -->
            <div id="copilot-vocal-hud" class="relative z-10 flex-1 flex items-center justify-center pointer-events-none opacity-0 transition-opacity duration-300">
              <div class="p-3.5 rounded-full bg-cyan-500/20 border border-cyan-400/50 backdrop-blur-md animate-pulse shadow-lg shadow-cyan-500/30 flex items-center justify-center">
                <span class="text-2xl">🎙️</span>
              </div>
            </div>

            <!-- Bottom Overlay: Persona Card & Animated Vocal Equalizer -->
            <div class="relative z-10 p-3.5 bg-gradient-to-t from-slate-950 via-slate-950/85 to-transparent space-y-1.5 border-t border-cyan-500/20">
              <div class="flex items-center justify-between">
                <div>
                  <h4 class="text-sm font-black text-white flex items-center gap-1.5">
                    <span>Кáрі (Kári)</span>
                    <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/30 text-cyan-200 font-mono border border-cyan-400/30">LEIÐSÖGUMAÐUR</span>
                  </h4>
                  <p class="text-[10px] text-slate-300 font-medium">Арктичний штурман • 15 років на F-Roads</p>
                </div>
                <button onclick="toggleCopilotMute()" id="btn-copilot-sound-toggle" class="p-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-cyan-300 text-xs border border-slate-700" title="Увімкнути/вимкнути голосові відповіді штурмана">
                  🔊
                </button>
              </div>

              <!-- Animated Voice Wave Bars -->
              <div id="copilot-soundwave-bars" class="flex items-center justify-between pt-1">
                <div class="flex items-end gap-1 h-3.5">
                  <span class="w-1 bg-cyan-400 rounded-full h-2 animate-bounce"></span>
                  <span class="w-1 bg-emerald-400 rounded-full h-3.5 animate-bounce" style="animation-delay: 0.1s"></span>
                  <span class="w-1 bg-cyan-400 rounded-full h-2 animate-bounce" style="animation-delay: 0.2s"></span>
                  <span class="w-1 bg-cyan-400 rounded-full h-3 animate-bounce" style="animation-delay: 0.15s"></span>
                  <span class="w-1 bg-emerald-400 rounded-full h-2 animate-bounce" style="animation-delay: 0.25s"></span>
                </div>
                <span id="copilot-wave-text" class="text-[9px] font-mono text-cyan-300 font-semibold">ГОТОВИЙ ДО ДІАЛОГУ</span>
              </div>
            </div>

          </div>
        </div>

        <!-- RIGHT: MISSION DASHBOARD, MORNING BRIEF & CHAT -->
        <div class="flex-1 flex flex-col justify-between space-y-3.5 min-w-0">
          
          <!-- Row 1: Spoken Morning Briefing Box -->
          <div class="p-3.5 rounded-xl bg-gradient-to-r from-emerald-950/40 via-slate-900 to-slate-900 border border-emerald-500/40 space-y-2">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="font-bold text-white text-xs flex items-center gap-2">
                <span>📻</span> Оперативний ранковий аудіо-бриф Leiðsöguskólinn (45 сек)
              </span>
              <button id="btn-ranger-audio-modal" onclick="playRangerAudio()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-xs flex items-center gap-1.5 shadow-md shadow-emerald-600/30 transition">
                <span>▶</span> <span id="lbl-ranger-btn-modal">Слухати бриф Штурмана</span>
              </button>
            </div>
            <p class="text-slate-300 leading-relaxed text-[11px] italic bg-slate-950/60 p-2.5 rounded-lg border border-slate-800" id="ranger-briefing-text">
              "Góðan daginn! Говорить черговий штурман Кáрі. Сьогодні ідеальний день для поїздки Південним кільцем. Траса 1 вільна (Greiðfært). Увага на мисі Дирхолей: бічний вітер 16 м/с — тримайте двері авто обома руками. На чорному пляжі Рейнісф'яра суворо дотримуйтесь жовтого світлофора безпеки. Увечері заплановано Kp 4.2 з чистим вікном низької хмарності. Безпечної експедиції!"
            </p>
          </div>

          <!-- Row 2: Real-time Telemetry Widgets -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
            <!-- Safety Index Widget -->
            <div class="p-2.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
              <span class="text-[9px] text-slate-400 uppercase font-mono font-bold">ІНДЕКС БЕЗПЕКИ:</span>
              <div class="text-lg font-black text-emerald-400 flex items-center justify-between">
                <span>92 / 100</span>
                <span class="text-[9px] px-1.5 py-0.2 rounded bg-emerald-500/20 text-emerald-300 font-sans font-bold">БЕЗПЕЧНО</span>
              </div>
              <p class="text-[10px] text-slate-400">Траса 1 суха, ожеледиця відсутня.</p>
            </div>

            <!-- Wind & Door Warning Widget -->
            <div class="p-2.5 rounded-xl bg-slate-900/90 border border-amber-500/30 space-y-1">
              <span class="text-[9px] text-amber-400 uppercase font-mono font-bold">⚠️ DOOR DANGER ALERT:</span>
              <div class="text-lg font-black text-amber-300 flex items-center justify-between">
                <span>16.2 м/с</span>
                <span class="text-[9px] px-1.5 py-0.2 rounded bg-amber-500/20 text-amber-300 font-sans font-bold">ВІТЕР</span>
              </div>
              <p class="text-[10px] text-amber-200/80">Дирхолей: тримайте двері обома руками!</p>
            </div>

            <!-- Aurora Radar Widget -->
            <div class="p-2.5 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-1">
              <span class="text-[9px] text-cyan-400 uppercase font-mono font-bold">🌌 АВРОРА СЬОГОДНІ:</span>
              <div class="text-lg font-black text-cyan-300 flex items-center justify-between">
                <span>Kp 4.2</span>
                <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/20 text-cyan-300 font-sans font-bold">АКТИВНА</span>
              </div>
              <p class="text-[10px] text-slate-400">Lágský: 12% (Скоугафосс після 22:00).</p>
            </div>
          </div>

          <!-- Row 3: Interactive Co-Pilot AI Chat & Voice Recital -->
          <div class="p-3.5 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-2.5">
            <div class="flex items-center justify-between">
              <span class="text-[11px] uppercase font-bold text-cyan-300 flex items-center gap-1.5">
                <span>💬</span> ЖИВИЙ ДІАЛОГ ЗІ ШТУРМАНОМ КÁРІ (ГОЛОСОВА ВІДПОВІДЬ)
              </span>
              <span class="text-[10px] text-emerald-400 font-mono font-bold">VOICE ACTIVE</span>
            </div>

            <div class="flex items-center space-x-1.5">
              <input type="text" id="copilot-mini-input" placeholder="Запитайте Кáрі про дорогу, вітер, гейзери чи Аврору..." class="flex-1 px-3 py-2 rounded-xl bg-slate-950 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 transition" onkeydown="if(event.key==='Enter') sendMiniCopilotQuery()">
              <button onclick="sendMiniCopilotQuery()" class="px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold shadow-md shadow-cyan-600/30 transition">
                Запитати
              </button>
            </div>

            <!-- Quick Suggestion Buttons -->
            <div class="flex items-center gap-1.5 text-[10px] overflow-x-auto pb-0.5 scrollbar-none">
              <button onclick="askMiniCopilot('Чи відкрита дорога до Віка?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">🛣️ Дорога до Віка</button>
              <button onclick="askMiniCopilot('Де сьогодні шукати Аврору?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">🌌 Де Аврора?</button>
              <button onclick="askMiniCopilot('Які секретні водоспади поруч?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">💧 Водоспади</button>
              <button onclick="askMiniCopilot('Що з вітром на Рейнісф\\'ярі?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">⚠️ Вітер на пляжі</button>
            </div>

            <!-- Response Box with Live Typography -->
            <div id="copilot-mini-reply" class="hidden p-3 rounded-xl bg-slate-950/90 border border-cyan-500/40 text-[11px] text-slate-200 leading-relaxed shadow-inner">
              <!-- Live response text -->
            </div>
          </div>

        </div>

      </div>

      <!-- Cockpit Footer -->
      <div class="px-5 py-2.5 border-t border-slate-800 bg-slate-950 flex items-center justify-between text-[11px] text-slate-400 shrink-0">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          <span>Штурман Кáрі контролює телеметрію вашого маршруту (115 локацій)</span>
        </div>
        <button onclick="closeCopilotModal()" class="px-4 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition">Закрити панель</button>
      </div>
    </div>
  </div>\n\n  '''

html = html[:start_idx] + new_copilot_html + html[end_idx:]
print("Replaced copilot modal with 9:16 video avatar layout.")

# ---------------------------------------------------------------------------
# 3. UPGRADE COPILOT SPEAKING AND ANIMATION LOGIC IN JAVASCRIPT
# ---------------------------------------------------------------------------
copilot_speaking_js = '''
    // ==========================================
    // CO-PILOT VIDEO AVATAR & VOCAL ANIMATION ENGINE
    // ==========================================
    let isCopilotMuted = false;

    function setCopilotSpeakingState(isSpeaking, customText = '') {
      const vid = document.getElementById('copilot-video');
      const hud = document.getElementById('copilot-vocal-hud');
      const dot = document.getElementById('copilot-live-dot');
      const label = document.getElementById('copilot-status-label');
      const waveText = document.getElementById('copilot-wave-text');

      if (isSpeaking) {
        if (vid) {
          vid.classList.add('copilot-speaking');
          vid.playbackRate = 1.15;
          if (vid.paused) vid.play().catch(() => {});
        }
        if (hud) hud.style.opacity = '1';
        if (dot) dot.className = 'w-2 h-2 rounded-full bg-cyan-400 animate-ping';
        if (label) {
          label.textContent = 'ШТУРМАН ПРОМОВЛЯЄ';
          label.className = 'font-bold uppercase tracking-wider text-cyan-300';
        }
        if (waveText) waveText.textContent = 'ГОЛОСОВА ВІДПОВІДЬ...';
      } else {
        if (vid) {
          vid.classList.remove('copilot-speaking');
          vid.playbackRate = 0.9;
        }
        if (hud) hud.style.opacity = '0';
        if (dot) dot.className = 'w-2 h-2 rounded-full bg-emerald-400 animate-ping';
        if (label) {
          label.textContent = 'НА ЗВ\\'ЯЗКУ';
          label.className = 'font-bold uppercase tracking-wider text-emerald-300';
        }
        if (waveText) waveText.textContent = 'ГОТОВИЙ ДО ДІАЛОГУ';
      }
    }

    function toggleCopilotMute() {
      isCopilotMuted = !isCopilotMuted;
      const btn = document.getElementById('btn-copilot-sound-toggle');
      if (btn) btn.textContent = isCopilotMuted ? '🔇' : '🔊';
      if (isCopilotMuted && 'speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        setCopilotSpeakingState(false);
      }
    }

    function speakCopilot(text) {
      if (isCopilotMuted) return;

      // Play tactical radio chirp
      try {
        initWebAudio();
        if (webAudioCtx) {
          const osc = webAudioCtx.createOscillator();
          const gain = webAudioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(580, webAudioCtx.currentTime);
          osc.frequency.setValueAtTime(880, webAudioCtx.currentTime + 0.05);
          gain.gain.setValueAtTime(0.04, webAudioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, webAudioCtx.currentTime + 0.12);
          osc.connect(gain);
          gain.connect(webAudioCtx.destination);
          osc.start();
          osc.stop(webAudioCtx.currentTime + 0.12);
        }
      } catch (e) {}

      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const u = new SpeechSynthesisUtterance(text);
        
        // Voice matching
        const voices = window.speechSynthesis.getVoices();
        const ukVoice = voices.find(v => v.lang.toLowerCase().includes('uk') || v.lang.toLowerCase().includes('ua'));
        if (currentLang === 'uk' && ukVoice) {
          u.voice = ukVoice;
          u.lang = ukVoice.lang;
        } else {
          u.lang = currentLang === 'uk' ? 'uk-UA' : 'en-US';
        }

        u.rate = 1.05;
        u.pitch = 0.95; // Confident, grounded ranger tone

        u.onstart = () => {
          setCopilotSpeakingState(true);
        };
        u.onend = () => {
          setCopilotSpeakingState(false);
        };
        u.onerror = () => {
          setCopilotSpeakingState(false);
        };

        window.speechSynthesis.speak(u);
      }
    }
'''

if "function setCopilotSpeakingState(" not in html:
    html = html.replace("function sendMiniCopilotQuery() {", copilot_speaking_js + "\n    function sendMiniCopilotQuery() {", 1)
    print("Injected copilot speaking animation functions.")

# Upgrade sendMiniCopilotQuery to speak aloud and animate the video
old_send_query = '''    function sendMiniCopilotQuery() {
      const inp = document.getElementById('copilot-mini-input');
      const q = inp.value.trim();
      if (!q) return;

      const replyEl = document.getElementById('copilot-mini-reply');
      replyEl.classList.remove('hidden');
      replyEl.innerHTML = `<span class="text-cyan-400 animate-pulse">Думаю...</span>`;

      setTimeout(() => {
        replyEl.innerHTML = generateCopilotAnswer(q);
        inp.value = '';
      }, 350);
    }'''

new_send_query = '''    function sendMiniCopilotQuery() {
      const inp = document.getElementById('copilot-mini-input');
      const q = inp.value.trim();
      if (!q) return;

      const replyEl = document.getElementById('copilot-mini-reply');
      replyEl.classList.remove('hidden');
      replyEl.innerHTML = `<span class="text-cyan-400 animate-pulse font-mono">Штурман Кáрі аналізує дані SafeTravel...</span>`;

      setTimeout(() => {
        const rawAnswer = generateCopilotAnswer(q);
        replyEl.innerHTML = rawAnswer;
        inp.value = '';

        // Strip HTML tags for clean speech recital
        const plainText = rawAnswer.replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
        speakCopilot(plainText);
      }, 400);
    }'''

if old_send_query in html:
    html = html.replace(old_send_query, new_send_query, 1)
    print("Upgraded sendMiniCopilotQuery with vocal speech recital and video animation.")

# Upgrade playRangerAudio to trigger speaking state on the video
old_ranger_audio = '''    function playRangerAudio() {
      if (isRangerPlaying) {
        stopAudio();
        return;
      }

      stopAudio();

      const text = "Доброго ранку! Це оперативний бриф Штурмана Ісландії. За даними Ведурштофа та Сафетревел, індекс безпеки сьогодні дев'яносто два зі ста. Траса номер один навколо острова повністю відкрита. Увага на південному узбережжі біля мису Дирхолей: пориви вітру досягають шістнадцяти метрів на секунду. Обов'язково тримайте двері автомобіля обома руками при виході. Прогноз Аврори сприятливий: планетарний індекс Kp чотири цілих дві десятих. Чисте небо очікується в районі озера Міватн та Скоугафосса після двадцять другої години.";

      const u = new SpeechSynthesisUtterance(text);
      u.lang = currentLang === 'uk' ? 'uk-UA' : 'en-US';
      u.rate = 1.0;

      u.onstart = () => {
        isRangerPlaying = true;
        const btn = document.getElementById('btn-ranger-audio-mini');
        if (btn) btn.innerHTML = '<span>⏹ Зупинити бриф</span>';
        const btnM = document.getElementById('btn-ranger-audio-modal');
        if (btnM) btnM.innerHTML = '<span>⏹ Зупинити бриф</span>';
      };
      u.onend = () => {
        stopAudio();
      };
    }'''

new_ranger_audio = '''    function playRangerAudio() {
      if (isRangerPlaying) {
        stopAudio();
        setCopilotSpeakingState(false);
        return;
      }

      stopAudio();

      const text = "Доброго ранку! Говорить черговий штурман Кáрі. За даними Ведурштофа та Сафетревел, індекс безпеки сьогодні дев'яносто два зі ста. Траса номер один навколо острова повністю відкрита. Увага на південному узбережжі біля мису Дирхолей: пориви вітру досягають шістнадцяти метрів на секунду. Обов'язково тримайте двері автомобіля обома руками при виході. Прогноз Аврори сприятливий: планетарний індекс Kp чотири цілих дві десятих. Чисте небо очікується в районі озера Міватн та Скоугафосса після двадцять другої години.";

      const u = new SpeechSynthesisUtterance(text);
      const voices = window.speechSynthesis.getVoices();
      const ukVoice = voices.find(v => v.lang.toLowerCase().includes('uk') || v.lang.toLowerCase().includes('ua'));
      if (currentLang === 'uk' && ukVoice) {
        u.voice = ukVoice;
        u.lang = ukVoice.lang;
      } else {
        u.lang = currentLang === 'uk' ? 'uk-UA' : 'en-US';
      }
      u.rate = 1.0;
      u.pitch = 0.95;

      u.onstart = () => {
        isRangerPlaying = true;
        setCopilotSpeakingState(true);
        const btn = document.getElementById('btn-ranger-audio-mini');
        if (btn) btn.innerHTML = '<span>⏹ Зупинити бриф</span>';
        const btnM = document.getElementById('btn-ranger-audio-modal');
        if (btnM) btnM.innerHTML = '<span>⏹ Зупинити бриф</span>';
      };
      u.onend = () => {
        stopAudio();
        setCopilotSpeakingState(false);
      };
      u.onerror = () => {
        stopAudio();
        setCopilotSpeakingState(false);
      };

      window.speechSynthesis.speak(u);
    }'''

if old_ranger_audio in html:
    html = html.replace(old_ranger_audio, new_ranger_audio, 1)
    print("Upgraded playRangerAudio with video avatar speech synchronization.")

# Also ensure video plays smoothly when opening copilot modal
old_open_copilot = '''    function openCopilotModal() {
      const m = document.getElementById('copilot-modal');
      if (m) m.classList.remove('hidden');
    }'''

new_open_copilot = '''    function openCopilotModal() {
      const m = document.getElementById('copilot-modal');
      if (m) {
        m.classList.remove('hidden');
        const vid = document.getElementById('copilot-video');
        if (vid) {
          vid.playbackRate = 0.9;
          vid.play().catch(() => {});
        }
      }
    }'''

if old_open_copilot in html:
    html = html.replace(old_open_copilot, new_open_copilot, 1)
    print("Upgraded openCopilotModal to trigger video autoplay.")

# Export window functions
if "window.toggleCopilotMute = toggleCopilotMute;" not in html:
    html = html.replace("window.setNavMode = setNavMode;", "window.toggleCopilotMute = toggleCopilotMute;\n    window.setCopilotSpeakingState = setCopilotSpeakingState;\n    window.setNavMode = setNavMode;", 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully.")
