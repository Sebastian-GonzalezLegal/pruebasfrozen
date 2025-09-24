import os
from app import create_app
from app.config import Config

# 🧱 INICIALIZAR FLASK
app = create_app()

if __name__ == "__main__":
    print("🚀 Iniciando API de Trazabilidad de Insumos...")
    print(f"🔧 Modo Debug: {Config.DEBUG}")
    print(f"🔗 Supabase URL: {Config.SUPABASE_URL}")
    print("📌 Endpoints disponibles:")
    print("    GET  /api/health")
    print("    GET  /api/insumos/catalogo")
    print("    POST /api/insumos/catalogo")
    print("    GET  /api/inventario/lotes")
    print("    POST /api/inventario/lotes")
    print("    POST /api/inventario/alertas")
    print("    GET  /dashboard")


    # 🌐 Ejecutar Flask
    flask_port = int(os.environ.get("FLASK_PORT", 5000))
    app.run(host="0.0.0.0", port=flask_port, debug=Config.DEBUG)


