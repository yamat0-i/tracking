# 注意
現状、
1. avi形式
1. 追跡対象が横方向に移動
1. 追跡対象がはじめからキャプチャされている

という動画にしか対応していません。  
縦方向に移動する動画を解析したいときは、事前に編集ソフトなどで90°回転してから使用してください。  
Ubuntu以外のOSでの動作は未確認です。たぶんWindowsでも動くはずですが、不具合があったら教えてください。


# インストール
プロジェクトごとダウンロードしてください。  
**このプロジェクトのフォルダがrootです。**
### pipの人  
安全のために仮想環境を作っておいてください。ターミナルでrootに移動して、
```
$ python -m venv .venv （.venvの名前は任意）
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
これで必要なライブラリのインストールができます。

### condaの人
安全のために仮想環境を作っておいてください。ターミナル（こだわりなければAnaconda promptとかでいいです）で、
```
$ conda create -n venv python （venvの名前は任意）
$ conda activate venv
$ conda install --file requirements.txt
```
これで必要なライブラリのインストールができます。


# 使い方
1. root/videoに解析対象の動画ファイルを入れてください。
1. root/tracking内にある'tracking.py'をエディターで開いてください。
1. 17行目に'videofilename'という変数があるので、そこに動画ファイルの名前を入れてください。  
**拡張子は不要です。**
```
videofilename = '（動画のファイル名）'
```
4. すぐ下の'umperpixel'という変数に、1ピクセルあたりの長さを入れてください。単位はumです。
```
umperpixel = 0.7170625782472173 #10x # Default
```
5. ターミナルでrootに移動し、"python -m tracking"を実行してください。  
エイリアス、環境変数の設定によってはpythonを別のコマンドに変える必要があるかもしれません。 
例：python3, winpty python  
```
$ python -m tracking
```
6. ウィンドウが開いたら追跡対象にカーソルを合わせて左クリック。
7. そのうちプロットが出ます。
