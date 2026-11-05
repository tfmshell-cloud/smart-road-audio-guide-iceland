# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# ---------------------------------------------------------------------------
# 1. ADD CSS STYLES FOR COLLAPSIBLE SIDEBAR & 3D WATER-SHIMMER TRIGGER
# ---------------------------------------------------------------------------
custom_styles = '''
    /* Collapsible Sidebar Transitions */
    #sidebar-panel {
      transition: margin-left 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }
    #sidebar-panel.collapsed {
      margin-left: -500px;
    }
    @media (max-width: 768px) {
      #sidebar-panel.collapsed {
        margin-left: -100%;
      }
    }

    /* 3D Glacial Water Shimmer Button */
    .glass-water-btn {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.28) 0%, rgba(14, 165, 233, 0.32) 50%, rgba(16, 185, 129, 0.25) 100%);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(103, 232, 249, 0.55);
      box-shadow: 0 10px 28px -5px rgba(6, 182, 212, 0.45), inset 0 1px 1px 0 rgba(255, 255, 255, 0.4);
      position: relative;
      overflow: hidden;
    }
    .glass-water-btn:hover {
      border-color: rgba(165, 243, 252, 0.85);
      box-shadow: 0 15px 35px -5px rgba(6, 182, 212, 0.65), inset 0 1px 2px 0 rgba(255, 255, 255, 0.6);
    }
    .water-ripple-layer {
      position: absolute;
      top: 0; left: -100%; width: 100%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent);
      animation: waterFlow 3.5s infinite;
      pointer-events: none;
    }
    @keyframes waterFlow {
      0% { left: -100%; }
      50% { left: 100%; }
      100% { left: 100%; }
    }
'''

if ".glass-water-btn" not in html:
    html = html.replace("</style>", custom_styles + "\n  </style>", 1)
    print("Added custom CSS for sidebar and 3D water button.")

# ---------------------------------------------------------------------------
# 2. UPDATE SIDEBAR: ADD ID="sidebar-panel" AND COLLAPSE BUTTON IN HEADER
# ---------------------------------------------------------------------------
old_aside_tag = '<aside class="w-full md:w-[460px] lg:w-[500px] shrink-0 bg-slate-950/95 border-r border-slate-800/80 flex flex-col z-20 shadow-2xl overflow-hidden backdrop-blur-md">'
new_aside_tag = '<aside id="sidebar-panel" class="w-full md:w-[460px] lg:w-[480px] shrink-0 bg-slate-950/95 border-r border-slate-800/80 flex flex-col z-20 shadow-2xl overflow-hidden backdrop-blur-md relative">'

if old_aside_tag in html:
    html = html.replace(old_aside_tag, new_aside_tag, 1)
    print("Updated aside tag with id='sidebar-panel'.")

# Add collapse toggle inside sidebar header
old_search_container = '''        <!-- Search bar -->
        <div class="relative">
          <input type="text" id="poi-search" oninput="filterPOIs()" placeholder="Пошук локації, вулкана, водоспаду, СПА..." class="w-full pl-9 pr-8 py-2 bg-slate-900/90 border border-slate-700/80 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 shadow-inner">
          <span class="absolute left-3 top-2.5 text-slate-400 text-xs">🔍</span>
          <button onclick="clearSearch()" class="absolute right-2.5 top-2.5 text-slate-500 hover:text-slate-300 text-xs">✕</button>
        </div>'''

new_search_container = '''        <!-- Search bar & Collapse Toggle -->
        <div class="flex items-center gap-1.5">
          <div class="relative flex-1">
            <input type="text" id="poi-search" oninput="filterPOIs()" placeholder="Пошук локації, вулкана, водоспаду, СПА..." class="w-full pl-9 pr-8 py-2 bg-slate-900/90 border border-slate-700/80 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 shadow-inner">
            <span class="absolute left-3 top-2.5 text-slate-400 text-xs">🔍</span>
            <button onclick="clearSearch()" class="absolute right-2.5 top-2.5 text-slate-500 hover:text-slate-300 text-xs">✕</button>
          </div>
          <button onclick="toggleSidebar()" class="px-2.5 py-2 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700/80 transition flex items-center gap-1 text-xs shrink-0" title="Приховати панель у лівий край (◀)">
            <span>◀</span>
            <span class="text-[10px] font-semibold hidden sm:inline">Згорнути</span>
          </button>
        </div>'''

if old_search_container in html:
    html = html.replace(old_search_container, new_search_container, 1)
    print("Added collapse button inside sidebar search bar.")

