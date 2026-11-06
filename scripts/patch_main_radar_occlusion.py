# -*- coding: utf-8 -*-
import re

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Expand CLOUD_SECTORS to include Oceanic Systems
old_sectors_marker = "const CLOUD_SECTORS = ["
new_sectors_code = """const CLOUD_SECTORS = [
        // Oceanic Synoptic Systems (Denmark Strait & North Atlantic Basin)
        { id: 'denmark_strait', name: "Датська протока (Гренландія)", center: [-28.5, 66.8], radiusKm: 160, windAngle: -0.45, speed: 36 },
        { id: 'south_atlantic', name: "Південна Атлантика (Штормовий фронт)", center: [-21.5, 60.5], radiusKm: 180, windAngle: -0.30, speed: 40 },
        { id: 'norwegian_sea', name: "Норвезьке море (Східна течія)", center: [-9.0, 65.5], radiusKm: 150, windAngle: -0.18, speed: 26 },"""

if old_sectors_marker in content and "denmark_strait" not in content:
    content = content.replace(old_sectors_marker, new_sectors_code, 1)
    print("Added Oceanic Sectors to CLOUD_SECTORS")

# 2. Expand WIND_STREAMERS spawn area to Oceanic Basin
old_wind = """      const WIND_STREAMERS = [];
      for (let i = 0; i < 90; i++) {
        WIND_STREAMERS.push({
          lng: -25.5 + Math.random() * 14.5,
          lat: 63.1 + Math.random() * 3.7,"""

new_wind = """      const WIND_STREAMERS = [];
      for (let i = 0; i < 120; i++) {
        WIND_STREAMERS.push({
          lng: -33.0 + Math.random() * 26.0,
          lat: 59.5 + Math.random() * 8.5,"""

if old_wind in content:
    content = content.replace(old_wind, new_wind, 1)
    print("Expanded WIND_STREAMERS to Oceanic Basin")

# 3. Add Live API Fetch to ResearchEngine.triggerResearch
old_research = """          setTimeout(() => {
            const deltaKp = parseFloat(((Math.random() - 0.45) * 0.35).toFixed(1));
            const newWindSpeed = Math.round(460 + Math.random() * 110);
            const newBz = parseFloat((-3.2 - Math.random() * 4.2).toFixed(1));
            const latShift = (newBz < -4.0) ? -0.25 : 0.15;

            this.telemetry.solarWindSpeed = newWindSpeed;
            this.telemetry.imfBz = newBz;
            this.telemetry.auroraLatDrift = parseFloat((this.telemetry.auroraLatDrift + latShift).toFixed(2));
            this.telemetry.cloudDriftKm += Math.round(18 + Math.random() * 12);

            const step = FORECAST_STEPS[currentStep];
            if (step) {
              step.kp = Math.max(1.8, Math.min(6.5, parseFloat((step.kp + deltaKp).toFixed(1))));
            }"""

new_research = """          // Asynchronous Live Poll from NOAA SWPC & Open-Meteo
          (async () => {
            try {
              const noaaResp = await fetch('https://services.swpc.noaa.gov/json/planetary_k_index_1m.json').catch(() => null);
              if (noaaResp && noaaResp.ok) {
                const noaaData = await noaaResp.json();
                if (noaaData && noaaData.length > 0) {
                  const latest = noaaData[noaaData.length - 1];
                  const val = parseFloat(latest.kp_index);
                  if (!isNaN(val)) {
                    FORECAST_STEPS[currentStep].kp = parseFloat(val.toFixed(1));
                  }
                }
              }
            } catch(e) {}
          })();

          setTimeout(() => {
            const deltaKp = parseFloat(((Math.random() - 0.45) * 0.35).toFixed(1));
            const newWindSpeed = Math.round(460 + Math.random() * 110);
            const newBz = parseFloat((-3.2 - Math.random() * 4.2).toFixed(1));
            const latShift = (newBz < -4.0) ? -0.25 : 0.15;

            this.telemetry.solarWindSpeed = newWindSpeed;
            this.telemetry.imfBz = newBz;
            this.telemetry.auroraLatDrift = parseFloat((this.telemetry.auroraLatDrift + latShift).toFixed(2));
            this.telemetry.cloudDriftKm += Math.round(18 + Math.random() * 12);

            const step = FORECAST_STEPS[currentStep];
            if (step) {
              step.kp = Math.max(1.8, Math.min(7.0, parseFloat((step.kp + deltaKp).toFixed(1))));
            }"""

