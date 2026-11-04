import 'package:flutter_tts/flutter_tts.dart';
import 'package:audioplayers/audioplayers.dart';
import '../models/poi_model.dart';

class TtsAudioService {
  final FlutterTts _flutterTts = FlutterTts();
  final AudioPlayer _audioPlayer = AudioPlayer();
  bool _isPlaying = false;
  String _currentLang = 'uk';

  TtsAudioService() {
    _initTts();
  }

  void _initTts() async {
    await _flutterTts.setSpeechRate(0.95);
    await _flutterTts.setPitch(1.0);
    _flutterTts.setCompletionHandler(() {
      _isPlaying = false;
    });
  }

  void setLanguage(String lang) {
    _currentLang = lang;
    _flutterTts.setLanguage(lang == 'uk' ? 'uk-UA' : 'en-US');
  }

  Future<void> speakPoiGuide(PoiModel poi) async {
    await stop();
    _isPlaying = true;
    final text = "${poi.getName(_currentLang)}. ${poi.getVector(_currentLang)}. ${poi.getGeology(_currentLang)} ${poi.getSaga(_currentLang)}";
    await _flutterTts.speak(text);
  }

  Future<void> stop() async {
    await _flutterTts.stop();
    await _audioPlayer.stop();
    _isPlaying = false;
  }

  bool get isPlaying => _isPlaying;
}
