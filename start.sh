#!/usr/bin/env bash
gunicorn -w 1 -b 0.0.0.0:10000 web.app:app
