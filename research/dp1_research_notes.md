# 次数1 nc del Pezzo：現行研究ノート

2026-11-16 / notes-v5.0。再開は `00_research_plan.md` → `research/dp1_research_plan.md`。本書は現在有効な知識・障害・文献比較を整理し、証明全文は論文に置く。以下、Mは `papers/nc_del_pezzo_degree1_moduli.tex`、Rは `papers/dp1_anticanonical_models.tex` を指す。

## 1. 主張の確実性と現在の焦点

R§6（ソース `papers/sections/elliptic_rank_filtration.tex`）のHilbert多項式、Gabriel–Krull filtration、構造対象のrank one/torsion-free性は、本作業で証明を構成・点検した。中心正則一次元と整なGorenstein種数1 THCR境界を仮定する。有限位数σ、整なnodal/cuspidal境界も含む。導来比較やAS被覆に依存しない。独立の新規性は未確定。

Rの `cor:elliptic-intrinsic-heart` と `prop:elliptic-numerical-rank` は、既存Rains環の入力および既存導来比較を明示的に用いる帰結である。この条件を忘れない。全q導来比較、Mの普遍点gluing、HH/KS、有限A∞ chart、weighted認識には既存の証明があるが、今回それら全ての独立全面監査を完了していない。

幾何点ごとのqgr-rank認識は所定の境界を持つ範囲で解決した。残る核心は相対heart・基底変更・降下、pointed Morita変形とintrinsic moduliの比較、一般公理からの中心境界認識である。Mに残る特殊楕円qgr-rankの未解決表示はR§6で解消された範囲を反映していないため、参照整理が必要である。

## 2. 中心一次元からのrank認識

仮定はRが連結局所有限右noetherian、g∈R₁が中心正則、R/g=B(E,L,σ)、Eが整な射影Gorenstein曲線でp_a(E)=1、deg L=d>0。Rの次数1生成、ASregular被覆、有限hdim、導来同値を仮定しない。

証明の要点はR: `lem:elliptic-hilbert-polynomial`, `thm:elliptic-filtration`, `thm:elliptic-rank`。

有限生成MについてT=Ann_M(g)、V=M/Mgとすると、T,Vは有限生成B加群であり

    0 → T(-1) → M(-1) --g→ M → V → 0,
    h_M(n)-h_M(n-1)=h_V(n)-h_T(n-1).

B加群のtailはcoh(E)のtwisted sectionsであり、RRから最終的に一次以下。差分を積分するとp_Mは二次以下となる。Tの項を落とさない。Tはgで一回殺される部分であり、全g冪torsionとの混同も避ける。gの次数が1であることは、準多項式ではなく通常の多項式を得る議論に使う。

C=qgr R、D_i={deg p≤i}とする。D_0の正整数定数値、D_1/D_0の正整数一次係数が部分対象列の長さを抑える。逆に単純対象には中心gによるF(-1)→Fが零か同型。零なら境界のcoherent sheafへ、同型なら差分零へ帰着する。商C/D_0でも同じ二分法を使い、C_0=D_0、C_1=D_1を得る。

非零右イデアルIには非零斉次aによるaR≅R(-s)が含まれる。R/Iの増大度は一次以下で、I自身は二次増大度。したがってπRはC_1-torsion-freeかつC/C_1で単純。中心gで全shiftが同型になり、有限生成性からgeneric quotientは一つの単純対象の有限直和で尽くされる。rank=length_{C/C_1}=2/d×p_Fの二次係数。これは仮定としてのrank oneから始めるMの一般論とは逆方向の認識である。

境界の滑らかさはこの議論に不要。整なGorenstein p_a=1曲線はω_E≅O_Eなのでh⁰(L_n)=nd (n>0)。可約・非被約の場合、Bの整域性と単一generic simpleが崩れ得るため、本定理には含めない。

有限長対象のHilbert定数を組成長と同一視しない。境界外の有限次元単純表現では定数値が1より大きくなり得る。

## 3. 数値rank・Euler多項式・相対化の注意

