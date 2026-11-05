# -*- coding: utf-8 -*-
INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. ENHANCE VOICE SETTINGS BOX WITH DIRECT SYSTEM VOICE PICKER & MAC GUIDE
# ---------------------------------------------------------------------------
old_settings_markup = """            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              <div>
                <label class="block text-[10px] uppercase font-mono text-cyan-300 mb-1">Оберіть движок синтезу мови:</label>
                <select id="copilot-voice-engine-select" onchange="changeCopilotVoiceEngine(this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:border-cyan-400">
                  <option value="neural">🏆 HD Neural Voice (Вбудований HD голос системи)</option>
                  <option value="radio">📻 Радіозв'язок Рейнджера (Expedition Intercom з DSP)</option>
                  <option value="elevenlabs">⚡ ElevenLabs Studio AI (Студійна якість)</option>
                  <option value="openai">🧠 OpenAI Audio TTS (onyx / alloy)</option>
                  <option value="mute">🔇 Лише текст (Без озвучення)</option>
                </select>
              </div>

              <div>
                <label class="block text-[10px] uppercase font-mono text-cyan-300 mb-1">Швидкість мови (Rate):</label>
                <input type="range" id="copilot-voice-rate" min="0.8" max="1.3" step="0.05" value="1.0" class="w-full accent-cyan-400" oninput="copilotSpeechRate = parseFloat(this.value)">
              </div>
            </div>"""

new_settings_markup = """            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              <div>
                <label class="block text-[10px] uppercase font-mono text-cyan-300 mb-1">Движок синтезу мови:</label>
                <select id="copilot-voice-engine-select" onchange="changeCopilotVoiceEngine(this.value)" class="w-full px-2.5 py-1.5 rounded-lg bg-slate-900 border border-slate-700 text-slate-200 text-xs focus:outline-none focus:border-cyan-400">
                  <option value="neural">🏆 HD Neural Voice (Вбудований голос системи / Siri)</option>
                  <option value="radio">📻 Радіозв'язок Рейнджера (Expedition Intercom з DSP)</option>
                  <option value="elevenlabs">⚡ ElevenLabs Studio AI (Голлівудський студійний звук)</option>
                  <option value="openai">🧠 OpenAI Audio TTS (onyx / alloy / echo)</option>
                  <option value="mute">🔇 Лише текст (Без озвучення)</option>
                </select>
              </div>

              <div>
                <label class="block text-[10px] uppercase font-mono text-cyan-300 mb-1">Швидкість вимови (Rate):</label>
                <input type="range" id="copilot-voice-rate" min="0.8" max="1.3" step="0.05" value="1.0" class="w-full accent-cyan-400" oninput="copilotSpeechRate = parseFloat(this.value)">
              </div>
            </div>

            <!-- Direct Installed System Voice Selector (Lesya / Daniel / Siri) -->
            <div id="system-voice-selector-box" class="p-2.5 rounded-lg bg-slate-900/90 border border-cyan-500/30 space-y-1.5">
              <div class="flex items-center justify-between">
                <span class="text-[10px] font-bold text-cyan-300 uppercase font-mono">🔊 Встановлений голос ОС (Mac / Windows / iOS):</span>
                <span id="detected-voice-badge" class="px-2 py-0.2 rounded bg-cyan-950 text-cyan-300 border border-cyan-500/40 text-[9px] font-mono">Автовибір</span>
              </div>
              <select id="copilot-system-voice-select" onchange="onManualSystemVoiceChange(this.value)" class="w-full px-2.5 py-1.5 rounded bg-slate-950 border border-slate-700 text-xs text-white focus:outline-none focus:border-cyan-400">
                <option value="auto">✨ Автоматичний найкращий HD Neural голос</option>
              </select>
              <p class="text-[10px] text-slate-400 leading-relaxed">
                💡 <b>Як прибрати робота на Mac безкоштовно:</b> <i>Системні параметри → Спеціальні можливості → Озвучення вмісту → Системний голос → Керування голосами...</i> → Завантажте <b>«Леся (Покращена / Enhanced)»</b> для UA та <b>«Daniel (Enhanced)»</b> для EN.
              </p>
            </div>"""

