from chatbot.chatbot import ask_best_chunk
from chatbot.pdf_loader import extract_text_from_pdf

def main():
    print("🔍 Carregando conteúdo do PDF...")
    try:
        pdf_text = extract_text_from_pdf("inputs/artigos.pdf")
    except FileNotFoundError:
        print("❌ Arquivo 'artigos.pdf' não encontrado na pasta 'inputs'.")
        return

    print("✅ PDF carregado com sucesso!")
    print("Digite sua pergunta ou 'sair' para encerrar.\n")

    while True:
        pergunta = input("❓ Sua pergunta: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando o chatbot. Até logo!")
            break

        resposta = ask_best_chunk(pergunta, pdf_text)
        print("🤖 Resposta:", resposta)
        print("-" * 50)

if __name__ == "__main__":
    main()
