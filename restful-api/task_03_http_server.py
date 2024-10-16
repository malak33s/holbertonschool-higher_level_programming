#!/usr/bin/python3
'''
Gère différents types de requêtes HTTP
'''
import json
import http.server


class HttpRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Classe pour gérer les requêtes HTTP
    """
    def do_GET(self):
        # Vérifie le chemin demandé
        if self.path == "/":
            # Réponse pour le chemin racine
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Bonjour, ceci est une simple API!')

        elif self.path == "/data":
            # Réponse avec des données JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Exemple de données
            data = {"name": "John", "age": 30, "city": "New York"}
            # Convertit et envoie les données au format JSON
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == '/info':
            # Réponse avec informations sur l'API
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_data = {
                "version": "1.0",
                "description": "Une simple API avec http.server"
            }
            self.wfile.write(json.dumps(json_data).encode("utf-8"))

        elif self.path == "/status":
            # Réponse pour l'état de l'API
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            # Gère les chemins non définis avec une erreur 404
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('Chemin non trouvé'.encode('utf-8'))


# Numéro du pot
PORT = 8000

# Configure et démarre le serveur HTTP
if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), HttpRequestHandler) as httpd:
        print(f"Serveur en cours d'exécution sur le port {PORT}...")
        httpd.serve_forever()

