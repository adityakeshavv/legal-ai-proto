# app/explain.py
from shared_model import tokenizer, model

def explain_clause(clause_text):
    prompt = f"explain: {clause_text}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
