# CASE-IA

## Descrição

O CASE-IA é um projeto desenvolvido como parte do processo seletivo para bolsista dev de IA no SENAI/PR.

A aplicação web baseada em Django oferece funcionalidades como criação de conta, login, edição de dados pessoais, exclusão de conta e upload de arquivos no formato .xls ou .xlsx para obter previsões de volume de vendas de produtos.

Vale ressaltar que os modelos de previsão foram testados, treinados e salvos separadamente, ou seja, não é possível realizar o retreinamento dos modelos através da aplicação web, está funcionalidade é uma melhoria que poderia ser implementada posteriormente.

## Como começar

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/weslleygere/CASE-IA.git
    cd CASE-IA
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - No Unix ou MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute a aplicação web:

    ```bash
    python manage.py runserver
    ```
6. makemigrations e migrate

      ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
### Uso

Ao abrir o aplicativo, o usuário será redirecionado para a página de login. Caso o usário possua uma conta ativa, basta acessá-la. Para criar uma nova conta, basta clicar no botão 'Criar Conta' e o usuário será redirecionado para a página de criação de conta. Após criar uma conta, o usuário será redirecionado novamente para a página de login.

Uma vez logado, o usuário pode acessar outras funcionalidades, como editar suas informações pessoais (nome, email e senha) ou excluir sua conta. Além disso, o usuário pode fazer o upload de um arquivo .xls ou .xlsx afim de visualizar as previsões dos produtos (categorias) que se encontram na coluna 'Category', como dito anteriormente, o usuário não pode retreinar o modelo e nem inserir um novo banco de dados que não aquele cujo o modelo foi treinado.

### Capturas de Tela

<p align="center">
  <img src="https://github.com/weslleygere/CASE-IA/assets/100441275/8a520719-332b-4065-b83c-ddb70dfdefef" alt="image">
</p>

<p align="center">
  <img src="https://github.com/weslleygere/CASE-IA/assets/100441275/569ebb1e-834d-4061-8268-3c930de83d5d" alt="image">
</p>

<p align="center">
  <img src="https://github.com/weslleygere/CASE-IA/assets/100441275/30cf8357-2ff0-4a8c-8e89-8b891ea3fe79" alt="image">
</p>

<p align="center">
  <img src="https://github.com/weslleygere/CASE-IA/assets/100441275/c96ed740-3d82-4b59-b28d-f7d58df63ca4" alt="image">
</p>

<p align="center">
  <img src="https://github.com/weslleygere/CASE-IA/assets/100441275/c7800337-ab67-4f65-8b42-884d057acf53" alt="image">
</p>


