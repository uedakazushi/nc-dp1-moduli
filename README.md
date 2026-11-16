# 次数1の非可換del Pezzo曲面のモジュライ

2026-11-16。こちらを**次数1 nc del Pezzoの独立した研究の正本**とする。元リポジトリ [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) の次数1専用の研究資産を引き継いだ。再開時は必ず [研究方針](00_research_plan.md) を最初に読む。

## 現行の公表用原稿
- [非可換del Pezzo曲面の内在的構造と次数1変形族](papers/nc_del_pezzo_degree1_moduli.tex)：rank/Artin–Zhang・10次元dg候補族・weighted sextic・復元・内在的モジュライ。
- [楕円境界を持つ非可換del Pezzo曲面の反標準モデルと共鳴](papers/dp1_anticanonical_models.tex)：指定Rains gluingと反標準qgrの導来比較、共鳴、境界の制約。

[現行研究ノート](research/dp1_research_notes.md) / [テーマ固有の計画](research/dp1_research_plan.md) / [検証状態](research/dp1_validation.md) / [再現手順](research/dp1_reproduction.md) / [Codex指示](AGENTS.md)

## 主要な成果と未解決点
次数1 del Pezzoの一点によるdg gluing、HH^2=10・HH^3=0、KS比較、Gabriel–Krull rank、追加仮定下の非可換重み付き6次超曲面認識、滑らかな楕円境界での導来比較を保持する。全intrinsic abelianモジュライの既約成分性、特異楕円境界、weak境界、非局所自由gluingなどは未完成。既存原稿の証明と移管後の独立再監査を区別する。

## 再現
```sh
latexmk papers/nc_del_pezzo_degree1_moduli.tex
latexmk papers/dp1_anticanonical_models.tex
```
LuaLaTeX・latexmk・LuaTeX-ja・必要なTeXパッケージを使用。PDF・SyncTeX・ビルドログは再生成し、Gitには追跡しない。

## 他研究との関係
Rains共鳴の一般次数の結果と四つのheartの比較は、引き続き [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli) が現行正本。非可換三次三様体は [nc-cubic-threefold-moduli](https://github.com/uedakazushi/nc-cubic-threefold-moduli) が正本。依存の仮定と版は主原稿に明記し、別リポジトリの古いノート復元を必要としない。