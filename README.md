
# FastAPIの要点まとめ

学習内容：https://www.udemy.com/course/python-fastapi/<br>

- アドレス可能性
1つのURIを用いて、全ての機能を表現可能<br>

- ステートレス性
全てのリクエストが完全に分離しており、セッションなどの状態管理は行われない<br>

- 接続性
情報に別の情報へのリンクを含めることが可能<br>

- 統一インターフェース
操作一式は全てHTTPメソッドで可能<br>

### APIゲートウェイ
APIの管理や実行を容易にする仕組み
例）Amazon API Gateway

<hr>

## フォルダ・ファイル構成
- app.py
Streamlitで作成したUI<br>

- database.py
データベースの定義<br>

- models.py
データベースの構造定義<br>

- schemas.py
Fast API用のデータ構造定義<br>

- crud.py
CRUD操作定義<br>

- main.py
Fast APIの処理定義<br>
