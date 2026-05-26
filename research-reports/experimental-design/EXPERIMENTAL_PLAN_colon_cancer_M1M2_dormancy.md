# EXPERIMENTAL DESIGN: Quantitative Dissection of M1 and M2 Macrophage Contributions to Dormancy Entry, Maintenance, and Exit in Colon Cancer

**Document Status:** DRAFT — Incorporating postdoc research findings as they arrive
**Date:** 26 May 2026
**Principal Investigators:** [To be assigned]
**Based on:** FINAL_COMPILATION.md, Section 4.8 (Temporal Switch Model and Quantitative Estimation)

---

## 1. SCIENTIFIC RATIONALE

### 1.1 Hypothesis

Our integrated analysis (FINAL_COMPILATION.md, Section 4.8) estimates that BOTH M1-like and M2-like macrophage phenotypes contribute to dormancy entry and exit in disseminated tumor cells (DTCs), but through distinct mechanisms with different temporal profiles:

- **Dormancy entry:** M1 contribution ~40% (Interferon gamma [IFN-gamma]/p38 Mitogen-Activated Protein Kinase [p38 MAPK]/Signal Transducer and Activator of Transcription 1 [STAT1] axis), M2 contribution ~25% (Transforming Growth Factor beta 2 [TGF-beta2]/Gap Junctional Intercellular Communication [GJIC])
- **Dormancy maintenance:** M1 ~15%, M2 ~50% (TGF-beta2, GJIC, niche architecture)
- **Dormancy exit:** M1 ~35% (Nuclear Factor kappa-light-chain-enhancer of activated B cells [NF-kappaB], inflammatory cytokines), M2 ~35% (angiogenic switch, Matrix Metalloproteinases [MMPs], TGF-beta1/Neuropilin 2 [NRP2])

**These estimates are based on mechanistic inference, not quantitative measurement.** This experiment aims to generate the first direct quantitative data testing these proportions.

### 1.2 Primary Objective

Quantify the causal contribution of M1-like and M2-like macrophages to each phase of dormancy (entry, maintenance, exit) in colon cancer disseminated tumor cells, using selective in vivo macrophage manipulation in a liver metastasis model.

### 1.2 Secondary Objectives

1. Identify the macrophage-derived signaling molecules that are necessary and sufficient for dormancy entry vs. exit
2. Determine whether the same macrophage subpopulation maintains dormancy and prevents exit, or whether these are distinct subsets
3. Map the single-cell transcriptomic landscape of macrophage-DTC interactions during each dormancy phase
4. Test whether therapeutic M1 repolarization (via PI3K-gamma inhibition or STING agonism) awakens dormant colon cancer DTCs before clearing them

---

## 2. MODEL SYSTEM

### 2.1 Cancer Cell Lines

| Cell Line | Species | Dormancy Capacity | Rationale |
|-----------|---------|-------------------|-----------|
| **MC38** | Mouse (C57BL/6) | Reported dormancy in liver; syngeneic → immunocompetent | Primary model — allows full immune system, genetic tools, macrophage manipulation |
| **CT26** | Mouse (BALB/c) | Aggressive, limited dormancy — negative control | Comparison of dormancy-prone vs. aggressive phenotype |
| **HT-29** | Human | Moderate dormancy capacity in 3D culture | For in vitro validation and patient-relevant organoid studies |
| **SW620** | Human | Derived from lymph node metastasis; dormancy reported | In vitro and patient-derived xenograft (PDX) validation |

**Primary model: MC38 in C57BL/6 mice** — this is a well-characterized, immunocompetent colon adenocarcinoma model that allows:
- Genetic macrophage manipulation via Cre/lox and DTR (Diphtheria Toxin Receptor) systems
- Syngeneic immune system with intact T cells, Natural Killer (NK) cells, and macrophages
- Published protocols for splenic injection → liver metastasis

**MC38 cells will be engineered with:**
- **GFP (Green Fluorescent Protein) / Luciferase dual reporter** — GFP for single-cell detection in tissue sections, Luciferase for in vivo bioluminescence imaging (BLI) of tumor burden
- **Fucci2a cell cycle reporter** — Fluorescent Ubiquitination-based Cell Cycle Indicator; red = G1 (dormant), green = S/G2/M (proliferating). Allows real-time cell cycle tracking at single-cell level
- **H2B-mCherry (histone-tagged)** — nuclear label for long-term tracking of single dormant DTCs

### 2.2 Mouse Strains