# ---------------------------------------------------------------------------
# 3. ADD 3D WATER-SHIMMER TRIGGER BUTTON & REDESIGN MAP LAYERS CONTROL
# ---------------------------------------------------------------------------
old_map_header = '''    <!-- RIGHT MAIN: MAPLIBRE GL 3D VIEWPORT -->
    <div class="flex-1 relative h-full" id="map-container">
      <div id="map"></div>

      <!-- Floating Map Layer & 3D Pitch Switcher (Top Right) -->
      <div class="absolute top-4 right-4 z-[10] flex flex-col space-y-1.5 glass-panel p-2 rounded-xl border border-slate-700/80 shadow-2xl">
        <div class="text-[10px] uppercase tracking-wider font-bold text-slate-400 px-1" id="lbl-layers-title">ШАРИ КАРТИ (БЕЗ ВОДЯНИХ ЗНАКІВ)</div>
        <button onclick="setBaseLayer('dark')" id="layer-dark" class="px-2.5 py-1 text-xs rounded-lg font-medium bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 flex items-center justify-between space-x-3 transition">
          <span>🌃 Dark Canvas</span> <span class="text-[10px] text-cyan-400 font-mono">Esri Dark</span>
        </button>
        <button onclick="setBaseLayer('satellite')" id="layer-satellite" class="px-2.5 py-1 text-xs rounded-lg font-medium text-slate-300 hover:bg-slate-800 border border-transparent transition flex items-center justify-between space-x-3">
          <span>🛰️ Satellite HD</span> <span class="text-[10px] text-slate-400 font-mono">Esri Real</span>
        </button>
        <button onclick="setBaseLayer('osm')" id="layer-osm" class="px-2.5 py-1 text-xs rounded-lg font-medium text-slate-300 hover:bg-slate-800 border border-transparent transition flex items-center justify-between space-x-3">
          <span>🗺️ OpenStreetMap</span> <span class="text-[10px] text-slate-400 font-mono">OSM Global</span>
        </button>
        <button onclick="setBaseLayer('liberty')" id="layer-liberty" class="px-2.5 py-1 text-xs rounded-lg font-medium text-slate-300 hover:bg-slate-800 border border-transparent transition flex items-center justify-between space-x-3">
          <span>🏔️ Vector Liberty</span> <span class="text-[10px] text-slate-400 font-mono">3D Terrain</span>
        </button>

        <div class="pt-2 border-t border-slate-700/60 flex items-center justify-between px-1">
          <span class="text-[10px] text-slate-400 font-mono">3D НАХИЛ:</span>
          <button onclick="toggle3DPitch()" id="btn-pitch-toggle" class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[10px] font-bold border border-cyan-500/30">
            58° ПЕРСПЕКТИВА
          </button>
        </div>
      </div>'''

