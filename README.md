![test](https://github.com/Yosukesakamoto/mypkg2/actions/workflows/test.yml/badge.svg)
# mypkg
  ロボットシステム学のROS2パッケージ

## インストール
  
    
    mkdir~/ros2のワークスペースの名前/src
    cd ~/ros2のワークスペースの名前/src
    git@github.com:Yosukesakamoto/mypkg2.git



### 概要
* トピック: countup
* messageの型: int16
* talkerが数字をカウントして、countupで送信し,
　listenerがメッセージを受け取り、表示する。

#### 実行方法

    ros2 run mypkg talker
    で実行し、もう一つの端末を開いて
    ros2 run mypkg listener

##### 必要なソフトウェア
* os
　 
     * Ubuntu22.04

* ROS2
     * テスト済み : Humble

* Python
     * テスト済み : 3.7~3.10

###### ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* © 2022 Yosuke sakamoto


>>>>>>> lesson10
