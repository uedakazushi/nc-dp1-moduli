# 次数1の非可換del Pezzo曲面：現行研究ノート

研究ノート：次数1 nc del Pezzoの普遍点族・内在的認識・avatar
2026-11-14 JST / version 4.0

現在有効な論点と文献比較を整理する。再開は00_research_plan.md、次にresearch/dp1_research_plan.mdから行う。
詳細な証明はpapers/nc_del_pezzo_degree1_moduli.texとpapers/dp1_anticanonical_models.texに置く。
本ノートでは全文を重複させない。R:は後者、その他のラベルは前者を指す。

1. 主張の状態と現在の範囲

既存本文に証明を備え、先に点検された部分（今回の全面再監査ではない）：
・sec:pointed-dg-family、thm:universal-gluing：
  N_p=L_{O_S}(I_p(-K_S))により、smooth degree1 del Pezzo Sの全点pから
  例外対象eを指定したsmooth proper dg圏T_{S,p}を構成する。
  相対対角イデアルによるperfect族であり、p=bでは(Perf(S),O_S)を回復する。
・thm:gluing-hh-ks：
  Ext^1(N_p,N_p)=T_pS、Ext^2(N_p,N_p)=0、
  HH^1(T_{S,p})=0、dim HH^2(T_{S,p})=10、HH^i=0 (i>=3)。
  曲面の8次元局所versal atlasの普遍曲面からのKSは全点で同型。
  dimensionの一致だけでなく、混合bar cochainを通した自然性を使う。

有限presentation chartでの結果：
・prop:finite-directed-chart、thm:finite-chart-component：
  長さ11のfull directed exceptional collectionと相対A-infinity modelを選ぶ。
  有限型のpresentation scheme Zとconnected smooth gauge group Gが得られ、
  主候補族のG飽和像の閉包はZの既約成分となる。
  族の構成は選択に依存しないが、このchart自体は補助選択に依存する。
  raw quotient [Z/G]はinner automorphismのstabilizerを持ち得るので、
  10次元DM stackやintrinsic weakly marked moduliと同一視しない。
  証明の要点と全Morita比較の残る箇所は第3項に記す。

追加仮定を明示して使う部分：
・prop:component-test：
  適切なalgebraic moduli chartと族への写像が存在し、その変形理論との比較や
  generic finiteness／局所étale性を確保したときの成分判定。
  これ自体はambient moduliの存在や全対象の分類を証明しない。
・prop:formal-hilbert：
  Perf(S)のArtin local base R上のsmooth proper dg変形C_R、Oのlift O_R、
  base change compatibleなrelative Serre functor S_Rを仮定する。
  tau_R=S_R^{-1}[2]に対し、各n>=0のRHom(O_R,tau_R^n O_R)は
  rank 1+n(n+1)/2のfree R-moduleとして次数0に集中する。
  特殊fiberの高次Ext消滅とperfect complexのderived Nakayamaを使う。
  全nを一括するZariski-open条件、abelian heart、AZ amplenessは結論しない。

全smooth proper Morita変形とのformal比較、有限presentation chartから
intrinsicな局所／global moduliへの移行と全退化境界でのheart認識は未完了。
滑らかな楕円領域のqgr heartと導来比較は以下の第1a項で扱う。
HH^3=0とKS同型だけを「全Morita変形の形式普遍族」や
「intrinsic nc del Pezzo moduliの成分」の完成証明と呼ばない。
既知族の構成・HH手法を用いており、今回の普遍点表示の独立の新規性は未確認である。

従来の有効な結果は保持する：
・thm:az：AZ再構成という既知定理の適用。右noetherian性とchi_1まで。
・sec:intrinsic-rank：intrinsic rank、generic quotient、domain、leading Hom growth。
・sec:weighted-recognition：中心境界とASregular coverを仮定したweighted sextic認識。
  これらの証明は前段階で点検済みであり、未解決の全分類と区別する。
・prop:marking、prop:weak、thm:yoneda、prop:classical、
  prop:point-class、prop:jump、prop:heart：
  ordered marking非単射、weak境界、固定実現での復元、古典型、数値類、
  Hom跳躍、条件付きheart一意性。本文に証明があることと、
  今回その全てを再監査したことは同じではない。
分類を支える数値計算や計算機証明は用いていない。

1a. 反標準qgrと稠密共鳴：現在の判定

主結果 R:thm:main（日本語論文 anticanonical_resonance、版1.0）：
Sはsmooth genuine del Pezzo（-K ample）、Eはsmooth anticanonical elliptic curve、
q∈Pic^0(E)。Rains gluing T_q=<O_S^perp,e>とtau=Serre^{-1}[2]から作る反標準環R_qに対して、
実際の導来切断Phi=pi RΓ_*は T_q ≅ Db(qgr R_q) を与える。
e->pi R、tau->(1)、hdim qgr R=2。有限位数q/σも含む。
これは同じパラメータで元のsmooth categoryと反標準モデルを比較する命題であり、
全qでT_q自体が同じ圏になるという主張ではない。
本文の証明を今回点検した。独立査読・形式検証・文献上の新規性は未確認。

