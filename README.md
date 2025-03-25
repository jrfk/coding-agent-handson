# 画像モザイク処理ツール

画像にモザイク処理を適用するPython製のCLIツールです。画像全体のモザイク処理と、顔認識を使用して顔部分のみをモザイク処理する機能を提供します。

## 機能

- 画像全体へのモザイク処理
- モザイクの強さ（粒度）の調整
- 顔認識を使用した顔部分のみのモザイク処理

## インストール

このツールを使用するには、以下のコマンドでインストールしてください：

```bash
# リポジトリをクローン
git clone https://github.com/yourusername/mosaic-tool.git
cd mosaic-tool

# 依存パッケージのインストール
pip install -e .
```

### 依存関係

- Python 3.7以上
- Pillow (PIL)
- Click
- OpenCV
- dlib

注: dlibのインストールには、C++コンパイラとCMakeが必要です。詳細は[dlib公式ドキュメント](https://github.com/davisking/dlib)を参照してください。

## 使い方

### 基本的な使い方

```bash
# 画像全体にモザイク処理を適用する
mosaic-tool input.jpg output.jpg --strength 5 --mode full

# 顔部分のみにモザイク処理を適用する
mosaic-tool input.jpg output.jpg --strength 5 --mode face
```

### オプション

- `--strength`: モザイクの強さを指定します (1-10の整数、デフォルト: 5)
- `--mode`: 処理モードを指定します (full: 画像全体、face: 顔のみ、デフォルト: full)

### 使用例

```bash
# 最弱のモザイク処理を適用
mosaic-tool input.jpg output.jpg --strength 1

# 最強のモザイク処理を適用
mosaic-tool input.jpg output.jpg --strength 10

# 顔のみにモザイク処理を適用
mosaic-tool portrait.jpg anonymized.jpg --mode face
```

## ライセンス

MITライセンス

## 開発者向け情報

### テスト実行

```bash
pytest
```

### ディレクトリ構成

```
mosaic-tool/
├── docs/                  # ドキュメント
│   ├── requirements.md    # 要件定義書
│   └── design.md          # 設計書
├── src/                   # ソースコード
│   ├── __init__.py        
│   ├── mosaic_tool.py     # CLIインターフェース
│   ├── image_processor.py # 画像処理エンジン
│   └── face_detector.py   # 顔検出モジュール
├── tests/                 # テストコード
│   ├── __init__.py
│   ├── test_mosaic_tool.py
│   ├── test_image_processor.py
│   └── test_face_detector.py
├── setup.py               # セットアップスクリプト
└── README.md              # このファイル
```

