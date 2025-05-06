from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def generate_answer(question, context_chunks):
    context = " ".join(context_chunks)
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