証明の非循環的な順序：
(A) R:thm:null：Ind(T_q)の全tau^n eに右直交する部分圏は
    {G∈Dqc(S):RΓ G=0, Li^*G=0} に同値。qに依存しない。
    E ampleならU=S\Eはaffine、Li^*G=0よりG=Rj_*j^*G、RΓG=0よりG=0。
    コンパクト圏内だけのspanningでなくInd-completionで生成を証明する。
(B) R:lem:trace：境界H^1(O_E)の非零拡大を実際に送り、Ext2のtraceの保存を示す。
    Extの次元一致だけからA-infinity同定を主張しない。
(C) R:lem:finiteness：σ∞はRSSBlow Prop2.4（degree>=1）。σ有限は境界BがPI、
    Yekutieli–Zhang Thm5.13->5.1(1)->4.5でbalanced dualizing、chi、有限cdを得る。
    RSSDownのdegree>=3、σ∞という全体仮定をdegree1へ誤用しない。
(D) R:prop:ess：sourceのsmooth proper性からpseudo-perfect moduleを表現し右随伴を得る。
    counit coneは全O_R(n)に右直交するため零。targetのsmoothnessやthick生成を先取りしない。
    Serre=(-1)[2]を運び、heartでのExt>2の消滅とExt2非零を得る。

共鳴の区別 R:prop:det：
K0をSODで同定し、r=rank v、α=c1(v)、m=χ(e,v)とすると
  det F_q(v)=O_E(α) tensor q^(m-r)。
rank0で境界restrictionが零となる必要条件はO_E(α) q^m=O_E。
全反標準orbitで見えない対象にはさらにm=0が必要。よって零指数条件はq独立。
genuine del Pezzoではroot αのO_E(α)は非自明（本文にRRとrestrictionで直接証明）。
非零mのisogeny fiberの和集合はdenseだが、そのdense性をderived kernelへ移さない。
境界外対象Fはtau F=F。χ(e,F)≠0ならderived sectionsに必ず残る。
元heartのExt1が残る場合はqgr側でcomplexとして現れ得る。
全共鳴でheartが必ず変わるとは結論しない。

帰結と未解決：
・genuine S、smooth Eのelliptic chartではderived-change locusもhdim∞ locusも空。
・degree1の(S,p)族でpを通るEがsmoothな非空openに適用。従って全族でbad locusはdenseでない。
・特異E、非局所自由gluing、weak avatarを含む全locusのclosednessは未証明。
・weak Sの(-2)曲線Cはsmooth Eと交わらず、O_C(-1)が全qで共通の非零orbit直交対象。
  それだけでは別のderived equivalenceの不存在やtargetのsingularityは証明されない。
・新qgr heartのGabriel–Krull rank-one/tfは別の認識課題。
・singular schemeでもDbcohはdg smoothになり得る（Lunts、Efimov Thm1.2）。
  Perf≠Db、singularity category、total Extのproperness、有限hdimを区別する。

今後有用な未完成の障害案：
weak Sのnull categoryがadmissibleでsmooth properなら、そのSerreが[2]なので
非零2-CY admissible summandになる。他方、T_qのHH homologyはrational Sのものと同じ。
この不整合からnullの非admissibilityを導き、有限hdimのqgrとの比較に利用できる可能性がある。
ただしnullのSerreのfunctorial同定、HH2の非零性、qgr有限hdimから必要な飽和性への移行は
まだ一連の定理として検証していない。これは研究案であって本稿の結論ではない。

2. 普遍点によるgluingの規約と再発防止事項

kは標数0の代数閉体、Sはsmooth degree1 del Pezzo、
H=-K_S、bは反標準pencilの唯一の単純基点とする。
B_S=O_S^perp={M | RΓ(S,M)=0}。
半直交分解の規約はHom(right,left)=0なのでPerf(S)=<B_S,O_S>。
L_O(F)=Cone(RHom(O,F) tensor O -> F)は包含B_S->Perf(S)の左随伴である。

I_p∈B_Sであり、
  N_p=L_O(I_p(H))=Serre(B_S)^{-1}(I_p)[2]。
gluingはRHom(e,M)=0、RHom(M,e)=RHom_B(M,N_p)とする。
右射影r_B(O_S)はCone(O_S -> O_S(K_S)[2])[-1]である。
基点のKoszul列からN_b=r_B(O_S)となる。

