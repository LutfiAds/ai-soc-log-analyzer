#!/bin/bash

echo "[+] Creating config directory if not exists..."
mkdir -p config

echo "[+] Downloading GeoLite2 City database..."

wget -O config/GeoLite2-City.mmdb https://git.io/GeoLite2-City.mmdb

if [ -f config/GeoLite2-City.mmdb ]; then
    echo "[+] GeoLite2 database downloaded successfully."
else
    echo "[!] Download failed. Please download manually from MaxMind."
fi
