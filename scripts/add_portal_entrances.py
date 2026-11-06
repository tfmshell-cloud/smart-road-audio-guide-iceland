# -*- coding: utf-8 -*-
"""
Add prominent separate entrance into Aurora Hunter Occlusion Lab across:
1. index.html Header Navigation Bar (dedicated top-level nav button)
2. index.html Floating Map Control Dock
3. index.html Sidebar Top Featured Portal Banner
4. cloud_radar_lab.html Header Return Link
"""
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"
LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/cloud_radar_lab.html"
BRAIN_LAB_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/brain/3cafaa28-e27e-4b4e-85d4-a0a0a9d89f86/cloud_radar_lab.html"

# ==============================================================================
# 1. UPDATE INDEX.HTML
# ==============================================================================
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    idx_content = f.read()

# A. Header Top-level Nav button
old_nav_marker = """      <!-- 1. MAP & WEATHER RADAR MODE -->
      <button onclick="switchAppSection('map')" id="nav-btn-map" class="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-cyan-500/25 to-teal-500/25 text-cyan-300 border border-cyan-400/50 flex items-center gap-2 shadow-sm transition">
        <span>🗺️</span> <span>Карта &amp; Радар</span>
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
      </button>"""

new_nav_button = """      <!-- 1. MAP & WEATHER RADAR MODE -->
      <button onclick="switchAppSection('map')" id="nav-btn-map" class="px-3.5 py-1.5 rounded-xl bg-gradient-to-r from-cyan-500/25 to-teal-500/25 text-cyan-300 border border-cyan-400/50 flex items-center gap-2 shadow-sm transition">
        <span>🗺️</span> <span>Карта &amp; Радар</span>
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
      </button>

      <!-- SEPARATE PORTAL ENTRANCE: AURORA HUNTER OCCLUSION LAB -->
      <a href="cloud_radar_lab.html" id="nav-btn-aurora-lab" class="px-3 py-1.5 rounded-xl bg-gradient-to-r from-emerald-500/20 via-teal-500/20 to-cyan-500/20 hover:from-emerald-500/35 hover:to-cyan-500/35 text-emerald-300 hover:text-white border border-emerald-500/40 hover:border-emerald-400 flex items-center gap-2 shadow-md shadow-emerald-500/20 transition group" title="Відкрити портал Aurora Hunter Occlusion Lab">
        <span class="text-sm group-hover:scale-110 transition-transform">🌌</span>
        <span class="font-bold">Aurora Hunter Lab</span>
        <span class="px-1.5 py-0.2 rounded-full bg-emerald-500/30 text-emerald-300 font-mono text-[9px] font-bold border border-emerald-400/50">10 LIVE</span>
      </a>"""

if old_nav_marker in idx_content and "nav-btn-aurora-lab" not in idx_content:
    idx_content = idx_content.replace(old_nav_marker, new_nav_button, 1)
    print("Added dedicated Aurora Hunter Lab button to header nav")

# B. Mobile Header Portal Pill
old_mobile_copilot = """      <!-- Quick Copilot Pill on mobile -->
      <button onclick="openCopilotModal()" class="md:hidden p-2 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs">
        🛡️ Штурман
      </button>"""

new_mobile_portal = """      <!-- Quick Aurora Lab Entrance on mobile -->
      <a href="cloud_radar_lab.html" class="md:hidden px-2 py-1.5 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs font-bold flex items-center gap-1">
        <span>🌌</span> <span>Lab</span>
      </a>

      <!-- Quick Copilot Pill on mobile -->
      <button onclick="openCopilotModal()" class="md:hidden p-2 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 text-xs">
        🛡️ Штурман
      </button>"""

if old_mobile_copilot in idx_content and "Quick Aurora Lab Entrance on mobile" not in idx_content:
    idx_content = idx_content.replace(old_mobile_copilot, new_mobile_portal, 1)
    print("Added mobile Aurora Lab quick pill")

# C. Floating Map Control Dock Entrance Pill
old_map_dock = """        <!-- Live Layer Switches -->
        <button onclick="RadarTimeLapse.toggleClouds()" id="map-pill-clouds" class="px-2.5 py-1.5 rounded-xl bg-cyan-500/25 text-cyan-300 border border-cyan-400/50 text-[11px] font-semibold flex items-center gap-1.5 transition shadow-sm">
          <span>☁️</span> <span class="hidden sm:inline">Хмари HD</span>
        </button>"""

