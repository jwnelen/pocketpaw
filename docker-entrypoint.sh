#!/bin/sh
set -e
# Railway (and Docker in general) mounts volumes as root. Fix ownership so the
# pocketpaw user can read/write its data directory before starting the app.
chown -R pocketpaw:pocketpaw /home/pocketpaw/.pocketpaw 2>/dev/null || true
exec runuser -u pocketpaw -- "$@"
