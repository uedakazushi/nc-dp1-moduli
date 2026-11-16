# 次数1の非可換del Pezzo曲面：価値最大化型研究計画

2026-11-16 / dp1-strategy-v2。再開時は `00_research_plan.md` を最初に読む。本書は本研究固有の現行戦略であり、一般原則・保存許可は同ファイルに置く。GitHub mainが現行正本。対象は次数1に限定し、一般次数のRains共鳴・heart比較は `nc-cubic-moduli` を正本として参照する。

## 1. 何を最優先で最大化するか

個別の既存構成の再実行でも、無条件の完全分類という最難問への固執でもなく、**重要性・新規性・証明の確実性・研究効率・公表可能性を総合した研究全体の価値**を最大化する。中心は、可換次数1 del Pezzo曲面を含む10次元のdg構成を、heartと構造対象を備えた内在的な非可換del Pezzo曲面のモジュライへ結び付けること。すでに得られた独立結果は完全分類の完成を待たず、適切な論文として完成・公表する。

本研究では三段階を厳密に区別する：
1. `(S,p)` の実際のsmooth proper dg族、HH・KS・有限directed表示での成分性。
2. 指定されたabelian heart、`O`、Serre作用、AZ-ampleness、Gabriel--Krull rankに関する **intrinsic abelian moduli** への射。
3. その射の成分性／全射性／分類（標識忘却・自己同型を含む）。
第1段階から第2・3段階へは自動では移らない。全Morita変形を有限非曲率A-infinity chartと同一視する際も比較証明が要る。

成功条件は優先順に (A) 局所形式モジュライ定理と明示的な同型groupoid、(B) 楕円領域のintrinsic heartの成立・認識、(C) 境界退化への自然な延長、(D) 条件を弱めた反標準環認識、(E) 適切に定式化した全分類。高リスクな(E)のために(A)--(D)の公表を停滞させない。

## 2. 現在の数学的資産と主張の状態

- **本文に証明あり・今回の全独立監査なし**：`papers/nc_del_pezzo_degree1_moduli.tex` の `thm:universal-gluing`、`thm:gluing-hh-ks`、`thm:finite-chart-component`。smooth genuine Sの全pに対し `N_p=L_{O_S}(I_p(-K_S))` を用いるsmooth proper dg族、基点bでの古典fiber、HH²=10、HH³=0、KS同型、有限型directed A-infinity presentation chart内の既約成分を扱う。**全pointed Morita変形**や**全intrinsic abelian stack**の成分性は未証明。
- **本文に証明あり・追加仮定に依存**：同稿のGabriel--Krull rankと成長、Serre-heartからのhomological dimension=2、中心正則一次切断とASregular境界被覆を仮定するweighted sextic認識・中心性判定。一般の内在的公理から中心元、境界、被覆が現れることは未証明。
- **本文に証明あり・独立再監査が必要**：`papers/dp1_anticanonical_models.tex` のsmooth genuine S / smooth E / q∈Pic⁰(E)のRains型gluingについて、Serre orbit生成と `T_q ≃ Db(qgr R_q)`、hdim qgr=2（有限位数qを含む）。Rainsの既知入力、traceと有限性の組合せ、全qを含む主張の新規性は個別監査が必要。numerical resonance、AZ-ampleness、t-exactness、derived equivalenceを混同しない。
- **未完成**：qgr heartのintrinsic rank-one/torsion-free判定、非曲率chartと全Morita変形の同定、有限presentation quotientとintrinsic groupoidの比較、nodal/cuspidal E、特異点での非局所自由gluing、weak del Pezzoの(-2)壁。
- **原稿内での既知入力**：Rains構成・Hilb¹、Artin--Zhang再構成、Kuznetsov HH、Orlov gluing等。本文に証明があることと今回の検証済み状態は別。現行確認記録は `research/dp1_validation.md`。

## 3. 先行研究：新規性の境界

