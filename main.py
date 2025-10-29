import google.generativeai as genai
from dotenv import load_dotenv
import os

# carregar arquivo .env -> arquivo que possui a chave da API do Gemini
load_dotenv()

# pegar a chave da API do Gemini no arquivo .env e colocar em uma variável
api_key = os.getenv("GEMINI_API_KEY")

# verificar se a chave da API foi encontrada
if not api_key:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

# configurar a API do Gemini
genai.configure(api_key=api_key)

# função para carregar o arquivo txt com o conteúdo base de História do Brasil
def carregar_txt(caminho_arquivo):
        # abre o arquivo txt e lê o conteúdo
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            return conteudo
        # tratar erro caso o arquivo não seja encontrado
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
            return ""
        # tratar outros erros de leitura do arquivo
        except Exception as e:
            print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
            return ""

# função principal do chatbot
def chatbot():
    
    print ("Bem vindo ao Chatbot de História!")
    print("Quando quiser encerrar a conversa, digite 'sair'.")

    # carregar o conteúdo base do arquivo txt
    base = carregar_txt("base.txt")
    
    # inicializar o modelo Gemini-2.5-flash
    model = genai.GenerativeModel ('gemini-2.5-flash')

    # definir o contexto do chatbot -> especializá-lo em História do Brasil
    contexto = ("Você é um professor de história do Brasil no ensino médio. Use o texto a seguir como base para responder às perguntas dos alunos. Responda com linguagem simples, curta e objetiva, de maneira didática.\n\n"f"Aqui está o texto base:\n{base}\n\n")
    
    # iniciar o loop de perguntas e respostas
    while True:
         input_aluno = input("Faça uma pergunta: ")

         if input_aluno.lower() == 'sair':
             print("Encerrando a conversa. Até mais!")
             break
         
         # criar o prompt completo com o contexto e a pergunta do aluno
         prompt = contexto + "\nPergunta do aluno: " + input_aluno

        # gerar a resposta do modelo
         resposta = model.generate_content(prompt)
         print ("Resposta:", resposta.text.strip())

if __name__ == "__main__":
    chatbot()
    