| Strain | Purpose | Source |
|--------|---------|--------|
| **C57BL/6J** | Wild-type control; host for MC38 cells | Jackson Labs #000664 |
| **C57BL/6-Tg(CAG-EGFP)131Osb/LeySopJ** | Universal GFP for control imaging | Jackson Labs |
| **Csf1r-CreERT2** x **Rosa26-DTA** | Tamoxifen-inducible macrophage depletion (all macrophages via Colony Stimulating Factor 1 Receptor [CSF1R] promoter) | Custom cross |
| **CD169-DTR** | Diphtheria toxin-mediated depletion of tissue-resident macrophages (including Kupffer cells) | Published strain |
| **LysM-Cre** x **Arg1fl/fl** | Myeloid-specific arginase-1 knockout (impairs M2 function) | Jackson Labs |
| **LysM-Cre** x **Nos2fl/fl** | Myeloid-specific iNOS knockout (impairs M1 function) | Custom cross |
| **Rosa26-LSL-tdTomato** x **Csf1r-CreERT2** | Macrophage lineage tracing (tdTomato marks all CSF1R+ cells after tamoxifen) | For identifying macrophages in contact with DTCs |
| **Cx3cr1-CreERT2** x **Rosa26-DTA** | Selective depletion of CX3CR1+ monocyte-derived macrophages (recruited, not resident) | Custom cross |

### 2.3 Metastatic Niche: Liver

The liver is the primary metastatic site for colon cancer. Liver-resident macrophages (Kupffer cells) are the dominant macrophage population and differ fundamentally from recruited monocyte-derived macrophages. This organ-specific biology is critical because:

- Kupffer cells constitute ~80-90% of hepatic macrophages under homeostatic conditions
- Recruited monocyte-derived macrophages infiltrate during inflammation/metastasis
- The Kupffer cell vs. recruited macrophage distinction parallels the tissue-resident vs. monocyte-derived distinction identified in our analysis (Dalla et al. 2024)
- Hepatic Stellate Cells (HSCs) and Kupffer cells form a dormancy-regulatory unit (Correia et al. 2021)

---

## 3. EXPERIMENTAL DESIGN

### 3.1 Overview

The experiment consists of **four arms**, each testing a specific aspect of the M1/M2 contribution model:

| Arm | Question | Key Manipulation | Readout |
|-----|----------|-----------------|---------|
| **Arm A: Total Depletion** | Are macrophages required for dormancy? | Clodronate liposomes (deplete all) vs. PBS liposomes (control) | DTC dormancy fraction, time to overt metastasis |
| **Arm B: M1 Impairment** | Are M1 macrophages required for dormancy entry? | LysM-Cre x Nos2fl/fl (M1-impaired) vs. LysM-Cre (control) | Dormancy entry rate, p-p38/p-ERK ratio |
| **Arm C: M2 Impairment** | Are M2 macrophages required for dormancy maintenance? | LysM-Cre x Arg1fl/fl (M2-impaired) vs. LysM-Cre (control) | Dormancy maintenance duration, TGF-beta signaling |
| **Arm D: Temporal Switch** | Does M2→M1 switching trigger exit? | Inducible M2→M1 skewing at defined timepoints | Exit kinetics, clearance vs. outgrowth |

### 3.2 Arm A: Total Macrophage Depletion — Establishing Causality

**Purpose:** Confirm that macrophages are required for dormancy regulation in colon cancer liver metastasis (not just correlated).

**Experimental Groups (n=15 mice per group):**

| Group | Treatment | Expected Outcome (based on our model) |
|-------|-----------|--------------------------------------|
| A1 | MC38-GFP-Luc + PBS liposomes (vehicle control) | Dormant DTCs persist; low BLI signal; eventual outgrowth in some mice |
| A2 | MC38-GFP-Luc + Clodronate liposomes (deplete all macrophages starting Day 1) | Predict: if macrophages maintain dormancy, depletion → more rapid outgrowth. If macrophages drive exit, depletion → prolonged dormancy |
| A3 | MC38-GFP-Luc + Clodronate liposomes (starting Day 14, after dormancy established) | Tests whether macrophages are needed for MAINTENANCE (not just entry) |
| A4 | MC38-GFP-Luc + Clodronate liposomes (starting Day 14) + CD169-DTR + DT (deplete resident Kupffer cells selectively) | Tests tissue-resident vs. recruited macrophage contribution |

