# grh-compact: the reading site

Built 2026-11-28T11:29Z by `rb.py site` (readback 0.9.0); artifact commit 72fead102f66, toolchain leanprover/lean4:v4.35.0.

Open `index.html` through a web server, not as a file. The reading mode needs http: PDF.js draws the pages of
each note (a browser runs it only over http), and the column beside the pages reads each structured proof and
each whole declaration from their own pages. Here:

    ./serve.sh            # then open http://127.0.0.1:8000/

(`serve.sh 8123` uses another port; it serves `.mjs` files as JavaScript, which older Pythons do not.)
On GitHub Pages the folder works as it is. Opened as a file, the chapters, units, structured proofs and Lean
source read as usual; a reading page then shows the note in the browser's own PDF viewer, moved to the page of
the chosen statement, without marks on the pages, and beside it the statement of each declaration.

Pages: 8 chapters, 47 notes (1254 PDF pages), 118 units, 986 structured proofs, 794 Lean files.
Software and fonts: see `assets/vendor/NOTICE.txt`. The Lean text belongs to its authors: see `about.html`.
