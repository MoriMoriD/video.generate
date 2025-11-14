import json

def json_to_marp():
    data = json.load(open("generated/structure.json", "r", encoding="utf-8"))
    md = """---
marp: true
theme: default
paginate: true
---

"""

    for sec in data:
        md += f"# {sec['title']}\n\n"

        for p in sec["points"]:
            md += f"- {p}\n"
        if sec.get("highlight"):
            md += f"\n> 💡 {sec['highlight']}\n"
        if sec.get("image"):
            md += f"\n![image](../input/{sec['image']})\n"

        md += "\n---\n"

    open("generated/slides.md", "w", encoding="utf-8").write(md)

if __name__ == "__main__":
    json_to_marp()