Rains gluingの境界triangleとrestrictionを入力し、r=rank[X]、α=c₁[X]、m=χ(e,X)、H=-K_S、H²=dとすると

    χ(e,τⁿX)-χ(e,τⁿ⁻¹X)=χ(E,ΨⁿF_qX)=H·α+ndr,
    χ(e,τⁿX)=m+n(H·α)+dr n(n+1)/2.

後者は全整数nで成立する。導来比較Φがeとshiftを保つ場合、ΦX=Fがqgr heart内なら高次Serre消滅でp_Fと比較でき、intrinsic rank(F)=rとなる。一般のXではΣ(-1)^i rank_intr H^i(ΦX)=r。これは元のRains heartに関するt-exactnessを意味しない。証明はR: `prop:elliptic-numerical-rank`。

### Artin基底で絶対rankを流用してはいけない

滑らかな整射影曲面S、A=k[ε]/(ε²)、自明族S_A=S×Spec Aを考える。総圏coh(S_A)のgeneric quotientは有限長k(S)[ε]/(ε²)-加群の圏である。構造層のgeneric stalkには

    0 ⊂ ε k(S)[ε]/(ε²) ⊂ k(S)[ε]/(ε²)

という長さ2の組成列があり、絶対Gabriel–Krull rankは2となる。一方、唯一の幾何fiberの構造層はrank1である。従って相対moduliの定義では基底線形性とfiberwise rankを使い、総圏の絶対rank-one条件をそのまま課さない。一般の長さℓのArtin基底の自明族でもgeneric lengthはℓとなる。この例は相対定義の整合性試験であり、新しい分類結果ではない。

相対R_Aからqgr R_Aを作る場合は各graded pieceのflatness、noetherian性、sectionの基底変更、高次消滅の一様性、同型groupoidを個別に検証する。幾何fiberの公理だけからfpqc降下は出ない。

## 4. 普遍点によるgluingの規約

k=C、Sはsmooth genuine degree1 del Pezzo、H=-K_S、bは反標準pencilの唯一の単純基点。B_S=O_S^⊥={M:RΓM=0}、半直交分解はPerf(S)=〈B_S,O_S〉でHom(right,left)=0。L=L_Oは包含B_S→Perf(S)の左随伴。

I_p∈B_S、N_p=L(I_p(H))=S_B^{-1}(I_p)[2]。gluingはRHom(e,M)=0、RHom(M,e)=RHom_B(M,N_p)。右射影r_B(O_S)=Cone(O_S→O_S(K_S)[2])[-1]。基点のKoszul列

    0 → O_S(K_S) → O_S² → I_b(H) → 0

からN_b=r_B(O_S)。ここでh⁰(I_bH)=2、h¹(I_bH)=1なので、mutationはH⁰だけでなくderived evaluationを使う。N_bの通常のcohomologyはH^{-1}=O_S(K_S)、H⁰=O_S。underived evaluationでは誤ってO_S(K_S)[1]となる。

相対構成はS×Sの対角イデアルI_ΔとF=I_Δ⊗p₁*O(H)から

    N = Cone(p₂* Rp₂*F → F)

を作る。perfect complexesの族であり、基点近傍のflat sheaf族とは限らない。p≠bで唯一のD∈|H|を用いるとN_p=i_*(I_{p,D}⊗O_D(H))。pがDのsmooth点ならO_D(H)=O_D(b)よりN_p=i_*O_D(b-p)。DがintegralなのはH ample・H·D=1から従う。特異点pではrank-one torsion-freeだが非局所自由となり、qをline bundleに限るavatarの外に出る。

Ext(N_p,N_p)はSerre自己同値でI_pへ戻し、Ext⁰=k、Ext¹=T_pS、他は0。これは複体のcanonical splittingやdg代数の分解を主張しない。Kuznetsovのgluing functor規約ではdual/oppositeが入るため、表現可能module h_N=RHom_B(-,N)の規約と混同しない。詳細はM: `thm:universal-gluing`。

## 5. HH・KS・有限A∞ chartと残るMorita比較

