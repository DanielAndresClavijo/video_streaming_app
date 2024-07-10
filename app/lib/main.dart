import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:video_streaming_app/config/config.dart';
import 'package:video_streaming_app/injector/injector.dart';
import 'package:video_streaming_app/ui/features/base/app.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final AppConfig config = AppConfig.setup();

  await Supabase.initialize(
    url: config.supabaseKey,
    anonKey: config.supabaseKey,
  );
  setupInjector(config);


  runApp(const ProviderScope(
    child: MyApp(),
  ));
}
