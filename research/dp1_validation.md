# dP1 統合原稿の検証状態

2026-11-16 / validation-v2（既往の2026-11-15検査は下記に明記）

## 2026-11-16 現状評価と証明監査の境界

- GitHub mainの研究方針、2本の論文の主要定理と証明、ノート、既往の組版検証記録を読んで現状を評価した。
- Okawa--Ueda、Rains、Etingof--Ginzburg、可換dP1のコンパクト化の関連一次資料を探索。特にRains arXiv:2504.16187 §16.4の次数1反標準環の既知結果との重複を次の監査対象とした。一次資料の全証明・全適用条件を今回独立に照合し終えたわけではない。
- **今回はTeXの新たな組版・数値検算・主張の独立全面検証を実行していない。** 以下に記す2026-11-15の組版成功は以前の作業の記録であり、今回のチェック結果ではない。
- `HH²=10, HH³=0, KS`、有限A∞ chart成分性、smooth elliptic derived comparison、weighted sextic認識は、本文で主張・証明された範囲と、全Morita/intrinsic moduliへの未完成の比較を区別する。研究価値最大化型の今後の監査順は `research/dp1_research_plan.md` を参照。

## 数学

- 本文は2026-11-14版のdP1研究ソース2件を内容と証明を削らず移植したもの。共鳴比較・KS計算・有限表示での成分性などは「既存原稿に証明を記載している」結果である。
- GitHub統合に際し、本文の全証明を独立に再監査したわけではない。新規性・外部査読・形式化は未確認。
- 元のRains共鳴条件は数値的amplenessの条件であり、AZ-ampleness、abel equivalence、dg derived equivalence、qgrのhomological smoothnessを区別する。
- 特異境界・非局所自由gluing、弱del Pezzo境界の収縮先、全intrinsic moduliへの成分性・同値は未証明。

## 資料の参照

移植元：`intrinsic_nc_del_pezzo_20261114_v4.zip`内の`intrinsic_nc_del_pezzo.tex`と`anticanonical_resonance.tex`。TeX中の参照先ファイル名を現行repoの`papers/`名へ置換。旧ZIP自体はGitに含めない。

## 組版・チェック

- 2026-11-15にリポジトリの `.latexmkrc` と同等の設定を用い、LuaLaTeX/latexmk で二つの原稿を組版した。主論文31ページ、共鳴論文9ページで、いずれも最終実行の終了コードは0。
- 主論文の最初の組版は実行時間制限で中断し、破損した一時auxを削除してclean buildで成功した。一時生成物はGitに含めない。
- 両TeXのlabel/refを静的に走査し、参照切れと重複labelは検出されなかった。ログにoverfull/undefined/multiply-definedの警告も検出されなかった。
- 組版は数学の独立再検証を意味しない。PDFと中間生成物はGit追跡しない。