**Protocol:**
1. **Day 0:** Splenic injection of 1 × 10^5 MC38-GFP-Luc-Fucci2a cells in 50 µL PBS (intrasplenic, subcapsular) under isoflurane anesthesia. Splenectomy 5 minutes post-injection to prevent local tumor growth.
2. **Days 1-3:** Liver seeding phase. DTCs extravasate into liver parenchyma.
3. **Day 3:** First BLI imaging to confirm seeding. Expect low signal (few proliferative cells + dormant cells below detection).
4. **Day 4-7:** Begin treatment per group assignment.
   - Clodronate liposomes: 200 µL i.v. tail vein, twice weekly
   - PBS liposomes: 200 µL i.v., twice weekly
5. **Weekly:** BLI imaging to monitor tumor burden
6. **Timepoints for tissue harvest:** Day 7 (early), Day 21 (dormancy), Day 42 (maintenance), Day 84 (late/outgrowth)
7. **At each timepoint:** Sacrifice 3-4 mice per group for tissue analysis

**Readouts at each timepoint:**
- Liver tissue: immunofluorescence (IF) for GFP+ DTCs, Ki67 (proliferation marker), NR2F1 (dormancy marker), p-p38, p-ERK
- Macrophage profiling: flow cytometry for CD11b+ F4/80+ CD86+ (M1-like) vs CD11b+ F4/80+ CD206+ (M2-like)
- Cytokine measurement: Multiplex ELISA (Enzyme-Linked Immunosorbent Assay) on liver homogenates — IFN-gamma, TNF-alpha, IL-12 (M1), IL-10, TGF-beta1, TGF-beta2 (M2)
- Single-cell RNA sequencing (scRNA-seq): 10x Genomics Chromium on dissociated liver at Day 21 (dormancy peak) and Day 42 (maintenance). Target: 10,000 cells per sample, minimum 3 mice per group.

**Primary endpoint:** Fraction of GFP+ DTCs that are Ki67- (dormant) vs Ki67+ (proliferating) at each timepoint. Statistical test: Fisher's exact test per timepoint, Kaplan-Meier survival analysis for time to detectable metastasis.

### 3.3 Arm B: M1 Impairment — Testing Dormancy Entry

**Purpose:** Test whether M1-like macrophages are required for colon cancer DTCs to ENTER dormancy (via IFN-gamma/p38/STAT1 pathway).

**Hypothesis:** If M1 contribution to entry is ~40% as estimated, M1 impairment should reduce dormancy entry rate by ~40% (from ~60-70% of DTCs entering dormancy to ~35-40%).

**Experimental Groups (n=15 per group):**

| Group | Genotype | Treatment |
|-------|----------|-----------|
| B1 | LysM-Cre x Nos2fl/fl (M1-impaired: no Inducible Nitric Oxide Synthase [iNOS] in myeloid cells) | MC38 injection |
| B2 | LysM-Cre (control for Cre toxicity) | MC38 injection |
| B3 | Nos2fl/fl (no Cre; control for floxed allele) | MC38 injection |
| B4 | Wild-type C57BL/6 + anti-IFN-gamma neutralizing antibody (200 µg i.p., twice weekly) | MC38 injection |
| B5 | Wild-type C57BL/6 + isotype control antibody | MC38 injection |

**Additional pharmacological M1 inhibition groups (n=10 each):**
| Group | Treatment | Rationale |
|-------|-----------|-----------|
| B6 | C57BL/6 + anti-IFN-gamma-neutralizing Ab starting Day -1 (before injection) | Block M1 entry signal from the start |
| B7 | C57BL/6 + anti-IFN-gamma Ab starting Day 7 (after seeding) | Block M1 during maintenance only |

**Protocol:** Same injection and timeline as Arm A.

**Key readouts:**
- **Day 7 (entry phase):** Quantify fraction of GFP+ DTCs that are Ki67- NR2F1+ (dormant) vs Ki67+ (proliferating)
- **p-p38/p-ERK ratio** in DTCs by intracellular flow cytometry or immunofluorescence
- **IFN-gamma levels** in liver homogenates (should be reduced in B4/B6/B7)
- **scRNA-seq** at Day 7: Focus on DTC transcriptomes (NR2F1, DEC2, p27 expression) and macrophage polarization states

**Primary endpoint:** Dormancy entry rate = (Ki67- NR2F1+ GFP+ cells) / (total GFP+ cells) at Day 7. Compare across groups using chi-squared test.

### 3.4 Arm C: M2 Impairment — Testing Dormancy Maintenance

**Purpose:** Test whether M2-like macrophages are required to MAINTAIN dormancy over extended periods.

**Hypothesis:** If M2 contribution to maintenance is ~50% as estimated, M2 impairment should reduce dormancy maintenance, leading to earlier exit (shorter dormancy duration).

**Experimental Groups (n=15 per group):**

