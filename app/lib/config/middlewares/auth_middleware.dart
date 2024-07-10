import 'package:dio/dio.dart';

class AuthMiddleware extends Interceptor {

  AuthMiddleware();

  @override
  void onRequest(
    RequestOptions options,
    RequestInterceptorHandler handler,
  ) {
    options.headers["auth"] = "Bearer $token";
    super.onRequest(options, handler);
  }
}