最優先の一次資料照合対象：
- Okawa--Ueda, *Marked Artin--Schelter surfaces of del Pezzo types*, arXiv:2508.04986, Def. 1.1, Thm. 6.4：strong helix標識付きAS型の楕円データへの双有理対応。Oだけを標識したintrinsic moduliとは異なる。
- Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301, Thm. 4.30、§5：gluing、次数1の点とPicard、一次変形の先行背景。
- Rains, *The noncommutative geometry of elliptic difference equations*, arXiv:1607.08876：smooth proper surface、Hilb¹、abelian equivalence；適用時q≠1と構造対象保存を点検。
- Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540, §2--3, 5--6：filtered変形と次数1 weighted family。既知の環提示と本稿の逆向き認識を峻別。
- **Rains, *The (noncommutative) geometry of difference equations*, arXiv:2504.16187, §16.4, Lemma 16.12：次数1の反標準環の生成元・関係式に関する具体的な先行結果。生成元・weighted sextic表示の単なる再発見を新定理としない。§12等の非可換surface/同型問題も逐次照合。**
- Etingof--Ginzburg, *Noncommutative del Pezzo surfaces and Calabi--Yau algebras*, JEMS 12 (2010), 1371--1416, DOI:10.4171/JEMS/235：E8変形・quantizationの既知範囲。
- Ascher--Bejleri, *Compact moduli of degree one del Pezzo surfaces*, Math. Ann. 384 (2022), 881--911, DOI:10.1007/s00208-021-02279-3、および *Moduli of double covers and degree one del Pezzo surfaces*, Eur. J. Math. 7 (2021), 557--569：可換境界コンパクト化との比較。
- Toën--Vaquié, *Moduli of objects in dg-categories*, Ann. Sci. Éc. Norm. Supér. 40 (2007), 387--444, DOI:10.1016/j.ansens.2007.05.001：**固定されたdg圏の対象のmoduli**の定理なので、変化するdg圏そのもののmoduli stackの存在を無条件に与えるものとして流用しない。

一次資料の全証明を今回読了したという意味ではなく、参照箇所の厳密な適用審査はP0の作業とする。個別結果の既知性と本研究の独立新規性は、定理ごとに確認する。

## 4. 直近のP0：論文に直結する証明監査（最高優先）

(A) `thm:universal-gluing`：普遍対角イデアルによる相対perfectness、bでのderived evaluation、pが特異点でも意味を持つmutated ideal、Orlov gluingのsmooth/properの相対性。
(B) `thm:gluing-hh-ks`：`HH*(B_S)`のKuznetsov同定、bar triangle、接写像の自然性、baseの10方向と `HH²` の一致。HH³=0だけで任意のMorita変形の非障害性を結論しない。
(C) `lem:relative-directed-model` と `thm:finite-chart-component`：相対split contraction、strict unitと有限性、曲率、`G`のstabilizer、`Z`のobstruction、family→chartのbase change。有限chartの成分とintrinsic quotientを分離。
(D) `dp1_anticanonical_models.tex`：Rains入力の全仮定（特にtorsion q/finite order）、Indでのorbit生成、trace、target有限性、pseudo-perfect表現可能性、essential surjectivity。
(E) `thm:weighted-hypersurface-recognition`：weighted正則性判定、normality、低次数持ち上げ、Rains §16.4との重複・追加分の同定。
各監査結果は「証明に書かれている／今回確認した／未検証／文献で既知／新規性未確定」を `research/dp1_validation.md` に反映する。反例があれば依存主張と要約も同時に訂正。

## 5. P1：普遍点族を局所形式モジュライにする

**目標定理（未証明）**：smooth degree1 Sとpの族 `U`（次元10）から、適切にrigidifyしたexceptional object付きsmooth proper dg categoryの形式変形関手または有限型atlasへの写像を作り、形式局所同値（自己同型groupoidを含む）または十分な局所étale性を証明する。全Morita deformationとの比較が難しければ、**有限directed presentation**の実際の既約成分性を独立した公表定理として完成させる。

着手：
1. 変形対象を「dg category + e + enhancement + 必要なら相対full exceptional collection」のどのgroupoidにするか定義し、framed/rigidified版とunframed版を分ける。
2. `(S,p)`相対gluingから有限A∞表示への比較を構成し、`HH²`接空間、`HH³`障害、`HH¹`とinner stabilizerの関係を明示。curved/Moritaとの差の補題を証明。
3. 古典基点bの局所模型、Bertini involutionの作用（8方向自明、点の2方向-1）、coarseとstackの差を検証。coarse tangentをHH²と同一視しない。
4. avatar `(S,D,P)`との相対Poincaré正規化とidentity section収縮のcompatibilityを確認。点ごとの同型を族の同型と取り違えない。

**判断基準**：global stackの構成に固執せず、厳密な形式局所定理と有限chart成分定理が独立に成立すれば第一論文を完成。全Morita比較に根本障害があれば対象functorを明示的に狭めて論文を成立させる。

## 6. P2：反標準heartのintrinsic性（P1と並走する短い橋）