| Group | Genotype/Treatment | Target |
|-------|-------------------|--------|
| C1 | LysM-Cre x Arg1fl/fl (M2-impaired: no Arginase 1 [ARG1] in myeloid cells) | M2 metabolic function |
| C2 | LysM-Cre (control) | — |
| C3 | Wild-type + anti-IL-4R alpha antibody (dupilumab analog, 200 µg i.p. twice weekly starting Day 14) | Block M2 skewing (IL-4/IL-13 signaling via Interleukin 4 Receptor alpha [IL-4Ralpha]) |
| C4 | Wild-type + isotype control | — |
| C5 | CD169-DTR + diphtheria toxin (starting Day 14) | Deplete Kupffer cells (tissue-resident, M2-like) during maintenance phase |
| C6 | Cx3cr1-CreERT2 x Rosa26-DTA + tamoxifen (starting Day 14) | Deplete recruited monocyte-derived macrophages during maintenance |

**Protocol:** Same injection as Arm A. Manipulations begin at Day 14 (after dormancy is established per Arm A pilot data).

**Key readouts:**
- **Days 21, 42, 63, 84:** Dormancy fraction (Ki67- NR2F1+ / total GFP+) at each timepoint
- **Kaplan-Meier analysis:** Time from injection to detectable BLI signal increase (>2-fold above baseline = dormancy exit event)
- **scRNA-seq at Day 42:** Macrophage polarization states in liver; identify which subsets are lost or altered
- **TGF-beta1 and TGF-beta2 levels** in liver homogenates (should decrease in C3 if M2 is main source)
- **GJIC measurement:** Dye transfer assay in liver tissue sections (calcein transfer from macrophages to DTCs)

**Primary endpoint:** Dormancy maintenance duration = time from Day 14 to first BLI signal increase. Kaplan-Meier with log-rank test across groups.

### 3.5 Arm D: Temporal Switch — Does M2→M1 Switching Trigger Exit?

**Purpose:** Test the core prediction of the Temporal Switch Model: that switching from M2-dominated to M1-dominated macrophage niche triggers dormancy exit.

**Hypothesis:** If M1-driven exit contributes ~35%, then forced M2→M1 switching should accelerate dormancy exit, but the outcome (clearance vs. outgrowth) depends on concurrent immune activation.

**Experimental Groups (n=15 per group):**

| Group | Treatment | Rationale |
|-------|-----------|-----------|
| D1 | M2→M1 switch: IL-4 complex (to establish M2 dominance Days 1-28) → STOP IL-4 + add IFN-gamma + LPS (Days 28-42) | Temporal switch from M2 maintenance to M1 inflammatory |
| D2 | Sustained M2: IL-4 complex continuously (Days 1-42) | M2 dominance throughout — should maintain dormancy |
| D3 | Sustained M1: IFN-gamma + poly(I:C) (TLR3 agonist) continuously (Days 1-42) | M1 dominance throughout — predict: initial dormancy entry but eventual inflammatory exit |
| D4 | Vehicle control: PBS injections throughout | Natural kinetics |
| D5 | M2→M1 switch + anti-PD-1 (200 µg i.p., Days 28-42) | M2→M1 switch + checkpoint blockade to test clearance |
| D6 | PI3K-gamma inhibitor (eganelisib 30 mg/kg oral daily, Days 28-42) | Pharmacological M2→M1 repolarization |

**IL-4 complex preparation:** 5 µg recombinant mouse IL-4 + 25 µg anti-IL-4 antibody (clone 11B11), forming immune complexes that extend IL-4 half-life from minutes to >48 hours. Inject i.p. every 3 days.

**IFN-gamma dose:** 10,000 U recombinant mouse IFN-gamma i.p. every other day.

**Key readouts:**
- **BLI kinetics:** Weekly imaging to capture exact timing of exit events relative to switch
- **Day 28 (pre-switch):** Harvest 3 mice per group for baseline macrophage polarization and DTC dormancy status
- **Days 35, 42 (post-switch):** Harvest remaining mice for:
  - DTC dormancy fraction
  - Macrophage polarization by flow cytometry
  - p-ERK/p-p38 ratio in DTCs
  - Immune infiltration (CD8+ T cells, NK cells, Tregs)
- **scRNA-seq at Day 35 (one week post-switch):** Paired macrophage-DTC analysis to map signaling changes

**Primary endpoint:** Time from M2→M1 switch (Day 28) to BLI signal doubling. Kaplan-Meier with log-rank test.

**Critical secondary endpoint in D5 vs D1:** Does anti-PD-1 (Programmed Cell Death Protein 1, a checkpoint inhibitor) co-administration convert "awakening" into "clearance"? If D5 mice show LESS outgrowth than D1 despite similar awakening kinetics, this validates the "awaken and eliminate" strategy.

