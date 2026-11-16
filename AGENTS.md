# Codex研究指示：次数1の非可換del Pezzoモジュライ

2026-11-16 / dp1-codex-v2。GitHub mainを研究の正本とする。**最初に `00_research_plan.md` と `research/dp1_research_plan.md` を読む。** 次に `research/dp1_research_notes.md`、2本の現行TeX、検証・再現資料を読み、現状の証明済み・仮定付き・未完成・計算観察・新規性未確認を区別する。

最優先原則は研究価値の最大化。既知のRains・Okawa--Ueda・Etingof--Ginzburgの構成を繰り返すだけではなく、intrinsic abelian moduli、局所Morita変形、heartの認識、退化の幾何を比較する。完全分類は長期目標とし、独立に公表できるP1--P3の成果を先に完成させる。

優先手順：
1. P0: `thm:universal-gluing`, `thm:gluing-hh-ks`, `thm:finite-chart-component` と反標準導来比較 `thm:main` の仮定、bar/trace、相対A∞ transfer、先行一次資料を監査し、ギャップ・既知性を明記。Rains arXiv:2504.16187 §16.4を特に確認。
2. P1: finite directed chartと、framed/rigidified pointed Morita変形を比較。HH²=10・HH³=0・KS同型だけでglobal intrinsic成分性を宣言しない。自己同型/Bertini・coarse vs stackを扱う。
3. P2: `qgr R_q` のGabriel--Krull rank-one/torsion-free性、AZ-ample heart、original Rains heartとの差、標識忘却groupoidを証明。
4. P3: 特異反標準曲線と非局所自由gluing、相対compactified Jacobianを検討。
5. P4/P5: 中心元／ASregular被覆の自動認識、weak境界。最初の成果の公表を遅らせない。

**守る区別**：numerical ampleness vs AZ ampleness、dg derived equivalence vs abelian equivalence、finite chart component vs intrinsic moduli component、Kuranishi stack vs coarse moduli、原稿中の証明 vs 今回の独立検証。誤りは依存する原稿・要約にも直ちに反映。一般次数のheart/resonanceは `nc-cubic-moduli` の現行正本を参照し、本repoに重複資産を増やさない。

原稿は日本語LuaLaTeX。重要な研究の区切り・目安15分のcheckpointで、現行方針・ノート・公表原稿・検証状態を整合させ、適切な組版と計算を検証する。過去の原稿や証明を消すことによる形式上の軽量化は行わない。PDF、ZIP、LaTeX中間物、変更履歴、古いbundleを追跡しない。

mainに直接通常のfast-forward pushし、**生成・検証・commit・push・remote SHA確認**を区別する。PR、GitHub Actions、force pushはしない。競合時はremoteを読み直して統合する。GitHubが正本で、Libraryはpush失敗時の緊急避難。自動の背景作業は約束しない。
