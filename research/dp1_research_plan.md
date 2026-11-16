# 次数1の非可換del Pezzo曲面：研究方針

2026-11-15 / integration-v3（大域次元公理の冗長性を整理）。再開時は`00_research_plan.md`、本書、`research/dp1_research_notes.md`、二つの現行TeX論文を読む。一般原則と保存許可は上位計画に置き、この文書には次数1固有の計画だけを記す。

## 目標と達成基準

quiverを分類対象に含めず、Ext有限・noetherianな非零abel圏、Serre関手とheartを保つ反Serre作用、rank-one torsion-free exceptional構造対象、Artin–Zhang ample pair、次数1のHilbert関数からweakly marked nc dP1を定義する。homological dimension 2はSerre双対性から自動的に従い、独立公理にはしない（命題prop:serre-heart-hdim）。可換dP1を含む10次元の候補族のintrinsicな既約成分性を証明し、幾何学的avatar、重み付き次数6超曲面、反標準qgrおよび弱標識の忘却と比較する。

特に、Rains型の数値的amplenessの共鳴条件と、導来圏の変化・homological singularityを厳密に区別する。公表に必要なのは仮定・同値関係・自然性・全射性を揃えた正確な定理と証明である。

## dense resonanceでの確定結果（次数1も含む）

`papers/nc_del_pezzo_resonance_hearts.tex`：Rainsのsimple-root既約sheaf存在条件の下、m=chi(e,M)に対して全tau-orbitでHom=max(m,0)、Ext¹=max(-m,0)、Ext²=0を証明。Rainsの導来双対R adによりm>0のExt¹消滅も解決。m<0では反標準AZ ampleが失敗し、自然導来切断の像はanticanonical qgrの次元(-m)の境界外アフィン表現[-1]、m>0では次元mの表現がdegree0、m=0ではMは導来的に不可視（genuine smooth avatarではm0共鳴が不在）。正負それぞれの共鳴が次数1の一般位置楕円blowup族でもdense。導来非同値・qgr特異化は従わない。既存`papers/dp1_anticanonical_models.tex`が主張する全q導来同値の独立監査は未実施。一般の研究ノートは`research/resonance_hearts.md`。

## Rains resonanceの非既約sheafと導来比較の検証条件

現行`papers/sections/resonance_extension_cancellation.tex`において、境界と交わらない一次元以下のsheafのextension-closed exact category Zでは、自然導来切断が振幅[0,1]を持ち、2つのcohomologyはA=R/(g-1)の有限次元加群となる。短完全列からの6項A線型完全列と、正負指数根の混合拡大のconnecting map δのrank公式を証明した。δが同型なら非零の中間sheafが自然導来切断で消えるので、既存dP1の全q導来同値の独立監査に使う。異なる根αβのExt¹次元はα·β、根の和が根となりmα+mβ=0の共鳴交叉はgenuine smooth avatarで不可能。既存全q導来同値は独立再監査していない。

## 現在有効な到達点と証明の所在

- **内在的rank・section環**：`papers/nc_del_pezzo_degree1_moduli.tex` の`sec:intrinsic-rank`。Gabriel–Krull長さをrankとし、適切なample条件の下でgeneric quotientのsemisimplicity、rankの加法性、反標準環の整域性、切断の二次増大を証明している。次数3と同じ数値的な一般化は`research/common_del_pezzo_framework.md`参照。
- **weighted sextic の条件付き認識**：同稿`sec:weighted-recognition`。中心正則一次元と適切な3次元AS正則境界被覆の存在を仮定した4次元AS正則ambientと正規6次商、追加条件での中心性。これらの仮定は全内在的対象から未証明。
- **10次元候補族**：同稿`sec:pointed-dg-family`。smooth genuine dP1の点pに対する相対mutated idealのgluing。p=bで可換曲面、適切なp≠bで楕円境界avatarを表す。Hochschild、Kodaira–Spencer計算と補助的な有限A-infinity chartの成分性が本文にある。全intrinsic abel moduliの既約成分性は未証明。
- **反標準モデル比較（特殊領域）**：`papers/dp1_anticanonical_models.tex`。滑らかなgenuine S、滑らかなE、q∈Pic^0(E)のRains型gluingについて、反標準qgrとの導来比較・homological dimension 2を主張し、証明を記載している。原稿の著者による点検と今回のGit統合時の独立検証を区別する。数値的共鳴のdense性だけからAZ失敗や導来圏消失を推論しない。
- **avatar・marking**：元の次数1avatarは順序付きrulingと例外曲線7本も指定する。構造対象Oだけのweak markingとの全単射は得られていない。固定した可換幾何的実現でのdg Yoneda復元と、無標識同値の降下は別問題。

## 最優先の未解決問題と具体的な着手

1. **特異反標準境界**：nodal/cuspidal EのTHCR、Serre作用、finite cohomological dimension と境界traceの比較を確立。特異点pで非局所自由となるmutated idealについては、line bundle gluingの公式を流用せず相対perfect moduleから調べる。
2. **閉性と導来圏**：自然な導来section functorの核、任意の導来同値の不存在、qgrのhomological singularityを分離。共鳴条件の各整数層の一般点で具体的に検査する。稠密な共鳴を稠密な導来変化と同一視しない。
3. **weak境界**：Sに(-2)-曲線がある場合のorbit直交と収縮先の核・singularity categoryを決定。曲線型avatarのeffective-root条件と区別する。
4. **intrinsic abelian 認識**：qgr心のGabriel–Krull rankとtorsion-free性、自然なheartの構成、AZ ample locusの本当の幾何を検証。既存dg componentをそのままabel moduliの成分と呼ばない。
5. **全parameterのweighted sextic・moduli**：中心/正規一次切断の自然変換、境界AS被覆の相対化、finite presentation chartから内在的pointed圏への同値とmarking忘却を比較。

## 関係する他の研究

次数3の内在的公理と正規一次境界からのAS4認識は`papers/weak_cubic_axioms.tex`、三次曲面avatarと関係代数の研究は`papers/cubic_surface_ambient_moduli.tex`。上位方針の共通課題とこの次数1特有の研究を混同しない。三次三様体研究の主張・検算は改変しない。

## 検証と再現

`research/dp1_validation.md`に取得資料・今回の組版と追加監査の範囲を記録する。`latexmk papers/nc_del_pezzo_degree1_moduli.tex`、`latexmk papers/dp1_anticanonical_models.tex`。GitではPDF・生成物・ZIPを追跡せず`build/`で組版する。主論文に証明が記載されていること、新たに証明を点検したこと、既知結果の引用、新規性未確認を常に区別する。
