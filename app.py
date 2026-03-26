#!/usr/bin/env python3
"""SnazzyShowcase – portfolio page for Snazzy vibe projects."""

from pathlib import Path

from flask import Flask, send_file, send_from_directory

app = Flask(__name__)

VIBE_ROOT = Path("/home/rdf/Scripts/vibe")
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".ico"}


@app.route("/")
def index():
    return send_from_directory(Path(__file__).parent, "index.html")


@app.route("/<path:filename>")
def static_files(filename: str):
    allowed = {".png", ".jpg", ".jpeg", ".svg", ".ico", ".json", ".css", ".js"}
    if Path(filename).suffix.lower() in allowed:
        filepath = Path(__file__).parent / filename
        if filepath.is_file():
            return send_file(filepath)
    return "Not found", 404


@app.route("/icon/<path:filepath>")
def icon(filepath: str):
    resolved = (VIBE_ROOT / filepath).resolve()
    if not str(resolved).startswith(str(VIBE_ROOT.resolve())):
        return "Forbidden", 403
    if resolved.suffix.lower() not in ALLOWED_EXTENSIONS:
        return "Forbidden", 403
    if not resolved.is_file():
        return "Not found", 404
    return send_file(resolved)


if __name__ == "__main__":
    app.run(debug=True, port=7777)
