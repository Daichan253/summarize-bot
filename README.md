# summarize-bot

📄 `.txt`ファイルをアップロードすると、ルールベースで要約結果を返す FastAPI アプリです。

## ✅ 機能概要

- .txtファイルをアップすると、中身を要約して JSON で返します
- 自作のルールベース要約ロジック（キーワード抽出 × 文スコア）を使用
- API化しており、`FastAPI` + `Swagger UI`で動作確認可能

## 🏃‍♂️ 使い方

### 1. 仮想環境を有効化

```bash
source venv/bin/activate