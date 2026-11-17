# 再現手順

2026-11-18 / reproduction-v3。全コマンドはリポジトリまたはbundleのrootで実行する。

## Artin方向（今回のbundle単独で実行可能）

```sh
python scripts/check_artin_rank.py
latexmk papers/dp1_artin_deformations.tex
```

Python3標準ライブラリのみ。LuaLaTeX、latexmk、LuaTeX-ja/ltjsarticle、amsmath、amssymb、amsthm、mathtools、enumitem、booktabs、geometry、hyperref、fix-cmを使用する。`.latexmkrc`でbuild/へ出力。外部bib・画像・データは不要。本文§2に必要な体上rank証明を含み、旧bundleの取得は不要。

検算は41次数のHilbert数、875組のArtin加群、二重数Ext、label/ref/citeを検査し、圏論的証明を形式化しない。結果の範囲は `research/dp1_validation.md` を参照。

## GitHub上の既存原稿

```sh
python -m pip install -r requirements-research.txt
python scripts/check_elliptic_rank.py
latexmk papers/dp1_anticanonical_models.tex
latexmk papers/nc_del_pezzo_degree1_moduli.tex
```

既存rank検算はSymPy1.14.0を使用する。反標準稿は `papers/sections/elliptic_rank_filtration.tex` を必要とする。これらの既存資産はGitHubに保持されるが、Artin方向のbundleは全repoの複製ではないため含めない。既存原稿の今回の再検査は未実施。

## 配布

今回のbundleには現行方針、Artin研究ノート、Artin原稿TeX/PDF、新検算、再現・検証情報のみを入れる。build/、ログ、aux、SyncTeX、旧PDF、旧ZIP、外部文献PDFを含めない。GitではPDF/ZIPを追跡しない。書誌・確認箇所は原稿とノートに記載する。
