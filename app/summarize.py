# app/summarize.py
from shared_model import tokenizer, model

def summarize_text(text):
    prompt = f"summarize: {text}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
