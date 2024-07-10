// import 'package:dio/dio.dart';
import 'dart:io';

import 'package:dio/dio.dart';
import 'package:retrofit/retrofit.dart';

import 'package:video_streaming_app/data/datasources/api/video_datasource.dart';
import 'package:video_streaming_app/domain/entities/video.dart';
import 'package:video_streaming_app/data/models/video_update_request.dart';

part 'video_api_datasource.g.dart';

@RestApi()
abstract class VideoApiDatasource extends VideoDatasource {
  factory VideoApiDatasource(Dio dio, {String baseUrl}) = _VideoApiDatasource;

  @GET("/videos")
  @override
  Future<List<Video>> getVideos();

  @GET("/videos/{video_id}")
  @override
  Future<Video> getVideoById({
    @Path("video_id") required int videoId,
  });

  @POST("/videos")
  @override
  Future<Video> createVideo({
    @Body() required Video video,
  });

  @PUT("/videos/{video_id}")
  @override
  Future<Video> updateVideo({
    @Path("video_id") required int videoId,
    @Body() required VideoUpdateRequest video,
  });

  @DELETE("/videos/{video_id}")
  @override
  Future<void> deleteVideo({
    @Path("video_id") required int videoId,
  });

  @POST("/videos/upload/{video_id}")
  @MultiPart()
  @override
  Future<Video> uploadVideoFile({
    @Path("video_id") required int videoId,
    @Part() required File file,
    @SendProgress() ProgressCallback? onSendProgress,
  });

  // @GET("/videos/stream/{video_id}")
  // @override
  // Future<Map<String, dynamic>> streamVideo({
  //   @Path("video_id") required int videoId,
  //   @Header("Range") required String? range,
  // });

  // @GET("/videos/snapshot/{video_id}")
  // @override
  // Future<Map<String, dynamic>> getVideoSnapshot({
  //   @Path("video_id") required int videoId,
  // });
}
