FROM node:18

# Python とフォント
RUN apt-get update && apt-get install -y python3 python3-pip fonts-noto-cjk

# Marp CLI
RUN npm install -g @marp-team/marp-cli

# Python ライブラリ
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# プロジェクトコピー
COPY . /app
WORKDIR /app

CMD ["python3", "scripts/run_all.py"]