基点ではh^0(I_b(H))=2、h^1(I_b(H))=1である。
従ってL_OのevaluationにH^0だけを使ってはならない。
対角イデアルI_Deltaを用いる相対derived evaluationが必要で、
基点fiberのN_bはH^{-1}=O_S(K_S)、H^0=O_Sを持つ。
族はperfect complexesの族であり、基点付近のflat sheaf族とは主張しない。

p≠bではpを通る反標準因子Dは一意で、
  N_p=i_*(I_{p,D} tensor O_D(H))。
pがDのsmooth pointならO_D(H)=O_D(b)によりN_p=i_*O_D(b-p)。
smooth D上ではこれは非自明なP∈Pic^0(D)を用いるRains/avatarのgluingである。
Dの特異点pにもmutationの式は適用できるが、境界上の対象は
rank-one torsion-free sheafとなり、Pをline bundleに限るavatarの範囲を越える。

Extの計算は自己同値Serre(B_S)^{-1}[2]を用いてI_pへ戻す。
RHom(N_p,N_p)のcohomologyはk、T_pS[-1]のみである。
複体としての分解をcanonical splittingやdg代数の分解とは主張しない。

Kuznetsovのgluing functorの規約では
phi(M)=RHom_B(M,N_p)^dualとなり、そのendomorphism代数はoppositeを伴う。
本文のrepresentable module h_N=RHom_B(-,N)によるbar計算では
REnd(h_N)=REnd(N)を直接使用できる。規約の違いを省略しない。

3. HH・Kodaira–Spencer・形式変形の境界

Kuznetsov Theorem8.5は、O_Sがexceptionalである場合の
HH^t(B_S)=H^t(O_S) ⊕ H^{t-1}(T_S)を与える。
degree1ではHH^0(B_S)=k、HH^2(B_S)=k^8、他は0である。
H^0(T_S)=H^2(T_S)=0、h^1(T_S)=8は、
8点blowupのtangent sequenceでも確認できる。

triangular gluingのHochschild triangleは
  C(T_{S,p}) -> C(B_S)⊕k -> RHom_B(N_p,N_p) -> C(T_{S,p})[1]。
次数0の写像は(a,c)↦(a-c)id_Nで全射であり、
  0 -> T_pS -> HH^2(T_{S,p}) -> H^1(T_S) -> 0
を得る。高次のExtとresidual HHが消えるのでHH^{>=3}(T)=0。

KS同型には自然性が必要である。
点の変形はHilb^1(S)=Sの普遍イデアルからExt^1(N_p,N_p)全体を与え、
曲面の変形はHKR projectionを通してHH^2(B_S)全体を与える。
混合bar cochainのconnecting mapがgluing moduleを変形したときのKSである。
これを普遍曲面のtangent exact sequenceと比較する。
基底は余分なframing方向を含まないétale/miniversal atlasとする。

有限presentation chartで閉じる議論：
長さ11のfull exceptional collectionからdirected strictly unital A-infinity modelを作る。
単位を除くcomposable stringは長さ10以下なので、m_nとgaugeのf_nはn<=10に限られる。
基底点のminimal modelを固定したgraded spaceに、m_1も変化を許して
Stasheff equationsを課すことで有限型scheme Zを得る。
f_1のinvertibleな部分と有限個のhigher f_nがconnected smooth algebraic group Gをなす。
対角Hom^2=0なのでm_0はなく、relative normalized cochainsが接・障害を計算する。
HH^3=0でZは対象点においてsmooth、KS同型でG×U->Zの微分は全射となる。
必要な開近傍へ制限するとこの写像はsmoothで、その像は開である。
GとUの既約性からG飽和像の閉包はZの一つの既約成分となる。
相対A-infinity transferとHom complexの局所free modelを使う段階を省略しない。
10はgauge orbitを除いた一次変形の次元であり、Zやraw [Z/G]の次元ではない。
HH^1=0でもinner automorphismsに由来するpresentation stabilizerは残る。

全Morita変形とのformal比較を完成する際の作業：
・変形functorをframed/rigidified pointed Morita変形として厳密に定義する。
・full exceptional collectionを補助的に用いるdirected strictly unital A-infinity modelでは、
  対角Hom^2=0によりm_0の曲率が出ない。k^{11}に相対的なnormalized cochainsを使う。
・例外対象のExt^2/Ext^1消滅でliftの存在・一意性を示し、
  perfect Homとderived Nakayamaでsemiorthogonality/fullnessの保持を確認する。
・このmodelと全対象のMorita変形との比較を記述してから、
  小拡大のliftをHH^2 tensor Iで調整する帰納によりall-orders versalityを示す。
この全Morita比較補題は完成した本文定理としては扱っていない。
上の有限presentation chart内での成分性は、この全比較を前提にしない。
古典点ではrational surfaceのtilting bundleを使った有限次元代数変形への縮約が候補。
exceptional collectionやtiltingを証明の補助に用いることは、
族自体がそのchoiceに依存することを意味しない。