new_map_header = '''    <!-- RIGHT MAIN: MAPLIBRE GL 3D VIEWPORT -->
    <div class="flex-1 relative h-full" id="map-container">
      <div id="map"></div>

      <!-- 3D WATER-SHIMMER SIDEBAR TOGGLE BUTTON (ACTIVATES WHEN SIDEBAR IS COLLAPSED) -->
      <button id="btn-toggle-sidebar" onclick="toggleSidebar()" class="hidden absolute top-3.5 left-3.5 z-30 group items-center gap-2.5 px-3.5 py-2 rounded-2xl glass-water-btn shadow-2xl transition-all duration-300 hover:scale-105 active:scale-95 cursor-pointer">
        <div class="relative flex items-center justify-center w-7 h-7 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 text-white shadow-md shadow-cyan-500/40 group-hover:rotate-12 transition">
          <span class="text-sm">🧭</span>
          <span class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-emerald-400 border border-slate-900 animate-ping"></span>
          <span class="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-emerald-400 border border-slate-900"></span>
        </div>
        <div class="flex flex-col text-left">
          <div class="flex items-center gap-1.5">
            <span class="text-xs font-black tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-cyan-300 via-teal-100 to-emerald-300">
              МАРШРУТИ &amp; POI (115)
            </span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/30 font-mono text-cyan-200">8 РЕГІОНІВ</span>
          </div>
          <span class="text-[10px] text-cyan-300/80 font-medium">
            Розгорнути навігаційне меню ▶
          </span>
        </div>
        <span class="water-ripple-layer"></span>
      </button>

      <!-- Sleek, Compact Semi-Transparent Map Layer & 3D Switcher (Top Right) -->
      <div class="absolute top-3.5 right-3.5 z-[10] flex items-center gap-1.5 p-1.5 rounded-xl bg-slate-950/45 hover:bg-slate-950/75 backdrop-blur-md border border-white/10 shadow-2xl transition-all duration-300">
        <div class="hidden sm:flex items-center gap-1 pl-1 pr-2 border-r border-slate-700/60">
          <span class="text-xs">🗺️</span>
          <span class="text-[9px] uppercase tracking-wider font-extrabold text-slate-300 font-mono" id="lbl-layers-title">ШАРИ КАРТИ</span>
        </div>

        <button onclick="setBaseLayer('dark')" id="layer-dark" class="px-2 py-1 text-[11px] rounded-lg font-semibold bg-cyan-500/25 text-cyan-300 border border-cyan-400/40 flex items-center gap-1 transition" title="Esri World Dark Canvas">
          <span>🌃</span> <span class="hidden md:inline">Dark</span>
        </button>
        <button onclick="setBaseLayer('satellite')" id="layer-satellite" class="px-2 py-1 text-[11px] rounded-lg font-medium text-slate-300 hover:text-white hover:bg-white/10 border border-transparent transition flex items-center gap-1" title="Esri Satellite HD">
          <span>🛰️</span> <span class="hidden md:inline">Sat HD</span>
        </button>
        <button onclick="setBaseLayer('osm')" id="layer-osm" class="px-2 py-1 text-[11px] rounded-lg font-medium text-slate-300 hover:text-white hover:bg-white/10 border border-transparent transition flex items-center gap-1" title="OpenStreetMap Global">
          <span>🗺️</span> <span class="hidden md:inline">OSM</span>
        </button>
        <button onclick="setBaseLayer('liberty')" id="layer-liberty" class="px-2 py-1 text-[11px] rounded-lg font-medium text-slate-300 hover:text-white hover:bg-white/10 border border-transparent transition flex items-center gap-1" title="3D Terrain Vector">
          <span>🏔️</span> <span class="hidden md:inline">3D</span>
        </button>

        <div class="h-4 w-px bg-slate-700/60 mx-0.5"></div>

        <button onclick="toggle3DPitch()" id="btn-pitch-toggle" class="px-2 py-1 rounded-lg bg-cyan-500/20 hover:bg-cyan-500/30 text-cyan-300 font-mono text-[10px] font-bold border border-cyan-500/30 flex items-center gap-1 transition" title="Перемикання 2D/3D кута нахилу">
          <span>📐</span> <span id="lbl-pitch-val">58° 3D</span>
        </button>
      </div>'''

if old_map_header in html:
    html = html.replace(old_map_header, new_map_header, 1)
    print("Replaced map layer control with compact semi-transparent bar & added 3D water button.")

# ---------------------------------------------------------------------------
# 4. REDESIGN COPILOT MODAL: PANORAMIC WIDESCREEN COCKPIT WITH VIKING AVATAR
# ---------------------------------------------------------------------------
old_copilot_modal_start = '<div id="copilot-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-3 sm:p-5">'
# Find entire copilot modal block and replace with widescreen dashboard
copilot_regex = r'<div id="copilot-modal".*?<!-- MODAL 2: NOTEBOOKLM AUDIO STUDIO -->'
copilot_match = re.search(copilot_regex, html, re.DOTALL)

