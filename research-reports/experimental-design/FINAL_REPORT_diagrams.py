#!/usr/bin/env python3
"""
Generate final report PDF with embedded workflow diagrams.
Requires: Pillow, reportlab (optional), or use pandoc with image embedding.
"""

from PIL import Image
import os
import subprocess

DIAGRAMS = "/home/huawei/src/polariz-masha/research-reports/experimental-design/diagrams"
OUTDIR = "/home/huawei/src/polariz-masha/research-reports/experimental-design"

# First create a combined markdown with images
md_content = r"""---
title: "Final Report: M1/M2 Macrophage Contributions to Colon Cancer DTC Dormancy"
subtitle: "Experimental Design with Workflow Diagrams and Bench Protocols"
date: "May 2026"
version: "1.0"
header-includes:
  - \usepackage{geometry}
  - \geometry{margin=0.7in}
  - \usepackage{graphicx}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{M1/M2 Dormancy Final Report}
  - \fancyhead[R]{Page \thepage}
  - \usepackage[compact]{titlesec}
  - \usepackage{xcolor}
  - \definecolor{linkblue}{RGB}{0,90,160}
  - \hypersetup{colorlinks=true,linkcolor=linkblue,urlcolor=linkblue}
---

\newpage

# Executive Summary

This report presents a comprehensive experimental plan to quantify the causal contribution of M1-like and M2-like macrophage phenotypes to dormancy entry, maintenance, and exit in colon cancer liver metastasis. The study is grounded in a multi-agent research analysis (FINAL_COMPILATION.md) that estimated M1 contributions at ~40% for entry and ~35% for exit, with M2 contributions at ~50% for maintenance and ~35% for exit. **These estimates are mechanistic inferences, not measurements. This experiment aims to generate the first direct quantitative data.**

**Model:** MC38 murine colon adenocarcinoma cells (GFP-Luciferase-Fucci2a reporters) injected intrasplenically into C57BL/6 mice to generate liver metastases.

**Scale:** 330 mice across 4 experimental arms, 7-month timeline, ~$184,000 budget.

**Key innovation:** This is the first study to simultaneously quantify M1 and M2 contributions to each phase of dormancy (entry, maintenance, exit) using selective genetic and pharmacological macrophage manipulation.

\newpage

# Diagram 1: Overall Project Workflow

![Overall project workflow from Phase 0 (cell engineering) through Phase IV (analysis and decision points)](diagrams/diagram1_workflow.png){ width=100% }

\newpage

# Diagram 2: Intrasplenic Injection and Dormancy Timeline

![Timeline from surgery through seeding, dormancy entry, maintenance, and exit phases](diagrams/diagram2_timeline.png){ width=100% }

\newpage

# Diagram 3: Expected Outcomes Decision Tree

![Decision tree showing how experimental results will validate or refute the Temporal Switch Model](diagrams/diagram3_decision_tree.png){ width=100% }

\newpage

# Diagram 4: Readout Hierarchy and Analysis Pipeline

![Three-tier readout hierarchy (primary, secondary, tertiary) with computational analysis pipeline](diagrams/diagram4_readouts.png){ width=100% }

\newpage

# Diagram 5: Macrophage-DTC Interaction Model

![Mechanistic model of M1-driven dormancy entry, M2-driven maintenance, and M2-triggered exit](diagrams/diagram5_interaction.png){ width=100% }

\newpage

# Diagram 6: Tissue Processing Pipeline

![Liver tissue processing at each sacrifice timepoint: IF, flow cytometry, scRNA-seq, and cytokine analysis](diagrams/diagram6_tissue_pipeline.png){ width=100% }

\newpage

# Diagram 7: Four Experimental Arms

![Summary of all four experimental arms with treatment groups, mouse numbers, and research questions](diagrams/diagram7_four_arms.png){ width=100% }

\newpage

# Scientific Rationale

## Hypothesis

Both M1-like (classically activated, pro-inflammatory) and M2-like (alternatively activated, tissue-repair) macrophage phenotypes contribute to dormancy entry and exit in Disseminated Tumor Cells (DTCs), but through distinct mechanisms with different temporal profiles:

- **Dormancy entry:** M1 contribution ~40% (IFN-gamma/p38 MAPK/STAT1 axis), M2 contribution ~25% (TGF-beta2/GJIC)
- **Dormancy maintenance:** M1 ~15%, M2 ~50% (TGF-beta2, GJIC, niche architecture)
- **Dormancy exit:** M1 ~35% (NF-kappaB, inflammatory cytokines), M2 ~35% (angiogenic switch, MMPs, TGF-beta1/NRP2)

## Primary Objective

Quantify the causal contribution of M1-like and M2-like macrophages to each phase of dormancy (entry, maintenance, exit) in colon cancer DTCs using selective in vivo macrophage manipulation in a liver metastasis model.

## Secondary Objectives

1. Identify macrophage-derived signaling molecules necessary and sufficient for dormancy entry vs. exit
2. Determine whether the same macrophage subpopulation maintains and prevents exit, or whether these are distinct subsets
3. Map the single-cell transcriptomic landscape of macrophage-DTC interactions during each dormancy phase
4. Test whether therapeutic M1 repolarization (PI3K-gamma inhibition or STING agonism) awakens dormant DTCs before clearing them

\newpage

# Model System

## Cancer Cell Line: MC38

MC38 murine colon adenocarcinoma (C57BL/6 background) is the primary model, chosen for:
- Compatibility with C57BL/6-based genetic tools (LysM-Cre, CD169-DTR)
- Published protocols for splenic injection to liver metastasis
- Immunocompetent syngeneic model with intact T cells, NK cells, and macrophages

**Engineered reporters:**

| Reporter | Purpose |
|----------|---------|
| GFP/Luciferase | BLI tracking + flow cytometry identification |
| Fucci2a | Real-time cell cycle (red=G1 dormant, green=S/G2/M proliferating) |
| H2B-mCherry | Nuclear label for single-cell tracking |

## Mouse Strains

| Strain | Purpose |
|--------|---------|
| C57BL/6J | Wild-type control |
| LysM-Cre x Nos2fl/fl | M1 impairment (no iNOS in myeloid cells) |
| LysM-Cre x Arg1fl/fl | M2 impairment (no arginase-1 in myeloid cells) |
| CD169-DTR | Kupffer cell-specific depletion |
| Cx3cr1-CreERT2 x Rosa26-DTA | Recruited monocyte-derived macrophage depletion |

## Metastatic Niche: Liver

The liver is the primary metastatic site for colon cancer. Kupffer cells (liver-resident macrophages, ~80-90% of hepatic macrophages) are the first cells DTCs encounter upon arrival. The distinction between Kupffer cells and recruited monocyte-derived macrophages is critical for interpreting M1/M2 contributions.

\newpage

# Experimental Design

## Arm A: Total Macrophage Depletion (n=60 mice)

**Question:** Are macrophages required for dormancy regulation?

| Group | Treatment | Start | Expected |
|-------|-----------|-------|----------|
| A1 | PBS liposomes (control) | Day 1 | Dormant DTCs persist |
| A2 | Clodronate liposomes (early) | Day 1 | Reduced entry or maintenance |
| A3 | Clodronate liposomes (late) | Day 14 | Impaired maintenance |
| A4 | Clodronate + CD169-DTR + DT | Day 14 | Kupffer-specific effect |

**Protocol:** 200 uL IV or IP twice weekly. Verify >80% depletion by flow cytometry.

## Arm B: M1 Impairment (n=90 mice)

**Question:** Are M1 macrophages required for dormancy entry?

| Group | Genotype/Treatment | Expected |
|-------|-------------------|----------|
| B1 | LysM-Cre x Nos2fl/fl | Entry rate: 65% to ~40% |
| B2 | LysM-Cre control | No change |
| B3 | Anti-IFN-gamma Ab (early) | Entry rate: ~40% |
| B4 | Anti-IFN-gamma Ab (late, Day 7) | Maintenance unaffected |
| B5 | Isotype controls | Baseline |

**Primary endpoint:** Dormancy entry rate (Ki67- NR2F1+ GFP+ cells / total GFP+) at Day 7.

## Arm C: M2 Impairment (n=90 mice)

**Question:** Are M2 macrophages required for dormancy maintenance?

| Group | Genotype/Treatment | Expected |
|-------|-------------------|----------|
| C1 | LysM-Cre x Arg1fl/fl | Maintenance: 8wk to ~4wk |
| C2 | Anti-IL-4Ralpha Ab (from Day 14) | Maintenance: ~5wk |
| C3 | CD169-DTR + DT (from Day 14) | Kupffer contribution |
| C4 | Cx3cr1-CreERT2 x DTA | Recruited MoM contribution |
| C5 | Controls | Baseline 8wk |

**Primary endpoint:** Dormancy maintenance duration (Kaplan-Meier, log-rank test).

## Arm D: Temporal Switch (n=90 mice)

**Question:** Does M2-to-M1 switching trigger dormancy exit?

| Group | Treatment | Expected |
|-------|-----------|----------|
| D1 | IL-4 complex -> IFN-gamma+LPS (switch) | Exit at ~3wk post-switch |
| D2 | IL-4 complex sustained (M2) | Prolonged dormancy >10wk |
| D3 | IFN-gamma + poly(I:C) sustained (M1) | Early inflammatory exit ~4wk |
| D4 | Switch + anti-PD-1 | Exit + clearance |
| D5 | PI3K-gamma inhibitor (eganelisib) | Gradual repolarization ~5wk |
| D6 | PBS vehicle | Natural kinetics |

**Critical comparison:** D4 vs D1 -- does anti-PD-1 convert "awakening" into "clearance"?

\newpage

# Statistical Framework

## Power Analysis

| Comparison | Effect Size | Alpha | Power | n per group |
|-----------|-------------|-------|-------|-------------|
| Dormancy entry rate (Arm B) | 65% vs 40% (25% diff) | 0.05 | 0.80 | 15 |
| Maintenance duration (Arm C) | HR=2.0 (8wk vs 4wk) | 0.05 | 0.80 | 15 |
| Temporal switch (Arm D) | 3wk vs 8+ wk | 0.05 | 0.80 | 15 |

## Statistical Tests

| Comparison | Test | Correction |
|-----------|------|-----------|
| Dormancy fraction | Fisher's exact | Bonferroni (6 arms) |
| Time to metastasis | Kaplan-Meier + log-rank | Bonferroni |
| p-ERK/p-p38 ratio | Mann-Whitney U | Holm-Bonferroni |
| scRNA-seq DEGs | Wilcoxon rank-sum | Benjamini-Hochberg FDR |
| Cytokine levels | One-way ANOVA + Tukey | Tukey HSD |
| Longitudinal BLI | Mixed-effects model | FDR |

**Total: 330 mice across 4 arms, 7-month timeline, ~$184,000.**

\newpage

# Expected Outcomes and Decision Criteria

## Predicted Results

| Arm | Key Group | Predicted Entry Rate | Predicted Maintenance |
|-----|-----------|:-------------------:|:--------------------:|
| A | A1 (control) | ~65% | ~8 weeks |
| A | A2 (all depleted, early) | ~30% | ~3 weeks |
| B | B1 (M1-impaired) | ~40% | ~7 weeks |
| C | C1 (M2-impaired) | ~60% | ~4 weeks |
| D | D1 (M2->M1 switch) | ~65% | Exit at ~3wk post-switch |
| D | D2 (sustained M2) | ~65% | >10 weeks |
| D | D4 (switch + anti-PD-1) | ~65% | Exit + clearance |

## Decision Framework

**Scenario 1 (Both contribute):** B1 shows reduced entry AND C1 shows reduced maintenance. D4 shows clearance.
-> Proceed to therapeutic testing. Design Phase I trial (PI3K-gamma inhibitor + anti-PD-1).

**Scenario 2 (Only M2):** B groups show no effect; only C groups change dormancy.
-> Revise model. Focus on M2-targeted maintenance strategies.

**Scenario 3 (Only M1):** C groups show no effect; only B groups affect dormancy.
-> Revise model. Focus on IFN-gamma/p38 pathway.

**Scenario 4 (Neither alone):** Only total depletion (Arm A) shows phenotype.
-> Macrophage contribution is non-specific (headcount, not phenotype).

\newpage

# Key Reagent and Vendor Summary

| Reagent | Vendor | Catalog | Dose/Schedule |
|---------|--------|---------|---------------|
| Clodronate liposomes | Liposoma BV | CP-005-005 | 200 uL IV, 2x/week |
| PBS liposomes | Liposoma BV | PB-005-005 | 200 uL IV, 2x/week |
| CpG-ODN 1826 | InvivoGen | tlrl-1826 | 50 ug IP, 3x/week |
| Recombinant mouse IL-4 | BioLegend | 574302 | 5 ug + 25 ug anti-IL-4 (complex) |
| Anti-IFN-gamma (XMG1.2) | Bio X Cell | BP0055 | 200 ug IP, 2x/week |
| Diphtheria toxin | Sigma | D0564 | 4 ng/g IP, every 72h |
| D-Luciferin | GoldBio | LUCK-1G | 150 mg/kg IP |
| Pexidartinib (PLX3397) | Selleckchem | S7818 | 290 mg/kg chow |
| Eganelisib (IPI-549) | Selleckchem | S8330 | 30 mg/kg oral daily |
| Anti-PD-1 (clone RMP1-14) | Bio X Cell | BP0146 | 200 ug IP, 2x/week |

\newpage

# Acronym Glossary

| Acronym | Full Term |
|---------|-----------|
| ARG1 | Arginase 1 |
| BLI | Bioluminescence Imaging |
| BMDM | Bone Marrow-Derived Macrophage |
| CRC | Colorectal Cancer |
| CSF1R | Colony Stimulating Factor 1 Receptor |
| CX3CR1 | C-X3-C Motif Chemokine Receptor 1 |
| DER | Dormancy Entry Rate |
| DMD | Dormancy Maintenance Duration |
| DT | Diphtheria Toxin |
| DTC | Disseminated Tumor Cell |
| DXR | Dormancy Exit Rate |
| ERK | Extracellular Signal-Regulated Kinase |
| Fucci2a | Fluorescent Ubiquitination-based Cell Cycle Indicator 2a |
| GJIC | Gap Junctional Intercellular Communication |
| IF | Immunofluorescence |
| IFN-gamma | Interferon gamma |
| IL | Interleukin |
| iNOS | Inducible Nitric Oxide Synthase (NOS2) |
| KC | Kupffer Cell |
| MMP | Matrix Metalloproteinase |
| MoM | Monocyte-derived Macrophage |
| NR2F1 | Nuclear Receptor Subfamily 2 Group F Member 1 |
| NRP2 | Neuropilin 2 |
| PD-1 | Programmed Cell Death Protein 1 |
| PI3K-gamma | Phosphoinositide 3-Kinase Gamma |
| scRNA-seq | Single-Cell RNA Sequencing |
| TAM | Tumor-Associated Macrophage |
| TGF-beta | Transforming Growth Factor Beta |
| TLR | Toll-Like Receptor |
"""

# Write the combined markdown
md_path = os.path.join(OUTDIR, "FINAL_REPORT_with_diagrams.md")
with open(md_path, 'w') as f:
    f.write(md_content)

print(f"Combined markdown written to {md_path}")
print(f"File size: {os.path.getsize(md_path)} bytes")
