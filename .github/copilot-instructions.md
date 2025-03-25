# copilot-instructions.md

## ロール定義

あなたは熟練のPythonプログラマとしてコードを書いてください。
このドキュメントは、GitHub Copilot AgentがRustプロジェクトの開発をTDD（テスト駆動開発）でサポートするための指示書です。


## 期待する回答

- 実装コードは省略せず、完全な形で提供
- 日本語での詳細な説明

# 注意事項

## ✅ 開発の進め方（TDD）

### 現在のブランチを確認する

作業を始める前に、必ず現在のブランチを確認し、最新をpullしてください。

```sh
git branch
git pull origin main
```

作業内容に応じてブランチを切り替え、新しいブランチで開発を始めてください。

```
git switch -c feature/your-feature-name
```

ブランチの命名規則は以下の通りです。

| 種類         | プレフィックス | 使用例                                     |
| ------------ | ------------ | ---------------------------------------- |
| 機能追加     | `feature/`   | `feature/add-clipboard-ui`               |
| バグ修正     | `fix/`       | `fix/issue-クリップボードが更新されない問題修正` |
| リファクタリング | `refactor/`  | `refactor/improve-history-struct`         |
| ドキュメント | `docs/`      | `docs/update-readme`                      |
| CI/CDや設定変更 | `chore/`     | `chore/update-pre-commit-hooks`          |


### はじめに設計書を作る

- 新規開発時は docs ディレクトリ以下に以下の内容を含む設計書を作成してください：
  - 要件定義書 requirements.md
  - 設計書（概略・機能・クラス構成） design.md
- 既存のソフトウェアを修正する場合：
  - 既存の設計書を参照してソフトウェアを開発してください
  - 修正内容に応じて設計書も更新してください
- 設計書を作成したら、コードを作成する前にユーザーに設計書のチェックを依頼してください


### コーディング規約

- PEP8に従ったコードを書いてください
- ruffのフォーマッタでファイルの保存と同時に自動整形するので、フォーマットの修正は不要です
- GoogleスタイルのDocstringを書いてください

### テスト駆動

テスト駆動開発の基本サイクルを守ってコードを書いてください。PyTestを使って、テストを以下の手順で進めてください。

1. **失敗するテストを書く**
2. **最小限のコードでテストを通す**
3. **必要に応じてリファクタリングする**

### テストの場所

- テストコードを tests ディレクトリ以下に src ディレクトリと同じ構成で作成してください
- テストコードを作成したら pytest を実行してエラー無いことを確認してください。エラーが出たら修正してください

## 📌 Git操作

- gitの操作は `git status` でステータスを確認しながら慎重に行ってください。
- git管理されているファイルは、必ず `git mv` や `git rm` を使って移動や削除を行ってください。

---

## 📌 Pull Request（PR）の操作

### PR作成時

- PRを要望されたら、まずgitコマンドで差分を慎重に確認した上で、`gh pr` コマンドを使ってPRを作成してください。

```bash
git status
git diff origin/main

gh pr create
```

- PRのdescriptionは `.github/pull_request_template.md` を読み取ってフォーマットを合わせてください。

### PRレビュー時

以下の手順でファイルごとにレビューコメントを付けてください。

1. チェックする観点は `.github/pull_request_template.md` を参照してください。

2. PRの差分を確認してください。

```bash
gh pr diff <PR番号>
```

3. ファイルごとに、変更後のファイル全体とPRの差分を確認した上で、レビューコメントを追加してください。

```bash
gh api repos/<owner>/<repo>/pulls/<PR番号>/comments \
  -F body="レビューコメント" \
  -F commit_id="$(gh pr view <PR番号> --json headRefOid --jq .headRefOid)" \
  -F path="対象ファイルのパス" \
  -F position=<diffの行番号>
```

#### パラメータ説明

- `position`: 差分（diff）の行番号（新規ファイルの場合は1から開始）
- `commit_id`: PRの最新のコミットIDを自動取得

---

以上の内容を守って、効率的で安全なPythonの開発を進めてください！

