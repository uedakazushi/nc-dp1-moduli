# 次数1 nc del Pezzo：価値最大化型研究計画

2026-11-16 / dp1-strategy-v3。一般原則と保存許可は `00_research_plan.md`。以下は本研究固有の現行計画である。

## 1. 到達基準と論理的な段階

中心は、可換次数1 del Pezzoを含む10次元dg族を、構造対象とabelian heartを指定した内在的モジュライへ接続すること。重要性、新規性、正確性、理解の深化、実現可能性、公表可能性を総合し、全分類が未完成でも独立に価値のある定理を完成・公表する。

区別する段階は、(a) 実際のdg族とHH/KS、(b) 有限directed A∞表示、(c) pointed Morita変形、(d) 相対abelian heartを備えたintrinsic moduli、(e) 全射性・標識忘却・完全分類である。前段階の成分定理を後段階へ無条件に移さない。

## 2. 現行の主張と証明の所在

- **今回証明を構成・点検した環論的結果**：反標準モデル論文 `sec:elliptic-rank`。中心正則g∈R₁と整なGorenstein種数1 THCR境界を持つ右noetherian環について、Hilbert多項式、Gabriel–Krull filtration、構造対象のrank one/torsion-free性、rank=2/d×二次係数を証明。σの位数は問わず、nodal/cuspidal境界を含む。導来比較・AS被覆・有限hdimから独立。新規性未確認。
- **条件付きの新しい接続**：同稿 `cor:elliptic-intrinsic-heart` と `prop:elliptic-numerical-rank`。既存の環構成と導来比較を入力し、全内在的公理と数値rank一致を得る。上流入力の全独立監査は未完了。
- **既存本文に証明あり**：主稿 `thm:universal-gluing`、`thm:gluing-hh-ks`、`thm:finite-chart-component`。全点(S,p)のdg gluing、古典fiber、HH²=10、HH³=0、KS同型、有限presentation chartの成分性。全Morita/intrinsic成分性ではない。
- **条件付き既存結果**：主稿 `thm:weighted-hypersurface-recognition`、`cor:central-sextic`。中心g、ASregular境界被覆、低次数関係式、必要に応じ負次数導分消滅を仮定する。抽象公理からのこれらの存在は未証明。
- **既存導来比較**：反標準モデル論文 `thm:main` はsmooth genuine S / smooth E / 全qを扱う。証明は保持したが独立全面監査未完了。新しいrank定理によって自動的に検証済みとはならない。

## 3. P0：上流証明の監査と原稿の整合

最初にRainsの環構成、finite-order境界でのYZ入力、Indでのorbit生成、境界trace、pseudo-perfect moduleの表現可能性を照合する。対象となるラベルは反標準モデル論文の `prop:ring-orbit`, `lem:finiteness`, `thm:null`, `lem:trace`, `prop:ff`, `prop:ess`。各入力について左右のmodule規約、smoothness、genuine/weak、有限/無限位数、中心元の次数を明記する。

HH/KS側ではKuznetsovのresidual HH同定、混合bar cochain、相対transfer、finite chartのgaugeとstabilizerを監査する。単なるHH²の次元一致やHH³=0から任意のMorita変形への形式普遍性を結論しない。

主稿に残る「楕円qgrのrank認識が未解決」という記述は、反標準モデル論文§6への参照へ整理する必要がある。現行の数学的状態は本計画と同節の定理を優先し、証明を重複させない。既存の有効な証明・例・障害は削除しない。

達成基準：主要入力の仮定を一次資料で照合し、依存する結論と未監査箇所を分離した公表用本文を得ること。

## 4. P1：局所形式モジュライ

目標（未証明）：(S,p)族から、適切にframed/rigidifiedな例外対象付きsmooth proper dg圏の変形groupoidへの写像を構成し、形式局所同値または局所étale性を証明する。

具体的な順序：変形functorを定義し、full exceptional collectionのExt²/Ext¹消滅から持上げを行い、derived Nakayamaでsemiorthogonality/fullnessを検査する。k¹¹相対normalized cochainsの非曲率directed A∞変形と全Morita変形の比較を閉じる。その後HH²でsmall extensionの持上げを調整する。HH¹=0でもinner stabilizerは残るのでraw [Z/G]を10次元DM stackと呼ばない。

基点bでのBertini involution（8方向自明・点方向の2次元に-1）とcoarse quotientを比較する。Poincaré bundleのbase twistを除き、avatar族と普遍点族の相対同値を構成する。幾何点で一致することと族の降下を区別する。

全Morita比較が難しい場合も、有限directed chartの成分定理を正確な独立成果として公表する。global stackの存在の問題で局所成果を停滞させない。

## 5. P2：fiberwise認識から相対heartへ

**解決した部分**：中心一次元と所定の種数1境界を持つ環のqgrでは、構造対象の内在的rank one/torsion-free性を追加仮定にする必要がない。既存導来比較の下では数値rankと一致する。

