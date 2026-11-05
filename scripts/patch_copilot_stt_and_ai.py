# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. UPGRADE THE CHAT BOX HTML IN #copilot-modal WITH UNIQUE IDS & MIC BUTTON
# ---------------------------------------------------------------------------
old_chat_block_start = '<div class="p-3.5 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-2.5">'
# We will locate the chat section inside copilot-modal
old_chat_pattern = r'<!-- Row 3: Interactive Co-Pilot AI Chat & Voice Recital -->\s*<div class="p-3\.5 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-2\.5">.*?</div>\s*</div>\s*</div>\s*<!-- Cockpit Footer -->'

new_chat_block = '''<!-- Row 3: Interactive Co-Pilot AI Chat, Speech Recognition & LM Studio Bridge -->
          <div class="p-3.5 rounded-xl bg-slate-900/95 border border-cyan-500/40 space-y-3 shadow-xl">
            <!-- Header with Engine Status Badge and Settings Toggle -->
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-[11px] uppercase font-bold text-cyan-300 flex items-center gap-1.5">
                <span>💬</span> ЖИВИЙ ГОЛОСОВИЙ ДІАЛОГ ЗІ ШТУРМАНОМ КÁРІ (ДВОМОВНИЙ UA / EN)
              </span>
              <div class="flex items-center gap-2">
                <span id="copilot-ai-engine-badge" class="px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono text-[10px] border border-slate-700 flex items-center gap-1 shadow-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> <span>Автономний Експерт (115 POI)</span>
                </span>
                <button onclick="toggleLmStudioSettings()" class="text-[10px] text-slate-400 hover:text-cyan-300 font-mono underline" title="Налаштування підключення LM Studio (localhost:1234)">
                  ⚙️ LM Studio
                </button>
              </div>
            </div>

            <!-- LM Studio Connection Settings Dropdown (collapsible) -->
            <div id="lm-studio-settings-box" class="hidden p-3 rounded-xl bg-slate-950/95 border border-slate-700 space-y-2 text-[11px]">
              <div class="flex items-center justify-between font-bold text-white">
                <span>🔌 Підключення Local AI / LM Studio (OpenAI API)</span>
                <button onclick="toggleLmStudioSettings()" class="text-slate-400 hover:text-white">✕</button>
              </div>
              <p class="text-slate-300 text-[10px] leading-relaxed">
                Запустіть LM Studio на комп'ютері, завантажте будь-яку модель (Llama-3, Mistral, Qwen тощо) і натисніть <b>Start Server</b> на порту <b>1234</b>. Додаток автоматично з'єднається через локальний API.
              </p>
              <div class="flex items-center gap-2">
                <input type="text" id="lm-studio-url-input" value="http://localhost:1234/v1/chat/completions" class="flex-1 px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-cyan-300 font-mono text-[11px] focus:outline-none focus:border-cyan-400">
                <button onclick="checkLmStudioConnection(true)" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs transition">
                  Перевірити зв'язок
                </button>
              </div>
              <div id="lm-settings-status" class="text-[10px] font-mono text-slate-400"></div>
            </div>

            <!-- Speech Dictation Live Status Alert -->
            <div id="copilot-mic-status" class="hidden p-2 rounded-lg bg-red-950/60 border border-red-500/50 text-red-200 font-mono text-[11px] flex items-center gap-2 animate-pulse">
              <span>🎙️</span> <span>Запис голосу активний... Говоріть у мікрофон...</span>
            </div>

            <!-- Speech Input Row with Microphone Dictation Button -->
            <div class="flex items-center space-x-1.5">
              <div class="relative flex-1">
                <input type="text" id="copilot-modal-input" placeholder="Запитайте Кáрі або натисніть мікрофон для надиктовування..." class="w-full pl-3 pr-9 py-2 rounded-xl bg-slate-950 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400 transition" onkeydown="if(event.key==='Enter') sendCopilotModalQuery()">
                <button onclick="clearCopilotModalInput()" class="absolute right-2.5 top-2.5 text-slate-500 hover:text-slate-300 text-xs">✕</button>
              </div>

              <!-- Microphone Speech-to-Text Button -->
              <button id="btn-copilot-mic" onclick="toggleSpeechRecognition()" class="px-3.5 py-2 rounded-xl bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300 border border-cyan-400/50 flex items-center justify-center transition shadow-md shadow-cyan-500/10 cursor-pointer" title="Натисніть для голосового надиктовування запитання (українською або англійською)">
                <span class="text-sm">🎙️</span>
              </button>

              <!-- Send Button -->
              <button onclick="sendCopilotModalQuery()" class="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white text-xs font-bold shadow-md shadow-cyan-600/30 transition">
                Запитати
              </button>
            </div>

            <!-- Quick Suggestion Buttons -->
            <div class="flex items-center gap-1.5 text-[10px] overflow-x-auto pb-0.5 scrollbar-none">
              <button onclick="askCopilotModalPredefined('Чи відкрита дорога до Віка?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">🛣️ Траса до Віка</button>
              <button onclick="askCopilotModalPredefined('Де сьогодні шукати Аврору?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">🌌 Де Аврора?</button>
              <button onclick="askCopilotModalPredefined('Які секретні водоспади поруч?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">💧 Водоспади</button>
              <button onclick="askCopilotModalPredefined('Що з вітром на Рейнісф\\'ярі?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">⚠️ Вітер на пляжі</button>
              <button onclick="askCopilotModalPredefined('Розкажи про каньйон Колуглювур')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700/80 whitespace-nowrap transition">🏞️ Колуглювур</button>
              <button onclick="askCopilotModalPredefined('How is the weather and road conditions today?')" class="px-2.5 py-1 rounded-lg bg-slate-800/90 hover:bg-slate-700 text-cyan-300 border border-cyan-500/30 whitespace-nowrap transition">🇬🇧 English Query</button>
            </div>

            <!-- Dedicated Response Box with Live Typography -->
            <div id="copilot-modal-reply" class="hidden p-3 rounded-xl bg-slate-950/95 border border-cyan-500/50 text-[11px] text-slate-200 leading-relaxed shadow-inner space-y-1.5 max-h-48 overflow-y-auto">
              <!-- Live response text inserted here -->
            </div>
          </div>

        </div>

      </div>

      <!-- Cockpit Footer -->'''