Kuznetsov Theorem8.5のresidual cochainsはRΓ(O_S⊕T_S[-1])。degree1ではH⁰(T_S)=H²(T_S)=0、h¹(T_S)=8。八点blowupの接束列でも確認できる。HH⁰(B_S)=k、HH²(B_S)=k⁸、他は0。

triangular gluingのHochschild triangleは

    C(T_{S,p}) → C(B_S)⊕k → RHom_B(N_p,N_p) →,
    0 → T_pS → HH²(T_{S,p}) → H¹(T_S) → 0.

次数0の写像(a,c)↦(a-c)id_Nが全射なのでHH¹(T)=0、HH²次元10、HH^{≥3}=0。KS同型には混合bar cochainのconnecting mapがgluing moduleの変形であることと、HKR projectionの自然性を使う。曲面のbaseは余剰framing方向のない8次元étale/miniversal atlasとする。

M: `lem:relative-directed-model`, `prop:finite-directed-chart`, `thm:finite-chart-component` では長さ11の相対full exceptional collectionを補助的に使う。単位以外のcomposable stringの長さは10以下なのでm_n,f_nもn≤10のみ。固定graded space上でm₁を変数に含め、相対Homのcohomology跳躍を許す。各Homの有限自由complexから基点でcontractibleな因子を消去し、可換環上のsplit contractionに沿うtransferを使う。体上のminimal-model定理だけで代替しない。

対角Hom²=0なのでこのdirectedモデルのm₀はない。relative normalized cochainsが接・障害を与え、HH³=0ならZは当該点でsmooth。KS同型とgauge方向からG×U→Zの微分が全射、縮小後smooth、像が開、その閉包が一つの既約成分となる。10はgauge orbitを除いた接次元であってZやraw quotient [Z/G]の次元ではない。HH¹=0でもinner stabilizerは残る。

全Morita変形への比較は未完成。exceptional objectsをExt²/Ext¹で持ち上げ、perfect Homとderived Nakayamaでsemiorthogonality/fullnessを保持し、k¹¹相対の非曲率モデルとMorita groupoidを比較した後にHH²によるsmall-extension帰納を行う必要がある。Keller–Lowenのcurvatureの注意を無視しない。Belmans–Okawa–RicolfiのSOD定理はsmooth proper geometric familyであり任意dg変形への無条件適用ではない。古典点ではHille–Perlingのtilting bundleが代替手段。

M: `prop:formal-hilbert` はArtin基底上のsmooth proper dg変形、Oの持上げ、相対Serreとbase changeを仮定し、固定n≥0ごとにRHom(O_A,τ_AⁿO_A)が次数0の自由加群、rank1+n(n+1)/2となることを示す。全nを一括するZariski開条件、heart存在、AZ-amplenessは結論しない。

## 6. identity section、Bertini involution、avatarの復元

P=O_Dの古典gluingはDに依存しない。したがって(S,D,P)のidentity sectionをそのまま10次元局所座標と見なしKS同型を言ってはいけない。Bl_bS→P¹のAbel写像p↦O_D(b-p)とidentity sectionの収縮で(S,p)を得る。smooth Dだけでは例外sectionのP¹の開部分しか見えず、完全な収縮には全pencilが必要。N_pのperfect族は特異点も含める。

Picard Lie algebraはO_{P¹}(-1)。普遍点dg族をblowup/relative Picard模型へ引き戻すとidentity上のKSはrank9、収縮後は基点でも10。元avatar族との相対同値にはPoincaré正規化、baseからのline bundle twist、指定eとの整合が必要。fiberごとのL_O(i_*P)=r_B(i_*P)を相対同定の代わりに使わない。formal logarithmのLie模型と幾何的line bundleも区別する。

一般の古典点のBertini involutionはbを固定し、H¹(T_S)の8方向には自明、T_bSの2方向には-1として作用する。従ってframed/stackのversal baseがsmooth10次元でも、coarse模型は8方向×A²/{±1}でZariski接次元11。Picard側の有限商はTot O(-2)の模型。HH²とcoarse tangentを同一視しない。この作用の全相対groupoidへの接続は別途監査する。

