# Codex研究指示：次数1の非可換del Pezzoモジュライ

2026-11-16 / dp1-codex-v3。最初に `00_research_plan.md`、`research/dp1_research_plan.md`、現行研究ノート、両論文、検証・再現資料を読む。研究全体の数学的価値を最優先にする。完全分類の完成を待って独立した成果の公表を停滞させない。

## 現在閉じた部分

`papers/dp1_anticanonical_models.tex` §6（`papers/sections/elliptic_rank_filtration.tex`）は、中心正則一次元と整なGorenstein種数1 THCR境界からHilbert多項式、Gabriel–Krull filtration、πRのrank-one/torsion-free性、rank=2/d×二次係数を証明する。σの位数、ASregular被覆、導来比較を仮定しない。整なnodal/cuspidal境界を含む。これを再び未解決と扱わない。独立の新規性は未確定。

既存Rains環・全q導来比較を入力した内在的公理と数値rank一致は、入力を明示した帰結である。既存導来比較全体の独立監査は未完了。今回の環論的証明で上流を検証済みにしてはいけない。

## 次の作業

1. 主稿の楕円qgr-rank未解決表示を反標準モデル論文§6への参照に整理し、有効な既存証明は保持する。
2. Rains環構成、finite-orderのYZ入力、Ind orbit生成、trace、pseudo-perfect表現可能性の一次資料を監査する。
3. Artin基底上の相対flat ring/qgr、基底変更、heart、指定OとSerre作用、同型groupoid・fpqc降下を構成する。総圏の絶対GK長さを相対rankに使わない。二重数自明族のgeneric lengthが2となる例を試験に使う。
4. 全Morita変形とfinite directed A∞ chartの比較、curvature、inner stabilizer、Bertini quotientを処理する。
5. 特異境界での環の存在・導来比較・非局所自由gluingを調べる。rank認識の拡張済み範囲と混同しない。

numerical ampleness / AZ-ampleness、derived / abelian equivalence、finite chart / intrinsic成分、stack / coarseを常に区別する。HH²=10・HH³=0・KS同型だけで全分類を宣言しない。Rains、Okawa–Ueda、EGの既知構成との差分を確認する。

## 検証と保存

日本語LuaLaTeX。rootで `python scripts/check_elliptic_rank.py` と必要な `latexmk` を実行し、成功・未実施を区別する。SymPy検算は圏論的証明ではない。研究の区切り、目安15分のcheckpointで方針・ノート・原稿・検証情報を整合させ、mainへ直接通常のfast-forwardで保存し、remote SHAを確認する。PR、GitHub Actions、force pushは使わない。他者の並行変更は取得して統合する。

GitではPDF、ZIP、中間物、旧版、履歴、キャッシュを追跡しない。GitHub mainが正本で、LibraryはGitHub保存失敗時の緊急避難のみ。背景の自動作業は約束しない。
