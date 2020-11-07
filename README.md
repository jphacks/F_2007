# 言の葉インク

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要

文章を入力し、「文章の色」と「インクの色」を DistilBERT を使って比較して最も傾向が近いインクをリコメンドするサービスです。今回は全 24 種類の色彩雫という色インクシリーズの中からおすすめを選んでいます。

### 背景(製品開発のきっかけ、課題等）

万年筆やガラスペンに使うインクは世界に数え切れないほどたくさんあります。
どれを買うか迷うのも楽しみの１つですが、自分の書いた「文章の色」と「インクの色」を比較しおすすめしてくれるサービスがあったら面白いのではないかと思い開発しました。

### 製品説明（具体的な製品の説明）

まずあらかじめ色彩雫シリーズのインク名（紫陽花、山葡萄、紫式部など）を DistilBERT で解析しておきます。そして実際にユーザーに入力してもらった文章を DistilBERT で解析し、最も近い言葉のベクトルを持つインクの色をおすすめとして表示します。

### 特長

1. 自分の文章を元にしてインクをおすすめしてくれる
2. 日本語自然モデル DistilBERT を使った解析

### 解決出来ること

世界には数え切れないほど多くの種類のインクがあります。どれにしようか迷うのも醍醐味の 1 つですが、この「言の葉インク」を使うことで気軽に自分にあったインクを知ることができます。 <br>
また、すでにインクを持っている人にも利用価値があります。例えば、万年筆を使って何か書きたいけど特に題材がないなというとき、Twitter での自分の呟きを言の葉インクに入力することで「そのツイートの色」を知れるので、実際にその色で文章を書き起こすことことができます。

### 今後の展望

- さらにインクの種類を増やしてより多くの選択肢を提供すること
- Twitter から呟きを引用

### 注力したこと（こだわり等）

「言葉に色をつける」の結果で画面上で実際のインクに近い色で文章を表示させたこと

## 開発技術

### 活用した技術

#### API・データ

- DistilBERT

#### フレームワーク・ライブラリ・モジュール

- Vue.js
- Flask
- AWS EC2

### 独自技術

#### ハッカソンで開発した独自機能・技術

- DistilBERT で言葉のベクトルを調べ、事前に登録したインクの色のベクトルと比較し、最も近いものをおすすめする
- https://github.com/jphacks/F_2007/commit/7508af9a4dd46312b500a2ac5c95c77836e41edb
