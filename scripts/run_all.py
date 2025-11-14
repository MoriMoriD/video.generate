import os

os.system("python scripts/1_generate_script.py")
os.system("python scripts/2_split_sections.py")
os.system("python scripts/3_generate_json.py")
os.system("python scripts/4_json_to_marp.py")
os.system("marp generated/slides.md --pdf --output generated/slides.pdf")

print("PDF 完成！ Canva にアップロードしてください。")