new_map_dock = """        <!-- Direct Portal Entrance to Aurora Hunter Occlusion Lab -->
        <a href="cloud_radar_lab.html" class="px-2.5 py-1.5 rounded-xl bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white font-bold text-[11px] flex items-center gap-1.5 transition shadow-lg shadow-emerald-500/30 border border-emerald-400/50 group" title="Вхід у портал: Aurora Hunter Occlusion Lab (10 Live Концептів)">
          <span class="group-hover:scale-110 transition-transform">🌌</span>
          <span class="hidden sm:inline">Aurora Hunter Lab</span>
          <span class="text-[10px] font-mono opacity-80">↗</span>
        </a>

        <!-- Live Layer Switches -->
        <button onclick="RadarTimeLapse.toggleClouds()" id="map-pill-clouds" class="px-2.5 py-1.5 rounded-xl bg-cyan-500/25 text-cyan-300 border border-cyan-400/50 text-[11px] font-semibold flex items-center gap-1.5 transition shadow-sm">
          <span>☁️</span> <span class="hidden sm:inline">Хмари HD</span>
        </button>"""

if old_map_dock in idx_content and "Direct Portal Entrance to Aurora Hunter Occlusion Lab" not in idx_content:
    idx_content = idx_content.replace(old_map_dock, new_map_dock, 1)
    print("Added Aurora Hunter Lab portal button to floating map dock")

# D. Sidebar Featured Portal Card right above POI search/filter
old_sidebar_header = """      <div class="p-3 border-b border-slate-800/80 space-y-2.5 bg-slate-900/40">
        <!-- Search bar & Collapse Toggle -->"""

new_sidebar_header = """      <div class="p-3 border-b border-slate-800/80 space-y-2.5 bg-slate-900/40">
        <!-- LUXURY PORTAL ENTRANCE BANNER: AURORA HUNTER OCCLUSION LAB -->
        <a href="cloud_radar_lab.html" class="group block p-2.5 rounded-2xl bg-gradient-to-r from-slate-950 via-emerald-950/40 to-slate-950 border border-emerald-500/40 hover:border-emerald-400 shadow-xl shadow-emerald-500/10 transition-all hover:scale-[1.01]">
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2.5">
              <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-emerald-500 to-cyan-500 flex items-center justify-center text-white text-base shadow-md shadow-emerald-500/40 group-hover:rotate-6 transition shrink-0">
                🌌
              </div>
              <div>
                <div class="flex items-center gap-1.5">
                  <span class="text-xs font-black tracking-wide text-white group-hover:text-emerald-300 transition">Aurora Hunter Occlusion Lab</span>
                  <span class="px-1.5 py-0.2 rounded-full bg-emerald-500/25 text-emerald-300 font-mono text-[9px] font-bold border border-emerald-400/40 animate-pulse">10 LIVE</span>
                </div>
                <p class="text-[10px] text-slate-400">Окремий портал: живий метеорадар Північної Атлантики &amp; 10 концептів</p>
              </div>
            </div>
            <span class="px-2 py-1 rounded-lg bg-emerald-500/20 text-emerald-300 text-[10px] font-bold font-mono border border-emerald-500/40 group-hover:bg-emerald-500 group-hover:text-slate-950 transition shrink-0">ВХІД ↗</span>
          </div>
        </a>

        <!-- Search bar & Collapse Toggle -->"""

if old_sidebar_header in idx_content and "LUXURY PORTAL ENTRANCE BANNER" not in idx_content:
    idx_content = idx_content.replace(old_sidebar_header, new_sidebar_header, 1)
    print("Added Luxury Portal Entrance Banner to sidebar")

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Updated index.html successfully!")

# ==============================================================================
# 2. UPDATE CLOUD_RADAR_LAB.HTML RETURN BUTTON
# ==============================================================================
with open(LAB_PATH, 'r', encoding='utf-8') as f:
    lab_content = f.read()

old_lab_return = """      <!-- Return to Main App -->
      <a href="index.html" class="px-3 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold flex items-center gap-1.5 transition" title="Повернутися до головного сайту">
        <span>⬅️</span> <span class="hidden md:inline">Головний сайт</span>
      </a>"""

new_lab_return = """      <!-- Return to Main App (Smart Road Audio Guide Iceland) -->
      <a href="index.html" class="px-3.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 hover:text-emerald-300 border border-emerald-500/30 hover:border-emerald-400 text-xs font-bold flex items-center gap-2 shadow-sm transition group" title="Повернутися до Smart Road Audio Guide Iceland">
        <span class="group-hover:-translate-x-0.5 transition-transform">⬅️</span>
        <span>Smart Road Audio Guide Iceland</span>
      </a>"""

if old_lab_return in lab_content:
    lab_content = lab_content.replace(old_lab_return, new_lab_return, 1)
    print("Updated return button in cloud_radar_lab.html")

with open(LAB_PATH, 'w', encoding='utf-8') as f:
    f.write(lab_content)

with open(BRAIN_LAB_PATH, 'w', encoding='utf-8') as f:
    f.write(lab_content)

print("Updated cloud_radar_lab.html successfully!")
