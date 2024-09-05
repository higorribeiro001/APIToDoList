﻿# APIToDoList

> Descrição:
### Implementação de microserviço para gerenciar uma lista de tarefas (to-do list) com os métodos do CRUD (Create, read, update, delete).

> Execução:

### - Para executar localmente:
### - No ambiente Windows, basta seguir os seguintes passos no terminal:
1. Criar uma rede docker:
~~~
docker network create app-network
~~~
3. Colocar o servidor PostgreSQL para rodar utilizando docker com o seguinte comando:
~~~
docker run --name db_fast_api -p 5432:5432 -e POSRGRES_DB=db_fast_api -e POSTGRES_PASSWORD=1234 -d postgres
~~~
3. Criar as migrações (já foi registrada a migration para criação do banco de dados, mas por via das dúvidas pode seguir os passos a seguir):
~~~~
alembic revision --autogenerate -m "Cria tabelas de contas a pagar e receber"
~~~~
4. Aplicar as migrações na base de dados:
~~~~
alembic upgrade head
~~~~
1. criar uma venv:
~~~python
python -m venv venv
~~~
2. executar a venv:
~~~python
./venv/scripts/activate
~~~
3. Por conta do docker o "tensorflow" não foi incluído no requirements.py, portanto rode o seguinte comando: 
~~~
pip install tensorflow
~~~
4. Instale todas as outras bibliotecas necessárias:
~~~
pip install -r requirements.txt
~~~
5. Executar o projeto:
~~~python
python manage.py runserver
~~~
#### obs: Não irei fazer passos para outros OS. Caso tenha problemas, pesquise na internet ou consulte alguma IA.
### - Para executar por meio do docker, basta digitar o seguinte comando no terminal:
~~~
docker compose up
~~~
#### Se quiser executar em segundo plano: 
~~~
docker compose up -d
~~~
### - Você pode abrir o swagger do projeto no navegador, pela rota: api/schema/swagger-ui/
### - Utilizando o swagger, faça o registro do paciente em "users" e posteriormente pode realizar a consulta do mesmo em "possibility_attack"
### - Para registrar o usuário basta:
~~~
{
  "name": "Higor",
  "cpf": "888.888.888-99"
}
~~~
#### Obs: O cpf será utilizado apenas para identificar o paciente e diferenciá-lo dos demais, portanto não necessita ser o dado real.
### - Já para a consulta, é necessário mais dados e detalhes, por exemplo:
~~~
{
  "age": 22,
  "sex": 1,
  "cp": 1,
  "trtbps": 110,
  "chol": 130,
  "fbs": 0,
  "restecg": 0,
  "thalachh": 150,
  "exng": 0,
  "oldpeak": 2.1,
  "slp": 1,
  "caa": 2,
  "thall": 3,
  "user_id": 1
}
~~~
> Mais Detalhes:
### - Para entender melhor o que significa cada uma das chaves citadas acima, deixarei abaixo os detalhes:
#### Idade : Idade do paciente (Inteiro, anos)
#### Sexo : Gênero (categórico; 1 = masculino, 0 = feminino)
#### CP : Tipo de dor no peito (categórica)
##### 1: angina típica
##### 2: angina atípica
##### 3: dor não anginosa
##### 4: assintomático
#### Trestbps : Pressão arterial em repouso (Inteiro, mm Hg)
#### Col : Colesterol sérico (Inteiro, mg/dl)
#### FBS : Glicemia de jejum > 120 mg/dl (categórico; 1 = verdadeiro, 0 = falso)
#### Restecg : Resultados eletrocardiográficos em repouso (categórico)
##### 0: normal
##### 1: Anormalidade da onda ST-T
##### 2: hipertrofia ventricular esquerda provável ou definitiva
#### Thalach : Frequência cardíaca máxima alcançada (Inteiro)
#### Exng : Angina induzida por exercício (categórico; 1 = sim, 0 = não)
#### Oldpeak : Depressão do segmento ST induzida pelo exercício em relação ao repouso (Inteiro)
#### Slp : Declive do segmento ST de pico do exercício (categórico)
##### 1: ascendente
##### 2: plano
##### 3: declive
#### Caa : Número de vasos principais coloridos pela fluoroscopia (Inteiro; 0-3)
#### Thal : Talassemia (Categórica)
##### 3: normal
##### 6: defeito corrigido
##### 7: defeito reversível
#### User_id : id do usuário, pode ser encontrado na lista de usuários registrados.

