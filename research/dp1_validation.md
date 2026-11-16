# dP1：現行の検証状態

2026-11-16 / validation-v3。証明の記載、今回の点検、機械的検算、組版、外部査読を区別する。

## 今回証明を構成・点検した事項

反標準モデル論文§6、`papers/sections/elliptic_rank_filtration.tex`：
- `lem:elliptic-hilbert-polynomial`：Ann_M(g)を含む完全列からHilbert多項式を得る。g-torsion-freeを仮定していない。
- `thm:elliptic-filtration`：有限長対象と商圏の単純対象への中心gの作用から、GK filtrationと多項式次数filtrationを一致させる。
- `thm:elliptic-rank`：斉次右イデアル内のaR、商の一次増大度、generic simple generatorからrank one、torsion-free、二次係数との一致を証明する。
- 整なGorenstein種数1境界に一般化した。σ-ampleness、RR、ω_E≅O_E、境界の単純層を確認し、nodal/cuspidalを含める。可約・非被約境界や非中心normal元を含めない。
- `prop:elliptic-numerical-rank`：境界triangleからEuler差分を導く。数値rankと内在的rankの比較には既存導来同値を明示的に入力する。

ここでの点検は本文中の推論の数学的点検であり、独立した第三者査読・形式証明ではない。結果の独立の新規性は未確定である。

## 一次資料の確認範囲

AOU arXiv:1411.7770v1 Appendix AのDefinitions A.3–A.4、Propositions A.5–A.6を本文・ページ画像で確認。非可換射影平面の定理を楕円環へそのまま適用せず別証明を与えた。

RSS arXiv:1308.2216v2 Proposition2.4を本文・ページ画像で確認。無限位数仮定を確認し、新しいrank証明には用いていない。既存導来比較での有限位数の扱いは依然独立監査対象。

Keeler arXiv:math/9912051v2 Theorem1.2を本文・ページ画像で確認。整な曲線の数値因子類はdegreeで決まり、自己同型の作用が自明なので正次数Lはσ-ample。

Artin–Van den Berghの原論文全体は今回取得・監査していない。Theorems1.3–1.4の再掲をChirvasitu–Kanda–Smith, Forum Math. Sigma9(2021)e4, Theorem2.4で本文確認し、Corollary2.8の境界圏埋込みも確認した。同論文PDFのwebページ画像取得は502で失敗したため、この資料は本文テキストでの確認にとどまる。引用は原論文と確認した再掲を併記した。

## 今回実行した機械的検査・組版

`python scripts/check_elliptic_rank.py` をSymPy1.14.0で実行：4件の多項式恒等式、38個の一意なlabel、52件の参照、11種類の引用keyの閉包を確認した。これは有限長性や導来同値を機械的に証明するものではない。

`latexmk papers/dp1_anticanonical_models.tex` をLuaLaTeXで実行し、版1.2の14ページPDFを生成、終了コード0を確認した。最終ログにundefined/multiply-defined/overfull/underfullの警告は検出しなかった。PDFのページ画像をレンダリングし、本文・新rank節の配置を確認した。PDFと中間生成物はGitに含めない。

## 今回実行していないこと

主稿全体の再組版・独立全面監査、全q導来比較の一次入力を通した全面再検証、Morita変形との全比較、相対heart・降下、全intrinsic成分性、網羅的な新規性調査は未実施・未完了である。主稿に残る特殊楕円qgr-rankの未解決表示の横断的参照整理も残る。現行のrank結果は反標準モデル論文§6が正本。

## 保持する既存検証情報

既往の2026-11-15検証では主稿31ページ、反標準モデル論文9ページのLuaLaTeX組版成功とlabel/refの閉包が記録されている。これは今回の主稿の再検査を意味しない。既存のgluing、HH/KS、有限chart、weighted認識、全q導来比較には証明が記載されているが、今回新たに全て検証したとはしない。

ファイル生成・検算・組版とGitHubへの保存は別の状態である。保存の成否は実際のcommit/main到達確認により報告し、この文書だけから推定しない。