Keller–Lowenの一般Morita変形におけるcurvatureの注意を無視しない。
Belmans–Okawa–RicolfiのSOD変形定理はsmooth proper geometric familyの結果であり、
任意のdg変形へ仮定の確認なしに流用しない。
有限presentation chartとintrinsic moduliの比較、代数化、formal versalityを区別する。

4. identity section・Bertini involution・coarse moduli

P=O_Dではgluing categoryがDに依存しない。
元の(S,D,P)座標のidentity sectionを単に残したまま
「10次元族なのでKS同型」と結論することはできない。

Bl_b(S)->P^1はsection付きintegral genus-one pencilで、
smooth locus上のp↦O_D(b-p)がrelative generalized Picardを記述する。
基点へのblowdownがidentity sectionを収縮し、普遍点の式はこの収縮後に実際のdg族を与える。
smooth Dだけに制限した場合、exceptional sectionはP^1の開部分に過ぎず、
完全な例外曲線の収縮には全pencilを考える必要がある。
特異点も含めた延長はN_pのperfect complexによる。

identity付近のPicard Lie algebraはO_{P^1}(-1)である。
本稿の(S,p)族をこのblowup/relative Picard模型へ引き戻した族のKSはidentity上でrank9、
収縮後の(S,p)族のKSは基点を含めrank10となる。
元のavatar族との全base上の相対同値は幾何点の一致だけからは従わない。
Poincare bundleの正規化、baseからのline bundle twist、例外対象の指定の整合が必要である。
特にL_O(i_*P)とr_B(i_*P)は各fiberで一致しても、相対対象としての同一視は別途確認する。
本稿では元のavatar族の降下やそのKSとの比較を、この確認なしに主張しない。
標数0のformal logarithmを用いる場合も、幾何学的なline bundleと
Lie algebraの局所模型の区別を保つ。

weak markingがOだけなら有限なAut(S)の商は残る。
genericな古典点ではBertini involutionはbを固定し、
H^1(T_S)に自明、T_bSに-1として作用する。
従ってstack/同定を固定したversal baseはsmooth 10次元でも、
coarseな局所模型は8方向とA^2/{±1}を持ち、coarse tangent dimensionは11となる。
元のPicard側で有限商を取るとTot O(-2)の模型になる。
HH^2とcoarse quotientのZariski tangentを直接同一視しない。

5. 内在的rankと反標準環に関して保持する知識

rankはHilbert係数を定義として採用せず、
A0=有限長対象、A1=A/A0で有限長となる対象、
rank(F)=length_{A/A1}(F)とする。
rank1 torsion-free OとAZ生成性からgeneric quotientは一つの除法環上の
有限次元加群圏となり、全対象のrankが有限・非負・加法的になる。
rank1 torsion-free対象間の非零射はmonoなのでorbit algebra Rはdomain。

leading Hom growthでは、AZ2による固定epiのHomのeventual全射性を使い、
rank0対象のh_F(n)=O(n)を示してから
h_F(n)=rank(F)n^2/2+O(n)を得る。
高次Ext消滅やEuler多項式をこの証明の前提にしていない。

Ext^2(O,tau^n F)は全Fでn>>0に消える。
Ext^1の一般消滅はF=Oのorbitに縮約したが、
e(n)=dim Ext^1(O,tau^n O)のtail消滅は未証明。
e(0)=0、e(n)=e(-n-1)を保持する。
AZ2を全extension classに対する一様消滅と誤読しない。

R_1=Hom(O,tau O)の次元2と、Z(R)_1やNat(theta,id)の存在・次元は別である。
任意のsectionからCartier anticanonical boundaryが得られるとは限らない。
Nat_tau(id,tau)≅Z(R)_1という評価写像を使う認識が次の候補。
非零中心元の存在、R/(g)の楕円幾何性、RのAS-Gorenstein性は一般には未証明。
現在のintrinsic公理の全てを満たす反例を得たわけではない。

6. weighted sextic認識とordinary gradedの比較

thm:weighted-hypersurface-recognitionの入力：
g∈R_1がcentral regular、R/g=C/(Omega0)、
Cがnoetherian ASregular dimension3・index6・Hilbert型(1,2,3)、
Omega0がnormal regular degree6、Cの最小relation degreesが6未満。
出力はR=A/(Omega)、AがASregular dimension4・index7・Hilbert型(1,1,2,3)、
Omegaがnormal regular degree6である。
Cの低次数関係式のliftとgのcommutatorだけを使ってAを提示する。
任意のA/g=Cという同定だけでは余分なg-torsionを排除できない。

