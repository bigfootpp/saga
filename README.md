<h1 align="center">Saga</h1>

<p align="center">Stremio addon for Jackett torrents</p>

# Features
- Stremio addon
- Jackett / Torznab scraper
- TMDB metadata (+ Kitsu lookup in background for anime titles)
- Torrent resolver with SQLite cache
- Live seeders check via UDP trackers
- Specialized in finding dubs
- Smart file matching with GuessIt

# Limitations
- Series only for now, TMDB IDs only
- Dub-focused: sub support is limited for now and will be improved later
- No debrid support, and probably never will

# Installation
Configure first with `.env` (see `.env-example`):

```sh
git clone https://github.com/bigfootpp/saga
cd saga
```

## From source
```sh
pip install uv
uv sync
uv run uvicorn saga.main:app --host 0.0.0.0 --port 3000
```

## Docker
```sh
docker compose up --build
```

# Configure
Configure the addon here and copy the link to Stremio:

`http://localhost:3000/configure`

From this page you can set your preferred dub languages (`preferredDubs`), and result limits (`dubMaxResult` default 5, `otherMaxResult` default 10). Then use `Install` or `Copy Link` — streams only work with a link generated from this page (`/{config}/manifest.json`).
