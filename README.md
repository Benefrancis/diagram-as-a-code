# Projeto Python : Diagram as a Code

Este documento explica como configurar e rodar este projeto Python, mesmo que você não tenha experiência prévia com Python.

## Requisitos

Antes de começar, certifique-se de ter o **Python** instalado. Para verificar, execute:

```sh
python --version
```

Se não estiver instalado, faça o download em [python.org](https://www.python.org/downloads/) e siga as instruções de instalação.

## Configuração do Ambiente Virtual

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta do projeto:

   ```sh
   cd caminho/para/seu/projeto
   ```

3. Crie um ambiente virtual:

   ```sh
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - **Windows**:

     ```sh
     venv\Scripts\activate
     ```

   - **Linux/Mac**:

     ```sh
     source venv/bin/activate
     ```

## Instalação das Dependências

1. Gere o arquivo `requirements.txt` (caso ainda não exista):

   ```sh
   pip freeze > requirements.txt
   ```

2. Instale as dependências listadas no `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```
3. Instale a biblioteca Diagrams

    ```sh
    pip install diagrams
    ```

## Executando o Projeto

Para rodar o projeto, execute:

```sh
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome do seu script principal.

## Desativando o Ambiente Virtual

Após finalizar o uso do projeto, você pode desativar o ambiente virtual com:

```sh
deactivate
```

## Considerações Finais

Agora seu projeto está pronto para rodar! Se encontrar problemas, verifique se todas as dependências foram instaladas corretamente e se o ambiente virtual está ativado.

