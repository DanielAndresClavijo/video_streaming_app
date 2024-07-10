import 'package:supabase_flutter/supabase_flutter.dart'
    show Supabase, SupabaseClient;
import 'package:video_streaming_app/domain/entities/user.dart';
import 'package:video_streaming_app/domain/repository/auth_repository.dart';

class AuthRepositoryImpl implements AuthRepository {
  final SupabaseClient _supabase = Supabase.instance.client;

  User? get loadedUser {
    final userDB = _supabase.auth.currentSession?.user;
    final token = _supabase.auth.currentSession?.accessToken ?? "";

    if (userDB == null) return null;

    final currentUser = User(id: userDB.id, email: userDB.email!, token: token);
    return currentUser;
  }

  @override
  Future<User> signIn(String email, String password) async {
    try {
      final response = await _supabase.auth.signInWithPassword(
        email: email,
        password: password,
      );
      final userDB = response.user;
      if (userDB == null) {
        signOut();
        return Future.error("Failed to login");
      }
      final token = response.session?.accessToken ?? "";
      final currentUser = User(
        id: userDB.id,
        email: userDB.email!,
        token: token,
      );
      return Future.value(currentUser);
    } catch (e) {
      return Future.error(e);
    }
  }

  @override
  Future<void> signOut() async {
    try {
      await _supabase.auth.signOut();
    } catch (e) {
      return Future.error(e);
    }
  }

  @override
  Future<User> signUp(String email, String password) async {
    try {
      final response = await _supabase.auth.signUp(
        email: email,
        password: password,
      );
      final userDB = response.user;
      if (userDB == null) {
        signOut();
        return Future.error("Failed to login");
      }
      final token = response.session?.accessToken ?? "";
      final currentUser = User(
        id: userDB.id,
        email: userDB.email!,
        token: token,
      );
      return Future.value(currentUser);
    } catch (e) {
      return Future.error(e);
    }
  }
}
