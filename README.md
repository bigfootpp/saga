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

# Requirements
- Linux only (does not work on Windows / macOS (not tested))
- Jackett is required: Saga gets all its torrents from it
- A TMDB API key (free at https://www.themoviedb.org/settings/api)
- Docker recommended if you are not a developer and for easier setup

> Jackett must be configured first: open `http://localhost:9117`, add your indexers/trackers, then copy your API key from the Jackett dashboard.
> With Docker, Jackett config is saved in the `jackett-config/` folder next to the `docker-compose.yml` file, so it is kept on restart.

# Installation

## 1. Get the project
```sh
git clone https://github.com/bigfootpp/saga
cd saga
```

## 2. Docker (recommended)
This starts 3 things: Saga (`http://localhost:3000`), Jackett (`http://localhost:9117`) and FlareSolverr.

1. Start Jackett once to generate its config:
```sh
docker compose up -d jackett
```

2. Open `http://localhost:9117`, add your indexers/trackers.

3. Copy your API key from the Jackett dashboard (top right).

4. Create your `.env` from the example:
```sh
cp .env-example .env
```
Then edit `.env`:
```sh
JACKETT_API_KEY=paste-your-key-here
JACKETT_BASE_URL=http://jackett:9117
TMDB_API_KEY=paste-your-tmdb-key-here
```

5. Start everything:
```sh
docker compose up --build
```

No data is lost on restart: Jackett config stays in `./jackett-config/` and Saga data in `./saga-data/`, right where your `docker-compose.yml` is.

## 3. From source (developers)
Create your `.env` first (`JACKETT_BASE_URL=http://localhost:9117`), Jackett must run separately.

```sh
pip install uv
uv sync
uv run uvicorn saga.main:app --host 0.0.0.0 --port 3000
```

# Configure
Configure the addon here and copy the link to Stremio:

`http://localhost:3000/configure`

From this page you can set your preferred dub languages (`preferredDubs`), and result limits (`dubMaxResult` default 5, `otherMaxResult` default 10). Then use `Install` or `Copy Link` — streams only work with a link generated from this page (`/{config}/manifest.json`).
