# 次数1の非可換del Pezzo曲面のモジュライ

2026-11-18 / research-v4。再開時は [研究方針](00_research_plan.md) を最初に読む。GitHub mainがソース正本であり、研究の区切りに自己完結した方向別bundleをLibraryへ保存する。

## 現在の到達点

種数1境界による体上の内在的rank認識を、平坦な次数付き環のArtin変形へ持ち上げた。flat対象には総圏のgeneric length = 基底環の長さ × 特殊fiberのrankが成立し、flat tail判定、torsion-free性の持上げ、基底変更を証明した。中心境界元の持上げは不要である。

指定e・相対Serre・RHomの基底変更を持つproper dg変形から平坦反標準環を構成し、De Deken–Lowenの定理を適用して外部の平坦Abel変形を得る。ただし元のdg圏へのheartの実現・全Morita比較・モジュライ成分性は未完成。

非正則Artin基底では自明族でもPerfと全Dbが一致しないため、次の比較先は基底上有限Tor振幅の部分とする。反標準軌道もexceptional helixではなく、有限thread定理を直接適用しない。新原稿の独立の新規性は未確定。

## 現行原稿

- [内在的構造と次数1変形族](papers/nc_del_pezzo_degree1_moduli.tex)：普遍点dg族、HH/KS、有限A∞ chart、抽象rank、条件付きweighted sextic。
- [反標準モデル，内在的rankと共鳴](papers/dp1_anticanonical_models.tex)：既存導来比較と独立な種数1境界のrank認識。
- [Artin変形と内在的rank](papers/dp1_artin_deformations.tex)：今回の9ページの研究companion。独立投稿か既存二稿への統合かは新規性と論理的まとまりの確認後に判断する。

[Artin研究ノート](research/artin_deformation_notes.md)、[全体ノート](research/dp1_research_notes.md)、[具体的計画](research/dp1_research_plan.md)、[検証](research/dp1_validation.md)、[再現](research/dp1_reproduction.md)、[Codex指示](AGENTS.md)。

主稿の特殊楕円qgr-rankを未解決としていた文章の横断修正は今回未実施。現在の解決範囲は反標準モデル論文§6およびArtin原稿§2–5に従う。一般公理からの中心境界認識は依然未解決。

## 再現

```sh
python scripts/check_artin_rank.py
latexmk papers/dp1_artin_deformations.tex
```

新検算はPython3標準ライブラリのみ。既存検算は `requirements-research.txt` のSymPyを使用する。PDF、ZIP、ビルド生成物はGit追跡しない。既存二稿の今回の再組版・独立全面監査は行っていない。

一般次数の共鳴・heart比較は `uedakazushi/nc-cubic-moduli` の外部正本を、参照版と仮定を確認して用いる。
