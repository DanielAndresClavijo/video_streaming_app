import 'package:flutter/cupertino.dart';
import 'package:go_router/go_router.dart';

final router = GoRouter(
  routes: [],
  redirect: _redirect,
);

Future<String?> _redirect(BuildContext context, GoRouterState state) {

  return Future.value(null);
}