ordered rulingsと七本の例外曲線はOだけのweak markingより強い。一般位置のE₁,E₂の交換だけでもordered avatar→weak markingの非単射が生じる。固定実現B_S=O_S^⊥と非自明Pの下ではacyclicityとYonedaからi_*P、annihilatorからDを復元できるが、抽象residualの幾何性や任意equivalenceの幾何性は出ない。

Mの点/ideal数値類は既知の数値構造と[O]の下でv_I=2τ_*[O]-τ_*²[O]。Hilb¹による逆構成ではuniversal familyの存在とresidual equivalence κのcanonical性を区別する。可換universal ideal kernelのFM functorはE↦Cone(RΓE⊗O→E)[-1]であり、B_S上では[-1]なのでshift補正が要る。Hom跳躍でのD検出は集合としての結果で、scheme構造とP復元は追加課題。M: `prop:heart` はAZ-amplenessに加え高次Serre消滅を仮定したheart一意性であり、存在定理ではない。

## 7. 一般内在的公理とweighted sextic

M: `sec:intrinsic-rank` はrank-one/torsion-free Oを仮定する一般の方向。A₀有限長、A₁=A/A₀で有限長、rank=length(A/A₁)と定義し、AZ生成性からgeneric quotientが除法環上の有限次元加群圏、rank加法性、orbit環のdomain性を得る。AZ2で固定epiのHomのeventual全射性を使い、rank0対象のHom増大度O(n)を示す。Euler式や高次消滅を前提にしない。

一般公理の下ではExt²(O,τⁿF)はn≫0で消え、Ext¹の一般消滅はOのorbitに縮約される。ただしe(n)=dim Ext¹(O,τⁿO)のtail消滅は未証明。e(0)=0、e(n)=e(-n-1)。AZ2を全extension classの一様消滅と読み違えない。今回の具体的境界環の結果はこの一般問題を自動的に解かない。

R₁の次元2とZ(R)₁の非零性は別である。τ-equivariantなNat(id,τ)のOでの評価とZ(R)₁の対応を使う認識が候補。中心元、種数1商、AS-Gorenstein性を一般公理から導くことは未解決で、全公理を満たす反例も得ていない。

weighted認識の入力：中心正則g∈R₁、R/g=C/(Ω₀)、Cはnoetherian ASregular dimension3・index6・Hilbert型(1,2,3)、Ω₀ normal regular degree6、最小relation degrees<6。出力：R=A/(Ω)、AはASregular dimension4・index7・Hilbert型(1,1,2,3)、Ω normal regular6。低次数関係式とgのcommutatorからAを作り、単にA/g=Cというだけではg-torsionを排除できない。

Cassidy–Shelton原典のdegree1前提を流用せず、Mは重み付きresolutionを行列で再構成する。top syzygy index6からのobstructionはdegree5で、sextic kernelのない次数までの正則性が働く。noetherianity、Hilbert級数、normal principal kernelの証明も本文に保持する。

Ω₀がcentralでもΩは自動的にcentralではない。Der(B)_{<0}=0を追加すれば中心性を得る。smooth elliptic translation boundary、char0ではRainsの導分消滅が入力。

障害例：A=k[g,v,w][u;δ]、weights(g,u,v,w)=(1,1,2,3)、δg=0、δv=2gv、δw=3gw、ua=au+δa。PBW基底でHilbert型は(1,1,2,3)、g central regular、A/g=k[u,v,w]。Ω=w²-v³はnormal regular sexticで[u,Ω]=6gΩ、normalizing automorphismはν(u)=u-6g。他の生成元は固定。B=k[u,v,w]/(w²-v³)には負次数導分∂uがある。I₆=kΩなので同じambient/kernelをcentral sexticで生成できない。ただしこの例はSerre/shift、hdim2等の全intrinsic公理を検証しておらず、それらへの反例ではない。

EGのgeneric E8 potentialはΦ=xyz-t yxz+c(P₆(x)+Q₃(y)+R₂(z))、weights(x,y,z)=(1,2,3)。下位係数8とcentral character1のRees weightsは(1,2,2,3,3,4,4,5,6)、固定境界でweighted P⁸、境界2方向と合わせて10。filtered HH²_{≤0}のsemiuniversalityとprojective HH²/成分性には比較が必要。c≠0なら∂zΦからzが冗長で、Rees coverの最小生成元は(1,1,2)になり得る。Hilbert型と最小生成元を混同しない。Rains Example3.1もσ²=idとそれ以外で生成元が変わる。全translation・退化でのASregular被覆は未照合。