**目標定理（未証明）**：smooth genuine S / smooth E / qに対応する `A_q=qgr R_q` の `pi R_q` が、Gabriel--Krull rank one、torsion-free、Hilbert関数、Serre/shift、AZ-amplenessを全て満たすこと。次に同じdg category上のRains heartと反標準qgr heartの関係、qのresonanceごとのt-exactness/heart wallを判定する。

着手：graded domain Rのgeneric quotient、rank filtration、`pi R`へのtorsion map消滅を検証。現在の `sec:intrinsic-rank` は **条件を仮定した場合**の結果であり、その条件を `qgr R_q` が満たすことを新たに証明する。Rainsのnumerical resonanceではm≷0の導来切断のcohomologyに注意し、derived equivalenceからheart一致を推論しない。weak markingがOのみであることを保ち、ordered rulings/7 exceptional curvesのforgetful groupoid（W(E8)・Autを含む）のgeneric degree/fiberを正確に記述する。

**判断基準**：反標準heartが内在的定義を満たすこと、あるいはそれが失敗する明確な反例が得られることのいずれも高価値。global分類を待たず論文化可能な形でまとめる。

## 7. P3：nodal/cuspidal境界と非局所自由gluing

`Bl_b(S)→P¹` のsmooth locusの相対Picardを普遍点族 `p↦O_D(b-p)` で記述し、相対compactified Jacobianに延長する。以下を混同しない：p=b、smooth D上のp、nodal/cuspidal Dの滑らかなp、Dの特異点p。
- Dの特異点では `N_p=i_*(I_{p,D}⊗O_D(H))` がrank-one torsion-freeで非局所自由になり、滑らかなline bundleのrestriction式を流用できない。
- まずrelative perfect moduleで `N_p` と`(S,p)`の族が与えるgroupoidを確認。次にsingular THCR・中心元・Serre trace・cohomological dimensionを場合分けして比較する。
- 境界への延長を明示した定理が得られれば第二論文。単純なsingular ringの計算に終始せずモジュライの退化の幾何を主張できる形へまとめる。

## 8. P4/P5：高リスクだが大きな成果につながる方向

P4: 抽象 `(A,O,tau)` のRから `Z(R)_1≠0` の自然な中心正則境界、種数1境界の幾何性、ASregular weighted coverの存在を導く。最初はopen subfunctorの条件付き認識を目標とし、arbitrary intrinsic objectへの無条件拡張は後回し。Hilbert型(1,1,2,3)と**最小生成元の重み**を区別し、Rains 2025 Lemma16.12/EGに対する真正の追加結果を抽出する。中心性に負次数導分消滅を用いる場合も条件を明示。

P5: weak Sの(-2)曲線での `O_C(-1)` のorbit直交、qgrのhomological singularityとderived非同値を分離して判定。可換dP1のAscher--Bejleri compactificationと整合する非可換境界のモデルを探る。非零orbit直交だけから「任意の導来同値が不存在」としない。

完全分類は、P1・P2で局所変形・heart・groupoidが成立し、P3・P4で適切な境界認識が得られた場合に主要目標へ格上げする。期待値が低ければ既に証明された成果の公表を優先する。

## 9. 公表単位・継続・再現

第一候補論文：`papers/nc_del_pezzo_degree1_moduli.tex` を**局所変形・intrinsic heartへの接続**を核として整理。第二候補：`papers/dp1_anticanonical_models.tex` を**滑らかな楕円領域の反標準導来比較**の独立論文としてP0監査後に完成。weighted recognitionを独立の中心定理にできる場合のみ別論文化し、既存の有効な証明は削除せず適切な現行論文に保持する。退化境界は成果が確立してから独立論文を検討。

再開順：`00_research_plan.md` → 本書 → `research/dp1_research_notes.md` → 2本の現行TeX → `research/dp1_validation.md` と `research/dp1_reproduction.md`。日本語LuaLaTeX。Gitはソースのみ、PDF・ZIP・過去版・ビルド生成物は追跡しない。各主要証明の根拠と未解決は現行ノート・原稿へ統合し、版を積み重ねない。作業区切りにテスト、commit、push、リモート検証を区別する。GitHub Actions、PR、force pushは用いない。

**次の具体的な一手**：`qgr R_q` のGabriel--Krull rank-one/torsion-free性の証明に着手しつつ、`thm:gluing-hh-ks` と `thm:finite-chart-component` の変形比較を独立に監査する。いずれも現在の中心目標へ直結し、短い公表可能な定理へ切り出せる。
