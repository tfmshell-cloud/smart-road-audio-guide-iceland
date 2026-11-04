import 'package:flutter/material.dart';

class B2bKioskScreen extends StatelessWidget {
  final String partnerName;
  final String licenseTier;
  final String fleetCarId;

  const B2bKioskScreen({
    Key? key,
    this.partnerName = 'Blue Car Rental (Keflavík Fleet)',
    this.licenseTier = 'Enterprise Fleet SaaS (200 Vehicles)',
    this.fleetCarId = 'IS-TOYOTA-RAV4-921',
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF070B14),
      appBar: AppBar(
        backgroundColor: const Color(0xFF0F172A),
        title: Text('B2B Fleet Kiosk • $partnerName', style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold)),
        actions: [
          IconButton(
            icon: const Icon(Icons.lock_outline, color: Colors.amber),
            onPressed: () {},
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0xFF1E293B).withOpacity(0.7),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: Colors.cyan.withOpacity(0.4)),
              ),
              child: Row(
                children: [
                  const Icon(Icons.directions_car, color: Colors.cyan, size: 36),
                  const SizedBox(width: 14),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('Vehicle Assigned: $fleetCarId', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 15)),
                      Text('License: $licenseTier', style: TextStyle(color: Colors.grey[400], fontSize: 12)),
                      const Text('Auto-Reset: After Return to KEF Airport Geofence', style: TextStyle(color: Color(0xFF10B981), fontSize: 11)),
                    ],
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),
            const Text('FLIGHT & RETURN SAFETY TELEMETRY', style: TextStyle(color: Colors.grey, fontSize: 11, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),
            ListTile(
              tileColor: const Color(0xFF0F172A),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              leading: const Icon(Icons.shield, color: Color(0xFF10B981)),
              title: const Text('SafeTravel.is Hazard Alerts Live', style: TextStyle(color: Colors.white, fontSize: 13)),
              subtitle: const Text('High wind warning: Vík í Mýrdal (gusts up to 28 m/s)', style: TextStyle(color: Colors.amber, fontSize: 11)),
            ),
          ],
        ),
      ),
    );
  }
}
