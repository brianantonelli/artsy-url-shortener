# Artsy URL Shortener

Based on [kutt](https://github.com/thedevs-network/kutt).

Multicontainer using:
- Nginx
- Express
- Redis
- Postgres

Runs on http://localhost

## Scraper

```
cd scraper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Docker

### Local

1. Add `artsy.co` to `/etc/hosts` pointing to `127.0.0.1`.
2. Start Docker containers: `docker-compose up`

### Remote

SCP app to EC2 or remote deploy via Docker (WIP).

```
docker context create ec2 --description "ec2" --docker "host=tcp://34.229.179.65:237,key=/Users/brianantonelli/.ssh/brian-personal.pem"
docker context use ec2
docker-compose up -d
```

## Finch

Install Finch VM: `finch vm init`

```
finch vm start # if its off
finch compose up
```