## 8. 反標準導来比較と共鳴の論理

R: `thm:main` の既存証明はsmooth genuine S、smooth E、q∈Pic⁰(E)についてT_q≃Db(qgrR_q)、e↦πR、τ↦(1)、hdim2を主張する。同じparameterでの比較であり、異なるqの圏が全て同じという主張ではない。独立全面監査は未完了。

非循環的に確認すべき順序：
(A) Ind(T_q)のorbit右直交を{G∈Dqc(S):RΓG=0,Li*G=0}に同定。E ampleなら補集合affineから零。コンパクト圏内のspanningだけでthick生成を言わない。
(B) 境界H¹(O_E)の具体的な非零拡大を送りExt² traceを保存。Extの次元一致からA∞同定を言わない。
(C) σ∞にはRSS Prop2.4 (deg L≥1)。σ有限では境界BのPI性とYZ Thm5.13→5.1(1)→4.5でdualizing/χ/有限cd。RSS blowing downのdegree≥3・σ∞仮定をdegree1へ流用しない。
(D) sourceのsmooth proper性でpseudo-perfect moduleを表現し右随伴を得る。counit coneの全O_R(n)からの直交と高次消滅で全射性を示し、targetのsmoothnessやthick生成を先取りしない。

数値規約はv=v_B+m[e]、r=rankv、α=c₁v、m=χ(e,v)。detF_q(v)=O_E(α)⊗q^{m-r}。rank0のrestriction消滅の必要条件はO_E(α)q^m=O_E。全orbitから見えない対象にはさらにm=0が必要。genuine Sの非零rootαはO_E(α)非自明（RRとrestrictionで直接確認）。非零mのisogeny fiberの和集合はdenseでも、derived kernelのdense性を意味しない。

境界外FはτF=F。χ(e,F)≠0なら導来切断で残る。元heartでExt¹が残ればqgr側ではcomplexになり得る。全共鳴でheartが必ず変わるとも言わない。一般次数の共鳴と混合拡大の研究は `nc-cubic-classification` が外部正本で、未固定の最新版を無条件に入力しない。

weak Sの(-2)曲線Cはsmooth Eと交わらず、O_C(-1)が全qで共通の非零orbit直交。これだけでは別のderived equivalenceの不存在やqgrの特異性は出ない。特異schemeでもDbcohがdg smoothになり得るので、Perf≠Db、singularity category、total Extのproperness、有限hdimを区別する。

未完成の障害案：weak null categoryがadmissible smooth properでSerre=[2]なら非零2-CY summandとなる。rational Sと同じHH homologyのT_qとの不整合を使える可能性がある。ただしnullのSerreのfunctorial同定、HH₂非零性、qgr有限hdimから必要な飽和性への移行は未検証であり、結論として使わない。

## 9. 一次文献の参照箇所と未確認点

### 今回のrank定理

AOU, *Compact moduli of noncommutative projective planes*, arXiv:1411.7770v1、Appendix A Definitions A.3–A.4 / Propositions A.5–A.6。非可換射影平面の比較対象で、境界環への直接適用ではない。
https://arxiv.org/abs/1411.7770

Artin–Van den Bergh, *Twisted homogeneous coordinate rings*, J.Algebra133(1990),249–271, Theorems1.3–1.4。
https://doi.org/10.1016/0021-8693(90)90269-T
原論文全体は今回未監査。再掲と境界埋込みはChirvasitu–Kanda–Smith, Forum Math.Sigma9(2021)e4, Theorem2.4 / Corollary2.8で本文確認。左/右の規約はopposite・σ^{-1}で照合する。
https://doi.org/10.1017/fms.2020.60
https://par.nsf.gov/servlets/purl/10225264

