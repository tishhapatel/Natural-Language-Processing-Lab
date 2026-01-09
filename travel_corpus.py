import pandas as pd
import re
import os

print("📌 Running from folder:", os.getcwd())

# ✅ Read CSV from the SAME folder
df = pd.read_csv("travel_blog_corpus.csv", engine="python", on_bad_lines="skip")

full_text = " ".join(df["content"].astype(str))
words = re.findall(r"[A-Za-z]+", full_text.lower())

with open("travel_words_only.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(words))

print("✅ Words-only dataset created successfully!")
print("📌 Saved as: travel_words_only.txt")
print("📌 Total words extracted:", len(words))
