import 'dart:io';

import 'package:dio/dio.dart';
import 'package:video_streaming_app/data/datasources/api/video_datasource.dart';
import 'package:video_streaming_app/domain/entities/video.dart';
import 'package:video_streaming_app/data/models/video_update_request.dart';
import 'package:video_streaming_app/domain/repository/video_repository.dart';

class VideoRepositoryImpl implements VideoRepository {
  final VideoDatasource api;

  VideoRepositoryImpl(this.api);

  @override
  Future<List<Video>> getVideos() async {
    final videoResponse = await api.getVideos();
    return Future.value(videoResponse);
  }

  @override
  Future<Video> getVideoById({required int videoId}) async {
    final videoResponse = await api.getVideoById(videoId: videoId);
    return Future.value(videoResponse);
  }

  @override
  Future<Video> createVideo({required Video video}) async {
    final videoResponse = await api.createVideo(video: video);
    return videoResponse;
  }

  @override
  Future<Video> updateVideo({
    required int videoId,
    required VideoUpdateRequest video,
  }) async {
    final videoResponse = await api.updateVideo(videoId: videoId, video: video);
    return videoResponse;
  }

  @override
  Future<bool> deleteVideo({required int videoId}) async {
    try {
      await api.deleteVideo(videoId: videoId);
      return Future.value(true);
    } catch (e) {
      print("Error al eliminar los datos de video: $e");
      return Future.value(false);
    }
  }

  @override
  Future<Video> uploadVideoFile({
    required int videoId,
    required File file,
    ProgressCallback? onSendProgress,
  }) async {
    try {
      final videoResponse = await api.uploadVideoFile(
        videoId: videoId,
        file: file,
      );
      return Future.value(videoResponse);
    } catch (e) {
      print("Error al subir archivo de video: $e");
      return Future.error(e);
    }
  }

  // @override
  // Future<ResponseBody> streamVideo({
  //   required int videoId,
  //   required String? range,
  // }) async {
  //   final response = await api.streamVideo(videoId: videoId, range: range);
  //   return ResponseBody.fromString(response[""], 200);
  // }

  // @override
  // Future<ResponseBody> getVideoSnapshot({
  //   required int videoId,
  // }) async {
  //   final response = await api.getVideoSnapshot(videoId: videoId);
  //   return ResponseBody.fromString(response[""], 200);
  // }
}
