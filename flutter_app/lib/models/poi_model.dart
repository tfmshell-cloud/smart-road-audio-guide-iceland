import 'dart:convert';

class PoiModel {
  final String id;
  final Map<String, String> name;
  final String region;
  final Map<String, String> type;
  final String icon;
  final double lat;
  final double lng;
  final int radius;
  final String badge;
  final Map<String, String> vector;
  final Map<String, String> geology;
  final Map<String, String> saga;
  final Map<String, String> practical;
  final List<dynamic> sources;

  PoiModel({
    required this.id,
    required this.name,
    required this.region,
    required this.type,
    required this.icon,
    required this.lat,
    required this.lng,
    required this.radius,
    required this.badge,
    required this.vector,
    required this.geology,
    required this.saga,
    required this.practical,
    required this.sources,
  });

  factory PoiModel.fromJson(Map<String, dynamic> json) {
    return PoiModel(
      id: json['id'] ?? '',
      name: Map<String, String>.from(json['name'] ?? {}),
      region: json['region'] ?? '',
      type: Map<String, String>.from(json['type'] ?? {}),
      icon: json['icon'] ?? '📍',
      lat: (json['lat'] as num).toDouble(),
      lng: (json['lng'] as num).toDouble(),
      radius: (json['radius'] as num).toInt(),
      badge: json['badge'] ?? 'Official Stop',
      vector: Map<String, String>.from(json['vector'] ?? {}),
      geology: Map<String, String>.from(json['geology'] ?? {}),
      saga: Map<String, String>.from(json['saga'] ?? {}),
      practical: Map<String, String>.from(json['practical'] ?? {}),
      sources: json['sources'] ?? [],
    );
  }

  String getName(String lang) => name[lang] ?? name['en'] ?? '';
  String getVector(String lang) => vector[lang] ?? vector['en'] ?? '';
  String getGeology(String lang) => geology[lang] ?? geology['en'] ?? '';
  String getSaga(String lang) => saga[lang] ?? saga['en'] ?? '';
  String getPractical(String lang) => practical[lang] ?? practical['en'] ?? '';
}
