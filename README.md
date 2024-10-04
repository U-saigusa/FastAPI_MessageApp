# FastAPI_MessageApp

## 技術スタック

言語：Python

フレームワーク：FastAPI

DB：SQLite

ORM：SQLAlchemy

サーバ：Uvicorn

データ検証：Pydantic

## Pydantic

Pythonのデータ検証ライブラリ。データのバリデーションや型ヒントを提供するもので、出力モデルの型と制約を保証する。

pydanticは基本的にPythonの標準データ型を使うように設計されているため、SQLAlchemyのオブジェクトをPydanticに渡すとエラーが発生する。
下記の指定をすると、ORMのオブジェクトからデータを抽出し、JSONなどのレスポンスに変換できる。

`orm_mode = True`

## Uvicorn

Python用のASGI Webサーバ。

## ASGI

PythonのWebアプリケーションを構築するためのインターフェースの1つで、非同期プログラミングをサポートしている。WSGI（同期的）の進化版。
また、WebSocketやHTTP/２など複数のプロトコルをサポートしている。さらに、非同期的な処理と同期的な処理を混在させることができる。

例)FlaskやDjangoなどはWSGIを使っている。FastAPIやDjango ChannelsはASGIを使っている。

## PythonのWebアプリケーションを構築するためのインターフェース

Webサーバとアプリケーションの間でリクエストとレスポンスをやり取りするための規約や標準のこと。これにより異なるWebフレームワークyあわーばが相互に連携できる。

## FastAPI

Pythonを使ったAPI構築のためのWebフレームワーク

### 依存性注入機能

依存性注入とはあるコンポーネント（関数やクラス）がほかのコンポーネントに依存している場合、その依存先を外部から提供する方法。

## SQLAlchemy

PythonのORMの1つ。ORMとしては、SQLインジェクション対策が標準でサポートされている。

sessionmaker：セッションを作成するためのファクトリ関数

ファクトリ関数：オブジェクトを生成する関数

セッションファクトリ：DBセッションのインスタンスを生成するための関数やクラス

## ORM

オブジェクト関係マッピング（Object-Relational Mapping）は、オブジェクト指向プログラミングと関係データベースの互換性を向上させるために設計されたプログラミング言語。ORMはクラスとデータベースのテーブルをマッピングすることにより、直接SQLクエリを作成することなくデータベースと相互作用できる。

[ORMの概念理解 - Qiita](https://qiita.com/minimabot/items/0a3fcc41fd7140dfdc41)

## マッピング

何かと何かを関連づけること

「URLとタイトルをマッピングする」

「CのライブラリをJavaにマッピングする」

## SQLiteとMySQLの比較

SQLiteはサーバーレス。アプリはクライアントサーバーアーキテクチャなしで直接データを読み書きできる。

MySQLはクライアントサーバモデルに準拠しているためサーバが必要。GUIとCLIが組み込まれている。

| 項目 | MySQL | SQLite |
| --- | --- | --- |
| **アーキテクチャ** | クライアント-サーバーモデル。クライアント層、サーバー層、ストレージ層からなる多層構造。 | サーバーレスDBMS。SQLをバイトコードにコンパイルし仮想マシンで実行。 |
| **データ型** | 静的型。テーブル作成時にカラムのデータ型を定義。 | 動的型。カラムに保存された値がデータ型を決定。 |
| **ストレージクラス** | 使用なし。 | NULL、INTEGER、TEXT、BLOB、REALのいずれかを使用。 |
| **スケーラビリティ** | クライアント-サーバーモデルで大規模データベースに対応。 | シングルユーザーアクセスに限定。データベースが大きくなるとパフォーマンス低下。 |
| **移植性** | 圧縮が必要で、大規模データベースは移動に時間がかかる。 | 1つのファイルにデータを保存し、移動やコピーが容易。 |
| **セキュリティ** | ユーザー管理やSSH対応などのセキュリティ機能が豊富。 | 認証システムがなく、ファイルパーミッションに依存。 |
| **セットアップの容易さ** | サーバー設定やユーザー管理が必要。 | 設定不要でインストールが簡単。 |
| **長所** | 高いパフォーマンス、複数ユーザー環境対応、広範な言語サポート。 | 低メモリ要求、ポータブル、自己充足的。 |
| **短所** | データが壊れる可能性、大量のメモリを必要とする。 | 複数ユーザー環境非対応、大規模データベースでパフォーマンス低下。 |

## SQLite

SQLiteは、デフォルトでは1つのスレッドからの接続に対して安全に動作しますが、複数のスレッドが同じ接続を使用する場合には注意が必要です。デフォルトでは、SQLiteは以下の2つのモードをサポートしています：

1. **Single-thread mode**: 1つのスレッドだけがデータベース接続を使用します。このモードでは、他のスレッドが同じ接続を使用することはできません。`check_same_thread=True` (デフォルト)
2. **Serialized mode**: 複数のスレッドが同じ接続を安全に使用できるようになります。ただし、この場合、各スレッドが接続を使用する際にロックを管理する必要があります。**`check_same_thread=False`**

## ジェネレータ関数

通常はreturnを使って値を返すが、ジェネレータ関数ではyeildを使って値を返す。yeildはその時点で関数の実行を一時停止し、次にその関数が再度呼び出されたときに停止した時点から再開される。

```jsx
def generator_function():
    yield 1
    yield 2
    yield 3

gen = generator_function()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

## JWT（JSON Web Token）

トークンベース認証の1つ。

アプリケーション側ではユーザのログイン状態を保存せず、ログイン時や情報を得たいときにHTTPリクエストにトークンを含めて送信する。そしてアプリケーション側がそのトークンが有効かを検証することで認証を行う方式。

- JWTには署名をつけるため中間者による改ざんを検知できる
- 複数のユーザー権限も再現可能
- シングルサインオンに使われることもある
- 改ざんを検知する仕組みであり防ぐものではない

**トークンが盗まれた場合、攻撃者はそのトークンを使用してユーザーを模倣することが可能**

[JWT認証の流れを理解する - Qiita](https://qiita.com/asagohan2301/items/cef8bcb969fef9064a5c)

## OAth2

セキュリティースキーム

[FastAPIチュートリアルの「OAuth2、JWTトークンによるBearer」がよくわからなかったので、調べてみた｜猩々博士](https://note.com/mega_gorilla/n/ncec503b5eb8d)

ローカル環境で使用しているパッケージ一覧をを取得しrequirements.txtに書き出す

`pip freeze > requirements.txt`

## デコレーター

関数の前にある＠から始まる文字列は「デコレータ」

関数をデコレーションできる。つまり既存関数の処理の前後に自分自身で処理を付け加えることができる。関数を呼ぶ関数。

フォームデータを扱うときは`pip install python-multipart`が必要だった

## FastAPIの非同期について

[FastAPIで非同期処理を理解する -FastAPIで安直にasyncしてはいけない- - Qiita](https://qiita.com/ikora128/items/35b02714eee7d44f44d6)

## 認証の流れ

- アカウント作成
- ログイン
- JWTトークン発行
- `Bearer`トークン形式でJWTトークンを含めてリクエスト
- エンドポイントごとにOAuthPasswordBearerを使ってトークンを抽出し、トークンを検証

※一般的にはトークンをクライアント側に保存するが今回はバックエンドのみの実装のた保存できず、リロードするとトークンが失われる。
