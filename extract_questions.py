import ollama

TEXT_FILE = "data/text/a.txt"   # your OCR output
OUT = "data/questions.txt"

with open(TEXT_FILE, "r", encoding="utf8") as f:
    raw = f.read()

prompt = f"""
Extract ONLY the MAIN exam questions from this text.

Rules:
- Ignore a), b), c), d)
- Ignore marks, BT, CO, headers
- Return one question per line
- Clean English

TEXT:
{raw}
"""

response = ollama.chat(
    model="mistral",
    messages=[{"role": "user", "content": prompt}]
)

questions = response["message"]["content"]

with open(OUT, "w", encoding="utf8") as f:
    f.write(questions)

print("LLM extraction completed!")
