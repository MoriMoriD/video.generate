from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_script():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    idea = open("input/idea.md", "r", encoding="utf-8").read()

    prompt = f"""
以下の企画に基づいて、解説動画用の台本を
「# 見出し」＋本文 の形式で作成してください。

条件:
- Sifuのように、簡潔で情報密度高い構成
- セクションは3〜6個
- 専門用語は平易な説明付き

企画:
{idea}
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content": prompt}]
    )

    with open("input/script.txt", "w", encoding="utf-8") as f:
        f.write(res.choices[0].message["content"])

if __name__ == "__main__":
    generate_script()
