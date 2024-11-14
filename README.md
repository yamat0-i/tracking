## 注意
現状、
1. avi形式
1. 追跡対象が横方向に移動
1. 追跡対象がはじめからキャプチャされている

という動画にしか対応していません。  
縦方向に移動する動画を解析したいときは、事前に編集ソフトなどで90°回転してから使用してください。  
Ubuntu以外のOSでの動作は未確認です。たぶんWindowsでも動くはずですが、不具合があったら教えてください。


## インストール
プロジェクトごとダウンロードしてください。  
**このプロジェクトのフォルダがrootです。**
### pipの人  
安全のために仮想環境を作っておいてください。
例えばbashの場合は、
```bash:bash
$ python -m venv .venv （.venvの名前は任意）
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
これで必要なライブラリのインストールができます。

### condaの人
安全のために仮想環境を作っておいてください。
```powershell:Anaconda
> conda create -n venv python （venvの名前は任意）
> conda activate venv
> conda install --file requirements.txt
```
これで必要なライブラリのインストールができます。


## 使い方
1. root/videoに解析対象の動画ファイルを入れてください。
1. root/tracking内にある'settings.py'から設定を変更できます。
1. 'settings.py'の中に'videofilename'という変数があるので、そこに動画ファイルの名前を入れてください。  
**拡張子は不要です。**
    ```python:settings.py
    # Path
    root_dir = Path.cwd()
    video_dir = root_dir / Path('video') # Default
    plots_dir = root_dir / Path('plots') # Default

    videofilename = 'videofilename'
    ```
1. すぐ下の'umperpixel'という変数に、1ピクセルあたりの長さを入れてください。単位はumです。
    ```python:settings.py
    # Pixel size(in microns):
    umperpixel = 0.7170625782472173 #10x # Default
    ```
1. x軸とy軸それぞれのプロット範囲の指定もできます。その際は'select_plotrange_x(y)'をTrueにしてください。
    ```python:settings.py
    # Plot range
    select_plotrange_x = False # Default: False
    select_plotrange_y = False # Default: False

    xMin = 0
    xMax = 15
    yMin = 0
    yMax = 600
    ```

1. ターミナルでrootに移動し、"python -m tracking"を実行してください。   
    ```bash:bash
    $ python -m tracking
    ```
1. ウィンドウが開いたら追跡対象にカーソルを合わせて左クリック。
1. そのうちプロットが出ます。
