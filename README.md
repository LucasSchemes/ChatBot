# Chatbot de História do Brasil com Google Gemini

Este é um chatbot simples, baseado em terminal, que atua como um professor de História do Brasil para alunos do ensino médio. Ele utiliza a API do Google Gemini (modelo `gemini-2.5-flash`) para gerar respostas com base em um arquivo de texto (`base.txt`) fornecido.

## 🚀 Funcionalidades

* **Contexto Especializado:** O chatbot é instruído a atuar como um professor de História do Brasil, respondendo de forma didática, simples e objetiva.
* **Base de Conhecimento Local:** Utiliza um arquivo `base.txt` como fonte exclusiva de informação, garantindo que as respostas sejam baseadas no material fornecido.
* **Gerenciamento de API Key:** Carrega a chave da API do Google Gemini de forma segura a partir de um arquivo `.env`.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Google Generative AI SDK** (`google-generativeai`)
* **Python Dotenv** (`python-dotenv`) para gerenciamento de variáveis de ambiente.

## 📋 Pré-requisitos

Antes de começar, você precisará ter:

* **Python 3.x** instalado.
* Uma **Chave de API do Google Gemini**. Você pode obter uma [aqui](https://aistudio.google.com/app/apikey).

## ⚙️ Instalação e Configuração

Siga estes passos para configurar o projeto localmente:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install google-generativeai python-dotenv
    ```
    *(Opcional: Crie um arquivo `requirements.txt` com as bibliotecas acima e rode `pip install -r requirements.txt`)*

4.  **Configure a Chave de API:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave de API do Gemini a este arquivo:
    ```
    GEMINI_API_KEY=SUA_CHAVE_API_VEM_AQUI
    ```

5.  **Crie a Base de Conhecimento:**
    * Crie um arquivo chamado `base.txt` na raiz do projeto.
    * Cole todo o conteúdo de História do Brasil que você deseja usar como fonte de informação para o chatbot dentro deste arquivo. O chatbot usará *apenas* este texto para formular suas respostas.

## ▶️ Como Usar

Após a instalação e configuração, execute o chatbot com o seguinte comando:

```bash
python main.py
