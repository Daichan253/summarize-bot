from fastapi import FastAPI, UploadFile, HTTPException
from summarize import extract_summary  # summarize.pyの関数を再利用

app = FastAPI()

@app.post("/txt-summary")
async def txt_summary(file: UploadFile):
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="テキストファイルをアップしてください。")

    contents = await file.read()
    text = contents.decode("utf-8")
    summary = extract_summary(text)

    return {"summary": summary}