# Computacao Distribuida 2016-1

Este e' um conjunto de exemplos para a disciplina de Computacao Distribuida da UFFS de 2016-1.
Os exemplos estao escritos usando python, o framework web bottle e o pacote requests.

## Trabalho 1
O trabalho 1 sincroniza mensagens entre vários servidores automaticamente. 

Vá até a pasta ```/t1-part1/``` para abrir o servidor e os clientes de sincronização.

Na inicialização é necessário informar a porta de pelo menos um servidor conhecido:
```bash
python3 chat.py 8000 8001
```
O primeiro número é a porta onde será instanciado o servidor, o segundo número é a porta do servidor conhecido.

Para acessar o chat, abra no navegador o endereço ```http://localhost:8000```.

Após enviar a primeira mensagem o nome utilizado será o nick para o envio das próximas mensagens automaticamente.

As seguintes requisições foram implementadas:

* ```GET /``` ou ```GET /<nick>```: Carrega a interface do chat (página WEB)
* ```GET /messages```: Lista as mensagens do servidor
* ```POST /messages```: Imprime um JSON das mensagens do servidor
* ```GET /peers/<url>```: Lista os peers conhecidos na rede e adiciona a <url> nos conhecidos
* ```GET /debug```: Imprime um JSON dos peers conhecidos
* ```POST /send```: Adiciona uma nova mensagem
* ```GET /static/<file>```: Busca um arquivo estático do servidor ```Ex: jquery.js```

## Trabalho 2
```bash
$ curl -w "\n" -X GET "http://localhost:8080/dht/abcd1234"
$ curl -w "\n" -X PUT "http://localhost:8080/dht/abcd1234/1234"
$ curl -w "\n" -X GET "http://localhost:8080/dht/abcd1234"
```
