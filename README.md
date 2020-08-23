# votes-rest-api
Votation REST API

## Instalation

### Localhost

#### Prerequisites
```
sudo apt-get install python3-dev python3-pip
sudo pip3 install -U virtualenv
```
#### Instalation
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requeriments.txt
```

## Django superuser
- User = adminroot
- Pass = 123toornimda

## Access
```
[SERVER_NAME]:[PORT] /api/ [VERSION] / [SERVICE]
```
- Example = localhost:8000/api/v0/agendas/