Keeler, *Criteria for σ-ampleness*, arXiv:math/9912051v2, Theorem1.2。projective schemeを許し、因子数値類へのquasi-unipotent作用ならample Lはσ-ample。整な曲線ではdegreeへの作用は自明。
https://arxiv.org/abs/math/9912051

### Rains構成・moduli・環

Rains, *The birational geometry of noncommutative surfaces*, arXiv:1907.11301v1, Theorem4.30とRemarks pp.60–62：residualとOのgluing、heart構成のblowdown依存、古典gluingのD非依存、一次変形の背景。§5 pp.69–70はdegree1の基点とPic⁰。§6 p.78は可換fiberで余分なDがあること。Theorem10.26直後p.124はrational caseのHilb¹。全点N_p/KSの先行定理を未発見であっても新規性の証明ではない。
https://arxiv.org/abs/1907.11301

Rains, *The noncommutative geometry of elliptic difference equations*, arXiv:1607.08876v4。Proposition11.48 pp.126–127 Hilb¹。Proposition9.29 q≠1でNat(θ,id)1次元。Proposition12.22はAut(Q),Pic(X),W(E_{m+1})でabelian equivalenceを記述するが、可換Sと異なるDが同じcohSを与えるため、境界を忘れた適用にはq≠1等の条件の確認が必要。degree1はm=7、W(E8)有限。O保存でPicard twistを除くことはgeneric finitenessの候補で、全dg族の同値分類は未完了。
https://arxiv.org/abs/1607.08876

Rains, *Filtered deformations of elliptic algebras*, arXiv:2107.13540v2。Lemma2.11/Theorem2.12 proof：smooth elliptic translation、char0の負次数導分消滅。Example3.1：degree1 resolutionとσ²=idの分岐。§4 pp.34–35：effective rootのdense resonanceは数値的amplenessの話。Corollary3.8 pp.21–22：orbit Ext/trace。Proposition5.1 pp.36–37：rigid torsion-free Mとslope条件から中心gとTHCR商。§6 Proposition6.1/(6.13)：固定境界E⁸ torsor/W(E8)≅P(1,2,2,3,3,4,4,5,6)。同節末のrank1 degree1,2の網羅性計算は任意AZ圏の認識ではない。filtered変形のgr標識、weak equivalenceのG_m、全Aut(B)商は別。
https://arxiv.org/abs/2107.13540

Rains, *The (noncommutative) geometry of difference equations*, arXiv:2504.16187 §16.4/Lemma16.12は計画に挙げた重点比較対象。次数1環の提示について既知結果との重複を再照合する。今回の作業で全証明を再確認したとはしない。
https://arxiv.org/abs/2504.16187

### 他の構成と変形理論

Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, arXiv:2508.04986v1。Definition1.1のAS surfaceは3dim ASregular Z-algebraのqgr、markingはvery strong helix。degree1でn=8, helix length11。Definition6.1の(E,L₀,L₁,M₁,…,M₈)、degL_i=3,degM_i=1、coarse/rigidified次元10だがliteral stackはgeneric G_m^{10} scalar inertiaを持つ。Theorem6.4はquiver-potential moduliとの双有理対応。Oだけの標識・heart・AZ作用との一致やordinary ASreg4 sexticを直接与えない。
https://arxiv.org/abs/2508.04986

Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS12(2010),1371–1416; arXiv:0709.3593v4。Theorems3.3.2/3.4.4/3.4.5、§8.5、§3.5(3.5.4)、Theorem3.6.2 proof。genericは可算個のproper closed setsの補集合という場合があり、一つのZariski開に強めない。formal量子化から任意の複素数への特殊化のASregular性も出ない。
https://arxiv.org/abs/0709.3593
https://doi.org/10.4171/JEMS/235

Kuznetsov arXiv:0904.4330v1 Theorem7.7/Remark7.8、Theorem8.5と証明。Orlov arXiv:1402.7364v5 Propositions3.22/Theorem3.25はperfect gluing、Theorem3.18/Corollary3.19はpseudo-perfect表現可能性、Theorem4.15はgeometric realization。
https://arxiv.org/abs/0904.4330
https://arxiv.org/abs/1402.7364

