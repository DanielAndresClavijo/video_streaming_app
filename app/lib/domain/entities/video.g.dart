// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'video.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Video _$VideoFromJson(Map<String, dynamic> json) => Video(
      id: (json['id'] as num).toInt(),
      userId: json['userId'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      url: json['url'] as String,
      createdAt: json['createdAt'] as String? ?? "",
      updatedAt: json['updatedAt'] as String? ?? "",
    );

Map<String, dynamic> _$VideoToJson(Video instance) => <String, dynamic>{
      'id': instance.id,
      'userId': instance.userId,
      'title': instance.title,
      'description': instance.description,
      'url': instance.url,
      'createdAt': instance.createdAt,
      'updatedAt': instance.updatedAt,
    };
