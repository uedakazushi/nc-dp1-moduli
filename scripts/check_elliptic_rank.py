#!/usr/bin/env python3
"""Exact identities and source checks; not a proof of the categorical theorems."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "papers/dp1_anticanonical_models.tex"


def expand(path: Path, stack: tuple[Path, ...] = ()) -> str:
    path = path.resolve()
    if path in stack:
        raise RuntimeError(f"Cyclic TeX input: {path}")
    text = path.read_text(encoding="utf-8")
    def sub(match: re.Match[str]) -> str:
        child = ROOT / match.group(1)
        if child.suffix != ".tex":
            child = child.with_suffix(".tex")
        return expand(child, stack + (path,))
    return re.sub(r"\\input\{([^}]+)\}", sub, text)


def main() -> None:
    n, d, r, s, a, m = sp.symbols("n d r s a m")
    p = 1 + d*n*(n+1)/2
    chi = m + n*a + d*r*n*(n+1)/2
    identities = {
        "Hilbert difference": p - p.subs(n, n-1) - d*n,
        "principal quotient": p - p.subs(n, n-s) - d*s*n - d*s*(1-s)/2,
        "Euler difference": chi - chi.subs(n, n-1) - a - d*r*n,
        "rank coefficient": sp.expand(chi).coeff(n, 2)*2/d - r,
    }
    for name, expression in identities.items():
        if sp.expand(expression) != 0:
            raise AssertionError(f"Failed: {name}: {expression}")
    text = expand(MAIN)
    # The manuscripts have no escaped %-comment interactions in labels.
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    refs = re.findall(r"\\(?:eqref|ref|pageref)\{([^}]+)\}", text)
    duplicates = sorted(k for k, count in Counter(labels).items() if count > 1)
    missing = sorted(set(refs) - set(labels))
    bib = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", text))
    cite_groups = re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", text)
    cites = {key.strip() for group in cite_groups for key in group.split(",")}
    if duplicates or missing or cites-bib:
        raise AssertionError({"duplicate_labels": duplicates, "missing_labels": missing,
                              "missing_citations": sorted(cites-bib)})
    print(f"PASS: {len(identities)} exact identities; {len(labels)} unique labels; "
          f"{len(refs)} references; {len(cites)} citation keys. SymPy {sp.__version__}.")
    print("This check does not prove finite-length, rank-one, or derived equivalence assertions.")


if __name__ == "__main__":
    main()