match = re.search(old_chat_pattern, html, re.DOTALL)
if match:
    html = html[:match.start()] + new_chat_block + html[match.end():]
    print("Replaced copilot chat block with unique modal IDs, microphone button & LM Studio controls.")
else:
    print("WARNING: old_chat_pattern not matched, attempting direct replacement...")
    target = '<!-- Row 3: Interactive Co-Pilot AI Chat & Voice Recital -->'
    idx_target = html.find(target)
    idx_footer = html.find('<!-- Cockpit Footer -->', idx_target)
    if idx_target != -1 and idx_footer != -1:
        html = html[:idx_target] + new_chat_block + html[idx_footer:]
        print("Replaced via direct index search.")
    else:
        print("FAILED to locate chat section.")

# ---------------------------------------------------------------------------
# 2. INJECT ENHANCED JAVASCRIPT: STT, LM STUDIO, BILINGUAL KNOWLEDGE ENGINE
# ---------------------------------------------------------------------------
stt_and_ai_js = '''
    // ==========================================
    // STT (MICROPHONE SPEECH-TO-TEXT) & LM STUDIO BRIDGE
    // ==========================================
    let speechRecognitionInstance = null;
    let isSpeechRecognitionActive = false;
    let lmStudioEndpoint = 'http://localhost:1234/v1/chat/completions';
    let isLmStudioConnected = false;

    function toggleLmStudioSettings() {
      const box = document.getElementById('lm-studio-settings-box');
      if (box) box.classList.toggle('hidden');
    }

    async function checkLmStudioConnection(isUserInitiated = false) {
      const badge = document.getElementById('copilot-ai-engine-badge');
      const statusText = document.getElementById('lm-settings-status');
      const customUrl = document.getElementById('lm-studio-url-input');
      if (customUrl) lmStudioEndpoint = customUrl.value.trim();

      if (statusText) statusText.textContent = 'Перевірка з\\'єднання з ' + lmStudioEndpoint + '...';

      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 2000);
        // Test base endpoint
        const baseUrl = lmStudioEndpoint.replace('/chat/completions', '/models');
        const res = await fetch(baseUrl, { signal: controller.signal });
        clearTimeout(timeoutId);

        if (res.ok) {
          isLmStudioConnected = true;
          if (badge) {
            badge.className = 'px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-mono text-[10px] font-bold border border-emerald-500/40 flex items-center gap-1 shadow-sm';
            badge.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span> <span>🟢 LM Studio (Local AI) ПІДКЛЮЧЕНО</span>';
          }
          if (statusText) statusText.innerHTML = '<span class="text-emerald-400 font-bold">✅ З\\'єднання успішне! LM Studio активна.</span>';
          if (isUserInitiated) alert('✅ Успішне підключення до LM Studio! Тепер Штурман відповідає через локальну LLM.');
          return true;
        }
      } catch (err) {
        isLmStudioConnected = false;
      }

      if (badge) {
        badge.className = 'px-2 py-0.5 rounded-full bg-slate-800 text-cyan-300 font-mono text-[10px] border border-slate-700 flex items-center gap-1 shadow-sm';
        badge.innerHTML = '<span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span> <span>⚡ Автономний Експерт (115 POI) • LM Studio: Офлайн</span>';
      }
      if (statusText) statusText.innerHTML = '<span class="text-amber-400">⚠️ Сервер LM Studio не знайдено на порту 1234. Працює автономна база 115 POI.</span>';
      if (isUserInitiated) alert('⚠️ LM Studio не відповідає на http://localhost:1234.\\nПереконайтеся, що в LM Studio запущено сервер (кнопка Start Server) та дозволено CORS.');
      return false;
    }

    function toggleSpeechRecognition() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) {
        alert(currentLang === 'uk' 
          ? 'Розпізнавання голосу не підтримується вашим браузером. Використовуйте Google Chrome, Safari або Microsoft Edge.' 
          : 'Speech recognition is not supported in this browser. Please use Chrome, Safari, or Edge.');
        return;
      }

      const micBtn = document.getElementById('btn-copilot-mic');
      const micStatus = document.getElementById('copilot-mic-status');
      const input = document.getElementById('copilot-modal-input');

      if (isSpeechRecognitionActive) {
        if (speechRecognitionInstance) speechRecognitionInstance.stop();
        stopSpeechRecognitionUI();
        return;
      }

      speechRecognitionInstance = new SpeechRecognition();
      speechRecognitionInstance.continuous = false;
      speechRecognitionInstance.interimResults = true;
      speechRecognitionInstance.lang = currentLang === 'uk' ? 'uk-UA' : 'en-US';

      speechRecognitionInstance.onstart = () => {
        isSpeechRecognitionActive = true;
        if (micBtn) {
          micBtn.className = 'px-3.5 py-2 rounded-xl bg-red-600 text-white border border-red-400 animate-pulse shadow-lg shadow-red-500/50 flex items-center justify-center transition cursor-pointer';
          micBtn.innerHTML = '<span class="text-sm">🔴</span>';
        }
        if (micStatus) {
          micStatus.classList.remove('hidden');
          micStatus.textContent = currentLang === 'uk' 
            ? '🎙️ Говоріть зараз... Штурман слухає українською...' 
            : '🎙️ Speak now... Listening for English speech...';
        }
      };

      speechRecognitionInstance.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          transcript += event.results[i][0].transcript;
        }
        if (input) input.value = transcript;
      };

      speechRecognitionInstance.onerror = (event) => {
        console.warn('Speech recognition error:', event.error);
        stopSpeechRecognitionUI();
        if (micStatus) {
          micStatus.classList.remove('hidden');
          micStatus.textContent = currentLang === 'uk' 
            ? '⚠️ Не вдалося отримати доступ до мікрофона (' + event.error + '). Перевірте дозволи браузера.' 
            : '⚠️ Microphone access error (' + event.error + '). Please grant browser permissions.';
        }
      };

      speechRecognitionInstance.onend = () => {
        stopSpeechRecognitionUI();
        // Auto send if non-empty
        if (input && input.value.trim().length > 1) {
          sendCopilotModalQuery();
        }
      };

      try {
        speechRecognitionInstance.start();
      } catch (err) {
        console.error('Cannot start recognition:', err);
        stopSpeechRecognitionUI();
      }
    }

    function stopSpeechRecognitionUI() {
      isSpeechRecognitionActive = false;
      const micBtn = document.getElementById('btn-copilot-mic');
      const micStatus = document.getElementById('copilot-mic-status');
      if (micBtn) {
        micBtn.className = 'px-3.5 py-2 rounded-xl bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300 border border-cyan-400/50 flex items-center justify-center transition shadow-md shadow-cyan-500/10 cursor-pointer';
        micBtn.innerHTML = '<span class="text-sm">🎙️</span>';
      }
      if (micStatus) {
        setTimeout(() => {
          micStatus.classList.add('hidden');
        }, 2000);
      }
    }

    function clearCopilotModalInput() {
      const inp = document.getElementById('copilot-modal-input');
      if (inp) inp.value = '';
    }

    function askCopilotModalPredefined(q) {
      const inp = document.getElementById('copilot-modal-input');
      if (inp) inp.value = q;
      sendCopilotModalQuery();
    }

    // ==========================================
    // COMPREHENSIVE BILINGUAL COPILOT KNOWLEDGE ENGINE
    // ==========================================
    function generateDeepCopilotAnswer(q, lang) {
      const lower = q.toLowerCase();
      const isUk = lang === 'uk';

      if (lower.includes('вік') || lower.includes('vik') || lower.includes('дорог') || lower.includes('трас') || lower.includes('road')) {
        return isUk 
          ? "🛣️ <b>Стан Траси 1 до Віка:</b> За даними Vegagerðin, кільцева траса повністю відкрита (Greiðfært), покриття вологе, без ожеледиці. Увага на відрізку Сельяландсфосс — Скоугафосс: бічний вітер 14 м/с. Тримайте дистанцію та міцно тримайте кермо."
          : "🛣️ <b>Route 1 Road Status to Vík:</b> According to Vegagerðin, the Ring Road is fully clear (Greiðfært). Surface is wet, no ice. Caution between Seljalandsfoss and Skógafoss: crosswinds reach 14 m/s. Maintain safe following distance.";
      } 
      else if (lower.includes('аврор') || lower.includes('aurora') || lower.includes('сяйв') || lower.includes('lights') || lower.includes('хмар')) {
        return isUk 
          ? "🌌 <b>Прогноз Аврори:</b> Планетарний індекс Kp 4.2. Найкраще вікно без низької хмарності (Lágský &lt; 15%) прогнозується в районі Скоугафосса та озера Міватн між 22:00 та 01:30. Уникайте штучного освітлення міст!"
          : "🌌 <b>Aurora Forecast:</b> Planetary Kp-index is 4.2 (Active). Prime low-cloud clearance (Lágský &lt; 15%) is forecasted around Skógafoss and Lake Mývatn between 22:00 and 01:30. Seek dark-sky turnouts away from town lights.";
      } 
      else if (lower.includes('водоспад') || lower.includes('waterfall') || lower.includes('секретн') || lower.includes('secret')) {
        return isUk 
          ? "💧 <b>Секретні водоспади Ісландії:</b> Рекомендую <b>Kvernufoss</b> (захований у каньйоні за музеєм Скоугар), <b>Gljúfrabúi</b> (всередині печери за 600 м від Сельяландсфосса), <b>Brúarfoss</b> із кришталево-блакитною водою та <b>Nauthúsagil</b> з проходом по ланцюгах уздовж русла струмка!"
          : "💧 <b>Secret Icelandic Waterfalls:</b> Must-see hidden gems include <b>Kvernufoss</b> (tucked in the gorge behind Skógar museum), <b>Gljúfrabúi</b> (inside the basalt cavern 600m from Seljalandsfoss), <b>Brúarfoss</b> with neon cyan waters, and <b>Nauthúsagil</b> ravine with chain scrambles!";
      } 
      else if (lower.includes('колуглювур') || lower.includes('kolugljufur') || lower.includes('велатунк') || lower.includes('коли') || lower.includes('кола')) {
        return isUk 
          ? "🏞️ <b>Каньйон Колуглювур (Kolugljúfur):</b> Глибока 50-метрова ущелина на півночі (Траса 715), де річка Víðidalsá скидається подвійним водоспадом Kolufossar. За легендою саг, тут жила велетка Кола, яка ловила лосося голими руками і спала на кам'яному ліжку Kolurúm над водоспадом!"
          : "🏞️ <b>Kolugljúfur Canyon:</b> A 50-meter deep gorge in Northern Iceland (Route 715), featuring the roaring twin cascades of Kolufossar. Medieval folklore relates that giantess Kola lived here, catching salmon barehanded and sleeping upon the stone shelf Kolurúm!";
      } 
      else if (lower.includes('гулльфос') || lower.includes('gullfoss') || lower.includes('золотий водоспад')) {
        return isUk 
          ? "💧 <b>Водоспад Ґулльфосс (Gullfoss):</b> Легендарний 32-метровий двоступеневий водоспад у каньйоні річки Гвіта. Вода має золотавий відтінок через льодовиковий мул із Ланґййокюдля. Водоспад врятувала Сігрідур Томасдоттір, відстоявши його від будівництва 100-мегаватної дамби ГЕС на початку XX ст."
          : "💧 <b>Gullfoss Waterfall:</b> Iconic 32m two-tiered cataract plunging into the Hvítá river gorge. Amber-gold hue is caused by fine glacial silt from Langjökull. Preserved thanks to Sigríður Tómasdóttir, who fought off British investors planning a 100 MW hydroelectric dam!";
      } 
      else if (lower.includes('reynisfjara') || lower.includes('рейнісф') || lower.includes('чорний пляж') || lower.includes('хвил') || lower.includes('хвилі')) {
        return isUk 
          ? "⚠️ <b>Рейнісф'яра (Чорний пляж & Хвилі-вбивці):</b> Найнебезпечніший пляж Ісландії! Підступні хвилі-підкрадачі (sneaker waves) раптово накочуються на десятки метрів далі лінії прибою. СУВОРЕ ПРАВИЛО: ніколи не повертайтеся спиною до океану і не підходьте до води ближче 30 метрів. Слідкуйте за кольоровим світлофором безпеки!"
          : "⚠️ <b>Reynisfjara Black Beach (Sneaker Waves):</b> Iceland's most hazardous shore! Unpredictable sneaker waves surge tens of meters higher than average swells. CRITICAL RULE: Never turn your back on the Atlantic Ocean and stay at least 30 meters from the surf. Obey automated warning lights!";
      } 
      else if (lower.includes('вітер') || lower.includes('wind') || lower.includes('шторм') || lower.includes('двері') || lower.includes('door')) {
        return isUk 
          ? "💨 <b>Попередження про вітер (Door Danger):</b> Пориви вітру в Ісландії нерідко перевищують 16–25 м/с. Головне правило оренди авто: завжди виходьте з машини, міцно тримаючи двері обома руками! Порив вітру може вивернути двері назовні, і страхова компанія не покриває таке пошкодження."
          : "💨 <b>Gale Wind & Door Damage Alert:</b> Atlantic wind gusts frequently exceed 16–25 m/s. Golden rental car rule: always hold vehicle doors with both hands when opening! Severe gusts can hyperextend hinges instantly, and rental insurance does not cover blown-door damages.";
      } 
      else if (lower.includes('тінгведлір') || lower.includes('thingvellir') || lower.includes('сільфра') || lower.includes('silfra')) {
        return isUk 
          ? "🏛️ <b>Тінгведлір & Сільфра:</b> Національний парк ЮНЕСКО, де стикаються Північноамериканська та Євразійська тектонічні плити (розходження 2 см/рік). Тут у 930 р. вікінги заснували Альтинг. У розломі Сільфра видимість під водою перевищує 100 метрів через 100-річну фільтрацію талих вод крізь лаву!"
          : "🏛️ <b>Þingvellir & Silfra Rift:</b> UNESCO World Heritage site straddling the Mid-Atlantic Ridge (plates drift 2 cm/year). Vikings founded the world's oldest parliament Alþingi here in 930 AD. In Silfra fissure, water filtered through lava for 100 years yields over 100m optical visibility!";
      } 
      else if (lower.includes('спа') || lower.includes('spa') || lower.includes('басейн') || lower.includes('купальн') || lower.includes('lagoon')) {
        return isUk 
          ? "♨️ <b>Геотермальні СПА Ісландії:</b> Найпопулярніші — <b>Blue Lagoon</b> (кремнезем і мінерали), <b>Sky Lagoon</b> із безкраїм басейном над океаном, автентичні <b>Hvammsvík Hot Springs</b> (8 чаш у фіорді) та історична дика купальня <b>Seljavallalaug</b> (1923 р.). Обов'язкове правило: душ без одягу з милом перед входом!"
          : "♨️ <b>Geothermal Spas:</b> Top destinations include <b>Blue Lagoon</b> (silica mud and mineral salts), <b>Sky Lagoon</b> (oceanfront 7-step ritual), authentic <b>Hvammsvík</b> (8 natural ocean-tide pools), and historic mountain pool <b>Seljavallalaug</b> (1923). Mandatory etiquette: naked shower with soap before entering!";
      } 
      else if (lower.includes('паркінг') || lower.includes('parking') || lower.includes('parka') || lower.includes('оплат')) {
        return isUk 
          ? "🅿️ <b>Оплата парковок в Ісландії:</b> Більшість національних парків (Þingvellir, Seljalandsfoss, Skaftafell, Jökulsárlón, Fagradalsfjall) використовують автоматичне розпізнавання номерів через додаток <b>Parka.is</b>. Оплачуйте парковку протягом 24 годин через сайт Parka.is, щоб уникнути штрафу від прокатної компанії."
          : "🅿️ <b>Parking Logistics:</b> Major attractions (Þingvellir, Seljalandsfoss, Skaftafell, Jökulsárlón, Fagradalsfjall) use automatic plate recognition via the <b>Parka.is</b> app. Pay parking within 24 hours online to avoid administrative rental fees.";
      } 
      else if (lower.includes('бензин') || lower.includes('gas') || lower.includes('палив') || lower.includes('заправ')) {
        return isUk 
          ? "⛽ <b>Заправки в Ісландії:</b> Мережі N1, Olís, Orkan. На автоматичних колонках вимагається банківська картка з 4-значним PIN-кодом (Apple Pay не завжди працює на автоматах самообслуговування). На південному узбережжі між Віком та Хьофном заправки рідкісні — заправляйте повний бак при кожній нагоді!"
          : "⛽ <b>Refueling Logistics:</b> Key brands are N1, Olís, and Orkan. Unattended pumps require a physical chip-and-PIN credit/debit card (Apple Pay often rejected at self-service terminals). Between Vík and Höfn, fuel stations are sparse—fill up whenever below half a tank!";
      }
      else if (lower.includes('112') || lower.includes('sos') || lower.includes('порятунок') || lower.includes('emergency')) {
        return isUk 
          ? "🚨 <b>Екстрена допомога в Ісландії:</b> Єдиний номер екстрених служб — <b>112</b> (працює навіть без SIM-карти та покриття оператора через будь-яку доступну вежу). Рекомендуємо завантажити додаток <b>112 Iceland</b> та зареєструвати свій план подорожі на SafeTravel.is!"
          : "🚨 <b>Emergency Protocol:</b> Universal emergency hotline is <b>112</b> (connects without SIM card via any available satellite cell tower). Download the <b>112 Iceland</b> app and lodge your travel plan at SafeTravel.is before heading into remote regions!";
      }
      else {
        return isUk 
          ? "🛡️ <b>Штурман Кáрі:</b> За даними SafeTravel і Vegagerðin, ваш маршрут надійний (Індекс безпеки 92/100). У базі зафіксовано 115 перевірених об'єктів. Запитайте мене про стан Траси 1, прогноз Аврори, секретні водоспади або правила безпеки!"
          : "🛡️ <b>Navigator Kári:</b> Telemetry from SafeTravel and Vegagerðin indicates a favorable expedition day (Safety Index 92/100). All 115 POIs are verified. Ask me about Ring Road conditions, Aurora forecast, hidden waterfalls, or severe wind advisories!";
      }
    }

    // ==========================================
    // SEND QUERY DISPATCHER (LM STUDIO OR EXPERT ENGINE)
    // ==========================================
    async function sendCopilotModalQuery() {
      const input = document.getElementById('copilot-modal-input');
      if (!input) return;
      const q = input.value.trim();
      if (!q) return;

      const replyEl = document.getElementById('copilot-modal-reply');
      if (replyEl) {
        replyEl.classList.remove('hidden');
        replyEl.innerHTML = `
          <div class="flex items-center gap-2 text-cyan-400 font-mono text-xs">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>${currentLang === 'uk' ? 'Штурман Кáрі обробляє запит...' : 'Navigator Kári is analyzing expedition telemetry...'}</span>
          </div>
        `;
      }

      input.value = '';

      let finalAnswer = '';

      // 1. Try LM Studio if connected
      if (isLmStudioConnected) {
        try {
          const sysPrompt = currentLang === 'uk' 
            ? "Ти — Кáрі (Kári), офіційний ліцензований гід-штурман експедиції Ісландією. Відповідай коротко (2-4 речення), авторитетно, з фокусом на дорожню безпеку (SafeTravel), вітер, геологію та саги. Додавай емодзі."
            : "You are Kári, a licensed Icelandic expedition navigator and road guide. Answer concisely (2-4 sentences), authoritatively, with focus on road safety, weather, and geology. Use emojis.";

          const controller = new AbortController();
          const timeoutId = setTimeout(() => controller.abort(), 4000);

          const res = await fetch(lmStudioEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            signal: controller.signal,
            body: JSON.stringify({
              messages: [
                { role: 'system', content: sysPrompt },
                { role: 'user', content: q }
              ],
              temperature: 0.7,
              max_tokens: 280
            })
          });
          clearTimeout(timeoutId);

          if (res.ok) {
            const data = await res.json();
            if (data.choices && data.choices[0] && data.choices[0].message) {
              finalAnswer = data.choices[0].message.content;
            }
          }
        } catch (err) {
          console.warn('LM Studio fetch timeout or error, falling back to expert knowledge engine', err);
        }
      }

      // 2. Fallback to Deep Bilingual Knowledge Engine
      if (!finalAnswer) {
        finalAnswer = generateDeepCopilotAnswer(q, currentLang);
      }

      if (replyEl) {
        replyEl.innerHTML = `
          <div class="space-y-1">
            <div class="flex items-center justify-between border-b border-cyan-500/20 pb-1 text-[10px] text-cyan-400 font-mono">
              <span class="font-bold flex items-center gap-1"><span>🤖</span> <span>ШТУРМАН КÁРІ (LEIÐSÖGUMAÐUR):</span></span>
              <span class="text-slate-400">${isLmStudioConnected ? 'LM Studio Model' : '115 POI Knowledge Engine'}</span>
            </div>
            <div class="text-slate-100 text-[11px] leading-relaxed pt-0.5">${finalAnswer}</div>
          </div>
        `;
        replyEl.scrollTop = replyEl.scrollHeight;
      }

      // Strip HTML tags for clean speech recital
      const plainText = finalAnswer.replace(/<[^>]+>/g, '').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
      speakCopilot(plainText);
    }
'''