new_panoramic_copilot = '''<div id="copilot-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-2 sm:p-4 md:p-6">
    <div class="glass-panel w-full max-w-7xl lg:w-[94vw] xl:w-[92vw] max-h-[75vh] md:max-h-[66vh] rounded-2xl border border-emerald-500/40 overflow-hidden shadow-2xl flex flex-col bg-slate-950/95 backdrop-blur-2xl">
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
                <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-mono text-[10px] font-bold border border-emerald-500/30">PANORAMA COCKPIT</span>
              </h3>
            </div>
            <p class="text-[11px] text-slate-400">Синхронізовано в реальному часі: SafeTravel.is • Vegagerðin • Veðurstofa Íslands • NOAA</p>
          </div>
        </div>
        <button onclick="closeCopilotModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm transition">✕</button>
      </div>

      <!-- Panoramic Cockpit 3-Column Grid -->
      <div class="p-4 overflow-y-auto flex-1 grid grid-cols-1 md:grid-cols-12 gap-3.5 text-xs">
        
        <!-- COLUMN 1: VIKING CO-PILOT PERSONA & AUDIO BRIEFING (4 cols) -->
        <div class="md:col-span-4 flex flex-col justify-between p-3.5 rounded-xl bg-slate-900/90 border border-emerald-500/30 space-y-3">
          <div class="space-y-2.5">
            <div class="flex items-center gap-3">
              <img src="assets/images/viking_copilot.jpg" alt="Viking Navigator Kári" class="w-16 h-16 rounded-xl object-cover border border-cyan-400/50 shadow-md shadow-cyan-500/20 shrink-0">
              <div>
                <div class="flex items-center gap-1.5">
                  <h4 class="text-sm font-bold text-white">Кáрі (Kári)</h4>
                  <span class="px-1.5 py-0.2 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[9px] border border-cyan-500/30">AI RANGER</span>
                </div>
                <p class="text-[10px] text-slate-400">Сертифікований штурман Leiðsöguskólinn</p>
                <div class="flex items-center gap-1 mt-1 text-[10px] text-emerald-400 font-semibold">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>На зв'язку • Слухає трасу</span>
                </div>
              </div>
            </div>

            <!-- Spoken Ranger Brief Excerpt -->
            <div class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300 leading-relaxed italic">
              "Góðan daginn! Говорить черговий штурман. Траса 1 вільна. На мисі Дирхолей бічний вітер 16 м/с — тримайте двері авто обома руками. Увечері Аврора Kp 4.2."
            </div>
          </div>

          <button id="btn-ranger-audio-modal" onclick="playRangerAudio()" class="w-full py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-xs flex items-center justify-center gap-2 shadow-md shadow-emerald-600/30 transition">
            <span>▶</span> <span>Слухати ранковий аудіо-бриф (45 сек)</span>
          </button>
        </div>

        <!-- COLUMN 2: REAL-TIME HAZARDS & ROAD TELEMETRY (4 cols) -->
        <div class="md:col-span-4 flex flex-col justify-between p-3.5 rounded-xl bg-slate-900/90 border border-slate-800 space-y-3">
          <div class="text-[11px] uppercase font-bold text-slate-400 flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span>🛣️</span> ТЕЛЕМЕТРІЯ VEGAGERÐIN &amp; SAFETRAVEL</span>
            <span class="text-emerald-400 font-mono">LIVE FEED</span>
          </div>

          <div class="space-y-2">
            <!-- Safety Index Widget -->
            <div class="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-slate-400 uppercase font-mono">ІНДЕКС БЕЗПЕКИ МАРШРУТУ:</span>
                <div class="text-base font-black text-emerald-400">92 / 100 • БЕЗПЕЧНО</div>
              </div>
              <span class="px-2 py-1 rounded bg-emerald-500/20 text-emerald-300 font-bold text-[10px]">Greiðfært</span>
            </div>

            <!-- Wind / Door Warning Widget -->
            <div class="p-2.5 rounded-lg bg-amber-950/20 border border-amber-500/40 flex items-center justify-between">
              <div>
                <span class="text-[10px] text-amber-400 uppercase font-mono font-bold">⚠️ ВІТЕР ТА РИЗИК ДВЕРЕЙ:</span>
                <div class="text-sm font-bold text-amber-300">16.2 м/с • Пориви на півдні</div>
              </div>
              <span class="text-[10px] px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono">Dyrhólaey</span>
            </div>

            <!-- Road Condition Snapshot -->
            <div class="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800 text-[11px] space-y-1">
              <div class="flex items-center justify-between">
                <span class="text-slate-300 font-medium">Траса 1 (Південь: Selfoss – Vík)</span>
                <span class="text-emerald-400 font-bold text-[10px]">Відкрито</span>
              </div>
              <div class="flex items-center justify-between">
                <span class="text-slate-300 font-medium">Перевал Öxi (Траса 939)</span>
                <span class="text-amber-400 font-bold text-[10px]">Ожеледиця (4x4)</span>
              </div>
            </div>
          </div>

          <div class="text-[10px] text-slate-500 font-mono text-center pt-1 border-t border-slate-800/80">
            Оновлено: 5 хв тому через офіційний API Vegagerðin
          </div>
        </div>

        <!-- COLUMN 3: AURORA RADAR & QUICK COPILOT CHAT (4 cols) -->
        <div class="md:col-span-4 flex flex-col justify-between p-3.5 rounded-xl bg-slate-900/90 border border-cyan-500/30 space-y-2.5">
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-[11px] uppercase font-bold text-cyan-300 flex items-center gap-1.5">
                <span>🌌</span> РАДАР АВРОРИ (IMO &amp; NOAA)
              </span>
              <span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-mono text-[10px] font-bold">Kp 4.2</span>
            </div>

            <!-- Aurora Low Cloud Widget -->
            <div class="p-2 rounded-lg bg-cyan-950/30 border border-cyan-500/30 text-[11px] flex items-center justify-between">
              <div>
                <span class="text-slate-400 text-[10px]">Низька хмарність (Lágský):</span>
                <div class="text-emerald-400 font-bold">12% • Вікно огляду 22:00-02:00</div>
              </div>
              <span class="text-xs">✨</span>
            </div>
          </div>

          <!-- Quick Interactive Copilot Query -->
          <div class="space-y-1.5">
            <div class="text-[10px] text-slate-400 uppercase font-mono font-bold">ШВИДКЕ ПИТАННЯ ШТУРМАНУ:</div>
            <div class="flex items-center space-x-1">
              <input type="text" id="copilot-mini-input" placeholder="Запитати про дорогу, вітер чи POI..." class="flex-1 px-2.5 py-1.5 rounded-lg bg-slate-950 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-cyan-400" onkeydown="if(event.key==='Enter') sendMiniCopilotQuery()">
              <button onclick="sendMiniCopilotQuery()" class="px-3 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition">Чат</button>
            </div>

            <div class="flex items-center gap-1 text-[10px] overflow-x-auto pb-1 scrollbar-none">
              <button onclick="askMiniCopilot('Чи відкрита дорога до Віка?')" class="px-2 py-0.5 rounded bg-slate-800/80 hover:bg-slate-700 text-slate-300 whitespace-nowrap">🛣️ Дорога до Віка</button>
              <button onclick="askMiniCopilot('Де сьогодні шукати Аврору?')" class="px-2 py-0.5 rounded bg-slate-800/80 hover:bg-slate-700 text-slate-300 whitespace-nowrap">🌌 Де Аврора?</button>
              <button onclick="askMiniCopilot('Які секретні водоспади поруч?')" class="px-2 py-0.5 rounded bg-slate-800/80 hover:bg-slate-700 text-slate-300 whitespace-nowrap">💧 Водоспади</button>
            </div>
            <div id="copilot-mini-reply" class="hidden p-2 rounded-lg bg-slate-950/90 border border-cyan-500/30 text-[11px] text-slate-200 leading-snug"></div>
          </div>

          <div class="text-[10px] text-cyan-400 font-mono text-center">
            Натисніть Enter або кнопку запитання
          </div>
        </div>

      </div>

      <!-- Cockpit Footer -->
      <div class="px-5 py-2.5 border-t border-slate-800 bg-slate-950 flex items-center justify-between text-[11px] text-slate-400 shrink-0">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          <span>Штурман веде вас за маршрутом 115 локацій</span>
        </div>
        <button onclick="closeCopilotModal()" class="px-4 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs transition">Закрити панель</button>
      </div>
    </div>
  </div>\n\n  <!-- MODAL 2: NOTEBOOKLM AUDIO STUDIO -->'''

