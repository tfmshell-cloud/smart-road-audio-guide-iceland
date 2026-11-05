# -*- coding: utf-8 -*-
import json
import re
from generate_facts_dataset import ICELAND_MASTER_FACTS

ENCYCLO_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/iceland_guide_encyclopedia.html"
INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract enriched POIS from index.html
pois_match = re.search(r'const POIS = (\[.*?\]);', index_html, re.DOTALL)
if not pois_match:
    raise Exception("Could not find POIS in index.html")
pois_list = json.loads(pois_match.group(1))
pois_dict = {p["id"]: p for p in pois_list}

with open(ENCYCLO_PATH, "r", encoding="utf-8") as f:
    encyclo_html = f.read()

# 1. Update ENCYCLO_DATA array with enriched facts and audioScripts from POIS
encyclo_match = re.search(r'const ENCYCLO_DATA = (\[.*?\]);', encyclo_html, re.DOTALL)
if encyclo_match:
    encyclo_list = json.loads(encyclo_match.group(1))
    for ep in encyclo_list:
        pid = ep["id"]
        if pid in pois_dict:
            src = pois_dict[pid]
            ep["facts"] = src.get("facts", {})
            ep["audioScript"] = src.get("audioScript", {})
            ep["badge"] = src.get("badge", ep.get("badge", "Must-See"))
            ep["geology"] = src.get("geology", ep.get("geology", {}))
            ep["saga"] = src.get("saga", ep.get("saga", {}))
            ep["practical"] = src.get("practical", ep.get("practical", {}))
    
    new_encyclo_json = json.dumps(encyclo_list, ensure_ascii=False)
    encyclo_html = encyclo_html[:encyclo_match.start()] + f"const ENCYCLO_DATA = {new_encyclo_json};" + encyclo_html[encyclo_match.end():]
    print(f"Updated ENCYCLO_DATA with {len(encyclo_list)} items.")

# 2. Inject MASTER_FACTS dataset
master_facts_json = json.dumps(ICELAND_MASTER_FACTS, ensure_ascii=False)
if "const MASTER_FACTS =" not in encyclo_html:
    encyclo_html = encyclo_html.replace("const ENCYCLO_DATA =", f"const MASTER_FACTS = {master_facts_json};\n    const ENCYCLO_DATA =", 1)
    print("Injected MASTER_FACTS into encyclo script.")

# 3. Add 'Цікаві факти' button to header
facts_btn_header = '''
        <!-- Open Facts Modal -->
        <button onclick="openFactsModal()" class="px-3.5 py-2 rounded-xl bg-gradient-to-r from-amber-500/20 to-orange-500/20 hover:from-amber-500/30 hover:to-orange-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition flex items-center gap-1.5 shadow-sm shadow-amber-500/10">
          <span>💡</span> <span>Цікаві факти про Ісландію</span>
          <span class="text-[9px] px-1 py-0.2 rounded bg-amber-500/30 font-mono text-amber-200">ТОП</span>
        </button>
'''
if "openFactsModal()" not in encyclo_html:
    encyclo_html = encyclo_html.replace('<!-- Return to Studio -->', facts_btn_header + '\n        <!-- Return to Studio -->', 1)
    print("Added Facts button to header in encyclopedia.")