---

## 4. STATISTICAL FRAMEWORK

### 4.1 Power Analysis

Based on published colon cancer liver metastasis dormancy data (estimated 60-70% of DTCs enter dormancy in untreated controls):

**For dormancy entry rate (Arm B):**
- Expected entry rate: 65% (control) vs. 40% (M1-impaired) = 25% absolute difference
- Alpha = 0.05, Power = 0.80
- Required DTC counts: ~80 DTCs per group (detected by IF)
- Expected DTCs per mouse: ~20-50 (based on injection dose)
- **Minimum 3-4 mice per group at Day 7 timepoint, 15 total to account for attrition**

**For dormancy maintenance duration (Arm C):**
- Expected median dormancy: 8 weeks (control) vs. 4 weeks (M2-impaired)
- Hazard ratio = 2.0
- Alpha = 0.05, Power = 0.80
- **12-15 events per group required → 15 mice per group**

**For temporal switch kinetics (Arm D):**
- Expected median time-to-exit: 3 weeks (D1, switched) vs. 8+ weeks (D2, sustained M2)
- **15 mice per group** for adequate Kaplan-Meier curves

### 4.2 Statistical Tests

| Comparison | Test | Multiple Comparison Correction |
|------------|------|-------------------------------|
| Dormancy fraction across groups (single timepoint) | Chi-squared or Fisher's exact | Bonferroni for 6 arms |
| Time to metastasis (Kaplan-Meier) | Log-rank test | Bonferroni |
| p-ERK/p-p38 ratio (continuous) | Mann-Whitney U or t-test (after normality check) | Holm-Bonferroni |
| scRNA-seq cluster proportions | Chi-squared per cluster | Benjamini-Hochberg False Discovery Rate [FDR] |
| Cytokine levels across groups | One-way ANOVA (Analysis of Variance) with Tukey post-hoc | Tukey HSD (Honestly Significant Difference) |
| Mixed-effects model (longitudinal BLI) | Linear mixed model with random intercept per mouse | FDR |

### 4.3 Sample Size Summary

| Arm | Groups | Mice per group | Total mice | Timepoints |
|-----|--------|:--------------:|:----------:|:----------:|
| A | 4 | 15 | 60 | D7, D21, D42, D84 |
| B | 7 | 10-15 | 90 | D7, D21, D42 |
| C | 6 | 15 | 90 | D21, D42, D63, D84 |
| D | 6 | 15 | 90 | D28, D35, D42 |
| **Total** | | | **330 mice** | |

**Estimated duration:** 12-14 weeks per experimental run. Two independent replicates required → **24-28 weeks total (6-7 months)**.

---

## 5. READOUT HIERARCHY

### 5.1 Primary Readouts (mandatory for all mice)

| Readout | Method | Quantitative Output |
|---------|--------|---------------------|
| Tumor burden | Bioluminescence imaging (BLI) | Total flux (photons/sec) — weekly |
| DTC dormancy fraction | IF for GFP, Ki67, NR2F1 | Ki67-/NR2F1+/GFP+ cells per mm² liver |
| Macrophage M1/M2 balance | Flow cytometry (CD86 vs CD206 on CD11b+F4/80+) | M1:M2 ratio per liver |
| Overt metastasis count | Gross pathology + histology | Number of surface liver nodules at endpoint |

### 5.2 Secondary Readouts (subset of mice per timepoint)

| Readout | Method | Purpose |
|---------|--------|---------|
| p-ERK/p-p38 in DTCs | Intracellular flow cytometry or multiplex IF | Quantify dormancy signaling switch |
| Cytokine milieu | Luminex multiplex on liver homogenate | IFN-gamma, TNF-alpha, IL-6, IL-10, TGF-beta1, TGF-beta2, IL-12, CXCL10 |
| Immune infiltration | Flow cytometry (CD8, CD4, NK1.1, FoxP3, CD11c) | T cell and NK cell context |
| Cell cycle (Fucci2a) | Intravital or ex vivo fluorescence | G1 (red) vs. S/G2/M (green) in real time |

### 5.3 Tertiary Readouts (dedicated cohort)

| Readout | Method | Mice | Purpose |
|---------|--------|------|---------|
| scRNA-seq | 10x Genomics Chromium | 3 per group at key timepoints | Unbiased macrophage and DTC transcriptomic profiling |
| Spatial transcriptomics | 10x Visium or MERFISH | 2 per group at key timepoints | Map macrophage-DTC spatial relationships in situ |
| Electron microscopy | Transmission EM | 1 per group | Confirm GJIC between macrophages and DTCs |
| ECM composition | Second harmonic generation (SHG) imaging | 2 per group | Quantify collagen I/III scaffold integrity |