Cassidy–Sheltonの原典は生成元次数1を仮定する。
本文の正の重み付き版はresolutionの行列を再構成して証明している。
index6のtop syzygyからg方向へのobstructionはdegree5であり、
sextic kernelのないこの次数までの正則性が働く。
noetherianity、Hilbert series、normal principal kernelの証明も本文にある。

Omega0 centralでも、lift Omegaのcentralityは自動ではない。
Der(C/(Omega0))_{<0}=0を追加するとcentralになる。
smooth elliptic translation boundary、char0ではこの導分消滅はRainsによる。

centralityの追加仮定が必要な環の例：
char0でA=k[g,v,w][u;delta]、weights(g,u,v,w)=(1,1,2,3)、
delta(g)=0、delta(v)=2gv、delta(w)=3gwとする。Ore規約はua=au+delta(a)。
PBW基底からAのHilbert型は(1,1,2,3)、gはcentral regular、A/g=k[u,v,w]。
Omega=w^2-v^3はnormal regular sexticで[u,Omega]=6gOmega≠0。
正規化自己同型はnu(u)=u-6g、他の生成元を固定する。
R=A/(Omega)でもgはregularでdegree1 del Pezzoと同じHilbert seriesを持つ。
Omega0はcentralだがB=k[u,v,w]/(w^2-v^3)にはdegree -1の導分∂uがある。
I_6=k Omegaなので、同じambientの同じkernelをcentral sexticでは生成できない。
Serreとshiftの整合、hdim2、smoothness等の圏論的公理を全て検証した例ではなく、
ユーザー提案のintrinsic定義への反例として用いてはならない。

EGのgeneric E8 familyではweights(x,y,z)=(1,2,3)、
Phi=xyz-t yxz+c(P_6(x)+Q_3(y)+R_2(z))。
下位係数8個とcentral character1個のRees scaling weightsは
(1,2,2,3,3,4,4,5,6)で、固定境界に対するweighted P^8を与える候補である。
境界の2方向を加えて10次元となり、RainsのE8 weighted projective familyと一致する。
EGのfiltered semiuniversalityはHH^2_{<=0}の主張であり、
projective categoryのHH^2や成分性へは比較が必要である。

c≠0では∂_zPhiの関係でzは冗長な生成元になる。
generic Rees coverの最小生成元の重みは(1,1,2)となり得る。
「Hilbert型(1,1,2,3)」と「4個の最小生成元の重み(1,1,2,3)」を区別する。
Rains Example3.1でもsigma^2=idとそれ以外で最小生成元が変わる。
全translationと退化境界を含むASregular cover認識は未照合である。

7. avatar・Hilb^1・heartの復元で保持する事項

ordered rulingsと7 exceptional curvesの強いmarkingはOのchoiceより強い。
一般の7点のE_1,E_2交換だけでもweakly marked categoryからの非単射が生じる。
順序付きavatarとの無条件の1:1対応は求めず、忘却groupoidを定める必要がある。

可換weak del Pezzoの(-2)曲線CではO_C(-1)が全反標準twistから検出されず、
AZ-amplenessが失敗する。さらに非可換Rains族にはdenseなroot resonanceがある
（詳細は次節）。weak surfaceのsmooth blowup heartとanticanonical Projを区別する。

固定された実現B_S=O_S^perpと非自明P∈Pic^0(D)の下では、
PのacyclicityとYonedaからi_*Pを復元し、annihilatorからDを得る。
これは任意のabstract residual categoryが可換Sから来ることを証明しない。
P=O_Dの場合のgluing対象はCone(O_S -> omega_S[2])[-1]でDに依存しない。

degree1 point/ideal classは構造対象の類も含む既知数値構造の下で計算した。
v_I=2 tau_*[O]-tau_*^2[O]からのHilbert moduli構成は逆方向の候補である。
RainsのHilb^1の可換曲面同定は既知だが、universal familyが存在することと
residual equivalence kappaがcanonicalに決まることは別である。
可換universal ideal kernelのFM functorは
E↦Cone(RΓ(E) tensor O_S -> E)[-1]であり、B_S上では[-1]。
従ってkappaの規約・shift補正を確認する。

Hom跳躍による反標準因子の復元は、Cartier因子に沿うExt局所計算に基づき、
特異点を含め集合として示した。scheme構造とPの復元はさらに必要である。
heart一意性 prop:heart はAZ-amplenessに加え高次Serre vanishingを仮定する。
この追加仮定を現在のintrinsic定義から自動的に得たとはしない。

8. 先行研究との比較と一次文献の確認箇所

