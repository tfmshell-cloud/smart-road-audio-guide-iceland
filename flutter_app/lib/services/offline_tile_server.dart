import 'dart:io';
import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart' as shelf_io;
import 'package:shelf_static/shelf_static.dart';

/// Embedded Localhost HTTP Server for streaming offline PMTiles / MBTiles to MapLibre GL
class OfflineTileServer {
  static HttpServer? _server;
  static int port = 8088;

  static Future<void> startServer() async {
    if (_server != null) return;

    try {
      final docDir = await getApplicationDocumentsDirectory();
      final tilesDir = Directory('${docDir.path}/tiles');
      if (!await tilesDir.exists()) {
        await tilesDir.create(recursive: true);
      }

      // Check if bundle has asset tiles and extract if needed
      final targetFile = File('${tilesDir.path}/iceland.mbtiles');
      if (!await targetFile.exists()) {
        try {
          final byteData = await rootBundle.load('assets/tiles/iceland.mbtiles');
          await targetFile.writeAsBytes(byteData.buffer.asUint8List());
        } catch (_) {
          // If asset is not yet copied in dev mode, server continues
        }
      }

      final handler = const Pipeline()
          .addMiddleware(logRequests())
          .addHandler(createStaticHandler(tilesDir.path, defaultDocument: 'index.html'));

      _server = await shelf_io.serve(handler, InternetAddress.loopbackIPv4, port);
      print('Offline Tile Server running on http://127.0.0.1:$port/');
    } catch (e) {
      print('Failed to start offline tile server: $e');
    }
  }

  static Future<void> stopServer() async {
    await _server?.close(force: true);
    _server = null;
  }
}
