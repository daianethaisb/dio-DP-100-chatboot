from transformers import pipeline
from operator import itemgetter

# Você pode trocar o modelo por outro mais robusto, como "deepset/roberta-base-squad2"
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def chunk_text(text, max_length=500):
    """
    Divide o texto em chunks com base em sentenças, respeitando o tamanho máximo.
    """
    sentences = text.split(". ")
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def ask_best_chunk(question, full_text):
    """
    Busca o chunk mais relevante com base na pergunta e retorna a melhor resposta.
    """
    chunks = chunk_text(full_text)
    results = []

    for chunk in chunks:
        try:
            answer = qa_pipeline(question=question, context=chunk)
            results.append((answer['score'], answer['answer'], chunk))
        except:
            continue

    if not results:
        return "Desculpe, não encontrei uma resposta adequada."

    best = max(results, key=itemgetter(0))
    return best[1]
