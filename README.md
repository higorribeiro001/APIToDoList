# APIToDoList

> Descrição:
### Implementação de microserviço para gerenciar uma lista de tarefas (to-do list) com os métodos do CRUD (Create, read, update, delete).

> Execução:

### - Para executar localmente:
### - No ambiente Windows, basta seguir os seguintes passos no terminal:
1. Criar uma rede docker:
~~~
docker network create app-network
~~~
2. Colocar o servidor PostgreSQL para rodar utilizando docker com o seguinte comando:
~~~
docker run --name db_fast_api -p 5432:5432 -e POSRGRES_DB=db_fast_api -e POSTGRES_PASSWORD=1234 -d postgres
~~~
3. Na raiz do projeto, criar um arquivo .env com o seguinte conteúdo:
~~~
BD_NAME="db_fast_api"
BD_USER="postgres"
BD_PASSWORD="1234"
BD_HOST="localhost"
BD_PORT=5432

HOST_REDIS="localhost"
PORT_REDIS=6379
~~~
4. Na raiz do projeto, criar uma venv:
~~~python
python -m venv venv
~~~
5. executar a venv:
~~~python
./venv/scripts/activate
~~~
6. Instale todas as bibliotecas necessárias:
~~~
pip install -r requirements.txt
~~~
7. Criar as migrações (já foi registrada a migration para criação do banco de dados, mas por via das dúvidas pode seguir os passos a seguir):
~~~~
alembic revision --autogenerate -m "Cria tabela de tasks"
~~~~
8. Aplicar as migrações na base de dados:
~~~~
alembic upgrade head
~~~~
9. Executar o projeto:
~~~python
uvicorn main:app --reload
~~~
Ou, por meio do docker:
Mas, para conseguir obter sucesso, será necessário editar o .env:
~~~
BD_NAME="db_fast_api"
BD_USER="postgres"
BD_PASSWORD="1234"
BD_HOST="db_fast_api"
BD_PORT=5432

HOST_REDIS="redis"
PORT_REDIS=6379
~~~
Agora basta rodar o docker compose:
~~~
docker compose up -d
~~~
### Para acessar a documentação, basta acessar o link disponibilizado na execução (localmente será: http://127.0.0.1:8000) e acessar "/docs", desta forma: http://127.0.0.1:8000/docs. Com isto você terá acesso ao Swagger com todos os métodos e seus detalhes para utilização.