---

## 6. CONTROLS AND VALIDATION

### 6.1 Essential Controls

| Control | Purpose |
|---------|---------|
| PBS liposomes (Arm A) | Vehicle control for clodronate liposomes |
| Isotype antibody (Arms B, C) | Control for neutralizing antibodies |
| LysM-Cre without floxed allele | Control for Cre recombinase toxicity |
| Nos2fl/fl without Cre | Control for floxed allele leakiness |
| Non-tumor-bearing mice | Baseline liver macrophage composition |

### 6.2 Validation Experiments

1. **In vitro dormancy co-culture:** MC38-Fucci2a cells co-cultured with Bone Marrow-Derived Macrophages (BMDMs) polarized to M1 (IFN-gamma + LPS) vs M2 (IL-4 + IL-13) vs unpolarized (M0). Readout: Fucci cell cycle, p-ERK/p-p38 by Western blot, NR2F1 expression. This validates in vivo findings in a controlled system.

2. **Macrophage depletion confirmation:** At each timepoint, verify macrophage depletion efficiency by flow cytometry (target: >80% reduction in CD11b+F4/80+ cells for clodronate; >70% reduction in specific subsets for genetic tools).

3. **Polarization confirmation:** Verify that pharmacological skewing (IL-4 complex, IFN-gamma) actually shifts the M1:M2 ratio in liver by flow cytometry at 48h and 7d post-treatment.

### 6.3 Potential Pitfalls and Mitigations

| Pitfall | Mitigation |
|---------|------------|
| Clodronate depletes ALL macrophages, not just M1 or M2 | Use genetic tools (LysM-Cre x Nos2fl/fl, LysM-Cre x Arg1fl/fl) for selective impairment |
| M1 and M2 are not truly binary — LysM-Cre targets overlap | Supplement with scRNA-seq to verify that targeted subsets are actually affected; acknowledge continuum |
| Kupffer cells may not be efficiently depleted by clodronate (they are tissue-resident) | Use CD169-DTR + diphtheria toxin for Kupffer cell-specific depletion (Arm A, group A4) |
| IL-4 complex has systemic effects beyond liver | Consider liposomal or nanoparticle-encapsulated IL-4 for liver-targeted delivery |
| MC38 may not enter dormancy efficiently | Pilot experiment with varying cell doses (5×10^4, 1×10^5, 5×10^5) to optimize dormancy rate |
| IFN-gamma from T cells, not macrophages, may drive dormancy entry | Include T cell depletion groups (anti-CD4, anti-CD8) in Arm B to disambiguate |

---

## 7. EXPECTED OUTCOMES AND DECISION CRITERIA

### 7.1 Predicted Results Based on Quantitative Estimation

| Arm | Group | Predicted Dormancy Entry Rate | Predicted Dormancy Maintenance (median weeks) |
|-----|-------|:----------------------------:|:---------------------------------------------:|
| A | A1 (control) | ~65% | ~8 |
| A | A2 (all depleted, early) | ~30% (reduced entry) | ~3 (premature exit or failure to maintain) |
| A | A3 (all depleted, late) | ~65% (entry unaffected) | ~4 (impaired maintenance) |
| A | A4 (Kupffer depleted) | ~65% | ~5 (tissue-resident macrophages contribute ~30% to maintenance) |
| B | B1 (M1-impaired genetic) | ~40% (↓ from 65%) | ~7 (maintenance less affected) |
| B | B4 (anti-IFN-gamma) | ~40% (similar to B1) | ~7 |
| C | C1 (M2-impaired genetic) | ~60% (entry less affected) | ~4 (↓ from 8 weeks) |
| C | C3 (anti-IL-4Ralpha) | ~60% | ~5 |
| C | C5 (Kupffer depletion) | ~65% | ~4 |
| D | D1 (M2→M1 switch) | ~65% | Exit at ~3 weeks post-switch |
| D | D2 (sustained M2) | ~65% | >10 weeks (prolonged) |
| D | D3 (sustained M1) | ~65% (but may show heterogeneous entry) | ~4 (early inflammatory exit) |
| D | D5 (M2→M1 + anti-PD-1) | ~65% | Exit at ~3 weeks BUT reduced outgrowth vs D1 |
| D | D6 (PI3K-gamma inhibitor) | ~65% | Exit at ~4-5 weeks (gradual repolarization) |

