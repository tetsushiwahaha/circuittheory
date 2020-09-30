# 電気回路及び演習 補助教材，Python 教材

## まずは Python, LaTeX の環境を整えよう

徳島大学は2019年度からPC必携となり，情報科学入門においてもPCを活用した
データサイエンスの授業が展開されようとしている．
情報・光システムコースのみなさんも例にもれずPCを持っているわけであるし，
コースの定義からもPCを主体的使えることが求められるであろう．

この授業は後期であるので，それまでにpython, LaTeX の環境は自分のPCに
入っている，かつ，最新のものに更新されている手はずが整えられていると
想像するのだが，万が一まだ準備していない，という人のために，最初の節では
各OSに応じた環境セットアップの情報を提供する．

なお，Pythonはできるだけ新しいバージョンのものをインストールすること．
もう2.7系は古い．2020.9.30時点では 3.8.5 が最新となっている．常に最新の
環境になるようアップデートする術も確認しておこう．

### Windows 
Windows は言わずと知れたMicorosoft の商用OSである．
Python Windows版のインストールは
https://www.python.jp/install/windows/index.html 
を参照のこと．
Windows10ならばMicrosoftネイティブなPython環境もあるのだが，いろいろ
小回りがきかないらしい．

### Linux
Linux はUNIX系OSのひとつで，様々なアーキテクチャのコンピュータで動作する．
OSやユーティリティを配布する方式（ディストリビューション）によって
有料であったり無償であったりする．

Python Linux版 Anaconda インストールは，
https://www.python.jp/install/anaconda/unix/install.html
を参照のこと．
Anaconda自体はPythonのデータサイエンス環境であるが，
理工学部の研究実践のために必要なツールが同梱されているので
便利であろう．

なお，Linux用の各種インストーラ，apt-get, yumyum などでもインストール
可能である．下記macOS用のHomebrew もLinuxでは利用可能である．

### FreeBSD
FreeBSD は様々なアーキテクチャのコンピュータで動作するフリーのOSである．
このOSをノートパソコンに入れて使ってる猛者はいるかな？
Portsコレクションによってソースコードから鍛える方法，および，
pkg コマンドを駆使してバイナリを直接インストールする方法が用意されている．

### macOS
macOS は基本的にはUNIXであり，シェルから対話的に使う用途には
向いている．

#### macports

オープンソースなツールやOSユーティリティは
ソースコードからコンパイルして整備できる．
[MacPorts](https://www.macports.org)はこの目的のツールである．Pythonは
バージョン別にインストールできるようになっている．

#### Homebrew
Homebrew は https://brew.sh/index_ja を参照のこと．
こちらはバイナリでインストールできる．

## 複素数計算
直流回路の計算と並列して，2章以降で用いる複素数について学んでゆく．
複素数計算の心強いツールとしても Python は使える．
Pythonは複素数をサポートしており，ちょっとした複素数計算のチェックに
利用すると理解が進むであろう．
```
% python
Python 3.8.5 (default, Sep  6 2020, 03:54:05)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> (3+1j) * (1-3j) 
(6-8j)
>>> import numpy as np
>>> np.exp(np.pi * 1j / 3)
(0.5000000000000001+0.8660254037844386j)
>>>
```
この例では numpy という数値計算パッケージを読み込んで np という短縮形で
使うことを指示したあと，j π/3 の指数関数値を計算した．結果は
1/2 + j √3/2  となっている．

## 1章 直流回路

### 直流回路を解く 

`SolvDiffDC.pdf`を読んでください．

### 直流回路の過渡応答

RRC回路の直流応答を調べる．
`RRCdc_func.py` を実行してみてほしい．

```
% python RRCdc_func.py
```
![Figure_1](https://user-images.githubusercontent.com/52724526/94141539-daad3780-fea7-11ea-804a-f97185be814e.png)


TEXの環境が無ければ `RRCdc_func_tex.py` を試してみよ．
同じ回路の数値計算バージョン`RRCdc_num.py`も試してみよ．
同じ結果が出るので面白くないとは思うが，是非コードを
読んででみてほしい．

## 2章 交流回路

### 正弦波を理解する `Fig2.2.1.py`

教科書図2.1.1 をダイナミックに理解する．改めて正弦波(sin 波)とは円周を一定速度
で周回する点の，y 軸への射影であることを理解しよう． x軸への射影は
余弦波(cos 波)である．

```
% python Fig.2.1.1.py
```

実行すると，アニメーションが表示される．

![Figure_1](https://user-images.githubusercontent.com/52724526/93433490-d01bfc80-f901-11ea-9a65-09e141006e69.png)

#### プログラムのポイント
* 前半の関数は x 軸でπを基準に刻みを作る仕事．あまり本質ではない．（LaTeXが
インストールされてないとうまく動かないかもしれない）
* ウィンドウのサイズをマウスで変えるとそれに応じてグラフの大きさも変わる．
* 時刻を-πから+5πの区間にとり，それに対して位相情報が入った正弦波を
描かせている．位相を色々変えてみるとよい．
* matplotlib の plot は，点列データを (x0, y0),  (x1, y1), ...  とすると，
1点のx座標，y座標を分けてリストにした，
[x0, x1, x2, ...] と [y0, y1, y2, ... ] を引数に与えることによって動作する．
* ωは 1 としている．これを変更するには，プログラムをどのように
変更すればよいか．
* 余弦波を描かせるにはどうしたらよいか．また，余弦波を正弦波と同時に
描かせるにはどうしたらよいか

### 位相の進み，遅れ `Fig.2.1.2.py`

位相について，図2.1.2 をダイナミックに理解する


```
% python Fig.2.1.1.py
```

![Figure_1](https://user-images.githubusercontent.com/52724526/93434635-600e7600-f903-11ea-9beb-c0776184f508.png)

右図の赤が sin(t) であり，
それより進んでいる（進相）波が青，
それより遅れている（遅相）波が緑となっている．
青→赤→緑の順番は変わらない．左側の三色の点が，それぞれ特徴的な位置
（x軸やy軸に重なる時刻など）をよく観察すること．

#### プログラムのポイント
* ほとんど `Fig.2.1.1.py` と同じである．`lead`と`lag`が，青と緑の位相を
決めている．いろいろ変えてみるとよい．
* LaTeX が原因でうまく動かない場合は，`Fig.2.1.2-nolatex.py`を試してみよう．

### 過渡応答の減衰 `LRac_func.py` `LRac_num.py` `LCRac_num.py`

`SolveDiff.pdf`を読んでください．
まずは微分方程式を手で解いて，時刻の関数を得た場合．（この解のことを
解析解という）その関数に従ってグラフを描かせたもの：

```
% python LRac_func.py
```

![Figure_1](https://user-images.githubusercontent.com/52724526/93469512-919b3780-f92b-11ea-9cec-aaae4404db8b.png)

電気回路では十分過渡応答が終わったあとの定常解について，超簡単に求める
方法を学ぶ．なお，微分方程式を数値的に求める手段を利用した，
同じ回路に対する数値解も示そう．

```
% python LRac_num.py
```

得られる図は前述の total の軌跡と変わりがない．ほとんど正確に数値解が
得られるのであれば最初から数値計算に頼ればいいじゃない，っと考えるのも
無理はないが，所詮は数値計算．誤差が混入しうる．
線系回路では小規模なものは手で解けるし，その経験がエンジニアとして大切である．


```
% python LCRac_num.py
```

LCR直列交流回路について数値計算するプログラムである．
いろいろとパラメータを変えて応答を観察せよ．
