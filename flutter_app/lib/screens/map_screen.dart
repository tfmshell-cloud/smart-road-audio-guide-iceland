import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/poi_model.dart';
import '../services/geofence_engine.dart';
import '../services/tts_audio_service.dart';

class MapScreen extends StatefulWidget {
  const MapScreen({Key? key}) : super(key: key);

  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> {
  List<PoiModel> pois = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadPois();
  }

  Future<void> _loadPois() async {
    final jsonStr = await rootBundle.loadString('assets/data/pois.json');
    final List<dynamic> decoded = json.decode(jsonStr);
    setState(() {
      pois = decoded.map((e) => PoiModel.fromJson(e)).toList();
      isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) {
      return const Scaffold(
        backgroundColor: Color(0xFF070B14),
        body: Center(child: CircularProgressIndicator(color: Colors.cyan)),
      );
    }

    final geofence = Provider.of<GeofenceEngine>(context);

    return Scaffold(
      backgroundColor: const Color(0xFF070B14),
      appBar: AppBar(
        backgroundColor: const Color(0xFF0D1424),
        elevation: 0,
        title: Row(
          children: const [
            Text('🇮🇸 ', style: TextStyle(fontSize: 20)),
            Text('Iceland Smart Road Guide', style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold)),
          ],
        ),
        actions: [
          Container(
            margin: const EdgeInsets.symmetric(vertical: 10, horizontal: 8),
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: const Color(0xFF10B981).withOpacity(0.2),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: const Color(0xFF10B981).withOpacity(0.4)),
            ),
            child: const Text('OFFLINE PMTILES', style: TextStyle(color: Color(0xFF10B981), fontSize: 11, fontWeight: FontWeight.bold)),
          ),
        ],
      ),
      body: Stack(
        children: [
          // 3D Map Area Placeholder (MapLibreGL or Interactive Vector View)
          Container(
            color: const Color(0xFF090D16),
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.explore_outlined, color: Colors.cyan, size: 64),
                  const SizedBox(height: 12),
                  const Text('MapLibre GL Native 3D Viewport', style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 6),
                  Text('34 POI Locked • 3D Pitch 55° • Local Tile Server :8088', style: TextStyle(color: Colors.grey[400], fontSize: 12)),
                  const SizedBox(height: 16),
                  ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.cyan[600],
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                    ),
                    onPressed: () {
                      // Trigger Seljalandsfoss test
                      final selj = pois.firstWhere((p) => p.id == 'seljalandsfoss');
                      geofence.setManualPosition(selj.lat, selj.lng, 88.0);
                    },
                    icon: const Icon(Icons.play_arrow),
                    label: const Text('Simulate Hit: Seljalandsfoss'),
                  ),
                ],
              ),
            ),
          ),

          // Active Geofence Alert Banner
          if (geofence.activeTriggerPoi != null)
            Positioned(
              bottom: 20,
              left: 16,
              right: 16,
              child: Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: const Color(0xFF0F172A).withOpacity(0.95),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: const Color(0xFF10B981)),
                  boxShadow: [
                    BoxShadow(color: const Color(0xFF10B981).withOpacity(0.3), blurRadius: 20, spreadRadius: 2),
                  ],
                ),
                child: Row(
                  children: [
                    Container(
                      width: 44,
                      height: 44,
                      decoration: BoxDecoration(
                        color: const Color(0xFF10B981).withOpacity(0.2),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Center(child: Text(geofence.activeTriggerPoi!.icon, style: const TextStyle(fontSize: 22))),
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text('GEOFENCE HIT • 3D VOICE TRIGGER', style: TextStyle(color: Color(0xFF10B981), fontSize: 10, fontWeight: FontWeight.bold)),
                          Text(geofence.activeTriggerPoi!.getName('uk'), style: const TextStyle(color: Colors.white, fontSize: 15, fontWeight: FontWeight.bold)),
                          Text(geofence.activeTriggerPoi!.getVector('uk'), style: TextStyle(color: Colors.grey[400], fontSize: 12)),
                        ],
                      ),
                    ),
                    IconButton(
                      icon: const Icon(Icons.volume_up, color: Colors.cyan),
                      onPressed: () {
                        geofence.ttsService.speakPoiGuide(geofence.activeTriggerPoi!);
                      },
                    ),
                  ],
                ),
              ),
            ),
        ],
      ),
    );
  }
}
