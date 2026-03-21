from pathlib import Path

from flask import Flask, send_from_directory
from flask_cors import CORS

from backend.config import settings
from backend.routes.chat_routes import chat_bp
from backend.services.watson_service import WatsonService


def create_app() -> Flask:
    frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    app = Flask(
        __name__,
        static_folder=str(frontend_dir),
        static_url_path="",
    )
    app.config["JSON_AS_ASCII"] = False
    app.config["WATSON_SERVICE"] = WatsonService(settings)
    CORS(app)
    app.register_blueprint(chat_bp)

    @app.get("/")
    def serve_frontend():
        return send_from_directory(app.static_folder, "index.html")

    @app.get("/assets/<path:filename>")
    def serve_assets(filename: str):
        return send_from_directory(assets_dir, filename)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=settings.port, debug=settings.debug)
