import 'package:dio/dio.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:get_it/get_it.dart';
import 'package:video_streaming_app/config/assets.dart';
import 'package:video_streaming_app/config/config.dart';
import 'package:video_streaming_app/config/middlewares/auth_middleware.dart';
import 'package:video_streaming_app/data/datasources/api/impl/video_api_datasource.dart';
import 'package:video_streaming_app/data/datasources/api/video_datasource.dart';
import 'package:video_streaming_app/data/repositories_impl/video_repository_impl.dart';
import 'package:video_streaming_app/domain/repository/video_repository.dart';
import 'package:video_streaming_app/domain/usecases/videos_usercase.dart';
import 'package:video_streaming_app/ui/features/video/video_list_screen_view_model.dart';

final _getIt = GetIt.instance;

void setupInjector(AppConfig config) {

  // Register Config
  _getIt.registerSingleton<AppConfig>( config);

  // Register Dio
  _getIt.registerLazySingleton<Dio>(() {
    final  Dio dio = Dio(BaseOptions(baseUrl: config.apiBaseUrl));
    dio.interceptors.add(AuthMiddleware());
    return dio;
  });

  // Register API
  _getIt.registerFactory<VideoDatasource>(
    () => VideoApiDatasource(_getIt<Dio>()),
  );

  // Register Video Repository
  _getIt.registerFactory<VideoRepository>(
    () => VideoRepositoryImpl(_getIt<VideoDatasource>()),
  );

  // Register Video Use Case
  _getIt.registerFactory<VideosUsecase>(
    () => VideosUsecase(_getIt<VideoRepository>()),
  );

  /// VideoListScreen ViewModel Provider
  _getIt.registerLazySingleton<
      StateNotifierProvider<VideoListScreenViewModel,
          VideoListScreenViewModelState>>(
    () => StateNotifierProvider<VideoListScreenViewModel,
        VideoListScreenViewModelState>(
      (ref) => VideoListScreenViewModel(videos: []),
    ),
    instanceName: "VideoListScreenStateNotifierProvider",
  );
}
