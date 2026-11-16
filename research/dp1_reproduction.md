# dP1：再現手順と資料間の参照

2026-11-15 / integration-v1

リポジトリrootで以下を実行する。

```sh
latexmk papers/nc_del_pezzo_degree1_moduli.tex
latexmk papers/dp1_anticanonical_models.tex
```

既存の`.latexmkrc`に従い、PDF、aux、SyncTeX等は`build/`へ出力する。外部bibliographyファイルや画像を必要とせず、TeXソースだけで本文を再生成できる。必要な依存：LuaLaTeX、ltjsarticle、amsmath、amsthm、mathtools、booktabs、enumitem、hyperref、geometry、fix-cm（必要に応じてTeX Live標準パッケージ）。

論文 `nc_del_pezzo_degree1_moduli.tex` は全体論文、`dp1_anticanonical_models.tex` は共鳴に焦点を当てた専門論文である。重複する説明は、それぞれの論文が独立に読めるための最小限にしてある。研究再開時の現行方針は `00_research_plan.md` → `research/dp1_research_plan.md` → `research/dp1_research_notes.md` の順。研究過去版を要しない。

`research/dp1_validation.md` は実際に実行した検証の状態を明記する。既存の三次曲面・三次三様体の計算資産はこれら2論文の再組版には不要。
