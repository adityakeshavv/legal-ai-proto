# app/qa.py
from shared_model import tokenizer, model

def ask_question(document_text, question):
    prompt = f"question: {question} context: {document_text}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
