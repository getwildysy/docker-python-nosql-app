# 1. 基礎映像檔：使用官方 Python 3.11 精簡版
FROM python:3.11-slim

# 2. 設定工作目錄 (Work Directory)：所有後續指令都在 /app 目錄下執行
WORKDIR /app

# 3. 複製 requirements.txt 並安裝函式庫 (利用 Docker 層快取機制)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 複製整個應用程式碼到容器內的工作目錄
COPY app/ .

# 5. 宣告容器將監聽 5000 埠號 (資訊性指令，非強制性)
EXPOSE 5000

# 6. 定義容器啟動時要執行的指令：使用 Gunicorn
# gunicorn -w [工作進程數] -b [綁定 IP:Port] [應用程式模組:應用程式實例名]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]