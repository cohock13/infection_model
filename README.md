# これは何

セルオートマトンを用いた感染モデルのシミュレータ.<br>
思いつきで作ったので確立した理論に基づいているわけではない.<br>

あるエージェントがもし感染している場合や発症している場合に,自分と一定距離以内にいる個体を確率で発症させる.<br>
発症した個体や,感染した個体は一定確率で治り,死ぬ.<br>
<br><br><br>
# 1.モデル1-1 (健康,発症,死亡,治癒)

```bash
python infection.py
```

![infection](https://user-images.githubusercontent.com/55901554/82142547-1ee45780-9878-11ea-9888-4eda73b441de.gif)


健康な個体,発症した個体,死亡した個体(動かない),治癒した個体からなるシミュレータ.
治癒した個体はもう二度と感染しない.
<br><br><br>
# 2.モデル1-2 (動く,動かない)

```bash
python infection_comparison.py
```

![comparison_simple](https://user-images.githubusercontent.com/55901554/82142558-2b68b000-9878-11ea-90ca-0e6e2f3b4408.gif)


1-1モデルと同様の条件で,発症した個体について移動をする/しない場合のシミュレータ.
乱数のシードを固定してないので,結果はまちまちであるが,やや動かない場合のほうが感染者の増加率が低いように見える.
<br><br><br>
# 3.モデル2-1 (健康,感染,発症,死亡,治癒)
Python
```bash
python infection_incubation.py
```

![incubation](https://user-images.githubusercontent.com/55901554/82142575-43d8ca80-9878-11ea-8b20-95a8f68dab94.gif)

健康な個体,感染した個体,発症した個体,死亡した個体(動かない),治癒した個体からなるシミュレータ.
感染した個体は一定確立で健康な個体に戻るか,感染するかになる.
他は12-1と同条件.
<br><br><br>
# 4.モデル2-2 (動く,動かない)

```bash
python infection_incubation.py
```
![comparison](https://user-images.githubusercontent.com/55901554/82142584-4e935f80-9878-11ea-9cef-f37e27eb5ffa.gif)

現実問題,感染しているかどうかわからない状態で人は動き回ってしまうはずである.
ので,2-1のモデルで発症者は固定するが,感染者は固定しない場合と両方とも動かすケースをシミュレーションしてみる.
結果からすると,どちらとも大差ないように思える.感染距離や確率パラメータに依存する部分はあるが,少なくともこういった閉鎖空間では止まる,止まらないは影響しないのではないか.
<br><br><br>

# 5.モデル3 (隔離)

```bash
python infection_isolation.py
```

![infection_isolation](https://user-images.githubusercontent.com/55901554/82142590-59e68b00-9878-11ea-8d26-91b10d30e4a9.gif)

2-1のモデルの派生版.発症した個体について,別の場所に隔離することによって周りへの拡大を防ぐシミュレータ.
気持ち拡大が遅れているような感じがする.
<br><br><br>

# 最後に

Q.確率依存のモデルなら,もっと結果は振れるはずではないのか.きれいな結果だけ抜き出してはいないか.<br>
A.正直その通りです.Readmeに載せてるgifはきれいになったものを載せてます.シミュレートしてもきれいにならない場合がけっこうあります.<br>
  100000回くらい試せば多分多少の有意差は出そうな気がします.<br>

Q.コードが汚い.classになぜしない.<br>
A.(めんどくさかったので...) 汚さに見かねた友人がきれいなコードのシミュレータ(simulator.py)を作ってくれたので,そちらをご参照ください.(友人に掲載許可確認済)







