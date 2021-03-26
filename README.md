# essh-stat

Simple log scraper that provides maybe accurate results

## Install
just clone

Requires python 3 (basically any, this thing isn't complex)

## Running

`python3 pit-calc.py`

The first run will complain that you don't have a config file.
Just locate your endlessh log file and copy it's path, then shove it in the config file.

example config:

```json
{"log_location": "/root/.pm2/logs/endlessh-out.log"}
```
