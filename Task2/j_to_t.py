import json
import re

# Read JSON
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

text = data["text"]

# Tokenization (simple)
tokens = re.findall(r"[A-Za-z']+", text.lower())

# Save as .toon file
with open("output.toon", "w", encoding="utf-8") as f:
    f.write("\n".join(tokens))

print("✅ Converted JSON to .toon (token format) successfully!")
