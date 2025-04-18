## コマンド一覧

env\Scripts\activate

python github_copilot_agents.py

git add github_copilot_agents.py templates/ README.md github_copilot_agents.pyproj requirements.txt


---

# Visual StudioとGitHub Copilot研修

---

## 目次

1. 環境セットアップ
2. UTF-8エンコーディング設定
3. マインスイーパー実装概要
4. GitHub Copilotの活用
5. Visual Studioでのフォーマッター設定
6. エラーの解消
7. チャットの固定
8. プロジェクトのディレクトリを左側に表示
9. まとめ

---

## 1. 環境セットアップ

### 仮想環境の作成とFlaskのインストール

1. **仮想環境の作成**
   ```cmd
   cd D:\project\github_copilot_agents\github_copilot_agents
   python -m venv env
   ```

2. **仮想環境の有効化**
   ```cmd
   env\Scripts\activate
   ```
   - コマンドプロンプトの先頭に `(env)` と表示されれば成功

---

## 1. 環境セットアップ（続き）

3. **Flaskのインストール**
   ```cmd
   pip install flask
   ```

4. **依存関係の保存**
   ```cmd
   pip freeze > requirements.txt
   ```

---

## 2. UTF-8エンコーディング設定

### Visual Studioでの正しいエンコーディング設定

1. **Pythonファイルのエンコーディング宣言**
   ```python
   # -*- coding: utf-8 -*-
   ```

2. **テンプレートファイルの保存設定**
   - ファイル > 名前を付けて保存 > エンコーディング設定
   - **「Unicode (UTF-8 署名なし)」を選択**
   - BOM（バイトオーダーマーク）なしのUTF-8を使用

---

## 2. UTF-8エンコーディング設定（続き）

3. **エンコーディングによる一般的なエラー**
   - `UnicodeDecodeError: 'utf-8' codec can't decode byte 0x83...`
     - 原因：日本語などの非ASCII文字が正しくエンコードされていない
     - 解決策：UTF-8（署名なし）で保存し直す

---

## 3. マインスイーパー実装

### ゲームロジック

```python
class Minesweeper:
    def __init__(self, rows, cols, mines):
        # ボード初期化、爆弾配置など
        
    def reveal_cell(self, row, col):
        # セル開示処理、ゲーム状態確認
```

### Flask統合

```python
app = Flask(__name__)
app.secret_key = 'secret_key'  # セッション用

@app.route('/')
def index():
    # 新しいゲーム作成
    
@app.route('/reveal', methods=['POST'])
def reveal():
    # セル開示処理
```

---

## 3. マインスイーパー実装（続き）

### フロントエンド実装

1. **基本レイアウト (`templates/index.html`)**
   - ゲームボード、メッセージ表示、コントロール

2. **Ajax通信**
   ```javascript
   // セル開示
   $.ajax({
       url: '/reveal',
       type: 'POST',
       data: {row: row, col: col},
       success: function(response) {
           // 画面更新
       }
   });
   ```

3. **部分的更新 (`templates/game_board_partial.html`)**
   - ゲームボードの部分的な更新用テンプレート

---

## 4. GitHub Copilotの活用

1. **コード補完**
   - コードを書き始めると、関連する補完が表示される
   - Tab キーで採用、Esc キーでキャンセル

2. **コメントからのコード生成**
   - 関数や機能の説明をコメントとして書くと、Copilotが対応するコードを提案

3. **エラー解決のサポート**
   - エラーメッセージをもとに解決策を提案

---

## 5. Visual Studioでのフォーマッター設定

1. **ツール > オプション > テキストエディター > Python > 書式設定** に移動します。

2. 「フォーマッター」のドロップダウンから **autopep8** を選択します。

3. 「OK」をクリックして設定を保存します。

---

## 6. エラーの解消

### 問題
- Blackフォーマッターを使用して選択範囲をフォーマットしようとすると、「Black does not support the Format Selection command」というエラーが発生しました。

### 解決策
- フォーマッターを **autopep8** に変更しました。
- 再度フォーマットを実行すると、エラーが解消されました。

---

## 7. チャットの固定

### 手順
- Visual Studioの右下に表示されるGitHub Copilotのチャットウィンドウを右クリックします。
- 「固定」を選択すると、ウィンドウが固定されます。

---

## 8. プロジェクトのディレクトリを左側に表示

- **表示 > ソリューションエクスプローラー** を選択します。
- ソリューションエクスプローラーが左側に表示されます。

---

## 9. まとめ

- GitHub Copilotをインストールし、Pythonプロジェクトを作成
- 仮想環境を作成し、**autopep8**をインストール
- Visual Studioの設定でフォーマッターを **autopep8** に変更
- エラーが解消され、コードフォーマットが正常に動作するようになりました

---

## エラー対処法

### 一般的なエラー

1. **エンコーディングエラー**
   - エラー：`UnicodeDecodeError: 'utf-8' codec can't decode byte...`
   - 解決策：すべてのファイルをUTF-8（署名なし）で保存

2. **モジュールが見つからないエラー**
   - エラー：`ModuleNotFoundError: No module named 'flask'`
   - 解決策：仮想環境が有効化されているか確認し、`pip install flask`を実行

---

## 発展課題

1. **機能拡張**
   - 難易度設定
   - タイマー機能
   - フラグ設置機能

2. **UIの改善**
   - CSSフレームワークの導入
   - レスポンシブデザイン

3. **コード最適化**
   - コードのモジュール化
   - パフォーマンス改善

---

## 質問・実習

お疑問やサポートが必要な方はお知らせください！