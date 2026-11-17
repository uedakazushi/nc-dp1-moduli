# 検証状態

2026-11-18 / validation-v4。新Artin原稿と既存原稿の検証を分離する。

## 今回の数学的点検

`papers/dp1_artin_deformations.tex` の特殊fiber入力、nilpotent noetherian性、GK filtration、絶対長さ公式、flat tail判定、socleを使ったtorsion-free性の持上げ、flat基底変更、反標準環の自由性と自然性、二重数障害、随伴付き同値の持上げの各証明を本文で構成・点検した。

平坦Abel変形の一般理論はDe Deken–LowenとLowen–Van den Berghの既知結果を入力する。前者arXiv版Proposition4.4/Theorem4.5/Proposition4.6と後者Theorem8.8を本文・ページ画像で確認。Stacksのflatness/perfect/二重数例も確認した。原著全体の独立再証明ではない。GLSV arXiv:2411.15359はabstractの確認にとどまり、証明入力ではない。

新しい原稿の結果の独立の新規性、第三者査読、形式証明は未確認・未実施。相対e/Serreと基底変更は明示的な入力である。全Morita/Abel変形の同値、元圏と相対perfect部分の比較、finite-type moduli、fpqc降下は未証明。

## 今回実行した検査

`python scripts/check_artin_rank.py`：
- 重み付き反標準Hilbert数をn=0,…,40の41次数で厳密計算。
- k[ε]/ε^ellとその商に関する長さ・Hilbert公式を875組で検算（ell=2,…,8）。
- 二重数の周期分解に由来するExt計算を次数0,…,12で有限次元線形代数として検算。
- 31個の一意なlabel、23件の参照、9種類の引用キーの閉包を確認。

これらは圏論的証明の機械検証ではなく、正規化・符号・参照の検査である。

`latexmk papers/dp1_artin_deformations.tex`：LuaLaTeXで9ページPDF、終了コード0。最終ログにundefined/multiply-defined/Overfull/Underfull/Warningは検出されなかった。全9ページを画像化し、一覧と代表ページで配置を確認した。PDFは334348 bytes（最終組版時）。ビルド生成物・ログ・画像はGit/bundleに含めない。

## 今回未実施

既存主稿と反標準モデル論文の再組版・独立全面監査、主稿内に残る旧rank未解決表示の横断修正は未実施。以前の14ページ反標準モデル論文の検証を今回再実行したとは報告しない。既存の体上rank定理は現行の有効な入力として保持した。

既存の記録：2026-11-15の主稿31ページ・旧反標準稿9ページ、2026-11-16の反標準稿14ページの組版と検算は、それぞれ当時の検査結果である。今回の成功範囲は上記Artin原稿と新スクリプトのみ。

GitHub保存・Library保存・ZIP整合性は実際の各操作後に別途確認する。この文書の存在だけから保存成功と推定しない。
