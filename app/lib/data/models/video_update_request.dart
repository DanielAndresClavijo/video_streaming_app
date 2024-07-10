import 'package:json_annotation/json_annotation.dart';

part 'video_update_request.g.dart';

@JsonSerializable()
class VideoUpdateRequest {
  final String? title;
  final String? description;
  final String? url;
  final String? updatedAt;

  const VideoUpdateRequest({
    this.title,
    this.description,
    this.url,
    this.updatedAt,
  });

  factory VideoUpdateRequest.fromJson(Map<String, dynamic> json) =>
      _$VideoUpdateRequestFromJson(json);

  Map<String, dynamic> toJson() => _$VideoUpdateRequestToJson(this);
}