**未解決の核心**：幾何点ごとの公理から、相対flat abelian category、base change、fpqc降下、同型groupoidへの射を構成すること。

最初は有限Artin基底A、flat graded A代数R_A、相対中心元g_AとTHCR境界を指定した変形問題に限定する。各次数のflatness、有限生成・noetherian性、relative section functorと高次消滅の一様性を別々に検証する。主稿 `prop:formal-hilbert` は固定nごとの自由性を与えるが、全nの一様な開条件を与えない。

相対rankは各幾何fiberで定義する。S×Spec(k[ε]/ε²)の構造層は、総圏をk線形圏と見た絶対generic quotientで長さ2を持つ。このため総圏へ絶対rank-one公理をそのまま課す定義は自明変形を除外する。研究ノートのこの例を最初の整合性試験に使う。

Rains heartとanticanonical heartの一致、共鳴でのt-exactness、弱標識忘却は別々の問題である。ordered rulings・七例外曲線・W(E8)・Autによるgroupoidを、構造対象Oだけの標識と照合する。

## 6. P3：特異境界とcompactified Jacobian

Bl_b(S)→P¹の相対Picardをp↦O_D(b-p)で普遍点族と比較し、相対compactified Jacobianへの延長を目指す。b、smooth D上のp、nodal/cuspidal Dのsmooth点、特異点pを区別する。

環論的rank定理は整なnodal/cuspidal境界に適用できる。しかしN_p=i_*(I_{p,D}⊗O_D(H))が非局所自由になる点で、F_q(M)=Li*M⊗q^{-1}を流用できない。relative perfect module、boundary functor、trace、finite cohomological dimension、導来比較の順に検証する。曲線上のrank-one torsion-free sheafのモジュライを、心のモジュライと同一視しない。

## 7. P4/P5：境界認識・完全分類・weak境界

抽象(A,O,τ)のorbit環RからZ(R)₁≠0、種数1商、ASregular被覆を導くことは未解決。まず指定境界付きの部分functorで認識を完成し、仮定を弱める。Hilbert型(1,1,2,3)と最小生成元の重みを区別する。Rains 2025 §16.4・EGの既知提示を再発見しただけの結果を新定理としない。

weak Sの(-2)曲線によるO_C(-1)のorbit直交、自然導来切断の核、任意の導来同値の不存在、qgrのhomological singularityは別々に扱う。可換コンパクト化との比較はAscher–Bejleriを出発点とする。全分類を主要目標に格上げする条件は、局所変形・相対heart・groupoid・境界認識が接続されたことである。

## 8. 文献照合と公表単位

直接使用・比較する一次資料は、AOU arXiv:1411.7770 Appendix A、Artin–Van den Bergh J.Algebra133(1990)249–271 Theorems1.3–1.4、Keeler arXiv:math/9912051v2 Theorem1.2、Chirvasitu–Kanda–Smith DOI10.1017/fms.2020.60 Theorem2.4/Corollary2.8、RSS arXiv:1308.2216v2 Proposition2.4である。確認範囲は検証文書に記す。

構成・新規性比較はRains arXiv:1907.11301v1 Theorem4.30/§5、1607.08876v4 Propositions9.29/11.48/12.22、2107.13540v2 §2–6、2504.16187 §16.4、Okawa–Ueda arXiv:2508.04986 Definition6.1/Theorem6.4、Etingof–Ginzburg arXiv:0709.3593v4による。最後の2025年Rains文献は重点再照合対象であり、今回全証明を読了したとは扱わない。

変形比較にはKuznetsov arXiv:0904.4330、Orlov arXiv:1402.7364、Lowen arXiv:math/0407019、Keller–Lowen IMRN2009 3221–3235、Hille–Perling arXiv:1110.5843、Belmans–Okawa–Ricolfi arXiv:2002.03303を用いる。Toën–Vaquié DOI10.1016/j.ansens.2007.05.001は固定dg圏の対象のモジュライであり、変動するdg圏のglobal stackの存在と混同しない。

公表は主稿（普遍点・局所変形・内在的認識）と反標準モデル論文（導来比較・rank認識・共鳴）の二本を中心とする。weighted recognitionや退化境界は独立した中心定理が確立してから分割を判断する。新規性の確認前に完成した新分類と称さない。

## 9. 次の具体的な着手と再現

上流のRains環入力を監査し、Artin基底上のrelative qgrモデルの定義を二重数自明族で試験する。並行して主稿のrank未解決表示を現行定理へ統合する。検算は `python scripts/check_elliptic_rank.py`、組版はrootで `latexmk papers/dp1_anticanonical_models.tex`。ソースの依存閉包と検証範囲は `research/dp1_reproduction.md` / `research/dp1_validation.md` にある。
