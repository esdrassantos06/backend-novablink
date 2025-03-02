# NovaBlink - Encurtador de URLs

NovaBlink é um encurtador de URLs desenvolvido com Python (Flask) no backend e React (Vite/TypeScript) no frontend. Ele utiliza um banco de dados PostgreSQL no AWS RDS para armazenamento de dados, garantindo alta disponibilidade e escalabilidade.

## Funcionalidades

-   Encurtamento de URLs longas para links curtos e amigáveis.
-   Redirecionamento automático para a URL original ao acessar o link curto.
-   Interface de usuário moderna e responsiva construída com React e TypeScript.
-   Backend robusto e seguro desenvolvido com Flask e PostgreSQL.
-   Utilização de variáveis de ambiente para configurações sensíveis.

## Tecnologias Utilizadas

-   **Backend:**
    -   Python
    -   Flask
    -   Flask-SQLAlchemy
    -   psycopg2
    -   python-dotenv
    -   PostgreSQL (AWS RDS)
-   **Frontend:**
    -   React
    -   TypeScript
    -   Vite
    -   axios

## Configuração do Ambiente

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    cd NovaBlink
    ```

2.  **Configuração do Backend:**

    -   Navegue até o diretório `backend`:

        ```bash
        cd backend
        ```

    -   Crie um ambiente virtual:

        ```bash
        python -m venv venv
        ```

    -   Ative o ambiente virtual:

        ```bash
        # No Linux/macOS
        source venv/bin/activate
        # No Windows
        venv\Scripts\activate
        ```

    -   Instale as dependências:

        ```bash
        pip install -r requirements.txt
        ```
        * Caso não tenha o arquivo requirements.txt, rode o comando: pip freeze > requirements.txt

    -   Crie um arquivo `.env` na raiz do diretório `backend` e configure as variáveis de ambiente (consulte a seção "Variáveis de Ambiente").

    -   Inicie o servidor Flask:

        ```bash
        python app.py
        ```

3.  **Configuração do Frontend:**

    -   Navegue até o diretório `frontend`:

        ```bash
        cd ../frontend
        ```

    -   Instale as dependências:

        ```bash
        npm install
        ```

    -   Crie um arquivo `.env.local` na raiz do diretório `frontend` e configure as variáveis de ambiente (consulte a seção "Variáveis de Ambiente").

    -   Inicie o servidor de desenvolvimento do Vite:

        ```bash
        npm run dev
        ```

## Variáveis de Ambiente

-   **Backend (`backend/.env`):**

    ```
    SECRET_KEY=sua_chave_secreta_aqui
    DATABASE_URI=postgresql://usuario:senha@endpoint:porta/nome_do_banco
    ```

    -   Substitua `sua_chave_secreta_aqui` por uma chave secreta forte.
    -   Substitua `usuario`, `senha`, `endpoint`, `porta` e `nome_do_banco` pelas informações do seu banco de dados PostgreSQL no AWS RDS.

-   **Frontend (`frontend/.env.local`):**

    ```
    VITE_API_URL=http://localhost:5000/api
    ```

    -   Configure a URL da API do backend.

## Considerações de Segurança

-   Nunca armazene informações confidenciais diretamente no código-fonte.
-   Utilize variáveis de ambiente e arquivos `.env`.
-   Adicione o arquivo `.env` ao `.gitignore` para evitar que ele seja enviado para o repositório Git.
-   Configure grupos de segurança adequados no AWS RDS para restringir o acesso ao banco de dados.
-   Utilize HTTPS para criptografar a comunicação entre o frontend e o backend.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

[Insira a licença do seu projeto, se aplicável]
