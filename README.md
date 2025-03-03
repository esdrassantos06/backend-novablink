# NovaBlink - Backend

Este é o backend do projeto NovaBlink, um encurtador de URLs construído com Python (Flask) e PostgreSQL (AWS RDS). Ele fornece uma API para encurtar URLs e redirecionar para as URLs originais.

## Tecnologias Utilizadas

-   Python
-   Flask
-   Flask-SQLAlchemy
-   psycopg2
-   python-dotenv
-   PostgreSQL (AWS RDS)

## Configuração do Ambiente

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/esdrassantos06/backend-novablink/

    cd backend-novablink
    ```

2.  **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**

    ```bash
    # No Linux/macOS
    source venv/bin/activate
    # No Windows
    venv\Scripts\activate
    ```

4.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configuração das Variáveis de Ambiente:**

    -   Crie um arquivo `.env` na raiz do diretório `backend`.
    -   Adicione as seguintes variáveis de ambiente:

        ```
        SECRET_KEY=sua_chave_secreta_aqui
        DATABASE_URI=postgresql://usuario:senha@endpoint:porta/nome_do_banco
        ```

        -   Substitua `sua_chave_secreta_aqui` por uma chave secreta forte.
        -   Substitua `usuario`, `senha`, `endpoint`, `porta` e `nome_do_banco` pelas informações do seu banco de dados PostgreSQL no AWS RDS.

6.  **Inicie o servidor Flask:**

    ```bash
    python app.py
    ```

## Estrutura de Pastas

    
    backend/
    ├── app.py
    ├── venv/
    ├── .env
    ├── Procfile
    ├── requirements.txt
    └── ...
    

## Considerações de Segurança

-   Nunca armazene informações confidenciais diretamente no código-fonte.
-   Utilize variáveis de ambiente e arquivos `.env`.
-   Adicione o arquivo `.env` ao `.gitignore` para evitar que ele seja enviado para o repositório Git.
-   Configure grupos de segurança adequados no AWS RDS para restringir o acesso ao banco de dados.
-   Utilize HTTPS para comunicação segura com o frontend.
-   Valide todas as entradas de dados do usuário no lado do servidor.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Esse projeto tem a licença [MIT](LICENSE)
