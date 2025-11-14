from openai import OpenAI
import os, json
from dotenv import load_dotenv

load_dotenv()

def section_to_json():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    sec_dir = "generated/sections"
    sections = sorted(os.listdir(sec_dir))
    output = []

    for f in sections:
        text = open(f"{sec_dir}/{f}", "r", encoding="utf-8").read()

        prompt = f"""
次のセクションを Marp スライド構成として JSON に変換してください。

必要項目:
- title: 見出し
- points: 箇条書き (最大4つ)
- highlight: 強調ポイント (任意)
- image: 画像名があれば (例: step1.png)

セクション:
{text}
        """

        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user", "content": prompt}]
        )

        output.append(json.loads(res.choices[0].message["content"]))

    json.dump(output, open("generated/structure.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

if __name__ == "__main__":
    section_to_json()
