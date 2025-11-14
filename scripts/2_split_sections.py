import os
import re

def split_script():
    os.makedirs("generated/sections", exist_ok=True)
    raw = open("input/script.txt", "r", encoding="utf-8").read()

    headers = re.findall(r"^# .+", raw, flags=re.MULTILINE)
    bodies = re.split(r"^# .+", raw, flags=re.MULTILINE)[1:]

    for idx, (h, b) in enumerate(zip(headers, bodies)):
        out = f"generated/sections/section_{idx}.txt"
        open(out, "w", encoding="utf-8").write(f"{h}\n{b.strip()}")

if __name__ == "__main__":
    split_script()
