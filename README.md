# votes-rest-api
Votation REST API

- Python 3.6
- Django 2.2 LTS
- Django REST Framework 3.11

## Endpoints
GET, POST, PUT, PATCH, DELETE
- Agenda
    - Fields: Title, Description
- Session
    - Fields: Begin, End, _Agenda
- User
    - Fields: Name, Email, CPF
- Vote
    - Fields: Opinion, _Session, _User 

### JSON response etities
```
"agenda":
{
    "title": "Teste",
    "description": "Teste"
    "sessions":
    [
        {
            "begin": "2020-08-24T16:30:00",
            "end": "2020-08-24T17:40:00",
            "votes":
            [
                {
                    "opinion": true,
                    "user":
                    {
                        "name": "Test",
                        "cpf": "65653428060",
                        "email": "teste@test.com"
                    }
                },
                {
                    "opinion": False,
                    "user":
                    {
                        "name": "Test2",
                        "cpf": "89414865055",
                        "email": "teste2@test.com"
                    }
                }
            ]
        },
        {
            "begin": "2020-08-24T16:30:00",
            "end": "2020-08-24T17:40:00",
            "votes":[...]
        }
    ]
}
```

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
cp .env.example .env
```
#### Run
```
python manage.py runserver
```


### Docker

#### Prerequisites
- docker
    - <code> sudo apt-get install docker-ce docker-ce-cli containerd.io </code>
- docker-compose
    - <code> sudo apt install docker-compose </code>

#### Run
```
docker build
docker-compose up -d
```


## Django superuser
- User = adminroot
- Pass = 123toornimda

## Access
```
[SERVER_NAME]:[PORT] /api/ [VERSION] / [SERVICE]
```
- Example = localhost:8000/api/v0/agendas/
- Heroku Demo = https://sleepy-anchorage-51645.herokuapp.com/api/v0/ 
