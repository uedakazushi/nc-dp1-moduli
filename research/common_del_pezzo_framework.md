# 非可換del Pezzo曲面の共通内在的枠組みとheart比較

2026-11-15 / hearts-v1。全次数のheart比較を上位課題とし、最初はcubic surfaceを研究する。次数1・3の既存研究を保持し、全次数の分類定理を主張しない。最初に `00_research_plan.md` と `research/heart_comparison.md` を読む。

## 金沢型量子FermatとOUのAS surfaceの厳密な差

**証明済み**：金沢型量子Fermat cubicのA=qgr B/(t³+x³+y³+z³)は、OU arXiv:2508.04986 Definition 1.1のAS surfaceではない。現行の完全証明は `papers/quantum_fermat_not_as_surface.tex` の定理3.1。H=(mu3)^2の非退化な2-cocycle αを使い、古典Fermat cubic Xに対し Db(A)≃Db(coh^α[X/H]) という明示的なgraded Morita同値を構成する。捩れ付きorbifold HKRと固定楕円曲線2本から HH_-1=2, HH_0=5, HH_1=2 を得る。有限群の全9元と指標は `computations/verify_quantum_fermat_ou_sectors.py` と証明書で検算。OU AS surfaceなら有限なvery strong helix、従って完全強例外列がありHH_i(i≠0)=0なので矛盾する。

**意味**：反Serre作用がheartを保ち、AZ ampleで、gd2・exceptional O・Hilbert関数を満たすintrinsic weak cubicはOU AS surfaceであるとは限らない。量子Fermatはその明示的な反例。次数3の全weak moduliがOU/AOUのmarked locusのW(E6)商だけからなるという全域分類は成立しない。一方、可換三次曲面を含むOU部分の大域化、R13支配部分のgeneric同定は別問題として保持する。全weakモジュライの代数性は未証明。

## 最優先のheart比較

Rains、Van den Bergh raw blow-up、AS helix、反標準qgrの四構成について、存在、realization Db(heart)→Tの同値、指定同値のt-exactness、構造対象・反Serre・境界restriction・rank・marking、族の降下を分離する。数値的non-amplenessをAZ失敗や導来変化と同一視しない。

cubicではVdBの振幅1同値からT=ker R¹δ_*、U=ker δ_*による一回のHRS tiltを得る。heart一致はU=0に帰着する。AOU Theorem 9.4の左辺はqgr Fであり、AS qgrとの導来比較を与える。t-exactnessと実際のmutation後の構造対象の同定は別課題。証明と判定補題は `papers/nc_del_pezzo_hearts.tex`、次の計算は `research/heart_comparison.md`。

## heart 比較の名称

比較する四つの構成の名称は **Rains heart、VdB heart、AS heart、anticanonical heart** に統一する。前二者が同じabel圏を表す可能性もあるが、対象の同定・導来同値・t-exactnessを個別に確認する。VdB heart は literal blow-up に由来する側を表し、section-algebra 型の射影モデルを自動的に指すものではない。四つの名称が四つの異なるheartの存在を意味するわけではない。

## 共有する候補公理

基礎体k上のExt有限・noetherianな非零abel圏Aを取り、D^b(A)にSerre関手Sが存在するとし、反標準作用tau=S^{-1}[2]を定義する。**homological dimension 2は別には要求しない。**tauはheartを両方向で保つexact autoequivalence、Oはrank-one torsion-free exceptional object、(O,tau)はArtin–Zhang ampleとする。次数dを全n≥0の

    dim_k Hom_A(O,tau^n O)=1+(d/2)n(n+1)

で指定する。Oを指定するのがweak marking。quiver、blowdown基底、例外列は定義に含めない。rankをGabriel–Krull長さで定義する場合の必要仮定・証明は次数1主論文を参照する。数値K群のrankと同一視するときには別途比較する。

反標準環 R=⊕_{n≥0}Hom_A(O,tau^nO) はArtin–Zhangの条件下でqgrへの再構成を与えるが、所望のambientの存在・正規境界・smoothnessをHilbert seriesだけから結論できない。

## Serre作用による大域次元の自動性

