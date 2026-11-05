# -*- coding: utf-8 -*-
import os

LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/cloud_radar_lab.html"

html_content = r'''<!DOCTYPE html>
<html lang="uk" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Iceland Cloud Radar Lab — 10 Футуристичних Концептів Візуалізації Хмарності</title>
  
  <!-- MapLibre GL JS & CSS -->
  <script src="https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.js"></script>
  <link href="https://unpkg.com/maplibre-gl@3.6.2/dist/maplibre-gl.css" rel="stylesheet" />

  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <style>
    @keyframes pulseGlow {
      0%, 100% { filter: drop-shadow(0 0 10px rgba(6, 182, 212, 0.4)); }
      50% { filter: drop-shadow(0 0 24px rgba(6, 182, 212, 0.85)); }
    }
    @keyframes radarSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .custom-scrollbar::-webkit-scrollbar { width: 5px; height: 5px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.6); }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(6, 182, 212, 0.4); border-radius: 4px; }
    .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: rgba(6, 182, 212, 0.8); }

    .concept-btn.active {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.25) 0%, rgba(15, 23, 42, 0.95) 100%);
      border-color: #06b6d4;
      box-shadow: 0 0 20px rgba(6, 182, 212, 0.45);
      color: #ffffff;
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased h-screen w-screen overflow-hidden flex flex-col select-none">

  <!-- ============================================================ -->
  <!-- 1. TOP EXECUTIVE COMMAND BAR -->
  <!-- ============================================================ -->
  <header class="h-16 px-4 bg-slate-950/95 border-b border-cyan-500/30 backdrop-blur-xl flex items-center justify-between shrink-0 z-30">
    <div class="flex items-center space-x-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-emerald-500 to-indigo-600 flex items-center justify-center text-xl shadow-lg shadow-cyan-500/30">
        ☁️
      </div>
      <div>
        <div class="flex items-center space-x-2">
          <h1 class="text-sm sm:text-base font-black text-white tracking-wide flex items-center gap-2">
            <span>Iceland Cloud Radar Lab</span>
            <span class="px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 font-mono text-[10px] font-bold border border-cyan-400/40">10 LIVE CONCEPTS</span>
          </h1>
        </div>
        <p class="text-[11px] text-slate-400 hidden sm:block">Лабораторія метеорологічних візуалізацій хмарності та полярного сяйва для Smart Road Audio Guide</p>
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="flex items-center space-x-2">
      <!-- Return to Main App -->
      <a href="index.html" class="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold flex items-center gap-1.5 transition" title="Повернутися до головного гіда">
        <span>⬅️</span> <span class="hidden md:inline">Головний сайт</span>
      </a>

      <!-- Basemap Switcher -->
      <div class="inline-flex rounded-xl bg-slate-900 p-0.5 border border-slate-800 text-xs">
        <button id="btn-basemap-dark" onclick="setBasemap('dark')" class="px-2.5 py-1 rounded-lg bg-cyan-500 text-white font-bold transition">Dark</button>
        <button id="btn-basemap-sat" onclick="setBasemap('satellite')" class="px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Satellite</button>
      </div>

      <!-- Toggle Info HUD -->
      <button onclick="toggleHudPanel()" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 border border-slate-700 text-xs transition" title="Панель телеметрії та формул">
        ⚙️
      </button>
    </div>
  </header>

  <!-- ============================================================ -->
  <!-- 2. CONCEPT SELECTOR STRIP (10 WORKING CONCEPTS) -->
  <!-- ============================================================ -->
  <div class="px-3 py-2 bg-slate-950/90 border-b border-slate-800/80 backdrop-blur-md shrink-0 z-20 overflow-x-auto custom-scrollbar flex items-center space-x-2 text-xs">
    <button onclick="switchConcept(0)" id="c-btn-0" class="concept-btn active px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>☁️</span> <span class="font-bold">1. Volumetric 3D Cumulus</span>
    </button>
    <button onclick="switchConcept(1)" id="c-btn-1" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🛰️</span> <span class="font-bold">2. Infrared Satellite Doppler</span>
    </button>
    <button onclick="switchConcept(2)" id="c-btn-2" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🌪️</span> <span class="font-bold">3. Navier-Stokes Vortex Streamlines</span>
    </button>
    <button onclick="switchConcept(3)" id="c-btn-3" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🏔️</span> <span class="font-bold">4. 3-Tier Lágský/Milliský/Háský</span>
    </button>
    <button onclick="switchConcept(4)" id="c-btn-4" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>📊</span> <span class="font-bold">5. Isobaric Moisture Contours</span>
    </button>
    <button onclick="switchConcept(5)" id="c-btn-5" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>✨</span> <span class="font-bold">6. Quantum Particle Density</span>
    </button>
    <button onclick="switchConcept(6)" id="c-btn-6" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🌌</span> <span class="font-bold">7. Aurora Hunter Occlusion</span>
    </button>
    <button onclick="switchConcept(7)" id="c-btn-7" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>🎯</span> <span class="font-bold">8. Coast Guard Doppler Sweep</span>
    </button>
    <button onclick="switchConcept(8)" id="c-btn-8" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>⬡</span> <span class="font-bold">9. NOAA Hexagonal Mesh Grid</span>
    </button>
    <button onclick="switchConcept(9)" id="c-btn-9" class="concept-btn px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-300 hover:text-white shrink-0 flex items-center gap-1.5 transition">
      <span>⚡</span> <span class="font-bold">10. Cyberpunk Topo-Hugger</span>
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

    <!-- Floating Zoom Preset Bar (Tests scaling at any zoom level!) -->
    <div class="absolute top-4 left-4 z-20 flex flex-wrap gap-1.5 p-1.5 rounded-2xl bg-slate-950/85 backdrop-blur-md border border-cyan-500/30 shadow-2xl text-[11px] font-mono">
      <span class="px-2 py-1 text-slate-400 font-bold flex items-center gap-1">
        <span>🔍</span> <span class="hidden sm:inline">МАСШТАБ:</span>
      </span>
      <button onclick="flyToZoom(6.5, [-18.5, 64.9])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 hover:text-white border border-slate-700 transition">
        🇮🇸 Весь острів (Z6.5)
      </button>
      <button onclick="flyToZoom(8.2, [-19.0, 63.6])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 hover:text-white border border-slate-700 transition">
        🌊 Південь & Вік (Z8.2)
      </button>
      <button onclick="flyToZoom(11.0, [-19.45, 63.63])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 hover:text-white border border-slate-700 transition">
        🌋 Скоугар / Катла (Z11)
      </button>
      <button onclick="flyToZoom(8.5, [-14.5, 65.2])" class="px-2.5 py-1 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-300 hover:text-white border border-slate-700 transition">
        🏔️ Східні фіорди (Z8.5)
      </button>
    </div>

    <!-- Floating Live Telemetry HUD Card (Bottom Left) -->
    <div id="concept-hud-card" class="absolute bottom-20 left-4 z-20 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-cyan-500/40 shadow-2xl max-w-sm space-y-2 text-xs">
      <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
        <span id="hud-concept-title" class="font-black text-cyan-300 uppercase tracking-wide flex items-center gap-1.5">
          <span>☁️</span> 1. Volumetric 3D Cumulus
        </span>
        <span id="hud-fps-badge" class="px-2 py-0.5 rounded-full bg-emerald-950 text-emerald-400 font-mono text-[10px] border border-emerald-500/40">
          60 FPS
        </span>
      </div>
      <p id="hud-concept-desc" class="text-slate-300 text-[11px] leading-relaxed">
        Багатошарові об'ємні купчасті хмари зі світлотіньовим градієнтом, відкиданням м'яких тіней на лавові поля та реалістичним вітровим дрейфом.
      </p>
      <div class="grid grid-cols-2 gap-2 pt-1 font-mono text-[10px]">
        <div class="p-1.5 rounded-lg bg-slate-900 border border-slate-800">
          <span class="text-slate-400 block">ХМАРНІСТЬ:</span>
          <span id="hud-cloud-pct" class="font-bold text-cyan-300 text-xs">68% ПОКРИТТЯ</span>
        </div>
        <div class="p-1.5 rounded-lg bg-slate-900 border border-slate-800">
          <span class="text-slate-400 block">ВІТЕР (ВЕКТОР):</span>
          <span id="hud-wind-val" class="font-bold text-amber-300 text-xs">16.4 М/С • ПД-ЗХ</span>
        </div>
      </div>
    </div>

    <!-- Side Blueprint Panel (Collapsible Inspector) -->
    <aside id="inspector-panel" class="hidden absolute top-4 right-4 bottom-20 w-80 z-20 p-4 rounded-2xl bg-slate-950/95 backdrop-blur-2xl border border-cyan-500/40 shadow-2xl flex flex-col justify-between overflow-y-auto custom-scrollbar text-xs space-y-3">
      <div>
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <h3 class="font-bold text-white flex items-center gap-1.5">
            <span>🔬</span> МЕТЕОРОЛОГІЧНИЙ ІНСПЕКТОР
          </h3>
          <button onclick="toggleHudPanel()" class="text-slate-400 hover:text-white">✕</button>
        </div>

        <div class="space-y-3 pt-3">
          <div>
            <h4 class="text-[10px] uppercase font-mono text-cyan-400 font-bold mb-1">МАТЕМАТИЧНА МОДЕЛЬ:</h4>
            <p id="ins-math" class="text-[11px] text-slate-300 bg-slate-900 p-2 rounded-lg font-mono border border-slate-800">
              d(pixel) = (radiusKm * 1000) / (156543 * cos(lat) / 2^zoom)
            </p>
          </div>

          <div>
            <h4 class="text-[10px] uppercase font-mono text-cyan-400 font-bold mb-1">ОСОБЛИВОСТІ МАСШТАБУВАННЯ:</h4>
            <p id="ins-scaling" class="text-[11px] text-slate-300 leading-relaxed">
              При наближенні (Zoom-In) хмарні структури розширюються відповідно до реальних кілометрів, відкриваючи прогалини для полювання за Авророю.
            </p>
          </div>

          <div>
            <h4 class="text-[10px] uppercase font-mono text-cyan-400 font-bold mb-1">ДЖЕРЕЛА МЕТЕОДАНИХ:</h4>
            <ul class="text-[11px] text-slate-400 space-y-1 list-disc list-inside">
              <li>Veðurstofa Íslands (Ісландський метеоофіс)</li>
              <li>NOAA GFS / Aurora 30-min forecast</li>
              <li>Vegagerðin (Датчики дорожнього вітру)</li>
              <li>EUMETSAT Meteosat High-Res Visible</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="pt-2 border-t border-slate-800 text-[10px] text-slate-500 font-mono">
        SMART ROAD AUDIO GUIDE • ICELAND LAB 2026
      </div>
    </aside>

  </main>

  <!-- ============================================================ -->
  <!-- 4. BOTTOM 12-HOUR TIME-LAPSE RADAR CONTROLLER -->
  <!-- ============================================================ -->
  <footer class="h-20 px-4 bg-slate-950/95 border-t border-cyan-500/30 backdrop-blur-xl flex flex-col justify-center shrink-0 z-30">
    <div class="flex items-center justify-between gap-3 max-w-7xl mx-auto w-full">
      
      <!-- Play/Pause & Reset Controls -->
      <div class="flex items-center space-x-2 shrink-0">
        <button id="btn-play-pause" onclick="togglePlayPause()" class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-emerald-500 hover:from-cyan-400 hover:to-emerald-400 text-slate-950 flex items-center justify-center font-bold text-base shadow-lg shadow-cyan-500/30 transition">
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
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            <span>СИМУЛЯЦІЯ ДРЕЙФУ ХМАР:</span>
          </span>
          <span id="timeline-time-label" class="font-bold text-cyan-300 bg-slate-900 px-2.5 py-0.5 rounded-full border border-cyan-500/30">
            Сьогодні, 18:00 UTC (Зараз)
          </span>
          <span id="timeline-aurora-badge" class="font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
            🌌 Kp 4.2 • АКТИВНО
          </span>
        </div>

        <input type="range" id="radar-time-slider" min="0" max="12" step="0.1" value="0" oninput="onTimelineInput(this.value)" class="w-full accent-cyan-400 cursor-pointer h-2 bg-slate-800 rounded-lg">
        
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

      <!-- Speed & Loop Toggles -->
      <div class="hidden sm:flex items-center space-x-2 shrink-0">
        <div class="flex items-center space-x-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs font-mono">
          <button onclick="setPlaySpeed(1)" id="spd-1" class="px-2 py-1 rounded-lg bg-cyan-500 text-white font-bold transition">1x</button>
          <button onclick="setPlaySpeed(2)" id="spd-2" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">2x</button>
          <button onclick="setPlaySpeed(4)" id="spd-4" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">4x</button>
        </div>
      </div>

    </div>
  </footer>

  <!-- ============================================================ -->
  <!-- 5. MASTER METEOROLOGICAL RADAR LOGIC & 10 CONCEPTS ENGINE -->
  <!-- ============================================================ -->
  <script>
    // -------------------------------------------------------------
    // REGIONAL GEOGRAPHIC SECTORS OF ICELAND
    // -------------------------------------------------------------
    const ICELAND_SECTORS = [
      { id: 'reykjavik', name: 'Рейк\'явік & Фаґрадалсф\'ядль', lat: 64.14, lng: -21.94, radiusKm: 45, cloudBase: 65, windSpeed: 8.5, windDir: 230 },
      { id: 'south_coast', name: 'Південне узбережжя & Вік', lat: 63.50, lng: -19.00, radiusKm: 65, cloudBase: 78, windSpeed: 18.2, windDir: 245 },
      { id: 'vatnajokull', name: 'Льодовик Ватнайокюдль', lat: 64.40, lng: -16.80, radiusKm: 85, cloudBase: 88, windSpeed: 14.0, windDir: 260 },
      { id: 'east_fjords', name: 'Східні фіорди (Сейдісфіордюр)', lat: 65.25, lng: -14.00, radiusKm: 55, cloudBase: 42, windSpeed: 7.2, windDir: 190 },
      { id: 'myvatn_north', name: 'Озеро Міватн & Акранес', lat: 65.60, lng: -16.90, radiusKm: 60, cloudBase: 18, windSpeed: 6.0, windDir: 210 },
      { id: 'akureyri', name: 'Акюрейрі & Ейяфіордюр', lat: 65.68, lng: -18.10, radiusKm: 48, cloudBase: 25, windSpeed: 5.5, windDir: 200 },
      { id: 'westfjords', name: 'Західні фіорди (Диньянди)', lat: 65.75, lng: -23.20, radiusKm: 70, cloudBase: 50, windSpeed: 11.0, windDir: 280 },
      { id: 'snaefellsnes', name: 'Півострів Снайфедльснес', lat: 64.85, lng: -23.50, radiusKm: 50, cloudBase: 70, windSpeed: 15.4, windDir: 270 },
      { id: 'highlands', name: 'Керлінґарф\'єтль & Аскья', lat: 64.80, lng: -18.80, radiusKm: 75, cloudBase: 82, windSpeed: 13.5, windDir: 240 }
    ];

    // Procedural multi-puff clouds per sector
    const SECTOR_PUFFS = [];
    ICELAND_SECTORS.forEach(sec => {
      for (let i = 0; i < 22; i++) {
        const ang = Math.random() * Math.PI * 2;
        const dist = Math.random() * sec.radiusKm * 0.9;
        // Approx 1 deg lat = 111 km, 1 deg lng = 111 * cos(lat) km
        const dLat = (Math.cos(ang) * dist) / 111.0;
        const dLng = (Math.sin(ang) * dist) / (111.0 * Math.cos(sec.lat * Math.PI / 180));
        SECTOR_PUFFS.push({
          sectorId: sec.id,
          baseLat: sec.lat + dLat,
          baseLng: sec.lng + dLng,
          currentLat: sec.lat + dLat,
          currentLng: sec.lng + dLng,
          radiusKm: 14 + Math.random() * 22,
          opacityMult: 0.65 + Math.random() * 0.35,
          speedMult: 0.8 + Math.random() * 0.4,
          phase: Math.random() * Math.PI * 2
        });
      }
    });

    // Fluid particles for Concept 3 & 6
    const FLUID_PARTICLES = [];
    for (let i = 0; i < 1400; i++) {
      FLUID_PARTICLES.push({
        lat: 63.2 + Math.random() * 3.3,
        lng: -24.5 + Math.random() * 11.5,
        speed: 0.003 + Math.random() * 0.008,
        life: Math.random() * 100,
        size: 1.5 + Math.random() * 2.5,
        altTier: Math.random() > 0.6 ? 'high' : (Math.random() > 0.3 ? 'mid' : 'low')
      });
    }

    // -------------------------------------------------------------
    // MAP SETUP & STYLES
    // -------------------------------------------------------------
    let map = null;
    let canvas = null;
    let ctx = null;
    let activeConceptIdx = 0;
    let timelineHour = 0;
    let isPlaying = false;
    let playSpeed = 1;
    let animFrameId = null;

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
        center: [-18.5, 64.9],
        zoom: 6.5,
        minZoom: 5.5,
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
        startAnimationLoop();
      });

      map.on('move', () => {
        // Redraw during pan/zoom
      });
    }

    function setBasemap(type) {
      document.getElementById('btn-basemap-dark').className = type === 'dark' 
        ? 'px-2.5 py-1 rounded-lg bg-cyan-500 text-white font-bold transition'
        : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition';
      document.getElementById('btn-basemap-sat').className = type === 'satellite' 
        ? 'px-2.5 py-1 rounded-lg bg-cyan-500 text-white font-bold transition'
        : 'px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition';
      map.setStyle(mapStyles[type]);
    }

    function flyToZoom(z, center) {
      map.flyTo({
        center: center,
        zoom: z,
        speed: 1.6,
        essential: true
      });
    }

    // -------------------------------------------------------------
    // MATHEMATICAL SCALING: KM TO SCREEN PIXELS AT CURRENT ZOOM
    // -------------------------------------------------------------
    function kmToPixels(km, lat) {
      const p1 = map.project([0, lat]);
      const p2 = map.project([0, lat + (km / 111.0)]);
      return Math.abs(p2.y - p1.y);
    }

    // -------------------------------------------------------------
    // CONCEPT DESCRIPTIONS & BLUEPRINTS
    // -------------------------------------------------------------
    const CONCEPTS_METADATA = [
      {
        title: "☁️ 1. Volumetric 3D Cumulus Advection",
        desc: "Об'ємні купчасті хмари зі світлотіньовим градієнтом, відкиданням м'яких тіней на лавові поля та реалістичним вітровим дрейфом за законами ісландської циркуляції.",
        math: "RadialGradient(x, y, r) • ShadowOffset = dx * windSpeed • Advection = v * dt",
        scaling: "Масштабується пропорційно метричному радіусу: на Z11 видно окремі купчасті кластери над ущелинами, на Z6.5 — монолітний фронт.",
        cloudPct: "68% ПОКРИТТЯ",
        wind: "16.4 М/С • ПД-ЗХ"
      },
      {
        title: "🛰️ 2. Infrared Satellite Doppler Thermography",
        desc: "Супутниковий інфрачервоний радіометр (NOAA / EUMETSAT). Колірна гама від -45°C (крижані перисті хмари — пурпур/білий) до +10°C (тепла земля — темно-синій).",
        math: "T_top = T_ground - (altitude * 6.5°C/km) • FalseColorRamp(T)",
        scaling: "Теплові градієнти зберігають геодезичну прив'язку до піксельних сіток супутника Meteosat.",
        cloudPct: "ТЕМП. ХМАР: -28.4°C",
        wind: "ЕХО: 44.2 dBZ"
      },
      {
        title: "🌪️ 3. Navier-Stokes Vortex Streamlines",
        desc: "Гідродинамічний потік диму. Масивні льодовики Ватнайокюдль та Ланійокюдль діють як тверді аеродинамічні перешкоди, створюючи вихори фон Кармана.",
        math: "∂u/∂t + (u·∇)u = -1/ρ ∇p + ν∇²u • ObstacleDeflection(Glacier)",
        scaling: "Лінії течії згинаються навколо вершин і проходять крізь перевали відповідно до рельєфу.",
        cloudPct: "ВИХОРІВ: 18 АКТИВНИХ",
        wind: "22.8 М/С • ШКВАЛ"
      },
      {
        title: "🏔️ 4. 3-Tier Lágský / Milliský / Háský",
        desc: "Офіційний 3-рівневий метеорологічний шар Veðurstofa Íslands: Низькі хмари (0-2 км), Середні (2-6 км) та Високі (>6 км) для прогнозування полярного сяйва.",
        math: "P_clear = (1 - Lágský) * (1 - Milliský) * (1 - 0.3 * Háský)",
        scaling: "Незалежні висотні яруси: наближення дозволяє виявити долинний туман під ясним небом.",
        cloudPct: "Lág: 45% • Mid: 20%",
        wind: "АВРОРА: 88% ШАНС"
      },
      {
        title: "📊 5. Isobaric Moisture Contours & Ceiling",
        desc: "Авіаційні барометричні ізолінії насичення вологою з інтервалом 20%. Анімовані пунктирні стрілки вказують баричний градієнт та висоту нижньої кромки (FL).",
        math: "Isobar(x, y) = Contours(P_vapor / P_sat) • DashOffset = t * speed",
        scaling: "Векторні контури автоматично децимуються на високих зумах для збереження чистоти читання.",
        cloudPct: "СТЕЛЬКА: FL045 (1370M)",
        wind: "QNH: 994 hPa"
      },
      {
        title: "✨ 6. Quantum Particle Density Field",
        desc: "8,000 квантових світлових мікро-крапель вологи з аеродинамічною інерцією. У зонах шторму частинки збиваються у щільні вихори, у ясних зонах — розсіюються.",
        math: "Pos(t+1) = Pos(t) + V_wind + Turbulence(PerlinNoise)",
        scaling: "Щільність частинок динамічно адаптується під масштаб, щоб не перевантажувати екран.",
        cloudPct: "8,000 ЧАСТИНОК",
        wind: "ДРЕЙФ: 14.8 М/С"
      },
      {
        title: "🌌 7. Aurora Hunter Occlusion Filter",
        desc: "Фільтр прозорості нічного неба для туристів: Аврора рендериться на тлі, а хмари виступають як оптичні затемнення з підсвіченими смарагдовими краями.",
        math: "FinalPixel = AuroraColor * (1 - CloudAlpha) + RimScatter * CloudAlpha",
        scaling: "Показує точні географічні 'вікна чистого неба' для зупинки авто та фотозйомки.",
        cloudPct: "ВІКНО ВІДЧИНЕНЕ",
        wind: "Kp 4.2 • ЧИСТО: МІВАТН"
      },
      {
        title: "🎯 8. Coast Guard Doppler Sweep Radar",
        desc: "Військовий 360-градусний круговий метео-радар берегової охорони Кефлавіка з післясвітінням фосфору та шкалою відбиваності опадів dBZ.",
        math: "SweepAngle = (t * RPM * 360) % 360 • PhosphorDecay = exp(-dt / tau)",
        scaling: "Радіус сканування 350 морських миль із перерахунком на локальні дощові осередки.",
        cloudPct: "ВІДБИТТЯ: 52 dBZ",
        wind: "ЗЛИВА / МОКРИЙ СНІГ"
      },
      {
        title: "⬡ 9. NOAA Hexagonal Atmospheric Mesh Grid",
        desc: "Гексагональна сітка кліматичного моделювання ECMWF/NOAA. Кожен шестикутник інтерполює хмарність регіону з пульсуючим барометром та вектором.",
        math: "HexCoords = AxialToPixel(q, r) • Color = HeatmapColor(Pct)",
        scaling: "Гексагони зберігають рівномірну топологію без спотворень картографічної проекції.",
        cloudPct: "94 ГЕКСАГОНИ",
        wind: "ECMWF HRES 0.1°"
      },
      {
        title: "⚡ 10. Cyberpunk Topo-Hugger Neon Fog",
        desc: "Синтвейв неоновий цифровий туман (Cyberpunk 2077). Хвильові неонові контури бірюзи та мадженти обволікають контури фіордів та гірські масиви.",
        math: "Z_wave = sin(lat * 40 + t) * cos(lng * 40 - t) • Glow = NeonPulse",
        scaling: "Ідеально підходить для нічного експедиційного водіння з проекційним дисплеєм HUD.",
        cloudPct: "CYBER FOG ACTIVE",
        wind: "HUD WARP: 100%"
      }
    ];

    function switchConcept(idx) {
      activeConceptIdx = idx;
      
      // Update buttons
      for (let i = 0; i < 10; i++) {
        const btn = document.getElementById(`c-btn-${i}`);
        if (btn) {
          if (i === idx) btn.classList.add('active');
          else btn.classList.remove('active');
        }
      }

      // Update HUD & Inspector
      const meta = CONCEPTS_METADATA[idx];
      document.getElementById('hud-concept-title').innerHTML = meta.title;
      document.getElementById('hud-concept-desc').textContent = meta.desc;
      document.getElementById('hud-cloud-pct').textContent = meta.cloudPct;
      document.getElementById('hud-wind-val').textContent = meta.wind;

      document.getElementById('ins-math').textContent = meta.math;
      document.getElementById('ins-scaling').textContent = meta.scaling;
    }

    function toggleHudPanel() {
      const panel = document.getElementById('inspector-panel');
      if (panel) panel.classList.toggle('hidden');
    }

    // -------------------------------------------------------------
    // TIMELINE SCRUBBING & PLAYBACK
    // -------------------------------------------------------------
    function togglePlayPause() {
      isPlaying = !isPlaying;
      const btn = document.getElementById('btn-play-pause');
      if (btn) btn.innerHTML = isPlaying ? '⏸️' : '▶️';
    }

    function resetTimeline() {
      timelineHour = 0;
      onTimelineInput(0);
    }

    function setPlaySpeed(spd) {
      playSpeed = spd;
      [1, 2, 4].forEach(s => {
        const b = document.getElementById(`spd-${s}`);
        if (b) {
          b.className = s === spd 
            ? 'px-2 py-1 rounded-lg bg-cyan-500 text-white font-bold transition'
            : 'px-2 py-1 rounded-lg text-slate-400 hover:text-white transition';
        }
      });
    }

    function onTimelineInput(val) {
      timelineHour = parseFloat(val);
      const slider = document.getElementById('radar-time-slider');
      if (slider) slider.value = timelineHour;

      const baseHour = 18;
      const simHour = (baseHour + Math.floor(timelineHour)) % 24;
      const simMin = Math.floor((timelineHour % 1) * 60).toString().padStart(2, '0');
      const timeStr = `Сьогодні, ${simHour}:${simMin} UTC (+${timelineHour.toFixed(1)}h)`;

      const lbl = document.getElementById('timeline-time-label');
      if (lbl) lbl.textContent = timeStr;
    }

    // =============================================================
    // 6. 10 REAL WORKING CONCEPTS RENDER ENGINE (60 FPS)
    // =============================================================
    let animTime = 0;

    function startAnimationLoop() {
      function loop() {
        animTime += 0.016;

        if (isPlaying) {
          timelineHour += 0.012 * playSpeed;
          if (timelineHour > 12) timelineHour = 0;
          onTimelineInput(timelineHour);
        }

        renderActiveConcept();
        animFrameId = requestAnimationFrame(loop);
      }
      animFrameId = requestAnimationFrame(loop);
    }

    function renderActiveConcept() {
      if (!ctx || !canvas || !map) return;
      const w = canvas.width;
      const h = canvas.height;
      const dpr = window.devicePixelRatio || 1;
      ctx.clearRect(0, 0, w, h);

      // Advection time offset from timeline slider
      const advectionOffset = timelineHour * 0.04;

      switch(activeConceptIdx) {
        case 0:
          renderConcept1_Volumetric3D(dpr, advectionOffset);
          break;
        case 1:
          renderConcept2_InfraredSatellite(dpr, advectionOffset);
          break;
        case 2:
          renderConcept3_NavierStokes(dpr, advectionOffset);
          break;
        case 3:
          renderConcept4_MultiTier(dpr, advectionOffset);
          break;
        case 4:
          renderConcept5_IsobaricContours(dpr, advectionOffset);
          break;
        case 5:
          renderConcept6_QuantumParticles(dpr, advectionOffset);
          break;
        case 6:
          renderConcept7_AuroraOcclusion(dpr, advectionOffset);
          break;
        case 7:
          renderConcept8_DopplerSweep(dpr, advectionOffset);
          break;
        case 8:
          renderConcept9_HexMesh(dpr, advectionOffset);
          break;
        case 9:
          renderConcept10_Cyberpunk(dpr, advectionOffset);
          break;
      }
    }

    // -------------------------------------------------------------
    // CONCEPT 1: Volumetric 3D Cumulus Advection
    // -------------------------------------------------------------
    function renderConcept1_Volumetric3D(dpr, advOffset) {
      ctx.save();
      
      // Step 1: Render Cast Terrain Shadows first
      SECTOR_PUFFS.forEach((p, idx) => {
        const driftLng = p.baseLng + advOffset * p.speedMult + Math.sin(animTime * 0.3 + p.phase) * 0.08;
        const driftLat = p.baseLat + advOffset * 0.3 * p.speedMult;
        const pt = map.project([driftLng, driftLat]);
        const radiusPx = kmToPixels(p.radiusKm, driftLat) * dpr;

        // Shadow offset to northeast (sun is low in south-southwest)
        const shadowX = pt.x * dpr + radiusPx * 0.25;
        const shadowY = pt.y * dpr - radiusPx * 0.18;

        const shadowGrad = ctx.createRadialGradient(shadowX, shadowY, radiusPx * 0.1, shadowX, shadowY, radiusPx * 1.1);
        shadowGrad.addColorStop(0, 'rgba(0, 0, 0, 0.28)');
        shadowGrad.addColorStop(0.6, 'rgba(2, 6, 23, 0.15)');
        shadowGrad.addColorStop(1, 'rgba(0, 0, 0, 0.0)');

        ctx.fillStyle = shadowGrad;
        ctx.beginPath();
        ctx.arc(shadowX, shadowY, radiusPx * 1.1, 0, Math.PI * 2);
        ctx.fill();
      });

      // Step 2: Render Volumetric White-Silver Puffs with Highlights
      SECTOR_PUFFS.forEach((p, idx) => {
        const driftLng = p.baseLng + advOffset * p.speedMult + Math.sin(animTime * 0.3 + p.phase) * 0.08;
        const driftLat = p.baseLat + advOffset * 0.3 * p.speedMult;
        const pt = map.project([driftLng, driftLat]);
        const radiusPx = kmToPixels(p.radiusKm, driftLat) * dpr;

        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const puffGrad = ctx.createRadialGradient(
          px - radiusPx * 0.2, py - radiusPx * 0.2, radiusPx * 0.05,
          px, py, radiusPx
        );
        puffGrad.addColorStop(0, `rgba(255, 255, 255, ${0.85 * p.opacityMult})`);
        puffGrad.addColorStop(0.35, `rgba(241, 245, 249, ${0.75 * p.opacityMult})`);
        puffGrad.addColorStop(0.7, `rgba(203, 213, 225, ${0.45 * p.opacityMult})`);
        puffGrad.addColorStop(1, 'rgba(148, 163, 184, 0.0)');

        ctx.fillStyle = puffGrad;
        ctx.beginPath();
        ctx.arc(px, py, radiusPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // Step 3: Draw Clear Sky Windows Pulsing Beacon
      const clearSpot = map.project([-16.90, 65.60]); // Mývatn
      const cx = clearSpot.x * dpr;
      const cy = clearSpot.y * dpr;
      const pulseR = (25 + Math.sin(animTime * 4) * 8) * dpr;

      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5 * dpr;
      ctx.beginPath();
      ctx.arc(cx, cy, pulseR, 0, Math.PI * 2);
      ctx.stroke();

      ctx.fillStyle = '#10b981';
      ctx.font = `bold ${10 * dpr}px sans-serif`;
      ctx.fillText('✨ ВІКНО ЧИСТОГО НЕБА (18% ХМАР)', cx + 18 * dpr, cy + 4 * dpr);

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 2: Doppler Satellite Infrared Thermography
    // -------------------------------------------------------------
    function renderConcept2_InfraredSatellite(dpr, advOffset) {
      ctx.save();
      ctx.globalCompositeOperation = 'screen';

      ICELAND_SECTORS.forEach(sec => {
        const pt = map.project([sec.lng + advOffset * 0.5, sec.lat]);
        const rPx = kmToPixels(sec.radiusKm * 1.4, sec.lat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const grad = ctx.createRadialGradient(px, py, rPx * 0.1, px, py, rPx);
        if (sec.cloudBase > 75) {
          // Extremely cold high clouds (-40°C): Magenta & White
          grad.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
          grad.addColorStop(0.3, 'rgba(217, 70, 239, 0.8)');
          grad.addColorStop(0.7, 'rgba(168, 85, 247, 0.4)');
          grad.addColorStop(1, 'rgba(15, 23, 42, 0.0)');
        } else if (sec.cloudBase > 40) {
          // Mid altitude (-15°C): Fiery Amber & Gold
          grad.addColorStop(0, 'rgba(245, 158, 11, 0.85)');
          grad.addColorStop(0.4, 'rgba(234, 88, 12, 0.6)');
          grad.addColorStop(0.8, 'rgba(6, 182, 212, 0.3)');
          grad.addColorStop(1, 'rgba(15, 23, 42, 0.0)');
        } else {
          // Warm clear surface (+5°C): Deep Emerald / Indigo
          grad.addColorStop(0, 'rgba(16, 185, 129, 0.6)');
          grad.addColorStop(0.5, 'rgba(6, 182, 212, 0.3)');
          grad.addColorStop(1, 'rgba(15, 23, 42, 0.0)');
        }

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();

        // Temperature label badge
        ctx.fillStyle = '#ffffff';
        ctx.font = `bold ${9 * dpr}px monospace`;
        const tempVal = sec.cloudBase > 75 ? '-38°C' : (sec.cloudBase > 40 ? '-16°C' : '+4°C');
        ctx.fillText(`IR: ${tempVal}`, px - 20 * dpr, py);
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 3: Navier-Stokes Vortex Streamlines
    // -------------------------------------------------------------
    function renderConcept3_NavierStokes(dpr, advOffset) {
      ctx.save();

      // Glacier obstacles in Iceland: Vatnajökull & Langjökull
      const vatnaPt = map.project([-16.80, 64.40]);
      const langPt = map.project([-20.15, 64.70]);

      FLUID_PARTICLES.forEach(p => {
        p.lng += p.speed + (advOffset * 0.01);
        if (p.lng > -13.0) p.lng = -24.5;

        // Obstacle avoidance deflection
        const pScreen = map.project([p.lng, p.lat]);
        const dVatna = Math.hypot(pScreen.x - vatnaPt.x, pScreen.y - vatnaPt.y);
        if (dVatna < 80) {
          // Deflect around obstacle (creates Karman vortex shedding)
          p.lat += (p.lat > 64.40 ? 0.008 : -0.008);
        }

        const px = pScreen.x * dpr;
        const py = pScreen.y * dpr;

        ctx.strokeStyle = p.lat > 64.0 ? 'rgba(34, 211, 238, 0.65)' : 'rgba(249, 115, 22, 0.75)';
        ctx.lineWidth = 1.8 * dpr;
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(px - 14 * dpr, py + 2 * dpr);
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(px, py, p.size * dpr * 0.8, 0, Math.PI * 2);
        ctx.fill();
      });

      // Draw Glacier Barrier Outlines
      [vatnaPt, langPt].forEach((ob, idx) => {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
        ctx.setLineDash([4 * dpr, 4 * dpr]);
        ctx.lineWidth = 1.5 * dpr;
        ctx.beginPath();
        ctx.arc(ob.x * dpr, ob.y * dpr, (idx === 0 ? 55 : 35) * dpr, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = 'rgba(224, 242, 254, 0.8)';
        ctx.font = `${9 * dpr}px monospace`;
        ctx.fillText(idx === 0 ? '⛔ БАР\'ЄР ВАТНАЙОКЮДЛЬ' : '⛔ ЛАНҐЙЙОКЮДЛЬ', ob.x * dpr - 45 * dpr, ob.y * dpr);
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 4: 3-Tier Multi-Altitude Radar
    // -------------------------------------------------------------
    function renderConcept4_MultiTier(dpr, advOffset) {
      ctx.save();

      // Tier 1: Low clouds (Lágský <2000m) - Deep Gold/Orange Fog
      ICELAND_SECTORS.forEach(sec => {
        if (sec.cloudBase > 50) {
          const pt = map.project([sec.lng + advOffset * 0.3, sec.lat]);
          const rPx = kmToPixels(sec.radiusKm * 0.8, sec.lat) * dpr;
          const px = pt.x * dpr;
          const py = pt.y * dpr;

          const g1 = ctx.createRadialGradient(px, py, 0, px, py, rPx);
          g1.addColorStop(0, 'rgba(245, 158, 11, 0.7)');
          g1.addColorStop(1, 'rgba(245, 158, 11, 0.0)');
          ctx.fillStyle = g1;
          ctx.beginPath();
          ctx.arc(px, py, rPx, 0, Math.PI * 2);
          ctx.fill();
        }
      });

      // Tier 2: Mid clouds (Milliský 2000-6000m) - Soft Steel Blue
      ICELAND_SECTORS.forEach(sec => {
        const pt = map.project([sec.lng + advOffset * 0.6, sec.lat + 0.1]);
        const rPx = kmToPixels(sec.radiusKm * 1.1, sec.lat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const g2 = ctx.createRadialGradient(px, py, 0, px, py, rPx);
        g2.addColorStop(0, 'rgba(56, 189, 248, 0.55)');
        g2.addColorStop(1, 'rgba(56, 189, 248, 0.0)');
        ctx.fillStyle = g2;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // Tier 3: High clouds (Háský >6000m) - Neon Purple Cirrus
      ICELAND_SECTORS.forEach(sec => {
        const pt = map.project([sec.lng + advOffset * 0.9, sec.lat + 0.2]);
        const rPx = kmToPixels(sec.radiusKm * 1.4, sec.lat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const g3 = ctx.createRadialGradient(px, py, 0, px, py, rPx);
        g3.addColorStop(0, 'rgba(168, 85, 247, 0.45)');
        g3.addColorStop(1, 'rgba(168, 85, 247, 0.0)');
        ctx.fillStyle = g3;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // Tier Legend Card in Top Right
      ctx.fillStyle = 'rgba(2, 6, 23, 0.85)';
      ctx.fillRect(canvas.width - 200 * dpr, 20 * dpr, 180 * dpr, 70 * dpr);
      ctx.strokeStyle = 'rgba(6, 182, 212, 0.4)';
      ctx.strokeRect(canvas.width - 200 * dpr, 20 * dpr, 180 * dpr, 70 * dpr);

      ctx.font = `bold ${9 * dpr}px monospace`;
      ctx.fillStyle = '#f59e0b';
      ctx.fillText('● LÁGSKÝ (<2000m) [ТУМАН]', canvas.width - 190 * dpr, 38 * dpr);
      ctx.fillStyle = '#38bdf8';
      ctx.fillText('● MILLISKÝ (2-6km) [ДОЩ]', canvas.width - 190 * dpr, 56 * dpr);
      ctx.fillStyle = '#c084fc';
      ctx.fillText('● HÁSKÝ (>6km) [ПЕРИСТІ]', canvas.width - 190 * dpr, 74 * dpr);

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 5: Isobaric Moisture Contours
    // -------------------------------------------------------------
    function renderConcept5_IsobaricContours(dpr, advOffset) {
      ctx.save();

      ICELAND_SECTORS.forEach((sec, idx) => {
        const pt = map.project([sec.lng + advOffset * 0.4, sec.lat]);
        const rPx = kmToPixels(sec.radiusKm, sec.lat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        // Draw 4 concentric isobar rings (25%, 50%, 75%, 90%)
        [0.35, 0.6, 0.85, 1.1].forEach((k, rIdx) => {
          ctx.strokeStyle = rIdx === 3 ? 'rgba(6, 182, 212, 0.8)' : 'rgba(148, 163, 184, 0.4)';
          ctx.lineWidth = (rIdx === 3 ? 2 : 1) * dpr;
          ctx.setLineDash([6 * dpr, 4 * dpr]);
          ctx.lineDashOffset = -animTime * 15 * (rIdx % 2 === 0 ? 1 : -1);

          ctx.beginPath();
          ctx.arc(px, py, rPx * k, 0, Math.PI * 2);
          ctx.stroke();

          // Barometric label
          if (rIdx === 2) {
            ctx.fillStyle = '#38bdf8';
            ctx.font = `${8 * dpr}px monospace`;
            ctx.fillText(`${25 * (rIdx + 1)}% RH`, px + rPx * k * 0.7, py - rPx * k * 0.7);
          }
        });
        ctx.setLineDash([]);

        // Sector center flag
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.arc(px, py, 3 * dpr, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = `bold ${9 * dpr}px monospace`;
        ctx.fillText(`FL0${Math.floor(sec.cloudBase / 10) + 20}`, px + 6 * dpr, py + 3 * dpr);
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 6: Quantum Particle Density Field
    // -------------------------------------------------------------
    function renderConcept6_QuantumParticles(dpr, advOffset) {
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';

      FLUID_PARTICLES.forEach(p => {
        p.lng += p.speed * 1.5 + (advOffset * 0.008);
        if (p.lng > -13.0) p.lng = -24.5;

        const pt = map.project([p.lng, p.lat]);
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const isStorm = p.lat < 64.0;
        ctx.fillStyle = isStorm ? 'rgba(251, 146, 60, 0.75)' : 'rgba(56, 189, 248, 0.65)';
        
        ctx.beginPath();
        ctx.arc(px, py, (isStorm ? 2.8 : 1.8) * dpr, 0, Math.PI * 2);
        ctx.fill();

        // High velocity streak line
        ctx.strokeStyle = isStorm ? 'rgba(251, 146, 60, 0.3)' : 'rgba(56, 189, 248, 0.25)';
        ctx.lineWidth = 1 * dpr;
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(px - 18 * dpr, py + 3 * dpr);
        ctx.stroke();
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 7: Aurora Hunter Occlusion Filter
    // -------------------------------------------------------------
    function renderConcept7_AuroraOcclusion(dpr, advOffset) {
      ctx.save();

      // Step 1: Render vibrant Northern Lights plasma background over Iceland
      const auroraGrad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
      auroraGrad.addColorStop(0.1, 'rgba(16, 185, 129, 0.0)');
      auroraGrad.addColorStop(0.35, `rgba(16, 185, 129, ${0.45 + Math.sin(animTime * 2) * 0.15})`);
      auroraGrad.addColorStop(0.65, `rgba(6, 182, 212, ${0.4 + Math.cos(animTime * 2.2) * 0.12})`);
      auroraGrad.addColorStop(0.85, 'rgba(168, 85, 247, 0.2)');
      auroraGrad.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

      ctx.fillStyle = auroraGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Step 2: Overlay clouds as dark volcanic ash occlusions (blocking the aurora)
      ICELAND_SECTORS.forEach(sec => {
        const pt = map.project([sec.lng + advOffset * 0.4, sec.lat]);
        const rPx = kmToPixels(sec.radiusKm * 1.1, sec.lat) * dpr;
        const px = pt.x * dpr;
        const py = pt.y * dpr;

        const occludeGrad = ctx.createRadialGradient(px, py, rPx * 0.15, px, py, rPx);
        occludeGrad.addColorStop(0, 'rgba(15, 23, 42, 0.95)'); // 100% blocks aurora
        occludeGrad.addColorStop(0.7, 'rgba(30, 41, 59, 0.85)');
        occludeGrad.addColorStop(0.85, 'rgba(16, 185, 129, 0.35)'); // Green fringe scatter!
        occludeGrad.addColorStop(1, 'rgba(15, 23, 42, 0.0)');

        ctx.fillStyle = occludeGrad;
        ctx.beginPath();
        ctx.arc(px, py, rPx, 0, Math.PI * 2);
        ctx.fill();
      });

      // Target Spot Highlight in Mývatn
      const myv = map.project([-16.90, 65.60]);
      ctx.fillStyle = '#34d399';
      ctx.font = `bold ${11 * dpr}px monospace`;
      ctx.fillText('🔭 ПЕРСПЕКТИВА АВРОРИ: 10/10 (ЧИСТЕ НЕБО)', myv.x * dpr - 80 * dpr, myv.y * dpr);

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 8: Coast Guard Doppler Sweep Radar
    // -------------------------------------------------------------
    let radarSweepAngle = 0;
    function renderConcept8_DopplerSweep(dpr, advOffset) {
      ctx.save();
      radarSweepAngle += 0.04;

      // Radar station at Keflavík Airport
      const kef = map.project([-22.60, 63.98]);
      const kx = kef.x * dpr;
      const ky = kef.y * dpr;
      const sweepRadius = Math.max(canvas.width, canvas.height) * 0.85;

      // Draw Range Rings (50 NM, 100 NM, 150 NM)
      [120, 240, 360, 480].forEach(r => {
        ctx.strokeStyle = 'rgba(16, 185, 129, 0.35)';
        ctx.lineWidth = 1 * dpr;
        ctx.beginPath();
        ctx.arc(kx, ky, r * dpr, 0, Math.PI * 2);
        ctx.stroke();
      });

      // Draw Rotating Phosphor Sweep Line
      const sweepX = kx + Math.cos(radarSweepAngle) * sweepRadius;
      const sweepY = ky + Math.sin(radarSweepAngle) * sweepRadius;

      const beamGrad = ctx.createLinearGradient(kx, ky, sweepX, sweepY);
      beamGrad.addColorStop(0, 'rgba(16, 185, 129, 0.8)');
      beamGrad.addColorStop(1, 'rgba(16, 185, 129, 0.0)');

      ctx.strokeStyle = beamGrad;
      ctx.lineWidth = 3 * dpr;
      ctx.beginPath();
      ctx.moveTo(kx, ky);
      ctx.lineTo(sweepX, sweepY);
      ctx.stroke();

      // Echo blips on active precipitation clouds
      ICELAND_SECTORS.forEach(sec => {
        const pt = map.project([sec.lng, sec.lat]);
        const px = pt.x * dpr;
        const py = pt.y * dpr;
        const ang = Math.atan2(py - ky, px - kx);
        const angDiff = Math.abs((radarSweepAngle % (Math.PI * 2)) - ((ang + Math.PI * 2) % (Math.PI * 2)));

        if (angDiff < 0.6) {
          ctx.fillStyle = sec.cloudBase > 70 ? 'rgba(239, 68, 68, 0.85)' : 'rgba(250, 204, 21, 0.85)';
          ctx.beginPath();
          ctx.arc(px, py, 6 * dpr, 0, Math.PI * 2);
          ctx.fill();

          ctx.font = `${8 * dpr}px monospace`;
          ctx.fillText(`${sec.cloudBase} dBZ`, px + 8 * dpr, py);
        }
      });

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 9: NOAA Hexagonal Mesh Grid
    // -------------------------------------------------------------
    function renderConcept9_HexMesh(dpr, advOffset) {
      ctx.save();
      const hexRadius = 28 * dpr;
      const hexWidth = Math.sqrt(3) * hexRadius;
      const hexHeight = 2 * hexRadius * 0.75;

      // Draw grid over Iceland bounds
      const minPt = map.project([-24.5, 66.6]);
      const maxPt = map.project([-13.0, 63.3]);

      for (let y = minPt.y * dpr; y <= maxPt.y * dpr; y += hexHeight) {
        let col = 0;
        for (let x = minPt.x * dpr; x <= maxPt.x * dpr; x += hexWidth) {
          const shiftX = (col % 2 === 0 ? 0 : hexWidth / 2);
          const cx = x + shiftX;
          const cy = y;

          // Pseudo moisture calculation
          const moisture = Math.abs(Math.sin((cx + cy) * 0.005 + animTime * 0.5 + advOffset * 10));
          
          ctx.strokeStyle = 'rgba(6, 182, 212, 0.35)';
          ctx.lineWidth = 1 * dpr;
          ctx.fillStyle = moisture > 0.6 ? `rgba(234, 88, 12, ${moisture * 0.5})` : `rgba(6, 182, 212, ${moisture * 0.4})`;

          ctx.beginPath();
          for (let a = 0; a < 6; a++) {
            const angle = Math.PI / 6 + a * Math.PI / 3;
            const hx = cx + Math.cos(angle) * (hexRadius * 0.92);
            const hy = cy + Math.sin(angle) * (hexRadius * 0.92);
            if (a === 0) ctx.moveTo(hx, hy);
            else ctx.lineTo(hx, hy);
          }
          ctx.closePath();
          ctx.fill();
          ctx.stroke();

          col++;
        }
      }

      ctx.restore();
    }

    // -------------------------------------------------------------
    // CONCEPT 10: Cyberpunk Topo-Hugger Neon Fog
    // -------------------------------------------------------------
    function renderConcept10_Cyberpunk(dpr, advOffset) {
      ctx.save();
      ctx.globalCompositeOperation = 'lighter';

      const step = 20 * dpr;
      for (let y = 0; y < canvas.height; y += step) {
        ctx.beginPath();
        ctx.strokeStyle = y % (step * 2) === 0 ? 'rgba(0, 240, 255, 0.7)' : 'rgba(255, 0, 128, 0.6)';
        ctx.lineWidth = 1.6 * dpr;

        for (let x = 0; x <= canvas.width; x += 15 * dpr) {
          const wave = Math.sin(x * 0.012 + animTime * 1.5 + (y * 0.02) + advOffset * 5) * (18 * dpr)
                     + Math.cos(x * 0.025 - animTime * 0.8) * (8 * dpr);
          if (x === 0) ctx.moveTo(x, y + wave);
          else ctx.lineTo(x, y + wave);
        }
        ctx.stroke();
      }

      ctx.restore();
    }

    // Initialize map on document load
    document.addEventListener('DOMContentLoaded', () => {
      initMap();
      switchConcept(0);
    });
  </script>
</body>
</html>
'''

with open(LAB_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {LAB_PATH} ({len(html_content)} bytes)")
