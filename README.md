# MyCousinVinyl Home Assistant Add-on

Home Assistant add-on for the MyCousinVinyl stack (frontend, API, workers, and Discogs service).
This add-on expects external MQTT and Postgres add-ons to be running.

## Install

1. Home Assistant: Settings -> Add-ons -> Add-on Store -> Repositories.
2. Add `https://github.com/cajo-dk/mycousinvinyl-ha`.
3. Install "MyCousinVinyl" and configure options.

## Requirements

- MQTT broker: Home Assistant Mosquitto add-on (default URL `mqtt://core-mosquitto:1883`).
- Postgres: Home Assistant PostgreSQL add-on (default URL `postgresql://postgres:postgres@core-postgres:5432/mycousinvinyl`).

## Default ports

- `80/tcp`: Web UI (nginx)
- `8000/tcp`: API (FastAPI)
- `8001/tcp`: Discogs service

## Option highlights

Required:
- `database_url`: PostgreSQL connection string.
- `mqtt_url`: MQTT broker URL.

Common:
- `mqtt_username`, `mqtt_password`, `mqtt_topic_prefix`
- `azure_tenant_id`, `azure_client_id`, `azure_audience`
- `azure_group_admin`, `azure_group_editor`, `azure_group_viewer`
- `discogs_user_agent`, `discogs_key`, `discogs_secret`

Frontend build-time (optional, baked into the UI during build):
- `vite_api_url`, `vite_azure_client_id`, `vite_azure_tenant_id`, `vite_azure_redirect_uri`, `vite_azure_group_admin`

## License

See `LICENSE.txt`.