Lowen, *Obstruction theory for objects in abelian and derived categories*, arXiv:math/0407019（Ext²/Ext¹の適用仮定）。Keller–Lowen, IMRN2009,3221–3235（curvature）。Hille–Perling arXiv:1110.5843（rational tilting）。Belmans–Okawa–Ricolfi arXiv:2002.03303v3（geometric familyのSOD）。
https://arxiv.org/abs/math/0407019
https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerLowenHochDefo.pdf
https://arxiv.org/abs/1110.5843
https://arxiv.org/abs/2002.03303

### 有限性・一般認識の適用条件

RSS arXiv:1308.2216v2 Proposition2.4はdegL≥1、σ∞。RSS *Ring-theoretic blowing down I*, DOI10.4171/JNCG/11-4-9のdegree≥3という全体仮定とLemma6.8を区別する。YZ *Rings with Auslander Dualizing Complexes*, J.Algebra213(1999),1–51, Theorems4.5/5.1(1)/5.13は有限σの場合の候補入力。Efimov arXiv:1308.0135v3 Theorem1.2はsingular schemeのDbcohとdg smoothnessの注意。
https://arxiv.org/abs/1308.2216
https://www.math.bgu.ac.il/~amyekut/publications/aus-gor/journal.pdf
https://arxiv.org/abs/1308.0135

Artin–Zhang DOI10.1006/aima.1994.1087 Theorem4.5(1)は再構成。既存確認ではAbdelgadir–Chan–Okawa–Ueda arXiv:2401.14798 Theorem7.3の再掲も用いた。原著全証明を今回監査したわけではない。
https://arxiv.org/abs/2401.14798
https://doi.org/10.1017/nmj.2025.10067

Cassidy–Shelton arXiv:math/0603375v2 §§1,3 Theorems3.6–3.7はdegree1生成。Reyes–Rogalski DOI10.1017/nmj.2020.32 Proposition3.18(3)はconnected A₀=kの左右・graded/ungraded global dimension検出。Mori–Ueyama arXiv:1708.00167v4 Definition3.9/Theorem3.11にはregular tiltingとRT3の高次消滅が必要で、O exceptionalだけでは使えない。
https://arxiv.org/abs/math/0603375
https://doi.org/10.1017/nmj.2020.32
https://arxiv.org/abs/1708.00167

Van den Bergh, J.Algebra195(1997),662–679, Theorem6.3には左右noetherian、左右有限local cd、左右full χが入力。Serre関手の存在から自動的に出るとはしない。YZ *Serre duality for noncommutative projective schemes*, Proc.AMS125(1997),697–707 Theorem4.2もbalanced dualizingからの方向。
https://cantate.be/site/dualcompl.ps
https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/paper.pdf

Lin–Rampazzo–Zhang arXiv:2609.10344v1 Theorem1.2は主稿でsmooth complex del Pezzo degree≤4のenhanced O^⊥のTorelliとして引用されている。既往のstatement確認と今回の全証明監査は別で、weak境界・任意equivalenceの幾何性・抽象residualの存在を与えるものとして使わない。
https://arxiv.org/abs/2609.10344

## 10. 他原稿との関係と公表上の焦点

元avatarの分類対象はordered rulingsと七例外曲線を保つ。指定頂点u8、P/P^{-1}、shift、構造対象、heartの直接gluingとの照合は未完了。旧添付稿を取得することを現在のrank定理の再開条件にしない。

既存Poisson量子化稿 `del_Pezzo_1_2_4_Poisson_quantization` §§7–9のforward存在、§9.1の条件付きASregular、§9.3の全coh変形網羅性を主張しない制限と、本研究の既存Rからambientをliftする逆向き認識は別である。外部稿の原本を本repoに重複保存せず、利用時に版と仮定を確認する。

公表上は普遍点・局所変形を核とするMと、導来比較・rank認識を核とするRを保持する。既知のgluing、Hilb¹、強標識10パラメータ族、filtered E8族を再構成しただけで新規性を宣言しない。今回のrank定理は内在的公理への橋として有用だが、研究全体の独自性は形式比較・相対heart・同型groupoid・境界の完成度によって評価する。
