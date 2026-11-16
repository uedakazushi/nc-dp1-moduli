# 研究方針：次数1の非可換del Pezzo曲面

2026-11-16 / dp1-plan-v3。再開時にはこのファイルを最初に読む。GitHub mainを現行研究の正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性、公表可能性を総合し、研究全体の価値を最大化する。目標は柔軟に変更する。重要な変更では現行方針の理由、元の目標について解決したこと・残ったことを簡潔に示し、時系列の履歴は蓄積しない。

証明済み、追加仮定に依存、未完成、予想、計算的観察を区別し、仮定、既知入力、証明の所在、未解決箇所を明記する。原稿に証明があること、今回検証したこと、計算で検算したこと、外部査読・形式化を混同しない。誤りは依存する主張、本文、要約、方針にも反映し、有用な反例・障害を現行ノートへ残す。

公表論文では関連する先行研究の一次資料を確認し、仮定・適用範囲・本研究との差をIntroductionで具体的に説明する。未確認の文献内容や書誌を推測で補わない。日本語LuaLaTeXを標準とし、成果を論理順に組織する。既存の有効な結果・完全な証明は軽量化のために削除しない。研究ノートは現在有効な着想、計算、障害、文献比較を保持し、作業日誌や重複する証明を蓄積しない。

研究継続用bundleは現行方針・ノート・公表原稿と、理解・検証・再生成に必要な最小限のソース、PDF、書誌、計算コード、入力、証明書、再現手順による自己完結した一式とする。研究の区切りごとの承諾不要なLibrary保存は一般的に許可されている。ただし本研究の個別指示はGitHub mainを正本とし、GitHub保存成功時はLibraryへ重複保存せず、失敗時のみ緊急避難に用いる。Library上の既存資料は明示的指示なく削除しない。

GitではPDF、ZIP、旧版、変更履歴、ビルド中間物、キャッシュを追跡せず、再生成可能なソースと必要な証明・検算資産を保持する。生成、検証、commit、mainへの反映、リモートSHA確認を別々に扱う。mainへ通常のfast-forwardで直接保存し、PR、GitHub Actions、force pushを使わない。競合時はremoteを再取得して統合し、他の作業を失わない。背景作業の自動実行は約束しない。

## II. 中心目標と現在の到達点

次数1の非可換del Pezzo曲面の内在的モジュライを、普遍点によるdg族、反標準qgr heart、graded algebraの認識と比較する。完全分類のみを成功条件にせず、独立して公表できる局所変形・heart認識・境界の定理を完成させる。

**環論的rank認識は証明を作成・点検した。** `papers/dp1_anticanonical_models.tex` §6（実体 `papers/sections/elliptic_rank_filtration.tex`）で、右noetherianな連結局所有限次数付きR、中心正則g∈R₁、R/g=B(E,L,σ)、Eが整な射影Gorenstein種数1曲線、deg L=d>0を仮定する。このとき全加群のHilbert関数は最終的に二次以下、Gabriel–Krull filtrationはHilbert多項式の次数filtrationと一致し、πRはrank oneでtorsion-freeとなる。rankは二次係数の2/d倍である。σの位数、AS-regular被覆、導来比較、有限homological dimensionを仮定しない。整なnodal/cuspidal境界にも適用できる。独立の新規性は未確認。

**条件付き帰結。** smooth genuine S / smooth Eの既存Rains環の入力が成立すれば上のrank定理を適用できる。さらに既存の全q導来比較を入力すれば次数1の全内在的公理が成立し、χ(e,τⁿX)=m+n(H·α)+dr n(n+1)/2から内在的rankと数値rankが一致する。既存導来比較の独立全面監査を今回完了したという意味ではない。

**保持する既存成果。** `papers/nc_del_pezzo_degree1_moduli.tex` の普遍点dg gluing、HH²=10・HH³=0・KS同型、有限directed A∞ chartの成分性、抽象公理からのrankの帰結、条件付きweighted sextic認識を保持する。全Morita変形、相対heart、全intrinsic abelian moduliの成分性は未完成。

## III. 現在の核心と優先順

1. **導来比較の入力監査。** `dp1_anticanonical_models.tex` の `prop:ring-orbit`、`lem:finiteness`、`thm:null`、`lem:trace`、`prop:ess` をRains・YZ・Orlovの一次資料と照合する。環論的rank定理をこれらの未完監査に巻き込まない。
2. **相対heartと局所モジュライ。** 幾何点ごとのrank認識を、flat graded ring族、qgrの基底変更、指定構造対象とSerre作用、同型groupoid・fpqc降下へ進める。Artin基底上の総圏の絶対Gabriel–Krull長さを相対rankと混同しない。研究ノートの二重数上の自明族の例から着手する。
3. **有限A∞とMorita変形。** 補助例外コレクションの持上げ、相対transfer、曲率、inner stabilizerを処理し、10次元族の形式局所普遍性を目指す。有限chart成分性をintrinsic成分性と同一視しない。
4. **特異境界。** rank認識は整なnodal/cuspidal境界へ拡張済みだが、その環の構成、boundary trace、導来比較、非局所自由gluing、相対compactified Jacobianは未完成。
5. **認識と分類。** 一般内在的公理から中心元・種数1境界・AS被覆が出ること、weak境界の(-2)曲線と特異性、標識忘却を調べる。先行する局所成果の公表を完全分類待ちにしない。

方針変更の理由：滑らかな楕円領域のrank-one/torsion-free性を独立の認識課題として残す必要はなくなった。元の目標であるintrinsic moduliへの接続は、相対化・同型群oid・導来比較の監査へ絞られた。一般の境界存在や全分類は解決していない。

## IV. 再開・原稿・再現

本書 → `research/dp1_research_plan.md` → `research/dp1_research_notes.md` → 二つの現行TeX → `research/dp1_validation.md` / `research/dp1_reproduction.md` の順に読む。rank認識の現行証明は反標準モデル論文§6が正本。主稿の楕円qgr-rankを未解決としていた記述の横断的な参照整理は残っており、そこを現行の未解決課題と解釈しない。主稿の一般公理からの境界認識は引き続き未解決である。

リポジトリrootで `latexmk papers/dp1_anticanonical_models.tex`。主稿は `latexmk papers/nc_del_pezzo_degree1_moduli.tex`。検算は `python scripts/check_elliptic_rank.py`（SymPy 1.14.0）。検算は多項式恒等式と参照閉包を確認し、圏論的証明や既存導来比較の正しさを保証するものではない。一般次数の共鳴・heart比較は `https://github.com/uedakazushi/nc-cubic-moduli` を外部正本とし、仮定と参照版を確認せず入力しない。
