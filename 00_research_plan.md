# 研究方針：次数1の非可換del Pezzo曲面

2026-11-16 / dp1-plan-v2。再開時にはこのファイルを最初に読む。GitHub main を現行の研究正本とする。

## I. 恒常的な研究原則と保存許可
数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究目標と方針を柔軟に変更する。重要な変更では理由、解決済みの事項と残された元の問題を現行方針に簡潔に整理するが、変更履歴を蓄積しない。証明済み、追加仮定に依存、未完成、予想、計算的観察を明確に区別する。仮定、既知入力、証明の所在、未解決箇所を明示し、原稿に証明があること・今回の検証・計算・外部査読を混同しない。誤りは依存する主張と要約にも反映し、有用な障害・反例は現行ノートに保持する。

公表論文では先行研究の一次資料を調べ、既知結果の仮定と本研究の貢献をIntroductionで具体的に比較する。未確認の文献内容や書誌を推測で補わない。日本語LuaLaTeX原稿を標準とし、現在の数学的成果の論理順で構成し、過去の有効な結果や完全な証明を軽量化のために削除しない。研究ノートは現在有効な知識、例、障害、計算と文献比較を保存し、研究日誌、重複する証明、履歴、旧ZIPを含めない。

研究継続用bundleは現行の方針、ノート、公表用論文、最小限のソース、PDF、書誌、計算コード、入力、証明書、再現手順による自己完結した一式とする。研究区切りごとのユーザー承諾不要なLibrary保存が一般的に許可されている。ただし本研究の個別指示ではGitHub mainを正本とし、GitHub保存が成功した場合はLibraryに重複保存せず、GitHub保存失敗時のみ緊急避難に用いる。既存のLibrary資料は指示なく削除しない。ZIP、旧版、変更履歴、PDF/TeX中間生成物、キャッシュをGitで追跡せず、数学的内容と再現性を損なわずに整理する。生成・検証・commit・push・リモート到達確認を別の状態として扱う。

mainに通常のfast-forwardで直接pushし、remote SHAを確認する。GitHub Actions、PR、force pushは使用しない。他者の並行更新を失わず、競合時は取得して内容を統合する。背景処理の自動実行は約束しない。

## II. 本研究固有の中心目標と達成基準
次数1の非可換del Pezzo曲面の**内在的モジュライ理論**を、既存の幾何的構成・graded algebra・導来変形と比較して確立する。数学的重要性、新規性、理解の深化、正確性、実現可能性、公表可能性を総合した研究価値の最大化を最優先とし、完全分類の達成のみを成功基準にはしない。特に `(S,p)` による10次元smooth proper dg族の局所変形を厳密に記述し、構造対象 `O` とheartを指定したintrinsic abelian moduliへの橋を作る。

必要な区別：①有限directed A∞表示の成分、②pointed Morita/dg圏の局所moduli、③abelian heartと構造対象を含むintrinsic moduli、④標識を忘れた完全分類。①から④への無条件の移行は禁止する。Rains/Okawa--Ueda/Etingof--Ginzburgの既知構成と新規な部分を分離する。局所定理・heart認識・境界の定理は完成次第独立に公表する。

## III. 現行の成果と確実性
- `papers/nc_del_pezzo_degree1_moduli.tex`：smooth genuine次数1 Sとpの相対dg gluing、古典基点、HH²=10・HH³=0・KS同型、有限directed A∞ chartの成分性を本文に証明として記載。全Morita変形やintrinsic abelian moduliの成分を確立したものではない。
- 同稿：Gabriel--Krull rank、Artin--Zhang再構成、中心正則gとASregular境界被覆を明示的に仮定したweighted sextic認識と中心性の十分条件。一般内在的対象からのgや被覆の存在は未証明。
- `papers/dp1_anticanonical_models.tex`：smooth genuine S・smooth E・q∈Pic⁰(E)に限定したRains gluingと反標準qgrの導来比較・hdim2（有限位数qも含む）を本文で主張し証明を記載。全退化境界は含まず、独立の全面監査と先行研究上の新規性確認は未完了。
- 今回の研究計画策定は既存原稿の読解と外部一次資料の探索であり、全証明の独立再監査・新たな組版・計算実行を意味しない。検証履歴の実態は `research/dp1_validation.md` を参照する。

## IV. 優先順位と具体的な着手
- **P0：証明と新規性の監査。** `thm:universal-gluing`、`thm:gluing-hh-ks`、`thm:finite-chart-component`、導来比較主定理を一次資料とともに照合。特にRainsの2025年論文 §16.4 の次数1反標準環との重複を調べる。
- **P1：局所形式モジュライ。** finite A∞とMorita変形の比較、gauge/inner stabilizerとBertini involution、generic finiteness、avatarの相対Poincaré正規化を検証し、10次元族の局所形式普遍性と適切な成分定理を目指す。
- **P2：intrinsic heart。** smooth elliptic Rains gluingからの `qgr R_q` についてGabriel--Krull rank-one/torsion-free性を示し、AZ-ampleness・元heartとの相違・弱標識忘却のgroupoidを確定する。
- **P3：特異境界。** `Bl_b(S)→P¹` の相対Picard/compactified Jacobianと普遍点族を自然変換の水準で比較。nodal/cuspidal Eと非局所自由sheaf、traceと導来比較の適用範囲を調べる。
- **P4/P5：高リスクの分類とコンパクト化。** 中心元・楕円境界・weighted ASregular被覆の自動性の検証、weak Sの(-2)壁でのorbit直交とsingularity判定。独立に公表可能なP1--P3をこれらの完成待ちにしない。

優先順位・到達条件・証明箇所・文献比較の詳細は `research/dp1_research_plan.md`。最初の実作業はP0のHH/KS・finite chart監査と、P2のrank-one/torsion-free補題の証明である。

## V. 再開・再現・保存
再開順：本書 → `research/dp1_research_plan.md` → `research/dp1_research_notes.md` → 2本のTeX原稿 → `research/dp1_validation.md`・`research/dp1_reproduction.md`。共鳴と一般次数のheart比較は `https://github.com/uedakazushi/nc-cubic-moduli` を正本として参照し、その最新版を仮定なしに使用しない。

`latexmk papers/nc_del_pezzo_degree1_moduli.tex`、`latexmk papers/dp1_anticanonical_models.tex` でLuaLaTeX再生成する。版ごとに原稿を重複保持せず、必要な内容・証明を現行の論文とノートに統合。GitHub mainへの保存を第一にし、既存の一般原則に従いpush成功時にはLibraryへの重複保存を行わず、push失敗時のみ緊急避難に用いる。GitHub Actions、PR、force pushは使わない。
