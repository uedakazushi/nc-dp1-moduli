# Codex研究指示：次数1の非可換del Pezzoモジュライ

2026-11-18 / dp1-codex-v4。最初に `00_research_plan.md`、`research/artin_deformation_notes.md`、`research/dp1_research_plan.md`、現行原稿・検証情報を読む。全体の既存資産は `research/dp1_research_notes.md` も参照する。

## 現在の確立範囲

体上の種数1境界によるGK-rank認識は反標準モデル論文§6。Artin原稿§4–5は次数ごとflatな環のnilpotent基底でのfiltration、flat tail、relative rank、torsion-free持上げ、base changeを証明する。中心g_Aの持上げを仮定しない。新規性未確定。

Artin原稿§6は指定e/relative Serre/RHom base changeを入力して平坦反標準環を構成し、既知のDe Deken–Lowen定理で外部のflat Abel変形を得る。元圏へのheart埋込み、全Morita同値、moduli成分性を得たとはしない。

## 最優先の作業

1. 比較先を全Db(qgr R_A)ではなく有限A-Tor振幅部分とし、導来切断・右随伴・unit/counitの基底変更を構成する。二重数自明族のPerf≠Dbを必ず試験に使う。
2. Z-代数の同時添字移動のcoherence、e/Serreの持上げと変形groupoid、full exceptional collectionとの比較を処理する。反標準軌道はExt²(τe,e)=kなのでgeometric helixの有限thread定理を直接使わない。
3. 既存のRains全q導来比較、finite-order入力、HH/KS・finite A∞ chartを独立監査する。主稿に残る特殊楕円qgr-rank未解決表示を現行結果への参照へ整理し、有効な証明を削除しない。
4. 一般公理からの中心境界認識、特異境界での導来比較、非局所自由gluing、weak壁と標識忘却は別課題として保持する。

## 作業原則

研究価値の最大化を優先し、完全分類待ちで独立した成果の公表を止めない。原稿は日本語LuaLaTeX。証明・引用の適用・今回の検算・組版・新規性を区別する。全局所Artin基底に関する主張と有限型Zariski開条件を混同しない。

区切りで `python scripts/check_artin_rank.py` と必要な `latexmk` を実行し、方針・ノート・原稿・検証を整合させる。mainへ通常のfast-forwardで直接保存、remote SHA確認。PR、Actions、force pushを使わず、並行変更は取得して統合する。GitにはPDF/ZIP/中間物を追跡しない。現行の自己完結したbundleを追加承諾なしでLibraryへ保存し、その範囲と成功状態を明記する。旧Library資料を削除しない。背景作業は約束しない。
