import 'package:flutter/material.dart';

class VideoListScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Video List'),
      ),
      body: Center(
        child: Text('List of videos will be shown here'),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // Navigate to video creation screen
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