# 4. Inject #facts-modal and #floating-audio-player before </body>
facts_modal_and_audio_html = '''
  <!-- FLOATING PERSISTENT AUDIO GUIDE BAR -->
  <div id="floating-audio-player" class="hidden fixed bottom-4 left-1/2 -translate-x-1/2 w-11/12 max-w-2xl z-40 bg-slate-900/95 backdrop-blur-xl border border-cyan-500/50 rounded-2xl shadow-2xl p-3.5 flex flex-col gap-2 transition-all duration-300">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2.5 overflow-hidden">
        <span class="text-xl">🎙️</span>
        <div class="truncate">
          <div class="flex items-center gap-1.5">
            <h4 class="text-xs font-bold text-white truncate" id="fplayer-title">Gullfoss</h4>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/20 text-cyan-300 font-mono">Аудіогід 75с</span>
          </div>
          <p class="text-[10px] text-slate-400 truncate" id="fplayer-status">Відтворення дикторської розповіді...</p>
        </div>
      </div>
      <div class="flex items-center space-x-2 shrink-0">
        <button onclick="toggleFloatingPlayPause()" id="btn-fplayer-toggle" class="w-8 h-8 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white flex items-center justify-center text-xs font-bold shadow-md shadow-cyan-600/30">
          ⏸
        </button>
        <button onclick="stopAudio()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs">
          ⏹
        </button>
      </div>
    </div>
    <div class="space-y-1">
      <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden cursor-pointer">
        <div id="fplayer-progress" class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
      </div>
      <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
        <span id="fplayer-curr-time">0:00</span>
        <span id="fplayer-note" class="text-amber-400 text-[9px]"></span>
        <span id="fplayer-total-time">1:15</span>
      </div>
    </div>
  </div>

  <!-- MODAL: MASTER INTERESTING FACTS ABOUT ICELAND -->
  <div id="facts-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-3 sm:p-5">
    <div class="glass-card-3d w-full max-w-4xl rounded-2xl border border-amber-500/40 overflow-hidden shadow-2xl flex flex-col max-h-[92vh]">
      <div class="px-5 py-4 border-b border-slate-800 bg-gradient-to-r from-amber-950/60 via-slate-900 to-slate-900 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 to-orange-500 flex items-center justify-center text-xl shadow-lg shadow-amber-500/20">
            💡
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h3 class="text-base font-bold text-white">Цікаві факти про Ісландію</h3>
              <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono text-[10px] font-bold border border-amber-500/30">ЕКСКЛЮЗИВ</span>
            </div>
            <p class="text-[11px] text-slate-400">Перевірені академічні інсайти ліцензованого гіда • Генетика, вулкани, саги та природа</p>
          </div>
        </div>
        <button onclick="closeFactsModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm">✕</button>
      </div>

      <div class="p-4 border-b border-slate-800 bg-slate-950/80 space-y-3">
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">🔍</span>
          <input type="text" id="facts-search-input" oninput="handleFactsSearch(this.value)" placeholder="Пошук фактів (напр. Gullfoss, коні, ДНК, вулкан, комар, мова, ГЕС)..." class="w-full pl-9 pr-4 py-2 bg-slate-900 border border-slate-700/80 rounded-xl text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-400 transition">
        </div>

        <div class="flex items-center gap-1.5 overflow-x-auto pb-1 text-[11px]" id="facts-category-pills">
          <button onclick="filterFactsCategory('all')" class="facts-pill active px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-amber-500 text-slate-950">Всі факти</button>
          <button onclick="filterFactsCategory('waterfalls_canyons')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">💧 Водоспади &amp; Каньйони</button>
          <button onclick="filterFactsCategory('volcanoes_geology')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🌋 Вулкани &amp; Геологія</button>
          <button onclick="filterFactsCategory('science_genetics')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🧬 Наука &amp; Генетика</button>
          <button onclick="filterFactsCategory('nature_fauna')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🐴 Фауна &amp; Коні</button>
          <button onclick="filterFactsCategory('society_culture')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🏛️ Суспільство &amp; Мова</button>
          <button onclick="filterFactsCategory('energy_climate')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">⚡ Зелена Енергія</button>
        </div>
      </div>

      <div class="p-4 overflow-y-auto space-y-3 text-xs" id="facts-container" style="max-height: 60vh;">
      </div>

      <div class="p-3 border-t border-slate-800 bg-slate-950 flex items-center justify-between text-[11px] text-slate-400">
        <div>Всього перевірених фактів у базі: <span id="facts-count-badge" class="font-bold text-amber-400">--</span></div>
        <button onclick="closeFactsModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200">Закрити</button>
      </div>
    </div>
  </div>
'''

if 'id="facts-modal"' not in encyclo_html:
    encyclo_html = encyclo_html.replace('</body>', facts_modal_and_audio_html + '\n</body>', 1)
    print("Injected #facts-modal and #floating-audio-player into encyclo HTML.")

# 5. Update renderCards in encyclo to display facts and 75s audioScript + audio button
old_render_cards_target = '''              <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 shadow-inner">
                <strong class="text-emerald-400 text-[11px] block mb-0.5">${t.lblSafety}</strong>
                <p class="text-[11px] text-slate-300 leading-relaxed">${p.practical[currentLang]}</p>
              </div>
            </div>
          </div>'''