任意のM,N∈AについてExt^i_A(M,N)≅Hom_{D^b(A)}(tau N,M[2−i])^*。tau(A)⊂Aからi>2の群は零であり、非零Nに対してExt²_A(tau N,N)≅End_A(tau N)^*≠0。よってhdim A=2は厳密に従う。tauのheart上での本質的全射性は不要。証明は次数1原稿の命題prop:serre-heart-hdim、次数3原稿の命題prop:serre-heart-global-dimensionに置く。

## 定義の整合

次数3の旧公理では構造対象のexceptionalityを独立には要求していなかった。その広い条件はpre-weakと呼び、現在のdegree 3のweakly markedは次数1と同様にexceptionalを要求する部分問題とする。pre-weakからExt^1(O,O)=0は未証明。量子Fermatと既存の正規三次超曲面商はexceptionalなので保持される。

Gabriel–Krull rank-one torsion-freeとn≥0のHilbert数値により負次数の切断数は零になる。非零のO→tau OとO→tau^{-m} Oを合成すれば非零射は単射なのでO(m)≅Oを強制し、h_d(m)>1に矛盾する。End(O)=kとExt^2(O,O)=0はこの結果とSerre双対から従う。追加のexceptionalityの実質はExt^1(O,O)=0。

## 共有する方法と次数別の差

| 項目 | cubic surface (d=3) | dP1 (d=1) |
|---|---|---|
| H_R(t) | (1+t+t²)/(1-t)³ = (1-t³)/(1-t)^4 | (1-t+t²)/(1-t)³ = (1-t⁶)/((1-t)²(1-t²)(1-t³)) |
| 典型ambient | AS4、4個の一次変数 | 重み(1,1,2,3)型 AS4 |
| 境界認識 | 3次元二次Koszul AS3 + 正規3次商 | 重み付き3次元AS3 + 正規6次商 |
| 可換モジュライ方向 | 4 | 8 |
| Poisson方向 | 4 | 2 |
| 合計期待次元 | 8 | 10 |
| 根格子 | E6 | E8 |

同じ帰結を無条件で証明したとみなさず、中心または正規一次境界が与えられたときの相対PBW / AS正則拡大と、内在的な境界の存在を別問題にする。例外collectionやpotentialは構成・計算上のchartとして使っても分類対象には含めない。BGRやBertini型自己同型を忘れる場合、同一視と残余慣性を明記する。

## 各論文の役割

- `papers/nc_del_pezzo_hearts.tex`：全次数のheart比較問題とcubicにおけるHRS・orbit・corner判定。
- `papers/weak_cubic_axioms.tex`：d=3。標準正規境界の認識定理と量子Fermat反例。
- `papers/cubic_surface_ambient_moduli.tex`：d=3。モジュライ成分・marked potentialとの比較。
- `papers/nc_del_pezzo_degree1_moduli.tex`：d=1。内在的rank、weighted sextic、pointed dg族、avatar。
- `papers/dp1_anticanonical_models.tex`：d=1。楕円領域の反標準qgrと共鳴、導来比較。
- `papers/nc_cubic_threefold_moduli.tex`：3-fold。別の中心課題であり、研究・論文は独立維持。

## 論理的状態

既存の各論文に記載された証明と、全てのintrinsic対象の網羅性、全モジュライの代数性・既約成分性、heartを保つ標識忘却の大域同値は区別する。次数1の特異楕円境界での導来比較、次数3の正規一次境界の一般存在はいずれも未解決。既存稿の証明記載と今回の点検を区別する。新しいheart研究はdP1の強い導来比較を入力にせず、cubicの一次文献から始める。

## 量子Fermat ambientの所属成分

量子Fermat BはPymのgraded Calabi–Yauのskew-polynomial成分 L(1,1,1,1) の3-torsion特殊点であり、L(1,1,2)の関係式中の二次補正項Qをu^2 Qにする平坦退化のu=0にもなる。従って少なくとも二成分の交点に属する。一方、既存の四頂点正規直線returnの閉incidenceによりR(1,3)の閉包外。その他の成分との交叉は未解決。式と証明は papers/weak_cubic_axioms.tex。
