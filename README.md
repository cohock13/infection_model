# これは何

セルオートマトンを用いた感染モデルのシミュレータ.
思いつきで作ったので確立した理論に基づいているわけではない.

あるエージェントがもし感染している場合や発症している場合に,自分と一定距離以内にいる個体を確率で発症させる.
発症した個体や,感染した個体は一定確立で治り,死ぬ.

# 1.モデル1-1 (健康,発症,死亡,治癒)
Python
```bash
python infection.py
```

健康な個体,発症した個体,死亡した個体(動かない),治癒した個体からなるシミュレータ.
治癒した個体はもう二度と感染しない.

# 2.モデル1-2 (動く,動かない)
Python
```bash
python infection_comparison.py
```

1-1モデルと同様の条件で,発症した個体について移動をする/しない場合のシミュレータ.
乱数のシードを固定してないので,結果はまちまちであるが,やや動かない場合のほうが感染者の増加率が低いように見える.

# 3.モデル2-1 (健康,感染,発症,死亡,治癒)
Python
```bash
python infection_incubation.py
```

健康な個体,感染した個体,発症した個体,死亡した個体(動かない),治癒した個体からなるシミュレータ.
感染した個体は一定確立で健康な個体に戻るか,感染するかになる.
他は12-1と同条件.

# 4.モデル2-2 (動く,動かない)
Python
```bash
python infection_incubation.py
```

現実問題,感染しているかどうかわからない状態で人は動き回ってしまうはずである.
ので,2-1のモデルで発症者は固定するが,感染者は固定しない場合と両方とも動かすケースをシミュレーションしてみる.
結果からすると,どちらとも大差ないように思える.感染距離や確率パラメータに依存する部分はあるが,少なくともこういった閉鎖空間では止まる,止まらないは影響しないのではないか　.

# 5.モデル3 (隔離)
Python
```bash
python infection_isolation.py
```

2-1のモデルの派生版.発症した個体について,別の場所に隔離することによって周りへの拡大を防ぐシミュレータ.
けっこう拡大が遅れているような感じがする.


# 最後に

Q.コードが汚い.classになぜしない
A.(めんどくさかったので...) 汚さに見かねた友人がきれいなコードのシミュレータ(simulator.py)を作ってくれたので,そちらをご参照ください.