new_render_cards_block = '''              <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800 shadow-inner">
                <strong class="text-emerald-400 text-[11px] block mb-0.5">${t.lblSafety}</strong>
                <p class="text-[11px] text-slate-300 leading-relaxed">${p.practical[currentLang]}</p>
              </div>

              <!-- FACTS DISPLAY -->
              <div class="p-3 rounded-xl bg-amber-950/20 border border-amber-500/30 shadow-inner space-y-1.5">
                <strong class="text-amber-400 text-[11px] flex items-center gap-1">
                  <span>💡</span> <span>${currentLang === 'uk' ? 'Цікаві факти & Інсайти:' : 'Curated Key Facts:'}</span>
                </strong>
                <ul class="space-y-1 text-[11px] text-slate-300">
                  ${(p.facts && p.facts[currentLang] ? p.facts[currentLang] : []).map(f => `<li class="leading-relaxed">• ${f}</li>`).join('')}
                </ul>
              </div>

              <!-- 75S AUDIO SCRIPT -->
              <div class="p-3 rounded-xl bg-cyan-950/20 border border-cyan-500/30 shadow-inner space-y-1.5">
                <div class="flex items-center justify-between">
                  <strong class="text-cyan-300 text-[11px] flex items-center gap-1">
                    <span>🎙️</span> <span>${currentLang === 'uk' ? 'Дикторський аудіоскрипт (75с):' : 'Guide Audio Script (75s):'}</span>
                  </strong>
                  <button onclick="playPoiAudio('${p.id}')" class="px-2 py-0.5 rounded bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300 text-[10px] font-semibold border border-cyan-500/30">
                    ▶ ${currentLang === 'uk' ? 'Слухати' : 'Listen'}
                  </button>
                </div>
                <p class="text-[11px] text-slate-300 italic leading-relaxed border-l-2 border-cyan-500/50 pl-2.5">
                  ${p.audioScript ? p.audioScript[currentLang] : p.geology[currentLang]}
                </p>
              </div>
            </div>
          </div>'''

if old_render_cards_target in encyclo_html:
    encyclo_html = encyclo_html.replace(old_render_cards_target, new_render_cards_block, 1)
    print("Upgraded renderCards card body in encyclo HTML.")