[Rains: gluingと普遍点の先行背景]
Eric M. Rains, The birational geometry of noncommutative surfaces,
arXiv:1907.11301v1.
https://arxiv.org/abs/1907.11301
Theorem4.30とRemarks pp.60–62：
O_S^perpとO_SをPic^0(D)の対象でglueする構成。
Remark1はheartの構成にblowdown structureを使う。
Remark2は古典gluingの表現対象がDに依存しないconeであることを述べる。
Remark3はresidual deformationとgluing deformationを分け、
この形が全first-order deformationsを与えると述べるが、
任意formal deformationへの拡張は示唆に留める。
§5 pp.69–70ではdegree1の反標準基点によってPic^0(Q)をQのsmooth componentと同定し、
点のblowupとq-gluingによるPic^0(Q)^2族を扱う。
全S上のN_p式とその全点KS同型を明記した先行定理は今回の調査では未発見であり、
不存在や新規性の証明とはしない。
§6 p.78は非可換fiberでQが復元され、可換fiberにはQの余分なchoiceがあると明記。
Theorem10.26直後p.124はrational caseのHilb^1を可換avatar曲面と同定する。
これらの原著の全証明を今回網羅的に監査したわけではない。

[Rains: abelian equivalencesとq≠1]
Eric M. Rains, The noncommutative geometry of elliptic difference equations,
arXiv:1607.08876v4.
https://arxiv.org/abs/1607.08876
smooth anticanonical curveを持つ構成族を扱う。
Proposition11.48 pp.126–127はHilb^1の可換曲面同定。
Proposition9.29はq≠1でNat(theta,id)が1次元とし、境界の内在性を支える。
Proposition12.22はabelian equivalenceをAut(Q)、Pic(X)、W(E_{m+1})で記述する。
印刷されたstatementにq≠1はないが、同じ可換Sと異なるD,D'は同じcoh(S)を与える。
したがって今回の境界を忘れた同値への適用はq≠1に限るか、
境界を保つ同値という条件を加える。省略条件か修正を要するかは未確定。
degree1ではHirzebruch7点blowup、m=7、W(E8)は有限。
Oを保存させてPicard twistを除く議論はgeneric finite忘却の候補だが、
今回の新しいdg族全体の同値分類までこの命題で得たとはしない。

[Rains: filtered familyとnon-Fano resonance]
Eric M. Rains, Filtered deformations of elliptic algebras,
arXiv:2107.13540v2.
https://arxiv.org/abs/2107.13540
Lemma2.11、Theorem2.12 proof：smooth elliptic、translation、char0で負次数導分が消滅。
Example3.1：degree1 elliptic algebraのresolution、sigma^2=idによる最小生成元の差。
§4 pp.34–35：simple rootがeffectiveとなるdenseなhypersurfaces、
およびpure1dim(-2)-classが存在すると反標準Qが数値的にampleでないことを明記する。
同節のampleはeffective coneの双対の内部という定義である。
数値的ample=>生成・消滅は使えるが、AZ-amplenessとの逆方向の同値は未確認である。
従って「numerically non-Fano」と「AZ非ample」を同一視しない。
Proposition5.1：rigid torsion-free Mとrestrictionのslope条件の下で、
Serre orbit環に正則中心degree1元とelliptic quotientを与える。
§6 Proposition6.1と(6.13)：rank1・degree1、固定したE,V,Psiで
E^8 torsor/W(E8)≅P(1,2,2,3,3,4,4,5,6)という族。
§6末：一般のfiltered deformationsの網羅性はConjecture1。
rank1・degree1,2は任意E,Psiでの計算が済み、surface constructionから得られると述べる。
これは任意のAZ categoryの認識ではない。
filtered deformationはgr同定付きで、weak equivalenceはgrading G_mを加える。
全Aut(B)による商とは異なる。
数値的なdense resonanceを除くことは一つのZariski-open条件ではない。
しかしAZ-ample heartやderived同値のlocusが同じ補集合になるとは言わない。
R:thm:mainにより、genuine del Pezzoとsmooth Eの場合は全qで反標準qgrに導来同値である。

[反標準導来比較の一次入力]
Rains 2107.13540v2 Cor3.8および証明（pp.21–22）：orbit Extと境界trace pairing。
Pro5.1（pp.36–37）：e=Oの場合の中心正則元とTHCR quotient。
Rogalski–Sierra–Stafford, Noncommutative Blowups of Elliptic Algebras,
arXiv:1308.2216v2 (2015), Prop2.4：degree>=1、σ∞を許すchi/cd/dualizing。
https://arxiv.org/abs/1308.2216
Yekutieli–Zhang, Rings with Auslander Dualizing Complexes,
J.Algebra 213 (1999),1–51, Thm4.5,5.1(1),5.13：有限σの場合の代替入力。
https://www.math.bgu.ac.il/~amyekut/publications/aus-gor/journal.pdf
Orlov 1402.7364v5 Thm3.18、Cor3.19：pseudo-perfect moduleの表現可能性。
Efimov 1308.0135v3 Thm1.2：Dbcoh singular schemeとdg smoothnessを区別する注意。
https://arxiv.org/abs/1308.0135
源資料の該当statementと必要な証明箇所をテキストで確認。
外部PDFのwebスクリーンショット取得はcache missで失敗し、ページ画像検証はできていない。

