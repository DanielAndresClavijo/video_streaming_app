// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'video_update_request.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

VideoUpdateRequest _$VideoUpdateRequestFromJson(Map<String, dynamic> json) =>
    VideoUpdateRequest(
      title: json['title'] as String?,
      description: json['description'] as String?,
      url: json['url'] as String?,
      updatedAt: json['updatedAt'] as String?,
    );

Map<String, dynamic> _$VideoUpdateRequestToJson(VideoUpdateRequest instance) =>
    <String, dynamic>{
      'title': instance.title,
      'description': instance.description,
      'url': instance.url,
      'updatedAt': instance.updatedAt,
    };
