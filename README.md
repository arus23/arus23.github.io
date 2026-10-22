# Arundhati Shanbhag — personal website

The approved floral design is served as static files from the repository root. `.nojekyll` disables the old template build. The previous site is preserved on `backup/pre-floral-2026-10-22` and in Git history; legacy source and downloads are retained.

## Updates
- Edit `site-source/content.json` for biography, email addresses, interests, and profile links.
- Run `python3 site-source/build.py` to regenerate `index.html`.
- Edit `site-source/build.py` for research and other page sections.
- Edit `style.css` for appearance.
- Replace `portrait.jpg` for the portrait; its frame is controlled by CSS.
- Commit the changed content and generated HTML to the GitHub Pages publishing branch.

The old CV download is retained but is not advertised as current. Publications link to Google Scholar until a verified publication list is added.