### 7.2 Decision Criteria

**Scenario 1: Both M1 and M2 contribute (confirms model):**
- B1/B4 show reduced entry (40% vs 65%) AND C1/C3/C5 show reduced maintenance (4-5 vs 8 weeks)
- D1 shows accelerated exit after M2→M1 switch
- **Action:** Proceed to therapeutic testing with combination strategies (Arm D5 validates "awaken and eliminate")

**Scenario 2: Only M2 matters (contradicts model):**
- B1/B4 show NO change in entry rate; only C groups show effects
- **Action:** Revise model — M1 contribution overestimated; focus on M2-targeted maintenance strategies

**Scenario 3: Only M1 matters (contradicts model):**
- C groups show no effect; only B groups affect dormancy
- **Action:** Revise model — M2 contribution overestimated; focus on IFN-gamma/p38 pathway

**Scenario 4: Neither M1 nor M2 alone matters (both redundant):**
- Single pathway impairment has no effect; only total depletion (Arm A) shows phenotype
- **Action:** Macrophage contribution is non-specific (headcount, not phenotype); revise to focus on total macrophage number or other niche cells

---

## 8. TIMELINE

| Week | Activity | Deliverable |
|------|----------|-------------|
| 1-4 | Cell line engineering (MC38-GFP-Luc-Fucci2a-H2B-mCherry), validation | Engineered cell bank |
| 1-4 | Mouse breeding for genetic crosses (Nos2fl/fl x LysM-Cre, Arg1fl/fl x LysM-Cre) | Breeding colonies established |
| 5 | Pilot injection: MC38 dose optimization (3 doses × 5 mice) | Optimal cell dose for ~60% dormancy rate |
| 5-6 | Macrophage depletion/skewing validation (pharmacokinetics) | Confirmed dosing schedules |
| 7-8 | ARM A launch: Total depletion experiment | Week 12-14 completion |
| 8-9 | ARM B launch: M1 impairment | Week 14-16 completion |
| 8-9 | ARM C launch: M2 impairment (parallel) | Week 14-16 completion |
| 10-11 | ARM D launch: Temporal switch (requires Arm A pilot data) | Week 16-18 completion |
| 12-18 | Tissue processing, scRNA-seq library prep, sequencing | Data generation |
| 18-22 | Data analysis: scRNA-seq, statistical analysis, manuscript figure preparation | Analysis complete |
| 22-24 | Manuscript writing | Submit manuscript |
| 24-28 | Independent replicate of key findings | Validation complete |

**Total duration: ~7 months**

---

## 9. BUDGET ESTIMATE

| Category | Item | Quantity | Unit Cost | Total |
|----------|------|----------|-----------|-------|
| Mice | C57BL/6J (and transgenic strains) | 400 (330 + 70 reserve) | $30 | $12,000 |
| Reagents | Clodronate/PBS liposomes | 50 vials | $100 | $5,000 |
| Reagents | MC38 engineering (lentiviral vectors, sorting) | 4 constructs | $2,000 | $8,000 |
| Reagents | Antibodies (flow cytometry, IF, neutralizing) | 20+ antibodies | $300-500 | $10,000 |
| Reagents | IL-4 complex, IFN-gamma, LPS, poly(I:C) | Multiple | — | $3,000 |
| Sequencing | 10x Genomics scRNA-seq | 60 samples (5 arms × 4 groups × 3 mice) | $1,500 | $90,000 |
| Imaging | BLI (IVIS) time | 300 scans | $20 | $6,000 |
| Imaging | Intravital microscopy time | 50 sessions | $200 | $10,000 |
| Analysis | Computational (AWS/server) | — | — | $5,000 |
| Personnel | 1 postdoc (50% FTE, 7 months) | — | — | $35,000 |
| **TOTAL** | | | | **~$184,000** |

---

## 10. DATA ANALYSIS PLAN

### 10.1 scRNA-seq Analysis Pipeline

1. **Preprocessing:** Cell Ranger (10x Genomics) → count matrix
2. **Quality control:** Remove cells with <200 genes, >20% mitochondrial reads, doublet removal (Scrublet)
3. **Integration:** Harmony or Seurat v5 integration across samples/timepoints
4. **Clustering:** Leiden algorithm at resolution 0.5-1.0
5. **Cell type annotation:** SingleR + manual marker verification
6. **Macrophage subset identification:** Module scores for M1 genes (Nos2, Tnf, Il12b, Cxcl9) and M2 genes (Arg1, Mrc1, Chi3l3, Retnla)
7. **DTC identification:** GFP+ cells (transgene), scored for dormancy (Nr2f1, Bhlhe41, Cdkn1b) vs. proliferation (Mki67, Pcna, Aurka)
8. **Trajectory analysis:** Monocle3 or PAGA for macrophage polarization continuum
9. **Cell-cell interaction:** CellPhoneDB or NicheNet to identify macrophage→DTC ligand-receptor pairs
10. **Spatial validation:** Visium spatial transcriptomics on selected samples to confirm co-localization