[Okawa–Ueda: 既知の強くmarkedな10パラメータ族]
Shinnosuke Okawa and Kazushi Ueda,
Marked Artin–Schelter surfaces of del Pezzo types,
arXiv:2508.04986v1 (2025-08-07).
https://arxiv.org/abs/2508.04986
Definition1.1：3dim ASregular Z-algebraのqgrをAS surfaceとし、
markingはvery strong helixのchoice。
degree dでn=9-d、helix parameter ell=12-d。degree1はn=8、ell=11。
Definition6.1のM_ellは(E,L0,L1,M1,...,M8)、
deg L0=deg L1=3、deg Mi=1。
curve isomorphismと各line bundleのisomorphismをmorphismに含める。
粗いparameter dimensionは1+2+8-1=10（最後はtranslationの商）。
literal stackにはgeneric G_m^{10}のscalar inertiaがあるため、
10次元という表現はcoarse／scalar rigidification／適切なatlasについて用いる。
Theorem6.4はM_ellとquiver potential moduli M_Qのbirational equivalence。
強いmarking付きの既約10パラメータ族の存在は既知である。
§6でnc blowupと明示的に得る同値はderived equivalenceであり、
今回のOだけのmarking、指定heart、AZ-ample tauとの一致は別問題。
ASregular Z-algebraの定義に今回の全abelian公理が直接含まれているわけではない。
この論文をordinary graded ASregular4のsextic表示定理として引用しない。

[Etingof–Ginzburg: filtered E8 chart]
Pavel Etingof and Victor Ginzburg,
Noncommutative del Pezzo surfaces and Calabi–Yau algebras,
J. Eur. Math. Soc. 12 (2010), no.6, 1371–1416,
arXiv:0709.3593v4; DOI 10.4171/JEMS/235.
https://arxiv.org/abs/0709.3593
Theorem3.3.2：homogeneous CY leading potentialからのfiltered CY変形と中心元。
Theorem3.4.4：generic E8 ambient familyは10、central quotientは11パラメータ。
Theorem3.4.5と§8.5：正規形とfiltered HH^2_{<=0}に対するsemiuniversality。
Definition3.4.3のgenericは可算個のproper closed subsetsを除く意味で、
一つのZariski openという主張へ無条件に強めない。
§3.5 (3.5.4)：中心元は非零因子、quotientはnoetherian THCR。
Theorem3.6.2 proofはhomogeneous ambientのASregular dimension3を明記する。
generic E8 chartではReesによるweighted ASregular4 coverを使用できる。
Lemma7.4.2、Proposition8.1.1(i)と相対Reesの議論は添付稿の形式量子化にも関係する。
全abstract categoryの認識や、任意の非零複素数への形式級数の特殊化ではない。

[Kuznetsovとdg gluing]
Alexander Kuznetsov, Hochschild homology and semiorthogonal decompositions,
arXiv:0904.4330v1.
https://arxiv.org/abs/0904.4330
Theorem7.7、Remark7.8：gluing Hochschild exact sequence。
Theorem8.5と証明：O^perpのHHと、HKRのtop polyvectorを除くrestriction。
Dmitri Orlov, Smooth and proper noncommutative schemes and gluing of DG categories,
Adv. Math. 302 (2016), 59–105; arXiv:1402.7364v5.
https://arxiv.org/abs/1402.7364
Proposition3.22、Theorem3.25：perfect bimodule gluingのsmoothness/properness。
Theorem4.15：geometricなdg圏のgluingのgeometric realization。
これらの適用箇所は共同作業で一次資料を確認したが、原著全体の再証明はしていない。

[変形比較に用いる文献]
Wendy Lowen, Obstruction theory for objects in abelian and derived categories,
Comm. Algebra 33 (2005), 3195–3223; arXiv:math/0407019.
https://arxiv.org/abs/math/0407019
object liftingのobstruction/liftはExt^2/Ext^1。適用するderived theoremの仮定を明示する。
Bernhard Keller and Wendy Lowen, On Hochschild cohomology and Morita deformations,
IMRN 2009, no.17, 3221–3235.
https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerLowenHochDefo.pdf
一般dg Morita変形に関するcurvatureの問題を踏まえる。
Lutz Hille and Markus Perling, Tilting bundles on rational surfaces and quasi-hereditary algebras,
Ann. Inst. Fourier 64 (2014), 625–644; arXiv:1110.5843.
https://arxiv.org/abs/1110.5843
古典点で通常の代数変形へ縮約するための参照。
Belmans–Okawa–Ricolfi, Moduli spaces of semiorthogonal decompositions in families,
arXiv:2002.03303v3.
https://arxiv.org/abs/2002.03303
smooth proper geometric familyにおけるSODのétale変動の結果。
任意のdg変形やnontrivial-SOD locusのopen-and-closed性に強めない。

