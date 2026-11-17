# 研究方針：次数1の非可換del Pezzo曲面

2026-11-18 / dp1-plan-v4。再開時は本書を最初に読む。GitHub mainをソースの正本とし、現行の研究継続用bundleをLibraryに保存する。

## I. 一般原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究全体の価値を最大化する。目標は柔軟に変更し、重要な変更の理由と、元の問題について解決した部分・残る部分を現行方針として簡潔に整理する。変更履歴を蓄積しない。

証明済み、追加仮定に依存、未完成、予想、計算的観察を区別する。仮定、既知入力、証明の所在、未解決箇所を明記し、原稿中の証明、今回の検証、計算、外部査読・形式化を混同しない。誤りは依存する本文・要約・方針にも反映し、有用な反例・障害は現行ノートに保持する。

公表論文では一次文献の仮定・適用範囲と貢献をIntroductionで具体的に比較する。未確認の内容・書誌・新規性を推測しない。原稿は原則として日本語LuaLaTeX、成果を論理順に構成し、有効な過去の結果・十分な証明を削らない。研究ノートは有効な知識、着想、計算、例、障害、文献比較を整理し、日誌や証明の重複を蓄積しない。

研究の区切りには、方針・ノート・公表用原稿と必要最小限のソース、PDF、文献、計算資産、再現手順による自己完結したbundleを、ユーザーの追加承諾なしにLibraryへ保存することが許可されている。GitHub mainをソース正本として併用する。旧版ZIP、旧原稿、バックアップ、履歴、キャッシュ、組版中間物をbundleへ含めず、既存Libraryファイルは明示的指示なく削除しない。全体でなく一方向のbundleの場合は範囲を明記し、その方向はbundle単独で再開可能にする。

日付・版を付し、現行版だけを配布する。生成、証明点検、検算、組版、GitHub保存、リモート確認、Library保存を別状態として報告する。再生成に必要な依存を揃え、参照とZIP整合性を確認する。Gitはソースと不可欠な入力のみを追跡し、PDF/ZIP/生成物を追跡しない。mainに通常のfast-forwardで直接保存し、PR、Actions、force pushを使わない。並行変更を取得して統合し、背景作業を約束しない。

## II. 目標と現在の到達点

目標は、次数1の普遍点dg族、反標準環、指定構造対象を持つAbel圏の変形を比較し、内在的モジュライ成分を認識すること。完全分類だけを成功条件にせず、正確で独立した局所成果を先に完成させる。

1. **体上のrank認識。** 中心正則一次元と整なGorenstein種数1 THCR境界を持つ右noetherian環について、Gabriel–Krull filtrationとHilbert多項式次数が一致し、構造対象はrank one・torsion-free。完全証明は `papers/dp1_anticanonical_models.tex` §6。Artin原稿§2にも必要な証明を再掲し単独で読める。
2. **Artin基底への認識の持上げ。** `papers/dp1_artin_deformations.tex` §4–5で、特殊fiberのrank仮定(H)の下、次数ごとに平坦な環変形の総圏のGK filtrationとgeneric lengthを証明。A-flat Fには λ_A(F)=length(A) rank(F_k)。flat tail判定、torsion-freenessの持上げ、任意の局所Artin基底変更を扱う。中心元の持上げを仮定しない。今回本文の証明を点検したが新規性は未確定。
3. **dg変形から外部の平坦Abel変形。** 同稿§6。実際のproper dg変形、構造対象の持上げ、相対SerreとRHomの基底変更を入力し、平坦な反標準環を構成する。De Deken–Lowen Proposition4.4の適用によりqgrの平坦Abel変形を得る。これは元のdg圏のheartの構成や全変形問題の同値ではない。
4. **保持する既存資産。** 普遍点N_p、HH²=10・HH³=0・KS同型、有限directed A∞ chart、条件付きweighted sexticは主稿に保持する。smooth elliptic全q導来比較も既存証明を保持するが、独立全面監査は未完了。今回これらを再検証済みとはしない。

## III. 重要な定式化と未解決の核心

非正則Artin基底では、比較先を全Db(qgr R_A)とすることは自明族でも不適切である。A=k[ε]/ε²上の自明族ではPerf(S_A)≠Db(coh S_A)、標準t構造もPerfへ制限されない。したがって次の目標は、元のproper dg圏と **基底上有限Tor振幅の部分 Db_{A-perf}(qgr R_A)** の比較であり、必要なheartは大きな導来圏側で考える。証明と具体例はArtin原稿§8。

反標準軌道にはExt²(τ^{i+1}e,τ^ie)=kがあるため、これをexceptional helixと扱わない。De Deken–Lowen Theorem4.5のZ-代数比較は使えるが、Theorem5.15の有限thread比較には別の仮定が必要。Z-代数変形から通常の次数付き環へ戻すcoherentな周期性も別問題である。

この修正は体上の既存定理を否定するものではなく、相対比較の目標を正すものである。元の目標のうち、各fiberと平坦Artin族のrank認識および外部Abel変形の構成が進み、内部実現・同型groupoid・成分性が残った。

## IV. 次の優先課題

**P0：相対perfect比較。** Artin原稿Lemma8.2を出口にして、導来切断関手と右随伴を構成し、有限A-Tor振幅、properness、単位・余単位の基底変更を確認する。元圏と全Dbの同値を目指さない。まず古典特殊fiber、指定e/Serreの変形に限定する。

**P1：変形groupoidと周期性。** 構成した外部Abel変形と全Morita変形の関係、e・Serreの持上げ、Z-代数のcoherent shift、full exceptional collectionとの比較を処理する。HHの次元だけで全形式普遍性や成分性を結論しない。

**P2：既存入力の監査。** Rains環構成、全q導来比較のInd生成・trace・有限位数のYZ入力、有限A∞ chartの変形比較を一次資料と照合する。一般のintrinsic公理から中心境界が生じること、特異境界での導来比較、非局所自由gluing、weak壁、標識忘却は独立課題として保持する。

## V. 再開・原稿・保存範囲

本書 → `research/artin_deformation_notes.md` → `papers/dp1_artin_deformations.tex` → `research/dp1_validation.md` / `research/dp1_reproduction.md`。他方向の詳細はGitHubの `research/dp1_research_plan.md` と `research/dp1_research_notes.md`、既存二原稿を読む。長い主稿に残る特殊楕円qgr-rankの未解決表示の横断修正は今回未実施で、現行の解決範囲は上記定理を優先する。

Artin原稿は既存結果の応用と証明済みの補題を整理する研究用companionであり、第三の独立投稿論文とするか既存二稿へ統合するかは新規性と論理的まとまりの監査後に判断する。

今回のLibrary bundleは **Artin変形方向の自己完結した一式** であり、リポジトリ全体の複製ではない。原稿は必要な体上のrank証明も含む。既存二稿と全研究資産はGitHub上に削除せず保持する。
