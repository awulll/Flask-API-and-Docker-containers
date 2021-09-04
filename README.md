This was a test proposed. I couldn't finish on time, but was a good experience. I used Flask to develop a API that receive data (contacts) from Json format and store on databases (two docker containers, MySQL and PostgreSQL) on specific formats.

Creating docker containers
```
docker-compose up
```

Verifying containers
```
docker ps -a
```

Verifying table on database MySQL
```
docker exec -it db_macapa bash
mysql -u admin -p
use admin; 
select * from contacts;
```

Verifying table on database PostgreSQL
```
docker exec -it db_varejao bash
psql -h localhost -p 5432 -U admin -d admin
\c
select * from contacts;
```

Running Flask API
```
cd app/              # if you're on main directory
python3 api.py
```

Inserting data on databases
```
python3 test_api.py  # if you're on main directory
```


Este foi um teste proposto. Não consegui terminar todas as etapas, mas foi uma boa experiência. Usei Flask para desenvolver uma API que recebe dados de contatos em Json e armazena os mesmos em databases (containers do docker, MySQL e PostgreSQL) em formatos específicos.

Criando container no docker
```
docker-compose up
```

Verificando containers criados

```
docker ps -a
```

Verificando se a tabela foi criada na database MySQL

```
docker exec -it db_macapa bash
mysql -u admin -p
use admin; 
select * from contacts; 
```

Verificando se a tabela foi criada na database PostgreSQL

```
docker exec -it db_varejao bash
psql -h localhost -p 5432 -U admin -d admin
\c
select * from contacts;
```

Rodando a API

```
cd app/              # Se estiver no diretório principal
python3 api.py
```

Inserindo dados nas duas databases

```
python3 test_api.py  # Se estiver no diretório principal
```
