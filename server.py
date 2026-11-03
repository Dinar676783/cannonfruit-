# -*- coding: utf-8 -*-
"""Мини-сервер для Фруктового Шутера. Работает локально и на Railway."""
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8000))  # Railway сам подставляет PORT


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # чтобы на телефоне всегда грузилась свежая версия игры
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass  # тихий лог


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", PORT), Handler) as srv:
        print(f"Фруктовый Шутер запущен: http://localhost:{PORT}")
        srv.serve_forever()