### 10.2 Quantitative Estimation Validation

The scRNA-seq data will be used to directly test the quantitative estimation from Section 4.8:

- **Dormancy entry rate per macrophage composition:** In each sample, calculate the fraction of DTCs in dormancy vs. the fraction of macrophages that are M1-like vs M2-like. If the model is correct, there should be a positive correlation between M1 fraction and dormancy entry, and between M2 fraction and dormancy maintenance.
- **Signaling molecule quantification:** Expression levels of Tgfb1, Tgfb2, Ifng, Il6, Il10, Tnf in macrophage subsets → test whether these correlate with DTC dormancy status.
- **GJIC gene expression:** Gap junction genes (Gja1/Connexin 43, Gjb2/Connexin 26) in macrophages → test whether M2-like macrophages specifically express gap junction components.

---

## 11. ETHICAL AND REGULATORY CONSIDERATIONS

- All animal experiments require IACUC (Institutional Animal Care and Use Committee) approval
- Splenic injection is classified as a major survival surgery — requires aseptic technique and post-operative analgesia
- Clodronate liposome treatment may cause systemic macrophage depletion — monitor for opportunistic infection
- scRNA-seq data sharing: Deposit raw data in GEO (Gene Expression Omnibus) upon publication
- Genetic mouse crosses: Verify genotypes by PCR before experiment initiation

---

## APPENDIX A: MASTER ACRONYM GLOSSARY

| Acronym | Full Term |
|---------|-----------|
| AIW | Abdominal Imaging Window |
| ANOVA | Analysis of Variance |
| ARG1 | Arginase 1 |
| BLI | Bioluminescence Imaging |
| BMDM | Bone Marrow-Derived Macrophage |
| CAG | CMV Early Enhancer/Chicken β-Actin |
| CRISPR | Clustered Regularly Interspaced Short Palindromic Repeats |
| CSF1R | Colony Stimulating Factor 1 Receptor |
| CX3CR1 | C-X3-C Motif Chemokine Receptor 1 |
| CXCL | C-X-C Motif Chemokine Ligand |
| DTC | Disseminated Tumor Cell |
| DT | Diphtheria Toxin |
| DTR | Diphtheria Toxin Receptor |
| ECM | Extracellular Matrix |
| EGFP | Enhanced Green Fluorescent Protein |
| ELISA | Enzyme-Linked Immunosorbent Assay |
| ERK | Extracellular Signal-Regulated Kinase |
| FDR | False Discovery Rate |
| Fucci2a | Fluorescent Ubiquitination-based Cell Cycle Indicator 2a |
| GFP | Green Fluorescent Protein |
| GJIC | Gap Junctional Intercellular Communication |
| HSC | Hepatic Stellate Cell |
| IF | Immunofluorescence |
| IFN-gamma | Interferon gamma |
| IL | Interleukin |
| iNOS | Inducible Nitric Oxide Synthase (NOS2) |
| i.p. | Intraperitoneal |
| i.v. | Intravenous |
| LPS | Lipopolysaccharide |
| LysM | Lysozyme M |
| MAPK | Mitogen-Activated Protein Kinase |
| MHC | Major Histocompatibility Complex |
| MMP | Matrix Metalloproteinase |
| NOS2 | Nitric Oxide Synthase 2 (iNOS) |
| NR2F1 | Nuclear Receptor Subfamily 2 Group F Member 1 |
| NRP2 | Neuropilin 2 |
| PD-1 | Programmed Cell Death Protein 1 |
| p-ERK | Phospho-Extracellular Signal-Regulated Kinase |
| PI3K-gamma | Phosphoinositide 3-Kinase Gamma |
| p-p38 | Phospho-p38 |
| scRNA-seq | Single-Cell RNA Sequencing |
| SHG | Second Harmonic Generation |
| STAT1 | Signal Transducer and Activator of Transcription 1 |
| TGF-beta | Transforming Growth Factor Beta |
| TLR | Toll-Like Receptor |
| TNF-alpha | Tumor Necrosis Factor Alpha |

---

*This document will be updated as postdoc research briefings arrive with validated model systems, reagent specifications, and additional colon cancer-specific considerations.*