# 6. Add facts and audio functions to encyclo script
encyclo_js_functions = '''
    // ==========================================
    // FACTS ENGINE & AUDIO PLAYER FOR ENCYCLOPEDIA
    // ==========================================
    let currentFactsCategory = 'all';
    let currentFactsSearch = '';
    let currentlyPlayingAudioPoiId = null;
    let audioScrubberInterval = null;
    let audioCurrentSeconds = 0;
    const AUDIO_TOTAL_SECONDS = 75;
    let isAudioPaused = false;
    let activeAudioPoi = null;

    function openFactsModal() {
      renderFactsList();
      const m = document.getElementById('facts-modal');
      if (m) m.classList.remove('hidden');
    }

    function closeFactsModal() {
      const m = document.getElementById('facts-modal');
      if (m) m.classList.add('hidden');
    }

    function filterFactsCategory(cat) {
      currentFactsCategory = cat;
      const buttons = document.querySelectorAll('#facts-category-pills button');
      buttons.forEach(btn => {
        btn.className = 'facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800';
      });
      event.target.className = 'facts-pill active px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-amber-500 text-slate-950';
      renderFactsList();
    }

    function handleFactsSearch(val) {
      currentFactsSearch = val.toLowerCase().trim();
      renderFactsList();
    }

    function renderFactsList() {
      const container = document.getElementById('facts-container');
      if (!container) return;

      let filtered = MASTER_FACTS.filter(item => {
        const matchCategory = currentFactsCategory === 'all' || item.category === currentFactsCategory;
        const textToSearch = (item.title[currentLang] + ' ' + item.fact[currentLang] + ' ' + (item.poiId || '')).toLowerCase();
        const matchSearch = !currentFactsSearch || textToSearch.includes(currentFactsSearch);
        return matchCategory && matchSearch;
      });

      document.getElementById('facts-count-badge').textContent = `${filtered.length} з ${MASTER_FACTS.length}`;
      container.innerHTML = '';

      if (filtered.length === 0) {
        container.innerHTML = '<div class="text-center py-8 text-slate-500"><div class="text-3xl mb-2">🔍</div><p>За вашим запитом нічого не знайдено.</p></div>';
        return;
      }

      filtered.forEach(item => {
        const poi = item.poiId ? ENCYCLO_DATA.find(p => p.id === item.poiId) : null;
        const card = document.createElement('div');
        card.className = 'p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/90 hover:border-amber-500/40 transition space-y-2';

        let poiActionBtn = '';
        if (poi) {
          poiActionBtn = `
            <a href="index.html?poi=${poi.id}" class="px-2.5 py-1 rounded-lg bg-gradient-to-r from-cyan-500/20 to-blue-500/20 hover:from-cyan-500/30 hover:to-blue-500/30 text-cyan-300 border border-cyan-500/40 text-[11px] font-semibold flex items-center gap-1 transition">
              <span>🗺️</span> <span>${poi.name[currentLang]} на 3D-карті</span>
            </a>
          `;
        }

        card.innerHTML = `
          <div class="flex items-center justify-between gap-2">
            <span class="px-2 py-0.5 rounded bg-amber-500/15 text-amber-300 font-mono text-[10px] font-bold border border-amber-500/30">
              ${item.category_name[currentLang]}
            </span>
            ${poi ? `<span class="text-[10px] text-slate-500 font-mono">POI: ${poi.name[currentLang]}</span>` : ''}
          </div>
          <h4 class="text-xs font-bold text-white">${item.title[currentLang]}</h4>
          <p class="text-[11px] text-slate-300 leading-relaxed">${item.fact[currentLang]}</p>
          ${poiActionBtn ? `<div class="pt-2 border-t border-slate-800/80 flex items-center justify-end">${poiActionBtn}</div>` : ''}
        `;
        container.appendChild(card);
      });
    }

    function playPoiAudio(poiId) {
      const poi = ENCYCLO_DATA.find(p => p.id === poiId);
      if (!poi) return;

      stopAudio();
      activeAudioPoi = poi;
      currentlyPlayingAudioPoiId = poiId;
      isAudioPaused = false;
      audioCurrentSeconds = 0;

      const fPlayer = document.getElementById('floating-audio-player');
      if (fPlayer) fPlayer.classList.remove('hidden');

      document.getElementById('fplayer-title').textContent = poi.name[currentLang];
      document.getElementById('btn-fplayer-toggle').textContent = '⏸';
      document.getElementById('fplayer-status').textContent = 'Відтворення дикторського скрипта...';

      // Start scrubber
      clearInterval(audioScrubberInterval);
      audioScrubberInterval = setInterval(() => {
        if (!isAudioPaused) {
          audioCurrentSeconds++;
          const progressPercent = Math.min(100, (audioCurrentSeconds / AUDIO_TOTAL_SECONDS) * 100);
          const progBar = document.getElementById('fplayer-progress');
          if (progBar) progBar.style.width = `${progressPercent}%`;

          const m = Math.floor(audioCurrentSeconds / 60);
          const s = audioCurrentSeconds % 60;
          const currTimeElem = document.getElementById('fplayer-curr-time');
          if (currTimeElem) currTimeElem.textContent = `${m}:${s < 10 ? '0' : ''}${s}`;

          if (audioCurrentSeconds >= AUDIO_TOTAL_SECONDS) {
            stopAudio();
          }
        }
      }, 1000);

      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const scriptText = (poi.audioScript && poi.audioScript[currentLang]) ? poi.audioScript[currentLang] : poi.geology[currentLang];
        const u = new SpeechSynthesisUtterance(scriptText);
        u.lang = currentLang === 'uk' ? 'uk-UA' : 'en-US';
        u.onend = () => stopAudio();
        window.speechSynthesis.speak(u);
      }
    }

    function toggleFloatingPlayPause() {
      if (!activeAudioPoi) return;
      if (isAudioPaused) {
        isAudioPaused = false;
        if ('speechSynthesis' in window && window.speechSynthesis.paused) window.speechSynthesis.resume();
        document.getElementById('btn-fplayer-toggle').textContent = '⏸';
        document.getElementById('fplayer-status').textContent = 'Відтворення...';
      } else {
        isAudioPaused = true;
        if ('speechSynthesis' in window && window.speechSynthesis.speaking) window.speechSynthesis.pause();
        document.getElementById('btn-fplayer-toggle').textContent = '▶';
        document.getElementById('fplayer-status').textContent = 'Пауза';
      }
    }

    function stopAudio() {
      clearInterval(audioScrubberInterval);
      audioScrubberInterval = null;
      audioCurrentSeconds = 0;
      isAudioPaused = false;
      activeAudioPoi = null;
      currentlyPlayingAudioPoiId = null;

      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
      const fPlayer = document.getElementById('floating-audio-player');
      if (fPlayer) fPlayer.classList.add('hidden');
    }
'''

if 'function openFactsModal()' not in encyclo_html:
    encyclo_html = encyclo_html.replace('// INIT ON LOAD', encyclo_js_functions + '\n    // INIT ON LOAD', 1)
    print("Added audio and facts JS functions to encyclo script.")

with open(ENCYCLO_PATH, "w", encoding="utf-8") as f:
    f.write(encyclo_html)

print("Saved updated iceland_guide_encyclopedia.html successfully.")
