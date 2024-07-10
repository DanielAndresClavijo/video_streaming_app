/// Clase de configuración de variables de la aplicación.
class AppConfig {
  /// Url para la conexion a la base de datos con supabase.
  final String supabaseUrl;

  /// Token de acceso a la base de datos con supabase.
  final String supabaseKey;
  
  /// Url base para la api del servidor.
  final String apiBaseUrl;

  const AppConfig({
    this.supabaseUrl = "",
    this.supabaseKey = "",
    this.apiBaseUrl = "",
  });


  /// Configura las variables de la aplicación.
  factory AppConfig.setup()  {
    return const AppConfig(
      supabaseUrl: "",
      supabaseKey: "",
      apiBaseUrl: "",
    );
  }
}
