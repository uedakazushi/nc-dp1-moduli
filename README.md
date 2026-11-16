# 次数1の非可換del Pezzo曲面のモジュライ

2026-11-16 / research-v3。GitHub mainが独立した研究の正本。再開時は必ず [研究方針](00_research_plan.md) を最初に読む。

## 現行の数学

中心正則一次元gと整なGorenstein種数1のtwisted homogeneous coordinate ring境界を持つ右noetherian環Rについて、qgr RのGabriel–Krull filtration、構造対象πRのrank one/torsion-free性、rankとHilbert二次係数の一致を証明した。境界自己同型の有限位数を排除せず、整なnodal/cuspidal境界も含む。この環論的結果は導来比較、ASregular被覆、有限homological dimensionから独立である。

既存Rains環と導来比較を入力すれば、次数1の内在的公理および数値rankとの一致が得られる。ただし既存全q導来比較の独立全面監査、相対heart・基底変更・降下、全intrinsicモジュライ成分性は未完成。新規性の網羅的確認も未完了。

## 公表用原稿と継続資料

- [内在的構造と次数1変形族](papers/nc_del_pezzo_degree1_moduli.tex)：普遍点dg族、HH/KS、有限A∞ chart、抽象rank、条件付きweighted sextic。
- [反標準モデル，内在的rankと共鳴](papers/dp1_anticanonical_models.tex)：既存導来比較と独立なrank認識。新証明は [種数1境界のrank節](papers/sections/elliptic_rank_filtration.tex) を本文に読み込む。
- [詳細計画](research/dp1_research_plan.md)、[現行ノート](research/dp1_research_notes.md)、[検証状態](research/dp1_validation.md)、[再現手順](research/dp1_reproduction.md)、[Codex指示](AGENTS.md)。

主稿の特殊楕円qgr-rankを未解決としていた文章の横断的参照整理は残る。現在の解決範囲は反標準モデル論文§6と研究方針を参照する。主稿の一般公理からの中心境界認識は依然未解決である。

## 再現

リポジトリrootで実行する。
```sh
python -m pip install -r requirements-research.txt
python scripts/check_elliptic_rank.py
latexmk papers/dp1_anticanonical_models.tex
latexmk papers/nc_del_pezzo_degree1_moduli.tex
```
LuaLaTeX・latexmk・LuaTeX-jaを使用。PDF、中間物、ZIPはGit追跡しない。検算は多項式恒等式と参照を確認し、圏論的証明を機械検証するものではない。

一般次数の共鳴・heart比較は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、三次三様体は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) の研究である。外部結果の仮定と版を明記して用いる。
