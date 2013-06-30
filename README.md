mymemos
=======

POC tornado / mongo / asyncmongo / openshift

Para preparar o ambiente de desenvolvimento 
(obs: estes comandos não estão completos, são só para exemplificar e lembrar o que tem que fazer)

- virtualenv mymemos
- source ./mymemos/bin/activate
- git clone https://github.com/soeirosantos/mymemos.git
- pip install -r requirements.txt 
- ./mongod --dbpath ../data/db
- python main.py