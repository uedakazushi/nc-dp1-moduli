# 研究方針：次数1の非可換del Pezzo曲面

2026-11-16 / dp1-plan-v1。再開時にはこのファイルを最初に読む。GitHub main を現行の研究正本とする。

## I. 恒常的な研究原則と保存許可
数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し、研究目標と方針を柔軟に変更する。重要な変更では理由、解決済みの事項と残された元の問題を現行方針に簡潔に整理するが、変更履歴を蓄積しない。証明済み、追加仮定に依存、未完成、予想、計算的観察を明確に区別する。仮定、既知入力、証明の所在、未解決箇所を明示し、原稿に証明があること・今回の検証・計算・外部査読を混同しない。誤りは依存する主張と要約にも反映し、有用な障害・反例は現行ノートに保持する。

公表論文では先行研究の一次資料を調べ、既知結果の仮定と本研究の貢献をIntroductionで具体的に比較する。未確認の文献内容や書誌を推測で補わない。日本語LuaLaTeX原稿を標準とし、現在の数学的成果の論理順で構成し、過去の有効な結果や完全な証明を軽量化のために削除しない。研究ノートは現在有効な知識、例、障害、計算と文献比較を保存し、研究日誌、重複する証明、履歴、旧ZIPを含めない。

研究継続用bundleは現行の方針、ノート、公表用論文、最小限のソース、PDF、書誌、計算コード、入力、証明書、再現手順による自己完結した一式とする。研究区切りごとのユーザー承諾不要なLibrary保存が一般的に許可されている。ただし本研究の個別指示ではGitHub mainを正本とし、GitHub保存が成功した場合はLibraryに重複保存せず、GitHub保存失敗時のみ緊急避難に用いる。既存のLibrary資料は指示なく削除しない。ZIP、旧版、変更履歴、PDF/TeX中間生成物、キャッシュをGitで追跡せず、数学的内容と再現性を損なわずに整理する。生成・検証・commit・push・リモート到達確認を別の状態として扱う。

mainに通常のfast-forwardで直接pushし、remote SHAを確認する。GitHub Actions、PR、force pushは使用しない。他者の並行更新を失わず、競合時は取得して内容を統合する。背景処理の自動実行は約束しない。

## II. 本研究固有の目標
非可換次数1 del Pezzo曲面を、quiverやblowdown標識を分類対象に加えず、Ext有限・noetherian Abel圏、Serre関手、心を保つ `tau=S^{-1}[2]`、Gabriel–Krull rank-one torsion-free exceptional構造対象、Artin–Zhang ample pair、および次数1の反標準Hilbert関数から内在的に認識する。反標準環、重み(1,1,2,3)の次数6超曲面、楕円境界・Rains gluing、dg変形、abelian moduli stack、同型群oid・慣性と既約成分を比較する。

成果は `papers/nc_del_pezzo_degree1_moduli.tex` と `papers/dp1_anticanonical_models.tex` に保持する。共鳴の一般次数・四つのheart比較の主原稿は別の現行リポジトリ https://github.com/uedakazushi/nc-cubic-moduli を正本として参照する。依存する結果は特定の版と仮定を明記し、別のリポジトリの最新版を無条件に入力しない。

## III. 現在の主要到達点
- smooth classical degree1 del Pezzo曲面Sと点pによる直交圏と例外対象のdg gluing、HH^2=10、HH^3=0、Kodaira–Spencer写像の同型を含む形式局所候補族を論文化した。これは全intrinsic abelian moduliの既約成分性を意味しない。
- Gabriel–Krull rankと反標準切断増大の関係、構造対象の認識、追加条件の下のweighted sextic正規超曲面表示、楕円境界の中心性、指定avatarと一点Hilbert schemeによる構成・復元を保持する。
- smooth genuine avatarと滑らかな楕円境界からのRains型gluingに限定し、反標準ring qgrとの全q導来比較を記述。有限位数qも排除しない。数値的ampleness、AZ-ampleness、heartの一致と導来同値を区別する。
- 各証明の検証状態は `research/dp1_validation.md`。移管前の原稿の証明を今回新たに独立全面検証したとは扱わない。

## IV. 未解決の核心と優先的着手
1. 構成した10次元dg変形族からsmooth properなabelian heartとrank-one構造対象を復元し、実際のintrinsic moduliの既約成分であることを証明する。有限A-infinity chartと相対同型群oidを比較する。
2. 楕円境界の存在と幾何性、重み付き6次超曲面・中心元の認識の仮定を可能な限り弱める。境界を持たない/特異な例を独立に検討する。
3. 退化境界・非局所自由gluing・weak del Pezzoの根壁でのheart、基底変更、fpqc降下、自然性を調べる。
4. Rains/anticanonicalモデルの一般次数の定理との関係を厳密にし、次数1固有の新規性を一次資料に照らして検証する。

## V. 研究再開と再現
本書 → `research/dp1_research_plan.md` → `research/dp1_research_notes.md` → 二本のTeX原稿 → `research/dp1_validation.md` / `research/dp1_reproduction.md` の順に読む。依存関係の詳細は各論文の文献表および参照節。 `latexmk papers/nc_del_pezzo_degree1_moduli.tex` および `latexmk papers/dp1_anticanonical_models.tex` でLuaLaTeX再生成する。必要な範囲の組版・検算、参照閉包を実施して状態を明記する。