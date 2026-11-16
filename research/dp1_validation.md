# dP1 統合原稿の検証状態

2026-11-15 / integration-v1

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
