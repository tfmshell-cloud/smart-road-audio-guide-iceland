import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'models/poi_model.dart';
import 'services/geofence_engine.dart';
import 'services/tts_audio_service.dart';
import 'services/offline_tile_server.dart';
import 'screens/map_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Start local embedded offline tile server for PMTiles
  await OfflineTileServer.startServer();

  // Load POIs
  final jsonStr = await rootBundle.loadString('assets/data/pois.json');
  final List<dynamic> decoded = json.decode(jsonStr);
  final pois = decoded.map((e) => PoiModel.fromJson(e)).toList();

  final ttsService = TtsAudioService();
  final geofenceEngine = GeofenceEngine(pois: pois, ttsService: ttsService);

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider<GeofenceEngine>.value(value: geofenceEngine),
        Provider<TtsAudioService>.value(value: ttsService),
      ],
      child: const IcelandGuideApp(),
    ),
  );
}

class IcelandGuideApp extends StatelessWidget {
  const IcelandGuideApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Iceland Smart Road Audio Guide',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.dark,
        scaffoldBackgroundColor: const Color(0xFF070B14),
        primaryColor: const Color(0xFF38BDF8),
        fontFamily: 'Roboto',
      ),
      home: const MapScreen(),
    );
  }
}
