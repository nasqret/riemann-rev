#!/bin/sh
# Serve the reading site at http://127.0.0.1:${1:-8000}/ (PDF.js needs http; a file:// page cannot load it).
cd "$(dirname "$0")" || exit 1
exec python3 -c 'import http.server, mimetypes, sys; mimetypes.add_type("text/javascript", ".mjs"); http.server.ThreadingHTTPServer(("127.0.0.1", int(sys.argv[1])), http.server.SimpleHTTPRequestHandler).serve_forever()' "${1:-8000}"
