#!/usr/bin/env python3
from __future__ import annotations
from typing import Any
from spotipy import Spotify  # type:ignore
from spotipy.oauth2 import SpotifyClientCredentials # type:ignore
from urllib.parse import urlparse
import json

playlists = [
    "https://open.spotify.com/playlist/3iLEJOL75n0J04oCr15Mhl"  # Fall 2023 - Week 1
]

def get_uri_from_url(url: str) -> str:
    pieces = urlparse(url)
    path = pieces.path
    assert "/playlist/" in path, f"Weird playlist URL: {url}"
    stem = "spotify:playlist:{playlist_id}"
    uri = stem.format(playlist_id=path.split("/")[-1])
    # print(f"Playlist URI: {uri}")
    return uri

def get_id_from_url(url: str) -> str:
    pieces = urlparse(url)
    path = pieces.path
    assert "/playlist/" in path, f"Weird playlist URL: {url}"
    id = path.split("/")[-1]
    # print(f"Playlist ID: {id}")
    return id

def get_songs(conn: Spotify, playlist_url: str) -> list[tuple[str, str]]:
    """Get songs from a playlist, return a list of artist, track."""
    id = get_id_from_url(playlist_url)
    data: dict[str, Any] = conn.playlist(id, fields="")
    print(json.dumps(data, indent=4, sort_keys=True))
    return []

def main() -> None:
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials())
    print(get_songs(sp, playlists[0]))

if __name__ == "__main__":
    main()
