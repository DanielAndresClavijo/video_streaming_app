import 'dart:io';

import 'package:dio/dio.dart';
import 'package:video_streaming_app/domain/entities/video.dart';
import 'package:video_streaming_app/data/models/video_update_request.dart';

abstract class VideoDatasource {
  Future<List<Video>> getVideos();

  Future<Video> getVideoById({required int videoId});

  Future<Video> createVideo({required Video video});

  Future<Video> updateVideo({
    required int videoId,
    required VideoUpdateRequest video,
  });

  Future<void> deleteVideo({required int videoId});

  Future<Video> uploadVideoFile({
    required int videoId,
    required File file,
    ProgressCallback? onSendProgress,
  });

  // Future<Map<String, dynamic>> streamVideo({
  //   required int videoId,
  //   required String? range,
  // });

  // Future<Map<String, dynamic>> getVideoSnapshot({
  //   required int videoId,
  // });
}
