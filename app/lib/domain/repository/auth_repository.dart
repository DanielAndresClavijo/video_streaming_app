import 'package:video_streaming_app/domain/entities/user.dart';

abstract class AuthRepository {
  Future<User> signIn(String email, String password);
  Future<void> signOut();
  Future<User> signUp(String email, String password);
}