if old_research in content:
    content = content.replace(old_research, new_research, 1)
    print("Integrated Live NOAA SWPC polling in triggerResearch")

# 4. In renderFrame, support Aurora Hunter Occlusion
# Replace cloud drawing grad with adaptive Basalt Occlusion when showAurora is true
old_cloud_grad = """              // High-definition multi-stop cumulus gradient
              const grad = ctx.createRadialGradient(pt.x, pt.y, radius * 0.05, pt.x, pt.y, radius);
              grad.addColorStop(0, `rgba(255, 255, 255, ${alpha})`);
              grad.addColorStop(0.35, `rgba(235, 245, 255, ${alpha * 0.88})`);
              grad.addColorStop(0.68, `rgba(185, 210, 235, ${alpha * 0.55})`);
              grad.addColorStop(0.88, `rgba(135, 165, 195, ${alpha * 0.22})`);
              grad.addColorStop(1, `rgba(100, 130, 160, 0.0)`);"""

new_cloud_grad = """              // High-definition multi-stop cumulus gradient (Aurora Hunter Occlusion mode when Aurora is ON)
              const grad = ctx.createRadialGradient(pt.x, pt.y, radius * 0.05, pt.x, pt.y, radius);
              if (showAurora) {
                // Basaltic Dark Occlusion with emerald fringe bleed
                grad.addColorStop(0, `rgba(15, 23, 42, ${alpha * 0.95})`);
                grad.addColorStop(0.55, `rgba(30, 41, 59, ${alpha * 0.85})`);
                grad.addColorStop(0.82, `rgba(16, 185, 129, ${alpha * 0.40})`); // Emerald fringe bleed
                grad.addColorStop(1, `rgba(15, 23, 42, 0.0)`);
              } else {
                // Standard daylight cumulus
                grad.addColorStop(0, `rgba(255, 255, 255, ${alpha})`);
                grad.addColorStop(0.35, `rgba(235, 245, 255, ${alpha * 0.88})`);
                grad.addColorStop(0.68, `rgba(185, 210, 235, ${alpha * 0.55})`);
                grad.addColorStop(0.88, `rgba(135, 165, 195, ${alpha * 0.22})`);
                grad.addColorStop(1, `rgba(100, 130, 160, 0.0)`);
              }"""

if old_cloud_grad in content:
    content = content.replace(old_cloud_grad, new_cloud_grad, 1)
    print("Upgraded cloud drawing to Aurora Hunter Occlusion")

# 5. Add a direct button linking to cloud_radar_lab.html in radar controls panel
old_layer_switches = """            <button onclick="RadarTimeLapse.toggleWind()" id="btn-toggle-wind" class="px-2 py-0.5 rounded-lg bg-blue-500/20 text-blue-300 border border-blue-500/40 font-mono text-[9px] font-bold transition">
              💨 Вітер: УВІМК
            </button>
          </div>"""

new_layer_switches = """            <button onclick="RadarTimeLapse.toggleWind()" id="btn-toggle-wind" class="px-2 py-0.5 rounded-lg bg-blue-500/20 text-blue-300 border border-blue-500/40 font-mono text-[9px] font-bold transition">
              💨 Вітер: УВІМК
            </button>
            <a href="cloud_radar_lab.html" class="px-2.5 py-0.5 rounded-lg bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-mono text-[9px] font-bold flex items-center gap-1 transition shadow-sm" title="Відкрити лабораторію 10 концептів Aurora Hunter Occlusion">
              <span>🔬</span> <span>10 Концептів Aurora Lab ↗</span>
            </a>
          </div>"""

if old_layer_switches in content and "10 Концептів Aurora Lab" not in content:
    content = content.replace(old_layer_switches, new_layer_switches, 1)
    print("Added 10 Концептів Aurora Lab button to radar controls")

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
