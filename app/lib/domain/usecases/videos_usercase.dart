import 'package:video_streaming_app/domain/entities/video.dart';
import 'package:video_streaming_app/domain/repository/video_repository.dart';

class VideosUsecase {
  final VideoRepository repository;

  VideosUsecase(this.repository);

  Future<List<Video>> getVideos() async {
    try {
      final res = await repository.getVideos();
      return res;
    } catch (e) {
      return Future.error(e);
    }
  }
}
