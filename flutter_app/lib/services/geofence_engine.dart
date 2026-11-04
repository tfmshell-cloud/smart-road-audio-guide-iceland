import 'dart:async';
import 'dart:math';
import 'package:flutter/foundation.dart';
import 'package:geolocator/geolocator.dart';
import '../models/poi_model.dart';
import 'tts_audio_service.dart';

class GeofenceEngine extends ChangeNotifier {
  final List<PoiModel> pois;
  final TtsAudioService ttsService;
  
  Position? currentPosition;
  double currentSpeedKmh = 0.0;
  PoiModel? activeTriggerPoi;
  final Set<String> _triggeredPoiIds = {};
  String currentLanguage = 'uk';
  bool isSimulationRunning = false;

  GeofenceEngine({required this.pois, required this.ttsService}) {
    _initGpsListener();
  }

  void _initGpsListener() async {
    bool serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) return;

    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) return;
    }

    Geolocator.getPositionStream(
      locationSettings: const LocationSettings(
        accuracy: LocationAccuracy.high,
        distanceFilter: 10,
      ),
    ).listen((position) {
      if (!isSimulationRunning) {
        updatePosition(position);
      }
    });
  }

  void updatePosition(Position pos) {
    currentPosition = pos;
    currentSpeedKmh = (pos.speed * 3.6).clamp(0.0, 140.0);
    _evaluateGeofences();
    notifyListeners();
  }

  void setManualPosition(double lat, double lng, double speed) {
    currentPosition = Position(
      latitude: lat,
      longitude: lng,
      timestamp: DateTime.now(),
      accuracy: 5.0,
      altitude: 100.0,
      heading: 0.0,
      speed: speed / 3.6,
      speedAccuracy: 1.0,
      altitudeAccuracy: 1.0,
      headingAccuracy: 1.0,
    );
    currentSpeedKmh = speed;
    _evaluateGeofences();
    notifyListeners();
  }

  double calculateDistanceTo(PoiModel poi) {
    if (currentPosition == null) return double.infinity;
    return _haversineMeters(
      currentPosition!.latitude,
      currentPosition!.longitude,
      poi.lat,
      poi.lng,
    );
  }

  void _evaluateGeofences() {
    if (currentPosition == null) return;

    for (var poi in pois) {
      double dist = calculateDistanceTo(poi);
      if (dist <= poi.radius) {
        if (!_triggeredPoiIds.contains(poi.id)) {
          _triggeredPoiIds.add(poi.id);
          activeTriggerPoi = poi;
          ttsService.speakPoiGuide(poi);
          notifyListeners();
        }
      }
    }
  }

  double _haversineMeters(double lat1, double lon1, double lat2, double lon2) {
    const R = 6371000.0;
    final dLat = (lat2 - lat1) * pi / 180;
    final dLon = (lon2 - lon1) * pi / 180;
    final a = sin(dLat / 2) * sin(dLat / 2) +
        cos(lat1 * pi / 180) * cos(lat2 * pi / 180) * sin(dLon / 2) * sin(dLon / 2);
    final c = 2 * atan2(sqrt(a), sqrt(1 - a));
    return R * c;
  }

  void resetTriggers() {
    _triggeredPoiIds.clear();
    activeTriggerPoi = null;
    notifyListeners();
  }
}
