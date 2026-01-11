#!/usr/bin/env bash
gunicorn -w 1 -b 0.0.0.0:10000 flask_app.app:app