if old_settings_markup in html:
    html = html.replace(old_settings_markup, new_settings_markup, 1)
    print("1. Replaced voice settings box markup with system voice selector.")
else:
    print("Warning: old_settings_markup not matched directly.")

# ---------------------------------------------------------------------------
# 2. ADD JS FOR POPULATING SYSTEM VOICES AND MANUAL SELECTION
# ---------------------------------------------------------------------------
old_voice_load_target = """    // Cache voices when loaded
    let cachedSystemVoices = [];
    if ('speechSynthesis' in window) {
      cachedSystemVoices = window.speechSynthesis.getVoices();
      window.speechSynthesis.onvoiceschanged = () => {
        cachedSystemVoices = window.speechSynthesis.getVoices();
      };
    }"""

new_voice_load_code = """    // Cache and populate available system voices
    let cachedSystemVoices = [];
    let manuallySelectedVoiceName = localStorage.getItem('copilot_selected_voice') || 'auto';

    function populateSystemVoiceDropdown() {
      const select = document.getElementById('copilot-system-voice-select');
      if (!select || !('speechSynthesis' in window)) return;

      const voices = window.speechSynthesis.getVoices();
      cachedSystemVoices = voices;
      if (!voices || voices.length === 0) return;

      const isUk = (currentLang === 'uk');
      const targetLangs = isUk ? ['uk', 'ua'] : ['en'];

      let relevant = voices.filter(v => {
        const l = (v.lang || '').toLowerCase();
        return targetLangs.some(tl => l.includes(tl));
      });

      if (relevant.length === 0) relevant = voices;

      select.innerHTML = '<option value="auto">✨ Автоматичний найкращий HD голос</option>';
      relevant.forEach(v => {
        const opt = document.createElement('option');
        opt.value = v.name;
        const isEnhanced = v.name.toLowerCase().includes('enhanced') || v.name.toLowerCase().includes('natural') || v.name.toLowerCase().includes('premium');
        opt.textContent = `${v.name} (${v.lang}) ${isEnhanced ? '★ HD Neural' : ''}`;
        if (v.name === manuallySelectedVoiceName) opt.selected = true;
        select.appendChild(opt);
      });

      const badge = document.getElementById('detected-voice-badge');
      const best = getBestSystemVoice(currentLang);
      if (badge && best) {
        badge.textContent = `${best.name} (${best.lang})`;
      }
    }

    function onManualSystemVoiceChange(val) {
      manuallySelectedVoiceName = val;
      localStorage.setItem('copilot_selected_voice', val);
      const badge = document.getElementById('detected-voice-badge');
      if (badge) badge.textContent = val === 'auto' ? 'Автовибір' : val;
    }

    if ('speechSynthesis' in window) {
      cachedSystemVoices = window.speechSynthesis.getVoices();
      window.speechSynthesis.onvoiceschanged = () => {
        cachedSystemVoices = window.speechSynthesis.getVoices();
        populateSystemVoiceDropdown();
      };
    }"""

if old_voice_load_target in html:
    html = html.replace(old_voice_load_target, new_voice_load_code, 1)
    print("2. Injected populateSystemVoiceDropdown code.")
else:
    print("Warning: old_voice_load_target not matched directly.")

# Also update getBestSystemVoice to honor manuallySelectedVoiceName
old_get_voice = """    function getBestSystemVoice(lang) {
      const voices = cachedSystemVoices.length > 0 ? cachedSystemVoices : (('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : []);
      if (!voices || voices.length === 0) return null;"""

new_get_voice = """    function getBestSystemVoice(lang) {
      const voices = cachedSystemVoices.length > 0 ? cachedSystemVoices : (('speechSynthesis' in window) ? window.speechSynthesis.getVoices() : []);
      if (!voices || voices.length === 0) return null;

      if (manuallySelectedVoiceName && manuallySelectedVoiceName !== 'auto') {
        const manualMatch = voices.find(v => v.name === manuallySelectedVoiceName);
        if (manualMatch) return manualMatch;
      }"""

if old_get_voice in html:
    html = html.replace(old_get_voice, new_get_voice, 1)
    print("3. Updated getBestSystemVoice to prioritize manual user selection.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html with system voice selector.")
