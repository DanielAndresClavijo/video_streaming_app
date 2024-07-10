import 'package:json_annotation/json_annotation.dart';

part 'video.g.dart';

@JsonSerializable()
class Video {
  final int id;
  final String userId;
  final String title;
  final String description;
  final String url;
  final String createdAt;
  final String updatedAt;

  const Video({
    required this.id,
    required this.userId,
    required this.title,
    required this.description,
    required this.url,
    this.createdAt = "",
    this.updatedAt = "",
  });

  factory Video.fromJson(Map<String, dynamic> json) => _$VideoFromJson(json);

  Map<String, dynamic> toJson() => _$VideoToJson(this);

  Video copyWith({
    int? id,
    String? userId,
    String? title,
    String? description,
    String? url,
    String? createdAt,
    String? updatedAt,
  }) {
    return Video(
      id: id ?? this.id,
      userId: userId ?? this.userId,
      title: title ?? this.title,
      description: description ?? this.description,
      url: url ?? this.url,
      createdAt: createdAt ?? this.createdAt,
      updatedAt: updatedAt ?? this.updatedAt,
    );
  }

  @override
  String toString() {
    return 'Video(id: $id, userId: $userId, title: $title, description: $description, url: $url, createdAt: $createdAt, updatedAt: $updatedAt)';
  }

  @override
  bool operator ==(covariant Video other) {
    if (identical(this, other)) return true;

    return other.id == id &&
        other.userId == userId &&
        other.title == title &&
        other.description == description &&
        other.url == url &&
        other.createdAt == createdAt &&
        other.updatedAt == updatedAt;
  }

  @override
  int get hashCode {
    return id.hashCode ^
        userId.hashCode ^
        title.hashCode ^
        description.hashCode ^
        url.hashCode ^
        createdAt.hashCode ^
        updatedAt.hashCode;
  }
}