[intrinsic rank・AZ]
Abdelgadir–Okawa–Ueda, arXiv:1411.7770v1 (2014), Appendix A：
Definitions A.3–A.4、Propositions A.5–A.6、Corollary A.7を本文確認。
原文の対象は3dim quadratic ASregularのnc plane。
一般Aへの適用を引用せず、長さを定義に採用して本文で必要な一般化を証明した。
https://arxiv.org/abs/1411.7770

Artin–Zhang 1994, DOI 10.1006/aima.1994.1087：
公刊ページの書誌とabstract、Theorem4.5(1)を再掲した
T. Abdelgadir, D. Chan, S. Okawa, K. Ueda,
Degenerations of orbifold curves as noncommutative varieties,
Nagoya Math. J. 261 (2026), e4, Theorem7.3を確認。
原著PDF全文の証明は今回未監査。
https://doi.org/10.1017/nmj.2025.10067
https://arxiv.org/abs/2401.14798

[weighted central extension]
Cassidy–Shelton, PBW-deformation theory and regular central extensions,
arXiv:math/0603375v2 (2006), §§1,3, Theorems3.6–3.7。
原典のdegree1前提と本文の重み付き再証明を区別する。
https://arxiv.org/abs/math/0603375
Reyes–Rogalski, Nagoya Math. J. 245 (2022), 100–153, Proposition3.18(3)：
connected nonnegative gradedの場合、左右・graded/ungradedのglobal dimensionを
kのprojective dimensionが検出する。A_0=kのseparabilityを確認して適用する。
https://doi.org/10.1017/nmj.2020.32

[高次Serre vanishingに関する適用条件]
Mori–Ueyama, A categorical characterization of quantum projective spaces,
arXiv:1708.00167v4, Definition3.9、Theorem3.11。
regular tiltingを仮定し、RT3が正反標準orbitの高次Ext消滅。
Oがexceptionalというだけでは適用できない。
https://arxiv.org/abs/1708.00167
Van den Bergh, Existence theorems for dualizing complexes over non-commutative
graded and filtered rings, J. Algebra 195 (1997), 662–679, Theorem6.3（著者版p.7）：
左右noetherian、左右local cohomological dimension有限、左右full chiが入力。
Serre functorの存在からこれらを自動的に得る定理ではない。
https://cantate.be/site/dualcompl.ps
Yekutieli–Zhang, Serre duality for noncommutative projective schemes,
Proc. AMS 125 (1997), 697–707, Theorem4.2（p.705）：
balanced dualizing complexからchiとSerre dualityを得る向き。
https://www.math.bgu.ac.il/~amyekut/publications/nc-serre/paper.pdf
適用条件は一次資料で確認したが、原著の全証明を再検証したとはしない。

[residual categorical Torelli]
Lin–Rampazzo–Zhang, arXiv:2609.10344v1 (2026-09-09), Theorem1.2：
smooth complex del Pezzo degree<=4についてenhanced O_S^perpがSの同型類を決める。
statementを本文で確認し、全証明は独立未監査。
weak境界、任意equivalenceの幾何性、任意AのO^perpの可換幾何性を与えない。
https://arxiv.org/abs/2609.10344

9. 添付原稿との関係と公表上の焦点

既存avatar原稿の定理はordered rulingsと7 exceptional curvesを保つ。
指定頂点u8、P/P^{-1}、shift、structure object、heartを直接gluingと照合する作業は未完了。
現在のbundleは添付原稿の全成果を置換せず、intrinsic認識と成分問題を自己完結に切り出す。

2026-11-11版2のdel_Pezzo_1_2_4_Poisson_quantization稿§7–9は、
Poisson構造に対する形式的中心超曲面量子化の存在を記載する。
§9.1のASregular性はboundary ASregular等を仮定した条件付き命題。
§9.3は全coh(X)変形の網羅性を主張していないと明記する。
本文のweighted認識はそのforward存在と異なり、既存Rからambientをliftする主張である。

gluing、Hilb^1復元、marked 10パラメータ族、filtered E8族は先行研究がある。
本研究の焦点は、普遍点による基点を含むquiver-free表示、
そのHHとKSの自然性、内在的rankの整合性、条件付きweighted認識を用いて、
Oだけのweak markingに対応する成分／heartを正確に認識することである。
初等補題や族そのものの新規性を推測で主張しない。
公表価値はformal比較・局所chart・heart認識の完成度と文献照合を踏まえて再評価する。
