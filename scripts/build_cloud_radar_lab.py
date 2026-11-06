# -*- coding: utf-8 -*-
"""
Master Builder for Iceland Cloud Radar Lab:
10 WOW-WOW-WOW Variations of Aurora Hunter Occlusion with Oceanic Scope & Real-Time Live Sync.
"""
import os

LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/cloud_radar_lab.html"
BRAIN_LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/brain/3cafaa28-e27e-4b4e-85d4-a0a0a9d89f86/cloud_radar_lab.html"

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="uk" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iceland Cloud Radar Lab — 10 Концептів Aurora Hunter Occlusion (Live Oceanic Sync)</title>
  
  <!-- MapLibre GL JS & CSS -->
  <script src="https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.js"></script>
  <link href="https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.css" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <style>
    @keyframes pulseGlow {
      0%, 100% { filter: drop-shadow(0 0 10px rgba(16, 185, 129, 0.4)); }
      50% { filter: drop-shadow(0 0 24px rgba(16, 185, 129, 0.85)); }
    }
    @keyframes radarSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.6); }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(16, 185, 129, 0.4); border-radius: 4px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(16, 185, 129, 0.8); }

    .concept-btn.active {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.25) 0%, rgba(15, 23, 42, 0.95) 100%);
      border-color: #10b981;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.45);
      color: #ffffff;
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased h-screen w-screen overflow-hidden flex flex-col select-none">

  <!-- ============================================================ -->
  <!-- 1. TOP EXECUTIVE COMMAND BAR & LIVE SYNC STATUS -->
  <!-- ============================================================ -->
  <header class="h-16 px-4 bg-slate-950/95 border-b border-emerald-500/30 backdrop-blur-xl flex items-center justify-between shrink-0 z-30">
    <div class="flex items-center space-x-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 via-teal-500 to-indigo-600 flex items-center justify-center text-xl shadow-lg shadow-emerald-500/30 animate-pulse">
        🌌
      </div>
      <div>
        <div class="flex items-center space-x-2">
          <h1 class="text-sm sm:text-base font-black text-white tracking-wide flex items-center gap-2">
            <span>Aurora Hunter Occlusion Lab</span>
            <span class="px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-mono text-[10px] font-bold border border-emerald-400/40">10 LIVE VARIATIONS</span>
          </h1>
        </div>
        <p class="text-[11px] text-slate-400 hidden sm:block">Північна Атлантика & Ісландія: хмари як темні маски, чисті вікна сяють смарагдовою Авророю</p>
      </div>
    </div>

    <!-- Center Live Sync Badge -->
    <div class="hidden lg:flex items-center space-x-2 bg-slate-900/90 px-3 py-1.5 rounded-xl border border-emerald-500/30 font-mono text-[11px]">
      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
      <span class="text-slate-300">LIVE SYNC:</span>
      <span id="live-sync-indicator" class="font-bold text-emerald-300">VEÐURSTOFA & NOAA SWPC (Kp <span id="sync-kp-val">3.8</span>)</span>
      <button onclick="fetchLiveMeteoData()" class="ml-2 text-slate-400 hover:text-emerald-300 transition" title="Оновити зараз">🔄</button>
    </div>

    <!-- Quick Actions -->
    <div class="flex items-center space-x-2">
      <!-- Return to Main App -->
      <a href="index.html" class="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold flex items-center gap-1.5 transition" title="Повернутися до головного сайту">
        <span>⬅️</span> <span class="hidden md:inline">Головний сайт</span>
      </a>

      <!-- Basemap Switcher -->
      <div class="inline-flex rounded-xl bg-slate-900 p-0.5 border border-slate-800 text-xs">
        <button id="btn-basemap-dark" onclick="setBasemap('dark')" class="px-2.5 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold transition">Dark</button>
        <button id="btn-basemap-sat" onclick="setBasemap('satellite')" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Satellite</button>
      </div>

      <!-- Toggle Info HUD -->
      <button onclick="toggleHudPanel()" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-300 border border-slate-700 text-xs transition" title="Панель телеметрії та формул">
        ⚙️
      </button>
    </div>
  </header>

  <!-- ============================================================ -->
  <!-- 2. CONCEPT SELECTOR STRIP (10 AURORA HUNTER OCCLUSION VARIATIONS) -->
  <!-- ============================================================ -->
  <div class="px-3 py-2 bg-slate-950/90 border-b border-slate-800/80 backdrop-blur-md shrink-0 z-20 overflow-x-auto custom-scrollbar flex items-center space-x-2 text-xs">
    <button onclick="switchConcept(0)" id="c-btn-0" class="concept-btn active px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🌋</span> <span class="font-bold">1. Basalt Clouds & Emerald Bleed</span>
    </button>
    <button onclick="switchConcept(1)" id="c-btn-1" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🌐</span> <span class="font-bold">2. NOAA Geomagnetic Oval</span>
    </button>
    <button onclick="switchConcept(2)" id="c-btn-2" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>✨</span> <span class="font-bold">3. Starlight Portals & Sea Glow</span>
    </button>
    <button onclick="switchConcept(3)" id="c-btn-3" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🌀</span> <span class="font-bold">4. Denmark Strait Synoptic Vortex</span>
    </button>
    <button onclick="switchConcept(4)" id="c-btn-4" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>📡</span> <span class="font-bold">5. LIDAR Transmittance Scanner</span>
    </button>
    <button onclick="switchConcept(5)" id="c-btn-5" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>⚡</span> <span class="font-bold">6. Cyber-Holo Neon Contours</span>
    </button>
    <button onclick="switchConcept(6)" id="c-btn-6" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>📷</span> <span class="font-bold">7. 30s Long Exposure Tripod</span>
    </button>
    <button onclick="switchConcept(7)" id="c-btn-7" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🏔️</span> <span class="font-bold">8. Marine Fog & Glacier Peak Cut</span>
    </button>
    <button onclick="switchConcept(8)" id="c-btn-8" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>⬡</span> <span class="font-bold">9. Hexagonal Exposure Matrix</span>
    </button>
    <button onclick="switchConcept(9)" id="c-btn-9" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>⚡</span> <span class="font-bold">10. Solar Wind Plasma Filaments</span>
    </button>
  </div>

  <!-- ============================================================ -->
  <!-- 3. MAIN INTERACTIVE STAGE: FULLSCREEN MAP + CANVAS OVERLAY -->
  <!-- ============================================================ -->
  <main class="flex-1 relative w-full h-full overflow-hidden">
    
    <!-- MapLibre Map Container -->
    <div id="map" class="absolute inset-0 w-full h-full"></div>

    <!-- Synchronized 60 FPS Radar Simulation Canvas -->
    <canvas id="radar-canvas" class="absolute inset-0 w-full h-full pointer-events-none z-10"></canvas>

    <!-- Floating Zoom Preset Bar (Wide Oceanic to Fjord Detail) -->
    <div class="absolute top-4 left-4 z-20 flex flex-wrap gap-1.5 p-1.5 rounded-2xl bg-slate-950/90 backdrop-blur-md border border-emerald-500/30 shadow-2xl text-[11px] font-mono">
      <span class="px-2 py-1 text-slate-400 font-bold flex items-center gap-1">
        <span>🔭</span> <span class="hidden sm:inline">ОХОПЛЕННЯ:</span>
      </span>
      <button onclick="flyToZoom(4.8, [-19.5, 64.2])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-300 hover:text-white border border-slate-700 transition" title="Океанічний фронт від Гренландії до Норвезького моря">
        🌊 Північна Атлантика & Океан (Z4.8)
      </button>
      <button onclick="flyToZoom(6.2, [-18.5, 64.9])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-300 hover:text-white border border-slate-700 transition" title="Вся Ісландія">
        🇮🇸 Ісландія (Z6.2)
      </button>
      <button onclick="flyToZoom(8.0, [-19.0, 63.6])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-300 hover:text-white border border-slate-700 transition" title="Південне узбережжя">
        🌊 Південь & Вік (Z8.0)
      </button>
      <button onclick="flyToZoom(8.5, [-16.9, 65.6])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-emerald-300 hover:text-white border border-slate-700 transition" title="Зона найчистішого неба">
        ✨ Озеро Міватн (Z8.5)
      </button>
    </div>

    <!-- Floating Live Telemetry HUD Card (Bottom Left) -->
    <div id="concept-hud-card" class="absolute bottom-20 left-4 z-20 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-emerald-500/40 shadow-2xl max-w-sm space-y-2 text-xs">
      <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
        <span id="hud-concept-title" class="font-black text-emerald-300 uppercase tracking-wide flex items-center gap-1.5">
          <span>🌋</span> 1. Basalt Clouds & Emerald Bleed
        </span>
        <span id="hud-fps-badge" class="px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-mono text-[10px] border border-emerald-500/40">
          60 FPS
        </span>
      </div>
      <p id="hud-concept-desc" class="text-slate-300 text-[11px] leading-relaxed">
        Темні базальтові хмари повністю блокують Аврору в центрі, проте на напівпрозорих периферіях смарагдове сяйво просочується крізь водяну пару, а у відкритих вікнах вибухає чистий іоносферний спалах.
      </p>
      <div class="grid grid-cols-2 gap-2 pt-1 font-mono text-[10px]">
        <div class="p-1.5 rounded-lg bg-slate-900 border border-slate-800">
          <span class="text-slate-400 block">ХМАРНІСТЬ (LIVE):</span>
          <span id="hud-cloud-pct" class="font-bold text-cyan-300 text-xs">58% ПОКРИТТЯ</span>
        </div>
        <div class="p-1.5 rounded-lg bg-slate-900 border border-slate-800">
          <span class="text-slate-400 block">NOAA Kp ІНДЕКС:</span>
          <span id="hud-kp-val" class="font-bold text-emerald-400 text-xs">Kp 3.8 • АКТИВНО</span>
        </div>
      </div>
    </div>

    <!-- Side Blueprint Panel (Collapsible Inspector) -->
    <aside id="inspector-panel" class="hidden absolute top-4 right-4 bottom-20 w-80 z-20 p-4 rounded-2xl bg-slate-950/95 backdrop-blur-2xl border border-emerald-500/40 shadow-2xl flex flex-col justify-between overflow-y-auto custom-scrollbar text-xs space-y-3">
      <div>
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <h3 class="font-bold text-white flex items-center gap-1.5">
            <span>🔬</span> МЕТЕОРОЛОГІЧНИЙ ІНСПЕКТОР
          </h3>
          <button onclick="toggleHudPanel()" class="text-slate-400 hover:text-white">✕</button>
        </div>

        <div class="space-y-3 pt-3">
          <div>
            <h4 class="text-[10px] uppercase font-mono text-emerald-400 font-bold mb-1">ФОРМУЛА ОКЛЮЗІЇ (BEER-LAMBERT):</h4>
            <p id="ins-math" class="text-[11px] text-slate-300 bg-slate-900 p-2 rounded-lg font-mono border border-slate-800 leading-relaxed">
              I_visible = I_aurora * exp(-COD) + I_ambient * (1 - exp(-COD))
            </p>
          </div>

          <div>
            <h4 class="text-[10px] uppercase font-mono text-emerald-400 font-bold mb-1">МАСШТАБУВАННЯ & ОКЕАН:</h4>
            <p id="ins-scaling" class="text-[11px] text-slate-300 leading-relaxed">
              Карта охоплює Північну Атлантику від Гренландії до Фарерських островів. Це дозволяє прогнозувати прихід циклонів з південного заходу за 6-12 годин до наближення до Ісландії.
            </p>
          </div>

          <div>
            <h4 class="text-[10px] uppercase font-mono text-emerald-400 font-bold mb-1">ДЖЕРЕЛА LIVE ДАНИХ:</h4>
            <ul class="text-[11px] text-slate-400 space-y-1 list-disc list-inside">
              <li>Open-Meteo High-Resolution (Ісландія + Океан)</li>
              <li>NOAA Space Weather Prediction Center (Live 1m Kp)</li>
              <li>Veðurstofa Íslands (Ісландський метеоофіс)</li>
              <li>EUMETSAT Polar Orbiting Sounder</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="pt-2 border-t border-slate-800 text-[10px] text-slate-500 font-mono">
        SMART ROAD AUDIO GUIDE • AURORA HUNTER LAB 2026
      </div>
    </aside>

  </main>

  <!-- ============================================================ -->
  <!-- 4. BOTTOM 12-HOUR TIME-LAPSE RADAR CONTROLLER -->
  <!-- ============================================================ -->
  <footer class="h-20 px-4 bg-slate-950/95 border-t border-emerald-500/30 backdrop-blur-xl flex flex-col justify-center shrink-0 z-30">
    <div class="flex items-center justify-between gap-3 max-w-7xl mx-auto w-full">
      
      <!-- Play/Pause & Reset Controls -->
      <div class="flex items-center space-x-2 shrink-0">
        <button id="btn-play-pause" onclick="togglePlayPause()" class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 flex items-center justify-center font-bold text-base shadow-lg shadow-emerald-500/30 transition">
          ▶️
        </button>
        <button onclick="resetTimeline()" class="w-10 h-10 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-700 flex items-center justify-center text-sm transition" title="Скинути на поточний час">
          ⏮️
        </button>
      </div>

      <!-- Interactive 12-Hour Range Slider with Forecast Ticks -->
      <div class="flex-1 space-y-1">
        <div class="flex items-center justify-between text-[11px] font-mono">
          <span class="text-slate-400 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
            <span>ПРОГНОЗ ДРЕЙФУ ХМАР & СЯЙВА:</span>
          </span>
          <span id="timeline-time-label" class="font-bold text-emerald-300 bg-slate-900 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
            Сьогодні, 18:00 UTC (Зараз)
          </span>
          <span id="timeline-aurora-badge" class="font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
            🌌 Kp 3.8 • АКТИВНО
          </span>
        </div>

        <input type="range" id="radar-time-slider" min="0" max="12" step="0.1" value="0" oninput="onTimelineInput(this.value)" class="w-full accent-emerald-400 cursor-pointer h-2 bg-slate-800 rounded-lg">
        
        <div class="flex justify-between text-[9px] font-mono text-slate-500 px-1">
          <span>ЗАРАЗ</span>
          <span>+2h</span>
          <span>+4h</span>
          <span>+6h (Північ)</span>
          <span>+8h</span>
          <span>+10h</span>
          <span>+12h (Світанок)</span>
        </div>
      </div>

      <!-- Speed Toggles -->
      <div class="hidden sm:flex items-center space-x-2 shrink-0">
        <div class="flex items-center space-x-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-mono">
          <button onclick="setPlaySpeed(1)" id="spd-1" class="px-2 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold transition">1x</button>
          <button onclick="setPlaySpeed(2)" id="spd-2" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">2x</button>
          <button onclick="setPlaySpeed(4)" id="spd-4" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">4x</button>
        </div>
      </div>

    </div>
  </footer>

  <!-- ============================================================ -->
  <!-- 5. MASTER SCRIPT: 10 CONCEPTS, OCEAN COVERAGE, LIVE APIS -->
  <!-- ============================================================ -->
  <script>
    // -------------------------------------------------------------
    // EXPANDED GEOGRAPHIC SECTORS (ICELAND + BROAD NORTH ATLANTIC)
    // -------------------------------------------------------------
    const REGIONAL_SECTORS = [
      // Oceanic weather systems approaching Iceland
      { id: 'denmark_strait', name: 'Датська протока (Гренландія)', lat: 67.2, lng: -29.5, radiusKm: 140, cloudBase: 85, windSpeed: 24.0, windDir: 40 },
      { id: 'south_atlantic_cyclone', name: 'Південна Атлантика (Штормовий фронт)', lat: 60.5, lng: -21.0, radiusKm: 170, cloudBase: 95, windSpeed: 28.5, windDir: 220 },
      { id: 'norwegian_sea', name: 'Норвезьке море (Східна течія)', lat: 65.5, lng: -8.5, radiusKm: 130, cloudBase: 60, windSpeed: 16.0, windDir: 170 },
      
      // Iceland Mainland sectors
      { id: 'reykjavik', name: 'Рейк\'явік & Фаґрадалсф\'ядль', lat: 64.14, lng: -21.94, radiusKm: 55, cloudBase: 70, windSpeed: 12.5, windDir: 210 },
      { id: 'south_coast', name: 'Південне узбережжя & Вік', lat: 63.50, lng: -19.00, radiusKm: 75, cloudBase: 82, windSpeed: 21.0, windDir: 235 },
      { id: 'vatnajokull', name: 'Льодовик Ватнайокюдль (Пік 2110м)', lat: 64.40, lng: -16.80, radiusKm: 90, cloudBase: 45, windSpeed: 18.0, windDir: 250 },
      { id: 'east_fjords', name: 'Східні фіорди (Сейдісфіордюр)', lat: 65.25, lng: -14.00, radiusKm: 65, cloudBase: 40, windSpeed: 9.5, windDir: 195 },
      { id: 'myvatn_north', name: 'Озеро Міватн (Вікно Аврори)', lat: 65.60, lng: -16.90, radiusKm: 70, cloudBase: 12, windSpeed: 7.0, windDir: 205 },
      { id: 'akureyri', name: 'Акюрейрі & Ейяфіордюр', lat: 65.68, lng: -18.10, radiusKm: 55, cloudBase: 22, windSpeed: 6.8, windDir: 190 },
      { id: 'westfjords', name: 'Західні фіорди (Диньянди)', lat: 65.75, lng: -23.20, radiusKm: 80, cloudBase: 65, windSpeed: 14.0, windDir: 275 },
      { id: 'snaefellsnes', name: 'Півострів Снайфедльснес', lat: 64.85, lng: -23.50, radiusKm: 60, cloudBase: 75, windSpeed: 17.5, windDir: 260 },
      { id: 'highlands', name: 'Керлінґарф\'єтль & Аскья', lat: 64.80, lng: -18.80, radiusKm: 85, cloudBase: 35, windSpeed: 15.0, windDir: 230 }
    ];

    // Procedural multi-puff clouds per sector
    const SECTOR_PUFFS = [];
    REGIONAL_SECTORS.forEach(sec => {
      const puffCount = sec.radiusKm > 100 ? 35 : 22;
      for (let i = 0; i < puffCount; i++) {
        const ang = Math.random() * Math.PI * 2;
        const dist = Math.random() * sec.radiusKm * 0.95;
        const dLat = (Math.cos(ang) * dist) / 111.0;
        const dLng = (Math.sin(ang) * dist) / (111.0 * Math.cos(sec.lat * Math.PI / 180));
        SECTOR_PUFFS.push({
          sectorId: sec.id,
          baseLat: sec.lat + dLat,
          baseLng: sec.lng + dLng,
          currentLat: sec.lat + dLat,
          currentLng: sec.lng + dLng,
          radiusKm: 18 + Math.random() * 32,
          opacityMult: 0.70 + Math.random() * 0.30,
          speedMult: 0.85 + Math.random() * 0.35,
          phase: Math.random() * Math.PI * 2
        });
      }
    });

    // 2,500 Night Sky Stars for Concept 3 & Concept 7
    const ASTRO_STARS = [];
    for (let i = 0; i < 2500; i++) {
      ASTRO_STARS.push({
        lat: 58.0 + Math.random() * 13.0,
        lng: -34.0 + Math.random() * 30.0,
        brightness: 0.2 + Math.random() * 0.8,
        size: 0.6 + Math.random() * 1.8,
        twinkleSpeed: 1.5 + Math.random() * 3.5
      });
    }

    // Geodesic Hexagonal Grid Points for Concept 9
    const HEX_GRID = [];
    for (let lat = 59.5; lat <= 68.5; lat += 0.55) {
      const isOdd = Math.round(lat / 0.55) % 2 === 1;
      const lngStep = 1.15;
      for (let lng = -31.0; lng <= -7.0; lng += lngStep) {
        const actualLng = isOdd ? lng + lngStep * 0.5 : lng;
        HEX_GRID.push({
          lat: lat,
          lng: actualLng,
          cloudCover: 50,
          kpVal: 3.8
        });
      }
    }

    // -------------------------------------------------------------
    // GLOBAL STATE & REAL-TIME METEOROLOGICAL ENGINE
    // -------------------------------------------------------------
    let map = null;
    let canvas = null;
    let ctx = null;
    let activeConceptIdx = 0;
    let timelineHour = 0;
    let isPlaying = false;
    let playSpeed = 1;
    let animFrameId = null;
    let animTime = 0;
    let liveKp = 3.8;
    let liveLastUpdated = 'Щойно';

    // Concept definitions metadata
    const CONCEPTS_METADATA = [
      {
        id: 0,
        title: '1. Basalt Clouds & Emerald Bleed',
        icon: '🌋',
        desc: 'Темні базальтові хмари відкидають глибоку тінь. У місцях, де товщина хмари спадає, смарагдове сяйво Аврори пробивається крізь прозорі краї з ефектом підповерхневого розсіювання.',
        math: 'Transmittance = exp(-COD); FringeBleed = smoothstep(0.2, 0.7, 1 - COD)'
      },
      {
        id: 1,
        title: '2. NOAA Auroral Oval Geomagnetic Ring',
        icon: '🌐',
        desc: 'Фізичний геомагнітний овал NOAA SWPC огинає Гренландію та Північну Атлантику. Вертикальні штори Аврори підпорядковуються Kp-індексу і маскуються масами хмар.',
        math: 'OvalRadius = 22.5° - (Kp * 1.8°); Curtain(z) = sin(lng*8 + time)*cos(lat*4)'
      },
      {
        id: 2,
        title: '3. Starlight Portals & Oceanic Phosphorescence',
        icon: '✨',
        desc: 'Зоряне небо з 2,500 зірками та Чумацьким Шляхом відкривається виключно у вікнах безхмарності. Океан під чистим небом віддзеркалює зелені хвилі Аврори.',
        math: 'StarAlpha = (1 - CloudMask) * Twinkle; SeaGlow = Dot(LightVector, Normal)'
      },
      {
        id: 3,
        title: '4. Denmark Strait Synoptic Vortex',
        icon: '🌀',
        desc: 'Масштабний океанічний циклон Датської протоки закручує хмарні рукави з південного заходу. В "оці циклону" та тиловому розриві спалахує потужна корона Аврори.',
        math: 'Spiral: r = a * exp(b * theta); Vorticity = curl(V_wind)'
      },
      {
        id: 4,
        title: '5. LIDAR Transmittance Scanner',
        icon: '📡',
        desc: 'Науковий супутниковий лідар сканує оптичну густину COD променем. Зелений лазерний сектор фіксує пропускну здатність > 85% для мисливців за Авророю.',
        math: 'COD = Integral(extinction * dz); SpotQuality = (COD < 0.4 ? 100% : 0%)'
      },
      {
        id: 5,
        title: '6. Cyber-Holo Neon Contours',
        icon: '⚡',
        desc: 'Голографічний кіберпанк-радар: ізолінії хмарності пульсують неоновими контурами, а вільні коридори світяться інтерактивними синтвейв-стрічками Аврори.',
        math: 'IsoLevel(p) = fract(CloudDensity * 6); AuroraRibbon = sin(freq * x - omega * t)'
      },
      {
        id: 6,
        title: '7. 30s Long Exposure Tripod Simulation',
        icon: '📷',
        desc: 'Симуляція камери на штативі: 30-секундне розмиття руху перетворює рухомі хмари на шовковистий туман, а спалахи Аврори створюють м\'які мальовничі полотна.',
        math: 'ExposureAccumulation = Sum(Frame_t * dt, 0..30s); StarTrailAngle = omega_earth * 30s'
      },
      {
        id: 7,
        title: '8. Marine Fog & Glacier Peak Cut-Through',
        icon: '🏔️',
        desc: 'Прибережні фіорди та океан вкриті низьким шаром морського туману (сіра імла), проте піки Ватнайокюдль та вулканів пробивають інверсію у чисте сяйво неба.',
        math: 'FogCutoff = Alt_terrain > InversionHeight (650m) ? 0 : DenseFog'
      },
      {
        id: 8,
        title: '9. Hexagonal Exposure Matrix',
        icon: '⬡',
        desc: 'Геодезична сітка гексагонів обчислює рекомендовані параметри зйомки (ISO 1600, f/1.8, 8s) та ймовірність спостереження в кожному квадранті Ісландії та Атлантики.',
        math: 'P_spot = (1 - CloudCover) * (Kp / 9); RecISO = 800 * (1 + CloudCover * 2)'
      },
      {
        id: 9,
        title: '10. Solar Wind Plasma Filament Discharge',
        icon: '⚡',
        desc: 'Магнітосферні струми Біркеланда: плазмові електричні філаменти спускаються з космосу, огинають грозові хмари та створюють коронні розряди по периметру фронту.',
        math: 'BirkelandCurrent = Div(J_parallel); CoronaDischarge = Gradient(E_field)'
      }
    ];

    // -------------------------------------------------------------
    // REAL-TIME API FETCH: OPEN-METEO & NOAA SWPC
    // -------------------------------------------------------------
    async function fetchLiveMeteoData() {
      const syncBadge = document.getElementById('live-sync-indicator');
      const kpBadge = document.getElementById('sync-kp-val');
      const hudKp = document.getElementById('hud-kp-val');
      const hudCloud = document.getElementById('hud-cloud-pct');
      
      if (syncBadge) syncBadge.innerHTML = 'СИНХРОНІЗАЦІЯ З СУПУТНИКАМИ... <span class="animate-spin inline-block">⏳</span>';

      try {
        // 1. Fetch NOAA Live Kp
        try {
          const respKp = await fetch('https://services.swpc.noaa.gov/json/planetary_k_index_1m.json');
          if (respKp.ok) {
            const noaaData = await respKp.json();
            if (noaaData && noaaData.length > 0) {
              const latest = noaaData[noaaData.length - 1];
              liveKp = parseFloat(latest.kp_index) || 3.8;
            }
          }
        } catch (e) {
          console.warn('NOAA fetch fallback:', e);
          liveKp = 4.2;
        }

        // 2. Fetch Open-Meteo Iceland & Atlantic points
        const meteoUrl = 'https://api.open-meteo.com/v1/forecast?latitude=64.14,65.68,64.25,66.07,61.50,67.20&longitude=-21.94,-18.10,-15.21,-23.12,-20.00,-29.50&current=cloud_cover,wind_speed_10m,wind_direction_10m';
        try {
          const respMeteo = await fetch(meteoUrl);
          if (respMeteo.ok) {
            const meteoData = await respMeteo.json();
            if (Array.isArray(meteoData)) {
              // Update sector cloud bases
              REGIONAL_SECTORS.forEach((sec, idx) => {
                const st = meteoData[idx % meteoData.length];
                if (st && st.current) {
                  sec.cloudBase = st.current.cloud_cover !== undefined ? st.current.cloud_cover : sec.cloudBase;
                  sec.windSpeed = st.current.wind_speed_10m || sec.windSpeed;
                  sec.windDir = st.current.wind_direction_10m || sec.windDir;
                }
              });
            }
          }
        } catch (e) {
          console.warn('Open-Meteo fetch fallback:', e);
        }

        const now = new Date();
        const timeStr = now.toLocaleTimeString('uk-UA', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        liveLastUpdated = timeStr;

        if (syncBadge) {
          syncBadge.innerHTML = `VEÐURSTOFA & NOAA SWPC (Kp ${liveKp.toFixed(1)} • ${timeStr} UTC)`;
        }
        if (kpBadge) kpBadge.textContent = liveKp.toFixed(1);
        if (hudKp) hudKp.textContent = `Kp ${liveKp.toFixed(1)} • ${liveKp >= 4 ? 'СИЛЬНИЙ СПАЛАХ' : 'АКТИВНО'}`;
        
        // Calculate average cloud cover
        let avgCloud = 0;
        REGIONAL_SECTORS.forEach(s => avgCloud += s.cloudBase);
        avgCloud = Math.round(avgCloud / REGIONAL_SECTORS.length);
        if (hudCloud) hudCloud.textContent = `${avgCloud}% ПОКРИТТЯ`;

      } catch (err) {
        console.error('Master sync error:', err);
        if (syncBadge) syncBadge.textContent = 'VEÐURSTOFA & NOAA (АВТОНОМНИЙ РЕЖИМ)';
      }
    }

    // -------------------------------------------------------------
    // MAPLIBRE MAP INITIALIZATION
    // -------------------------------------------------------------
    const mapStyles = {
      dark: {
        version: 8,
        sources: {
          'esri-dark': {
            type: 'raster',
            tiles: ['https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'],
            tileSize: 256
          },
          'esri-dark-ref': {
            type: 'raster',
            tiles: ['https://services.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}'],
            tileSize: 256
          }
        },
        layers: [
          { id: 'esri-dark-base', type: 'raster', source: 'esri-dark', minzoom: 0, maxzoom: 19 },
          { id: 'esri-dark-labels', type: 'raster', source: 'esri-dark-ref', minzoom: 0, maxzoom: 19 }
        ]
      },
      satellite: {
        version: 8,
        sources: {
          'esri-sat': {
            type: 'raster',
            tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
            tileSize: 256
          }
        },
        layers: [
          { id: 'esri-sat-layer', type: 'raster', source: 'esri-sat', minzoom: 0, maxzoom: 19 }
        ]
      }
    };

    function initMap() {
      map = new maplibregl.Map({
        container: 'map',
        style: mapStyles.dark,
        center: [-19.5, 64.2], // Wide North Atlantic centering
        zoom: 5.2,
        minZoom: 4.0,
        maxZoom: 14.0,
        pitch: 0,
        bearing: 0
      });

      canvas = document.getElementById('radar-canvas');
      ctx = canvas.getContext('2d');

      function resizeCanvas() {
        if (!canvas) return;
        const rect = canvas.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
      }

      window.addEventListener('resize', resizeCanvas);
      map.on('load', () => {
        resizeCanvas();
        fetchLiveMeteoData();
        setInterval(fetchLiveMeteoData, 45000); // 45s live polling
        startAnimationLoop();
      });
    }

    function setBasemap(type) {
      document.getElementById('btn-basemap-dark').className = type === 'dark' 
        ? 'px-2.5 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold transition'
        : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition';
      document.getElementById('btn-basemap-sat').className = type === 'satellite' 
        ? 'px-2.5 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold transition'
        : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition';
      map.setStyle(mapStyles[type]);
    }

    function flyToZoom(z, center) {
      if (!map) return;
      map.flyTo({
        center: center,
        zoom: z,
        speed: 1.2,
        curve: 1.4,
        essential: true
      });
    }

    function kmToPixels(km, lat) {
      const z = map.getZoom();
      const metersPerPx = (156543.03392 * Math.cos(lat * Math.PI / 180)) / Math.pow(2, z);
      return (km * 1000) / metersPerPx;
    }

    // -------------------------------------------------------------
    // CONCEPT SWITCHER & UI CONTROL
    // -------------------------------------------------------------
    function switchConcept(idx) {
      activeConceptIdx = idx;
      
      // Update Button Styles
      for (let i = 0; i < 10; i++) {
        const btn = document.getElementById(`c-btn-${i}`);
        if (btn) {
          if (i === idx) {
            btn.className = 'concept-btn active px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition';
          } else {
            btn.className = 'concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition';
          }
        }
      }

      // Update HUD metadata
      const meta = CONCEPTS_METADATA[idx];
      if (meta) {
        document.getElementById('hud-concept-title').innerHTML = `<span>${meta.icon}</span> ${meta.title}`;
        document.getElementById('hud-concept-desc').textContent = meta.desc;
        document.getElementById('ins-math').textContent = meta.math;
      }
    }

    function toggleHudPanel() {
      const panel = document.getElementById('inspector-panel');
      if (panel) panel.classList.toggle('hidden');
    }

    function togglePlayPause() {
      isPlaying = !isPlaying;
      const btn = document.getElementById('btn-play-pause');
      btn.innerHTML = isPlaying ? '⏸️' : '▶️';
    }

    function resetTimeline() {
      timelineHour = 0;
      document.getElementById('radar-time-slider').value = 0;
      onTimelineInput(0);
    }

    function setPlaySpeed(spd) {
      playSpeed = spd;
      [1, 2, 4].forEach(s => {
        const b = document.getElementById(`spd-${s}`);
        if (b) {
          b.className = (s === spd)
            ? 'px-2 py-1 rounded-lg bg-emerald-500 text-slate-950 font-bold transition'
            : 'px-2 py-1 rounded-lg text-slate-400 hover:text-white transition';
        }
      });
    }

    function onTimelineInput(val) {
      timelineHour = parseFloat(val);
      const hInt = Math.floor(timelineHour);
      const mInt = Math.floor((timelineHour - hInt) * 60);
      const label = document.getElementById('timeline-time-label');
      if (label) {
        label.textContent = `+${hInt} год ${mInt < 10 ? '0' : ''}${mInt} хв (UTC +${timelineHour.toFixed(1)}h)`;
      }
    }

    // -------------------------------------------------------------
    // MASTER 60 FPS ANIMATION LOOP
    // -------------------------------------------------------------
    function startAnimationLoop() {
      let lastTime = performance.now();

      function loop(now) {
        const dt = Math.min(0.06, (now - lastTime) / 1000);
        lastTime = now;
        animTime += dt;

        if (isPlaying) {
          timelineHour += dt * 0.4 * playSpeed;
          if (timelineHour > 12) timelineHour = 0;
          document.getElementById('radar-time-slider').value = timelineHour;
          onTimelineInput(timelineHour);
        }

        renderActiveConcept();
        animFrameId = requestAnimationFrame(loop);
      }
      animFrameId = requestAnimationFrame(loop);
    }

    function renderActiveConcept() {
      if (!ctx || !map || !canvas) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const dpr = window.devicePixelRatio || 1;
      const advectionOffset = timelineHour * 0.45;

      switch(activeConceptIdx) {
        case 0:
          renderConcept1_BasaltBleed(dpr, advectionOffset);
          break;
        case 1:
          renderConcept2_NOAAOval(dpr, advectionOffset);
          break;
        case 2:
          renderConcept3_StarlightPortals(dpr, advectionOffset);
          break;
        case 3:
          renderConcept4_SynopticVortex(dpr, advectionOffset);
          break;
        case 4:
          renderConcept5_LidarCOD(dpr, advectionOffset);
          break;
        case 5:
          renderConcept6_CyberContours(dpr, advectionOffset);
          break;
        case 6:
          renderConcept7_LongExposureTripod(dpr, advectionOffset);
          break;
        case 7:
          renderConcept8_MarineFogGlacier(dpr, advectionOffset);
          break;
        case 8:
          renderConcept9_HexExposure(dpr, advectionOffset);
          break;
        case 9:
          renderConcept10_PlasmaFilaments(dpr, advectionOffset);
          break;
      }
    }

    // =============================================================
    // VARIATION 1: BASALT CLOUDS & EMERALD BLEED
    // =============================================================
    function renderConcept1_BasaltBleed(dpr, advOffset) {
      ctx.save();

      // 1. Vibrant Northern Lights plasma background
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      const intensity = 0.5 + Math.sin(animTime * 1.5) * 0.15 + (liveKp / 10) * 0.35;
      auroraGrad.addColorStop(0.1, 'rgba(16, 185, 129, 0.0)');
      auroraGrad.addColorStop(0.35, `rgba(16, 185, 129, ${intensity * 0.85})`);
      auroraGrad.addColorStop(0.65, `rgba(6, 182, 212, ${intensity * 0.70})`);
      auroraGrad.addColorStop(0.85, 'rgba(168, 85, 247, 0.25)');
      auroraGrad.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. Basaltic Dark Volcanic Clouds with Emerald Bleed
      SECTOR_PUFFS.forEach(p => {
        const driftLng = p.baseLng + advOffset * p.speedMult + Math.sin(animTime * 0.3 + p.phase) * 0.1;
        const driftLat = p.baseLat + advOffset * 0.25 * p.speedMult;
        const pt = map.project([driftLng, driftLat]);
        const rPx = kmToPixels(p.radiusKm, driftLat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const occludeGrad = ctx.createRadialGradient(px, py, rPx * 0.15, px, py, rPx);
        occludeGrad.addColorStop(0, 'rgba(10, 15, 28, 0.96)'); // Completely blocks aurora
        occludeGrad.addColorStop(0.65, 'rgba(15, 23, 42, 0.88)');
        occludeGrad.addColorStop(0.82, `rgba(16, 185, 129, ${0.45 * p.opacityMult})`); // Green Emerald Fringe Bleed!
        occludeGrad.addColorStop(1, 'rgba(10, 15, 28, 0.0)');

        ctx.fillStyle = occludeGrad;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // Target Spot Highlight: Lake Mývatn Clear Window
      const myv = map.project([-16.90, 65.60]);
      ctx.fillStyle = '#34d399';
      ctx.font = `bold ${12 * dpr}px monospace`;
      ctx.fillText('🔭 ВІКНО АВРОРИ: 100% ВИДИМІСТЬ (MÝVATN)', myv.x * dpr - 90 * dpr, myv.y * dpr);

      ctx.restore();
    }

    // =============================================================
    // VARIATION 2: NOAA AURORAL OVAL GEOMAGNETIC RING
    // =============================================================
    function renderConcept2_NOAAOval(dpr, advOffset) {
      ctx.save();

      // 1. Draw Physical Geomagnetic Oval across Denmark Strait, Greenland, Iceland
      const ovalCenterLat = 67.5 - (liveKp - 2) * 0.7; // Equatorward expansion on high Kp
      ctx.lineWidth = 35 * dpr;
      ctx.lineCap = 'round';

      const ovalGrad = ctx.createLinearGradient(0, 0, canvas.width, 0);
      ovalGrad.addColorStop(0, 'rgba(168, 85, 247, 0.3)');
      ovalGrad.addColorStop(0.4, 'rgba(16, 185, 129, 0.85)');
      ovalGrad.addColorStop(0.8, 'rgba(52, 211, 153, 0.9)');
      ovalGrad.addColorStop(1, 'rgba(6, 182, 212, 0.3)');

      ctx.strokeStyle = ovalGrad;
      ctx.beginPath();
      let first = true;
      for (let lng = -33; lng <= -6; lng += 0.8) {
        const wave = Math.sin(lng * 0.4 + animTime * 1.5) * 0.8;
        const pt = map.project([lng, ovalCenterLat + wave]);
        if (first) { ctx.moveTo(pt.x * dpr, pt.y * dpr); first = false; }
        else { ctx.lineTo(pt.x * dpr, pt.y * dpr); }
      }
      ctx.stroke();

      // 2. Dynamic Vertical Rayed Curtains
      for (let lng = -31; lng <= -8; lng += 1.4) {
        const wave = Math.sin(lng * 0.5 + animTime * 2.2) * 0.9;
        const pt = map.project([lng, ovalCenterLat + wave]);
        const curtainH = (70 + Math.sin(lng + animTime * 3) * 35) * dpr;

        const rayGrad = ctx.createLinearGradient(pt.x * dpr, pt.y * dpr - curtainH, pt.x * dpr, pt.y * dpr);
        rayGrad.addColorStop(0, 'rgba(236, 72, 153, 0.65)'); // Magenta top
        rayGrad.addColorStop(0.4, 'rgba(16, 185, 129, 0.85)'); // Emerald middle
        rayGrad.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

        ctx.fillStyle = rayGrad;
        ctx.fillRect(pt.x * dpr - 4 * dpr, pt.y * dpr - curtainH, 8 * dpr, curtainH);
      }

      // 3. Occlusion by oceanic & Icelandic clouds
      SECTOR_PUFFS.forEach(p => {
        const driftLng = p.baseLng + advOffset * p.speedMult;
        const driftLat = p.baseLat + advOffset * 0.25 * p.speedMult;
        const pt = map.project([driftLng, driftLat]);
        const rPx = kmToPixels(p.radiusKm, driftLat) * dpr;

        const occlude = ctx.createRadialGradient(pt.x * dpr, pt.y * dpr, rPx * 0.2, pt.x * dpr, pt.y * dpr, rPx);
        occlude.addColorStop(0, 'rgba(15, 23, 42, 0.95)');
        occlude.addColorStop(0.7, 'rgba(30, 41, 59, 0.85)');
        occlude.addColorStop(1, 'rgba(15, 23, 42, 0.0)');

        ctx.fillStyle = occlude;
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      ctx.restore();
    }

    // =============================================================
    // VARIATION 3: STARLIGHT PORTALS & OCEANIC PHOSPHORESCENCE
    // =============================================================
    function renderConcept3_StarlightPortals(dpr, advOffset) {
      ctx.save();

      // 1. Aurora Wash
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      auroraGrad.addColorStop(0.2, 'rgba(5, 150, 105, 0.15)');
      auroraGrad.addColorStop(0.5, 'rgba(16, 185, 129, 0.65)');
      auroraGrad.addColorStop(0.8, 'rgba(6, 182, 212, 0.25)');
      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. Stars rendering (Twinkling Sub-Arctic Sky)
      ASTRO_STARS.forEach((s, idx) => {
        const pt = map.project([s.lng, s.lat]);
        const alpha = Math.abs(Math.sin(animTime * s.twinkleSpeed + idx)) * 0.65 + 0.35;
        ctx.fillStyle = `rgba(224, 242, 254, ${alpha * s.brightness})`;
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, s.size * dpr, 0, Math.PI * 2);
        ctx.fill();
      });

      // 3. Dense Cloud Occlusion Masks (Hides stars + creates portals)
      SECTOR_PUFFS.forEach(p => {
        const driftLng = p.baseLng + advOffset * p.speedMult;
        const driftLat = p.baseLat + advOffset * 0.25 * p.speedMult;
        const pt = map.project([driftLng, driftLat]);
        const rPx = kmToPixels(p.radiusKm, driftLat) * dpr;

        const occlude = ctx.createRadialGradient(pt.x * dpr, pt.y * dpr, rPx * 0.25, pt.x * dpr, pt.y * dpr, rPx);
        occlude.addColorStop(0, 'rgba(8, 12, 22, 0.98)');
        occlude.addColorStop(0.75, 'rgba(15, 23, 42, 0.90)');
        occlude.addColorStop(1, 'rgba(8, 12, 22, 0.0)');

        ctx.fillStyle = occlude;
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // 4. Oceanic Water Shimmer in Clear Zones (South Coast & Greenland Sea)
      const seaPt = map.project([-19.0, 62.0]);
      const seaGrad = ctx.createRadialGradient(seaPt.x * dpr, seaPt.y * dpr, 10 * dpr, seaPt.x * dpr, seaPt.y * dpr, 180 * dpr);
      seaGrad.addColorStop(0, 'rgba(16, 185, 129, 0.35)');
      seaGrad.addColorStop(0.7, 'rgba(6, 182, 212, 0.15)');
      seaGrad.addColorStop(1, 'rgba(2, 6, 23, 0.0)');
      ctx.fillStyle = seaGrad;
      ctx.beginPath();
      ctx.arc(seaPt.x * dpr, seaPt.y * dpr, 180 * dpr, 0, Math.PI * 2);
      ctx.fill();

      ctx.restore();
    }

    // =============================================================
    // VARIATION 4: DENMARK STRAIT SYNOPTIC VORTEX (OCEAN CYCLONE)
    // =============================================================
    function renderConcept4_SynopticVortex(dpr, advOffset) {
      ctx.save();

      // Synoptic Cyclone Center in Denmark Strait
      const cycloneCenter = map.project([-26.5 + advOffset * 0.2, 65.5]);
      const cx = cycloneCenter.x * dpr;
      const cy = cycloneCenter.y * dpr;

      // 1. Background Aurora Storm in Clear Areas
      const auroraGrad = ctx.createRadialGradient(cx, cy, 20 * dpr, cx, cy, 500 * dpr);
      auroraGrad.addColorStop(0, 'rgba(16, 185, 129, 0.85)'); // Cyclone Eye is Crystal Clear!
      auroraGrad.addColorStop(0.2, 'rgba(52, 211, 153, 0.6)');
      auroraGrad.addColorStop(0.5, 'rgba(6, 182, 212, 0.35)');
      auroraGrad.addColorStop(1, 'rgba(2, 6, 23, 0.0)');
      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. Cyclonic Logarithmic Cloud Arms
      const armCount = 4;
      for (let a = 0; a < armCount; a++) {
        const baseAngle = (a * Math.PI * 2) / armCount + animTime * 0.5;
        ctx.beginPath();
        for (let r = 30 * dpr; r < 450 * dpr; r += 12 * dpr) {
          const theta = baseAngle + Math.log(r / (25 * dpr)) * 1.8;
          const px = cx + Math.cos(theta) * r;
          const py = cy + Math.sin(theta) * r;

          ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
          ctx.beginPath();
          ctx.arc(px, py, 22 * dpr + (r / 20), 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Eye of Cyclone Label
      ctx.fillStyle = '#6ee7b7';
      ctx.font = `bold ${11 * dpr}px monospace`;
      ctx.fillText('🌀 ОКО ЦИКЛОНУ (ЧИСТЕ ВІКНО АВРОРИ)', cx - 80 * dpr, cy - 25 * dpr);

      ctx.restore();
    }

    // =============================================================
    // VARIATION 5: SCIENTIFIC LIDAR TRANSMITTANCE SCANNER & COD
    // =============================================================
    let lidarScanAngle = 0;
    function renderConcept5_LidarCOD(dpr, advOffset) {
      ctx.save();
      lidarScanAngle += 0.03;

      // Draw Aurora background
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      auroraGrad.addColorStop(0.3, 'rgba(16, 185, 129, 0.65)');
      auroraGrad.addColorStop(0.7, 'rgba(6, 182, 212, 0.45)');
      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Occluding cloud bodies
      SECTOR_PUFFS.forEach(p => {
        const pt = map.project([p.baseLng + advOffset * p.speedMult, p.baseLat]);
        const rPx = kmToPixels(p.radiusKm, p.baseLat) * dpr;

        ctx.fillStyle = 'rgba(15, 23, 42, 0.94)';
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // LIDAR Scanner Origin (Reykjavík Weather Radar)
      const radarPt = map.project([-21.94, 64.14]);
      const rx = radarPt.x * dpr;
      const ry = radarPt.y * dpr;
      const scanRadius = Math.max(canvas.width, canvas.height) * 0.75;

      // Sweeping LIDAR Laser Beam
      const beamGrad = ctx.createRadialGradient(rx, ry, 5 * dpr, rx, ry, scanRadius);
      beamGrad.addColorStop(0, 'rgba(52, 211, 153, 0.9)');
      beamGrad.addColorStop(0.5, 'rgba(16, 185, 129, 0.35)');
      beamGrad.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(rx, ry);
      ctx.arc(rx, ry, scanRadius, lidarScanAngle, lidarScanAngle + 0.35);
      ctx.closePath();
      ctx.fillStyle = beamGrad;
      ctx.fill();
      ctx.restore();

      // LIDAR Transmittance HUD
      ctx.strokeStyle = 'rgba(52, 211, 153, 0.5)';
      ctx.lineWidth = 1 * dpr;
      [150, 300, 450].forEach(r => {
        ctx.beginPath();
        ctx.arc(rx, ry, r * dpr, 0, Math.PI * 2);
        ctx.stroke();
      });

      ctx.fillStyle = '#34d399';
      ctx.font = `bold ${10 * dpr}px monospace`;
      ctx.fillText('📡 LIDAR COD: 0.12 (TRANSMITTANCE 94%)', rx + 15 * dpr, ry - 15 * dpr);

      ctx.restore();
    }

    // =============================================================
    // VARIATION 6: CYBER-HOLO NEON CONTOURS & SYNTHWAVE GLOW
    // =============================================================
    function renderConcept6_CyberContours(dpr, advOffset) {
      ctx.save();

      // 1. Synthwave Neon Aurora Curtains
      const cybGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      cybGrad.addColorStop(0.1, 'rgba(168, 85, 247, 0.2)');
      cybGrad.addColorStop(0.4, 'rgba(6, 182, 212, 0.7)');
      cybGrad.addColorStop(0.65, 'rgba(16, 185, 129, 0.85)');
      cybGrad.addColorStop(0.9, 'rgba(236, 72, 153, 0.3)');
      ctx.fillStyle = cybGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. Dark Cloud Masses with Electric Neon Isolines
      SECTOR_PUFFS.forEach(p => {
        const pt = map.project([p.baseLng + advOffset * p.speedMult, p.baseLat]);
        const rPx = kmToPixels(p.radiusKm, p.baseLat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        // Dark Occlusion Body
        ctx.fillStyle = 'rgba(8, 12, 24, 0.95)';
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();

        // Neon Contour Rings
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.8)';
        ctx.lineWidth = 1.5 * dpr;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.stroke();

        ctx.strokeStyle = 'rgba(16, 185, 129, 0.6)';
        ctx.beginPath();
        ctx.arc(px, py, rPx * 0.6, 0, Math.PI * 2);
        ctx.stroke();
      });

      ctx.restore();
    }

    // =============================================================
    // VARIATION 7: 30S LONG EXPOSURE TRIPOD SIMULATION
    // =============================================================
    function renderConcept7_LongExposureTripod(dpr, advOffset) {
      ctx.save();

      // Silky Smooth motion-blurred Aurora Curtains
      for (let layer = 0; layer < 3; layer++) {
        const ribbonGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
        ribbonGrad.addColorStop(0.2, 'rgba(16, 185, 129, 0.0)');
        ribbonGrad.addColorStop(0.5, `rgba(16, 185, 129, ${0.45 + layer * 0.15})`);
        ribbonGrad.addColorStop(0.8, 'rgba(5, 150, 105, 0.0)');

        ctx.fillStyle = ribbonGrad;
        ctx.beginPath();
        ctx.moveTo(0, canvas.height * (0.3 + layer * 0.15));
        for (let x = 0; x <= canvas.width; x += 30) {
          const y = canvas.height * (0.3 + layer * 0.15) + Math.sin(x * 0.004 + animTime * 0.8 + layer) * (60 * dpr);
          ctx.lineTo(x, y);
        }
        ctx.lineTo(canvas.width, canvas.height);
        ctx.lineTo(0, canvas.height);
        ctx.closePath();
        ctx.fill();
      }

      // Motion-blurred smoky clouds
      SECTOR_PUFFS.forEach(p => {
        const pt = map.project([p.baseLng + advOffset * p.speedMult, p.baseLat]);
        const rPx = kmToPixels(p.radiusKm, p.baseLat) * dpr;

        // Soft blurred streak
        const streakGrad = ctx.createRadialGradient(pt.x * dpr, pt.y * dpr, rPx * 0.1, pt.x * dpr, pt.y * dpr, rPx * 1.3);
        streakGrad.addColorStop(0, 'rgba(15, 23, 42, 0.92)');
        streakGrad.addColorStop(0.7, 'rgba(30, 41, 59, 0.6)');
        streakGrad.addColorStop(1, 'rgba(15, 23, 42, 0.0)');

        ctx.fillStyle = streakGrad;
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx * 1.3, 0, Math.PI * 2);
        ctx.fill();
      });

      // Camera HUD Overlay
      ctx.fillStyle = '#ffffff';
      ctx.font = `bold ${10 * dpr}px monospace`;
      ctx.fillText('📷 TRIPOD EXPOSURE: 30s • ISO 3200 • f/1.4 RAW', 20 * dpr, canvas.height - 35 * dpr);

      ctx.restore();
    }

    // =============================================================
    // VARIATION 8: MARINE FOG & GLACIER PEAK CUT-THROUGH
    // =============================================================
    function renderConcept8_MarineFogGlacier(dpr, advOffset) {
      ctx.save();

      // Dazzling Clear Sky Aurora Dome
      const skyGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      skyGrad.addColorStop(0.1, 'rgba(16, 185, 129, 0.85)');
      skyGrad.addColorStop(0.4, 'rgba(52, 211, 153, 0.7)');
      skyGrad.addColorStop(0.8, 'rgba(6, 182, 212, 0.3)');
      ctx.fillStyle = skyGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Low-Altitude Marine Fog blanket (Opaque Grey/White on Oceans & Coasts)
      const fogGrad = ctx.createLinearGradient(0, canvas.height * 0.4, 0, canvas.height);
      fogGrad.addColorStop(0, 'rgba(148, 163, 184, 0.0)');
      fogGrad.addColorStop(0.3, 'rgba(100, 116, 139, 0.88)');
      fogGrad.addColorStop(1, 'rgba(51, 65, 85, 0.95)');
      ctx.fillStyle = fogGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Glacier Summits Piercing the Fog Layer (Vatnajökull 2,110m, Eyjafjallajökull, Snæfellsjökull)
      const summits = [
        { name: 'ВАТНАЙОКЮДЛЬ (2,110м)', lng: -16.80, lat: 64.40, radius: 45 },
        { name: 'ЕЙЯФ\'ЯДЛАЙОКЮДЛЬ (1,666м)', lng: -19.62, lat: 63.63, radius: 28 },
        { name: 'СНАЙФЕДЛЬСЙОКЮДЛЬ (1,446м)', lng: -23.77, lat: 64.80, radius: 24 }
      ];

      summits.forEach(s => {
        const pt = map.project([s.lng, s.lat]);
        const rPx = kmToPixels(s.radius, s.lat) * dpr;

        // Cut through fog mask (Clear aperture)
        ctx.save();
        ctx.globalCompositeOperation = 'destination-out';
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();

        // Radiance Ring
        ctx.strokeStyle = '#34d399';
        ctx.lineWidth = 2 * dpr;
        ctx.beginPath();
        ctx.arc(pt.x * dpr, pt.y * dpr, rPx, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = '#34d399';
        ctx.font = `bold ${10 * dpr}px monospace`;
        ctx.fillText(`🏔️ ${s.name} • НАД ТУМАНОМ`, pt.x * dpr - 65 * dpr, pt.y * dpr - rPx - 8 * dpr);
      });

      ctx.restore();
    }

    // =============================================================
    // VARIATION 9: HEXAGONAL EXPOSURE MATRIX
    // =============================================================
    function renderConcept9_HexExposure(dpr, advOffset) {
      ctx.save();

      // Aurora background
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      auroraGrad.addColorStop(0.3, 'rgba(16, 185, 129, 0.45)');
      auroraGrad.addColorStop(0.7, 'rgba(6, 182, 212, 0.35)');
      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Render Hex Grid Cells
      HEX_GRID.forEach((cell, idx) => {
        const pt = map.project([cell.lng, cell.lat]);
        const px = pt.x * dpr;
        const py = pt.y * dpr;
        const hexSize = 22 * dpr;

        if (px < -50 || px > canvas.width + 50 || py < -50 || py > canvas.height + 50) return;

        // Dynamic cloud coverage simulation per hex
        const distToMyvatn = Math.hypot(cell.lng - (-16.9), cell.lat - 65.6);
        const isClearZone = distToMyvatn < 2.5;

        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
          const angle = (i * Math.PI) / 3;
          const x = px + hexSize * Math.cos(angle);
          const y = py + hexSize * Math.sin(angle);
          if (i === 0) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.closePath();

        if (isClearZone) {
          // Clear sky hex: Green pulse & camera recommendation
          ctx.fillStyle = 'rgba(16, 185, 129, 0.28)';
          ctx.strokeStyle = '#34d399';
          ctx.lineWidth = 1.5 * dpr;
          ctx.fill();
          ctx.stroke();
        } else {
          // Cloud covered hex: Dark occlusion
          ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
          ctx.strokeStyle = 'rgba(51, 65, 85, 0.5)';
          ctx.lineWidth = 1 * dpr;
          ctx.fill();
          ctx.stroke();
        }
      });

      // Target Hex Callout
      const myv = map.project([-16.9, 65.6]);
      ctx.fillStyle = '#6ee7b7';
      ctx.font = `bold ${11 * dpr}px monospace`;
      ctx.fillText('⬡ CELL #84: ISO 1600 • 8s • f/1.8 (95% ЧАНС)', myv.x * dpr - 80 * dpr, myv.y * dpr + 35 * dpr);

      ctx.restore();
    }

    // =============================================================
    // VARIATION 10: SOLAR WIND PLASMA FILAMENTS (BIRKELAND CURRENTS)
    // =============================================================
    function renderConcept10_PlasmaFilaments(dpr, advOffset) {
      ctx.save();

      // 1. Plasma Glow Base
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      auroraGrad.addColorStop(0.2, 'rgba(16, 185, 129, 0.5)');
      auroraGrad.addColorStop(0.6, 'rgba(6, 182, 212, 0.4)');
      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. High-Energy Electric Plasma Filaments snaking from space
      const filamentCount = 8;
      for (let f = 0; f < filamentCount; f++) {
        const startLng = -32 + f * 3.5;
        ctx.strokeStyle = f % 2 === 0 ? 'rgba(52, 211, 153, 0.95)' : 'rgba(236, 72, 153, 0.85)';
        ctx.lineWidth = (2 + (f % 3)) * dpr;
        ctx.beginPath();

        let ptStart = map.project([startLng, 69.0]);
        ctx.moveTo(ptStart.x * dpr, ptStart.y * dpr);

        for (let lat = 68.5; lat >= 61.0; lat -= 0.6) {
          const jitterLng = startLng + Math.sin(lat * 3 + animTime * 4 + f) * 0.7;
          const pt = map.project([jitterLng, lat]);
          ctx.lineTo(pt.x * dpr, pt.y * dpr);
        }
        ctx.stroke();
      }

      // 3. Dense Dark Basalt Clouds with Corona Edge Discharges
      SECTOR_PUFFS.forEach(p => {
        const pt = map.project([p.baseLng + advOffset * p.speedMult, p.baseLat]);
        const rPx = kmToPixels(p.radiusKm, p.baseLat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        // Dark Body
        ctx.fillStyle = 'rgba(15, 23, 42, 0.96)';
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();

        // Corona Edge Discharge Sparkle
        ctx.strokeStyle = `rgba(52, 211, 153, ${0.4 + Math.sin(animTime * 6 + p.phase) * 0.4})`;
        ctx.lineWidth = 2 * dpr;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.stroke();
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // INITIALIZATION ON WINDOW LOAD
    // -------------------------------------------------------------
    window.addEventListener('DOMContentLoaded', () => {
      initMap();
    });
  </script>
</body>
</html>
'''

with open(LAB_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

with open(BRAIN_LAB_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print(f"Successfully built cloud_radar_lab.html (size: {len(HTML_CONTENT)} bytes)")
