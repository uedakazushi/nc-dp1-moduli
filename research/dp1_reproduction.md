# dP1：再現手順

2026-11-16 / reproduction-v2。リポジトリrootを作業ディレクトリにする。

## 原稿

```sh
latexmk papers/dp1_anticanonical_models.tex
latexmk papers/nc_del_pezzo_degree1_moduli.tex
```

`.latexmkrc`によるLuaLaTeXを使用する。必要なTeXパッケージはltjsarticle/LuaTeX-ja、amsmath、amssymb、amsthm、mathtools、enumitem、booktabs、hyperref、geometry、fix-cm。PDF/aux/SyncTeX等はbuild/へ生成し、Gitで追跡しない。

反標準モデル論文は `papers/sections/elliptic_rank_filtration.tex` を読み込む。この依存ファイルを省略しない。外部bibliographyファイルや画像は不要。二つの公表原稿は数学的内容を削らず保持し、rankの完全な証明は反標準モデル論文§6に置く。

## 厳密な多項式検算と参照検査

```sh
python -m pip install -r requirements-research.txt
python scripts/check_elliptic_rank.py
```

Python3とSymPy1.14.0を使用。Hilbert差分、principal quotientの多項式、Euler差分、rank二次係数を記号計算し、反標準モデル論文のinputを展開してlabel/ref/citeの閉包を検査する。固定入力データは不要。この計算は圏論的証明・有限長性・導来同値の機械検証ではない。

## 再開

`00_research_plan.md` → `research/dp1_research_plan.md` → `research/dp1_research_notes.md` → 両TeX → `research/dp1_validation.md`。旧ZIP・過去会話・外部の旧ノートを前提にしない。必要な既知入力の書誌と適用範囲は本文と研究ノートにある。実際に完了した組版・検証はvalidationを参照し、未実施分を実施済みと扱わない。