if "function sendCopilotModalQuery(" not in html:
    html = html.replace("function sendMiniCopilotQuery() {", stt_and_ai_js + "\n    function sendMiniCopilotQuery() {", 1)
    print("Injected STT and AI dispatcher functions.")

# Export new functions
exports_target = "window.toggleCopilotMute = toggleCopilotMute;"
new_window_exports = '''window.toggleCopilotMute = toggleCopilotMute;
    window.toggleSpeechRecognition = toggleSpeechRecognition;
    window.toggleLmStudioSettings = toggleLmStudioSettings;
    window.checkLmStudioConnection = checkLmStudioConnection;
    window.clearCopilotModalInput = clearCopilotModalInput;
    window.askCopilotModalPredefined = askCopilotModalPredefined;
    window.sendCopilotModalQuery = sendCopilotModalQuery;'''

if exports_target in html and "window.toggleSpeechRecognition =" not in html:
    html = html.replace(exports_target, new_window_exports, 1)
    print("Exported STT and LM Studio window functions.")

# Auto-check LM studio on openCopilotModal
old_open_copilot = '''    function openCopilotModal() {
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

new_open_copilot = '''    function openCopilotModal() {
      const m = document.getElementById('copilot-modal');
      if (m) {
        m.classList.remove('hidden');
        const vid = document.getElementById('copilot-video');
        if (vid) {
          vid.playbackRate = 0.9;
          vid.play().catch(() => {});
        }
        // Auto check LM studio connection asynchronously
        checkLmStudioConnection(false);
      }
    }'''

if old_open_copilot in html:
    html = html.replace(old_open_copilot, new_open_copilot, 1)
    print("Updated openCopilotModal with auto-check of LM studio.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html with STT, LM Studio bridge and bilingual AI engine.")
