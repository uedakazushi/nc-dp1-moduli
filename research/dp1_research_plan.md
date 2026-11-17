# 次数1 nc del Pezzo：現在の具体的研究計画

2026-11-18 / dp1-strategy-v4。一般原則・保存許可・到達点は `00_research_plan.md`。Artin方向の詳細は `research/artin_deformation_notes.md`、その他の有効な知識と文献比較は `research/dp1_research_notes.md` に保持する。

## 成功条件と段階

普遍点(S,p)の10次元dg族を、構造対象とAbel圏の内在的モジュライへ接続する。段階は実際のdg族、finite directed A∞表示、pointed Morita変形、相対Abel圏と同型groupoid、成分・全分類に分かれる。HH²=10、HH³=0、KS同型から後半を自動的に結論しない。独立に公表価値のある局所結果は全分類待ちにしない。

## 閉じた部分と新しい境界

種数1境界を持つ体上の環についてrank-one/torsion-free性は反標準稿§6で認識済み。Artin稿§4–5ではnilpotent基底のGK filtration、flat tail、λ_A(F)=length(A) rank(F_k)、torsion-free持上げを証明。任意の局所Artin基底変更と両立し、中心g_Aの存在は要求しない。

Artin稿§6は実際のproper dg変形とe_A、相対Serre、RHom/τのbase changeを仮定して反標準環を構成し、既知のDe Deken–Lowen理論へ接続する。これは外部のflat Abel変形であり、元のdg圏内のheartや全変形functor同値ではない。各入力の存在を独立に検証する必要がある。

## P0：相対perfect比較

二重数自明族でもPerf(S_A)≠Db(coh S_A)。比較先をDb_{A-perf}(qgr R_A)に修正する。まず古典特殊fiberで、導来切断をD(QGr R_A)へ定義し、像の有界coherent性・有限A-Tor振幅、RHomのA-perfectnessを示す。次に右随伴を構成し、unit/counitを含む基底変更を確認する。最後にArtin稿Lemma8.2の特殊fiberによる同値判定を用いる。随伴を仮定した補題を随伴構成の代わりにしない。

関連するGLSV arXiv:2411.15359のt構造付き変形理論は、今回abstractのみ確認した。大きな導来圏とderived injective ind-dg objectsの比較がどこまで使えるか、本文の仮定を次に点検する。properな小圏への標準t構造の制限は仮定しない。

## P1：全形式変形とgroupoid

De Deken–Lowen Theorem4.5は反標準ample sequenceに適用できるが、Z-代数から通常のgraded algebraへ戻すcoherentな周期性は別途必要。Ext²(τ^{i+1}e,τ^ie)=kなので反標準軌道へTheorem5.15のgeometric helix/finite threadを流用しない。

既存長さ11のfull exceptional collectionのlift、relative transfer、curvature、inner stabilizerを処理して全Morita変形との比較を行う。基点bのBertini作用、stack/coarse、Poincaré正規化とavatar族の相対同値も同型groupoidの一部として扱う。generic finitenessや有限型atlasが実際に構成されるまではintrinsic成分性を宣言しない。

## P2：既存上流定理の監査

Rainsの中心境界環、smooth elliptic全q導来比較のInd orbit生成・境界trace・pseudo-perfect表現可能性、有限位数σのYZ入力を照合する。HH/KSのbar自然性、finite A∞ chartの相対split contraction、gaugeとの比較も確認する。旧原稿に証明があることと今回の監査済み状態を区別する。

長い主稿の特殊楕円qgr-rank未解決表示を反標準稿§6とArtin稿へ参照整理する課題は残る。一般公理から中心境界を得る問題まで解決したと読み替えない。

## P3以降：退化・認識・分類

Bl_b(S)→P¹の相対Picard/compactified Jacobianと普遍点族を、smooth境界、nodal/cuspidalのsmooth点、特異点の非局所自由gluingに分けて比較する。rank認識の拡張済み範囲と導来比較の未完成範囲を区別する。

中心元Z(R)₁≠0、種数1境界の幾何性、weighted ASregular被覆の自動認識は高リスクの独立問題。Rains arXiv:2504.16187 §16.4、EG、Okawa–Uedaとの新規性比較を続ける。Hilbert型と最小生成元を区別する。

weak Sの(-2)曲線のorbit直交、自然関手の核、任意derived equivalenceの不存在、targetの特異性は別々に判定する。Ascher–Bejleriの可換compactificationとの比較と標識忘却は、この基盤が閉じてから進める。

## 原稿と再現

既存二稿を保持し、新Artin稿は補助的な研究companionとして扱う。第三の独立投稿とするか統合するかは、新規性と中心定理のまとまりを確認して判断する。必要な証明を削って形式的に短くしない。

`python scripts/check_artin_rank.py`、`latexmk papers/dp1_artin_deformations.tex`。実施済みの範囲は `research/dp1_validation.md`。各bundleは対象方向を明記し、その方向の再開に旧会話・旧ZIPを要しない一式にする。
