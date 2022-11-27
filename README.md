# Artsy URL Shortener

Based on [kutt](https://github.com/thedevs-network/kutt).

Multicontainer using:
- Express (Node)
- Redis
- Postgres

Runs on http://localhost:3000

## Docker

### Local

```
docker-compose up
```

### Remote

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