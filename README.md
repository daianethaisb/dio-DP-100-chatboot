# Chatbot com PDFs usando IA

Este projeto implementa um chatbot que responde a perguntas com base em conteúdo de arquivos PDF. Ele utiliza embeddings para busca vetorial e IA generativa para respostas contextuais.

## Tecnologias

- Python
- PyMuPDF
- FAISS
- SentenceTransformers
- Hugging Face Transformers
- Streamlit (interface web)

## Como executar

1. Crie uma pasta chamada `inputs/`
2. Coloque seu PDF em `inputs/artigos.pdf` (ou faça upload pela interface)
3. Crie (ou ative) um ambiente virtual (opcional, mas recomendado):
    python -m venv .venv

   ```bash
   .venv/bin/activate # Linux/macOS
   ```
   
    ```bash
   .venv\\Scripts\\activate # Windows
   ```
5. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Para rodar no terminal:

```bash
python app.py
```

6. Para rodar com interface web:

```bash
streamlit run streamlit_app.py
```
