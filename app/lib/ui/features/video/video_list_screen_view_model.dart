import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:video_streaming_app/domain/entities/video.dart';

class VideoListScreenViewModelState {
  final List<Video> videos;

  const VideoListScreenViewModelState({
    required this.videos,
  });

  VideoListScreenViewModelState copyWith({
    List<Video>? videos,
  }) {
    return VideoListScreenViewModelState(
      videos: videos ?? this.videos,
    );
  }
}

class VideoListScreenViewModel
    extends StateNotifier<VideoListScreenViewModelState> {
  VideoListScreenViewModel({
    required List<Video> videos,
  }) : super(const VideoListScreenViewModelState(videos: []));
}