if copilot_match:
    html = html[:copilot_match.start()] + new_panoramic_copilot + html[copilot_match.end():]
    print("Replaced copilot modal with widescreen panoramic cockpit dashboard.")

# ---------------------------------------------------------------------------
# 5. ADD JAVASCRIPT FOR SIDEBAR TOGGLE
# ---------------------------------------------------------------------------
js_sidebar_toggle = '''
    // ==========================================
    // SIDEBAR COLLAPSE / EXPAND TOGGLE
    // ==========================================
    function toggleSidebar() {
      const sidebar = document.getElementById('sidebar-panel');
      const triggerBtn = document.getElementById('btn-toggle-sidebar');
      if (!sidebar) return;

      sidebar.classList.toggle('collapsed');
      const isCollapsed = sidebar.classList.contains('collapsed');

      if (triggerBtn) {
        if (isCollapsed) {
          triggerBtn.classList.remove('hidden');
          triggerBtn.classList.add('flex');
        } else {
          triggerBtn.classList.add('hidden');
          triggerBtn.classList.remove('flex');
        }
      }

      // Smoothly resize map
      setTimeout(() => {
        if (map) map.resize();
      }, 350);
    }
'''

if "function toggleSidebar()" not in html:
    html = html.replace("window.setNavMode = setNavMode;", js_sidebar_toggle + "\n    window.toggleSidebar = toggleSidebar;\n    window.setNavMode = setNavMode;", 1)
    print("Added toggleSidebar JS function.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully.")
