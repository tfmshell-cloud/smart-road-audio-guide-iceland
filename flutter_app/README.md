# Iceland Smart Road Audio Guide — Mobile Application (Flutter)

Autonomous, Offline-First, 3D Geo-Contextual Audio Guide for Iceland Route 1 and Golden Circle.
Designed for consumer tourism (B2C) and car rental fleet integration (B2B SaaS: Hertz, Europcar, Blue Car Rental, Lotus).

## Key Architecture Components
1. **MapLibre GL Native (`maplibre_gl`)**:
   - 60 FPS hardware accelerated 3D vector map rendering with 55° camera pitch.
   - Zero vendor API costs ($0 / unlimited users).
2. **Offline Vector Pack (`iceland.pmtiles` / `iceland.mbtiles`)**:
   - Packaged inside `assets/tiles/` (~140 MB total).
   - Served by embedded localhost server (`shelf_io`) at `http://127.0.0.1:8088/`.
   - Works 100% offline in dead zones (Skeiðarársandur, Eastfjords, Highlands).
3. **Background Geofence Engine (`geofence_engine.dart`)**:
   - Monitors GPS stream even when screen is locked or while Waze / Google Maps is open.
   - Dual-state hysteresis (enters at POI radius, clears at radius + 250m).
4. **Bilingual Narration (`tts_audio_service.dart`)**:
   - Offline voice synthesis in Ukrainian (uk-UA) and English (en-US).
   - Fallback to pre-recorded studio MP3 files.
5. **B2B Kiosk Screen (`b2b_kiosk_screen.dart`)**:
   - Enterprise tablet mode for rental car dashboards with automatic return trip reset.

## Build Instructions
```bash
flutter pub get
flutter run -d chrome # or ios / android
```
