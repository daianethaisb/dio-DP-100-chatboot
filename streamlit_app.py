import streamlit as st
from chatbot.chatbot import ask_best_chunk  # Correção aqui
from chatbot.pdf_loader import extract_text_from_pdf

def main():
    st.title("Chatbot baseado em PDF")

    # Carregar o PDF
    st.subheader("📄 Carregar PDF")
    pdf_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

    if pdf_file is not None:
        # Carregar conteúdo do PDF
        pdf_text = extract_text_from_pdf(pdf_file)
        st.write("✅ PDF carregado com sucesso!")
        
        # Perguntar algo ao chatbot
        st.subheader("❓ Pergunte ao Chatbot")
        pergunta = st.text_input("Qual sua pergunta?")
        
        if pergunta:
            resposta = ask_best_chunk(pergunta, pdf_text)
            st.write(f"Resposta: {resposta}")
    
if __name__ == "__main__":
    main()
