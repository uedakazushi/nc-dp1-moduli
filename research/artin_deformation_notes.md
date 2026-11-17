# Artin変形：現行の研究知識

2026-11-18 / artin-notes-v1。最初に `00_research_plan.md`。証明全文は `papers/dp1_artin_deformations.tex`、以下のラベルは同稿を指す。新規性未確定、独立査読・形式化は未実施。

## 現在閉じた部分

特殊fiberの仮定(H)は、全Hilbert関数が最終的に二次以下、GK filtrationと多項式次数の一致、generic quotientが単一simpleの半単純圏、Oのtorsion-freenessとrank=2/d×二次係数。中心正則一次元と整なGorenstein種数1 THCR境界からの完全な証明を `prop:field-input` に含めた。

Aは剰余体kの局所Artin k代数、R_Aは次数ごと有限自由、R_A0=A、特殊fiberR。nilpotent m-filtrationからR_Aのnoetherian性・有限生成を得る。中心g_Aの持上げは必要ない。ここで「平坦Abel変形」という圏全体の性質と「A-flat対象」は異なる。

`thm:artin-rank`：p_F^A=Σp_{m^jF/m^{j+1}F}。単純対象のEndは除法環なのでnilpotentなmは零作用。商圏でも同じ論法を用い、GK filtrationを持ち上げる。generic quotientは一つのsimpleを持つlength圏だが、半単純とは限らない。絶対長さλ_A(F)=Σrank(F_j)=2/d×二次係数。

`lem:flat-tail`：F=πMのA-flatness ⇔ πTor¹_A(k,M)=0 ⇔ M_nがn≫0で有限自由。Tor加群が有限生成であることをnoetherian性から確認して初めて「一様なtail」を取る。固定nのflatnessから無限個のZariski開を取る議論ではない。

`thm:relative-rank`：A-flatならF_j=(m^j/m^{j+1})⊗F_k、λ_A(F)=length(A) rank(F_k)。相対rankはfiberで定義する。純性の持上げにはAnn_F(m)=soc(A)⊗F_kを使い、仮想的な低次元部分対象の最後の非零m層をここへ単射させる。R_Aのdomain性を使わず証明できる。flat tailのtensorから任意の局所Artin基底変更に対応する。

## 非flat対象と相対heartの障害

A=k[ε]/ε^ell、F=π(R_A/ε^jR_A)、1≤j<ellでは特殊fiberがOでもλ_A(F)=j。λ_A/ellを全対象のrankと呼ぶと分数になる。正規化はflat対象に限る。O_Aは相対rank1だが絶対長さellであり、generic quotientはεの非零作用を持つため半単純でない。

二重数基底の自明族ではG=O_{S_A}⊗kのExt^j(G,G)=kが全j≥0で非零。Perf(S_A)はproperなA線形圏だがDb(coh S_A)は同じ圏ではない。二項perfect complex [O --ε→ O]のcohomologyはGなので標準t構造はPerfへ制限されない。任意のbounded heart不存在は主張しない。

この障害から、研究目標の「proper dg変形の内部に通常のcoherent heartを復元する」は一般に修正が必要。大きな導来圏のheartと、その相対perfect部分を区別する。相対perfectとは基底上有限Tor振幅であり、proper scheme上ではさらにpushforwardがperfectとなるが、単なる大域切断のperfectnessを定義として使わない。

## 反標準環による外部Abel変形

`thm:abelian-envelope`：実際のproper dg変形T_A、Oを持ち上げるe_A、相対Serre S_A、RHomとτ=S_A^{-1}[2]の基底変更、τの冪のcoherenceを仮定。K_n=RHom(e_A,τ^n e_A)はA-perfect、特殊fiberは次数0のk^{1+n(n+1)/2}。minimal perfect complexの判定で全n≥0に同時に自由性と基底変更を得る。積は合成由来なのでgraded algebraとして両立する。

得られたR_AのqgrはDe Deken–Lowen Proposition4.4とLowen–Van den Bergh Theorem8.8の適用で平坦Abel変形となる。一般の変形定理は既知で、本研究の新規定理として扱わない。e_Aの持上げ・相対Serreの存在は入力のままであり、HH²=10から自動的に全てを得たとは言わない。

この方法は外部にAbel圏を作るが、元のT_AとDb_{A-perf}(qgr R_A)との比較functorは未構成。`lem:lift-equivalence` は比較と右随伴・単位余単位の基底変更を構成できた後、特殊fiber同値から全体同値を出す出口であり、構成自体の代用ではない。

## Z-代数と有限presentationの比較

反標準ample sequenceはDe Deken–Lowen Theorem4.5の正方向Ext¹,²消滅を満たすので、Abel変形はZ-代数変形で表せる。しかし通常のgraded algebraへ戻すにはcoherentな添字移動のデータが別途必要。

Ext²(τ^{i+1}e,τ^i e)=kだから反標準軌道は二項exceptional sequenceさえない。Theorem5.15のgeometric helix/finite thread比較を直接適用しない。既存の長さ11full exceptional collectionとの比較を別に作る必要がある。

## 文献と確認範囲

O. De Deken, W. Lowen, Abelian and derived deformations in the presence of Z-generating geometric helices, J.Noncommut.Geom.5(2011),477–505, DOI10.4171/JNCG/83。arXiv:1001.4265v3(2010-09-14)のProposition4.4、Theorem4.5、Proposition4.6を本文・PDF画像で確認。Theorem5.15は追加仮定の区別に用いる。公刊版とarXivの番号差の可能性を避け、原稿では参照版を明記した。
https://arxiv.org/abs/1001.4265
https://doi.org/10.4171/JNCG/83

W. Lowen, M. Van den Bergh, Deformation theory of abelian categories, Trans.AMS358(2006),5441–5483。arXiv:math/0405226の§8.5 Theorem8.8を本文・PDF画像で確認。全原著の独立再証明ではない。ページ範囲は著者の文献一覧でも確認した。
https://arxiv.org/abs/math/0405226
https://wendylowen.com/writing

Stacks Tags051E（Artin環上のflatness）、0656（perfect）、0A5Q（二重数例）、0DHZ（相対perfect）を本文確認。
https://stacks.math.columbia.edu/tag/051E
https://stacks.math.columbia.edu/tag/0A5Q
https://stacks.math.columbia.edu/tag/0DHZ

F. Genovese, W. Lowen, J. Symons, M. Van den Bergh, Deformations of triangulated categories with t-structures via derived injectives, arXiv:2411.15359(2024)。今回abstractを確認した関連先行研究。bounded t-deformationsとderived injective ind-dg objectsの変形比較を扱う。本文の全仮定・証明は今回未監査であり、当原稿の証明には入力しない。今後の大きな導来圏のheartの比較で優先的に確認する。
https://arxiv.org/abs/2411.15359

体上のrankの基礎入力は原稿のAV、Keeler、CKS、AOU参照。今回新たにそれら全原著の全面監査をしたとはしない。既存Rains全q導来比較、HH/KS、有限A∞成分の全面監査も別課題である。

## 次の着手

古典特殊fiberと指定e/Serreに限定し、T_Aから大きなD(QGr R_A)への導来切断を定義する。像が有界coherentかつ有限A-Tor振幅であること、対象間RHomのA-perfectness、右随伴、unit/counitの基底変更を順に示す。そこが閉じればLemma8.2を使う。全Dbを比較先にしてNakayamaを適用してはいけない。
