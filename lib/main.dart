import 'package:flutter/material.dart';

void main() => runApp(RafidianApp());

class RafidianApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'رافديان',
      home: HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('رافديان شات')),
      body: Center(
        child: Text('اهلا يصگر، التطبيق اشتغل ✅', style: TextStyle(fontSize: 24)),
      ),
    );
  }
}
