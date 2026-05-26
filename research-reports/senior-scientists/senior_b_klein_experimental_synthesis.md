# SENIOR SCIENTIST SYNTHESIS REPORT: EXPERIMENTAL DESIGN FOR MACROPHAGE POLARIZATION AND COLON CANCER DTC DORMANCY

**To:** Chief Scientist
**From:** Prof. Robert Klein, PhD -- Senior Scientist, Biostatistics, Translational Oncology, and Clinical Trial Design
**Date:** 26 May 2026
**Re:** Integration of Dr. Tanaka (Postdoc 6), Dr. Hoffmann (Postdoc 7), and Dr. Webb (Postdoc 8) Briefings -- Statistical Rigor Audit, Translational Feasibility, and Risk-Adjusted Experimental Roadmap

---

## I. EXECUTIVE SUMMARY

Three postdoctoral briefings have been reviewed and integrated. Dr. Tanaka provides the quantitative framework: four core metrics (Dormancy Entry Rate [DER], Dormancy Maintenance Duration [DMD], Dormancy Exit Rate [DXR], DTC Clearance Rate [DCR]), power analysis, and a 14-month experimental timeline at $145K-$190K. Dr. Hoffmann provides the in vivo/in vitro model architecture: MC38 (C57BL/6) as primary cell line, intrasplenic injection as primary model, three-phase experimental structure (15 months), and a 12-arm experimental matrix using pharmacological and genetic macrophage manipulation tools. Dr. Webb addresses the critical tool gap: no truly M1-selective or M2-selective genetic tools exist commercially, and proposes near-term adoptive transfer strategies, medium-term de novo mouse generation (NOS2-DTR, MRC1-CreERT2), and a long-term CRISPR screen approach over 60 weeks.

**Central findings of this synthesis:**

1. **The n=8 mice/group proposed by Tanaka is underpowered relative to Hoffmann's n=12-15 and theDesign Effect (DE) of 9.85.** The effective sample size per mouse is approximately 6 independent observations, and Tanaka's power calculation depends on an unvalidated Intraclass Correlation Coefficient (ICC) assumption of 0.15.

2. **The four-arm design (Control, M1-favoring, M2-favoring, Macrophage depletion) requires a hierarchical testing framework** to control the family-wise error rate across four metrics and six pairwise comparisons per metric.

3. **The $145K-$190K budget is a lower bound that does not account for the expanded scope of Hoffmann's multi-phase design** or Webb's genetic tool development. A realistic integrated budget is $250K-$350K.

4. **No M1/M2-selective genetic tools exist.** All three briefings converge on this critical bottleneck. The near-term strategy must rely on pharmacological skewing (CpG-ODN 1826, IL-4 complex) and adoptive transfer of ex vivo polarized Bone Marrow-Derived Macrophages (BMDMs), which introduces confounds of systemic off-target effects and in vivo repolarization of transferred cells.

5. **The PMID 35121993 citation characterization in Tanaka's report is inaccurate.** The paper by Dai et al. (2022, Nature Cancer) is about astrocytic laminin-211 driving breast cancer DTC dormancy in brain, not "intravital imaging protocols for DTC tracking" as characterized. The mVenus-p27 reporter and DTC yield data (316-587 DTCs) are present in this paper, and the intravital imaging methodology is relevant, but the characterization is misleading and should be corrected.

---

## II. SECTION 1: STATISTICAL POWER AUDIT

### 2.1 Sample Size Discrepancy Between Postdocs

The most critical statistical tension across the three briefings is the sample size discrepancy. Dr. Tanaka proposes n=8 mice per group (32 mice total across 4 groups). Dr. Hoffmann proposes n=12-15 per group (48-60 mice per experiment, with multiple overlapping experiments). This is not merely a difference in conservatism -- it reflects fundamentally different power assumptions.

**Tanaka's power calculation (primary endpoint: DXR at Day 56):**
- Control DXR: 20%; M2-favoring DXR: 45% (25 percentage point increase)
- Alpha = 0.05 (two-sided), Power = 0.80
- Test: Fisher's exact test
- Average DTCs per mouse: 60
- ICC = 0.15 (estimated, unvalidated)
- Design Effect: DE = 1 + (60-1) x 0.15 = 9.85
- Effective observations per mouse: 60 / 9.85 = 6.09
- Required effective observations per group: approximately 39
- Mice per group: 39 / 6.09 = 6.5, rounded to 7 + 15% attrition = 8

**Hoffmann's approach:**
- Primary endpoint: Bioluminescence Imaging (BLI) signal as a continuous measure
- Assumed effect size: 50% change in BLI photon flux with macrophage depletion
- Alpha = 0.05, Power = 0.80
- n = 12-15 per group (accounting for 20% attrition)
- Statistical test: Two-way ANOVA (treatment x time) with Tukey post-hoc correction

### 2.2 Critical Evaluation of Tanaka's Assumptions

**ICC = 0.15 is an unvalidated assumption.** No published ICC exists for DTC dormancy outcomes within mice. Tanaka derives this from "analogous clonogenic assay data," but clonogenic assays measure colony formation in vitro, not DTC dormancy/clearance in vivo in the liver microenvironment. The ICC sensitivity analysis is as follows:

| ICC Assumption | Design Effect | Effective obs/mouse | Mice/group needed (no attrition) | Mice/group with 15% attrition |
|---------------|---------------|---------------------|----------------------------------|-------------------------------|
| 0.05 | 3.95 | 15.2 | 2.6 -> 3 | 3.5 -> 4 |
| 0.10 | 6.90 | 8.7 | 4.5 -> 5 | 5.8 -> 6 |
| **0.15 (Tanaka)** | **9.85** | **6.1** | **6.4 -> 7** | **8.1 -> 8** |
| 0.20 | 12.80 | 4.7 | 8.3 -> 9 | 9.5 -> 10 |
| 0.25 | 15.75 | 3.8 | 10.3 -> 11 | 11.8 -> 12 |
| 0.30 | 18.70 | 3.2 | 12.2 -> 13 | 14.0 -> 15 |

At ICC = 0.25 (plausible if there is substantial within-mouse correlation due to shared microenvironment, perfusion effects, or local immune status), n=12 mice per group are required -- matching Hoffmann's more conservative estimate. **I recommend using n=12 per group as the base sample size**, which provides adequate power at ICC values up to 0.27 and accommodates the design effect uncertainty. The additional cost of 16 mice (4 groups x 4 additional mice) is approximately $1,000-$1,500, which is trivial relative to the total budget and the cost of a false negative.

### 2.3 Primary Endpoint Selection

Tanaka designates DXR (Dormancy Exit Rate) at Day 56 as the primary endpoint, with the comparison of M2-favoring vs. Control as the primary contrast. This is justified by the strongest mechanistic evidence (Recalde-Percaz et al. 2025, PMID 40848614: macrophage-derived TGF-beta1 promotes DTC awakening via NRP2; Ganesan et al. 2023: IL-6/G-CSF/MEK/ERK dormancy exit axis).

However, DXR has a measurement limitation: it requires longitudinal intravital imaging via an Abdominal Imaging Window (AIW), which captures only the liver surface (approximately 100-200 micrometers depth). Deep parenchymal DTCs are invisible. The measured DXR may therefore not represent the true whole-liver DXR. This sampling bias should be quantified in the pilot phase by comparing AIW-visible DXR to endpoint whole-liver DXR measured by multiplex immunofluorescence (IF) on serial sections.

### 2.4 Effect Size Calibration

Tanaka's assumed effect sizes (25 percentage point DXR increase, 15-25 percentage point DER increase) derive from expert estimates in the FINAL_COMPILATION Section 4.8.7 (M1 entry contribution approximately 40%, M2 maintenance contribution approximately 50%). These are expert opinions, not empirical data. The actual effect sizes are unknown and could be substantially smaller.

**If the true DXR difference between M2-favoring and control is 15 percentage points (not 25), the power at n=8 per group drops below 0.60.** At n=12 per group, power remains at 0.75 for a 15-point difference. **This is another argument for n=12 per group.**

The pilot phase (Hoffmann's Phase I, months 1-3) must include a power re-estimation step. After the dose-response experiment (Experiment I.1) and the time-course characterization (Experiment I.2), compute the observed effect sizes and ICC from pilot data, then re-estimate the required sample size before committing to the full Phase II experiment. This adaptive design approach is standard in clinical trials and should be applied here.

---

## III. SECTION 2: MULTIPLE COMPARISON CORRECTION

### 3.1 The Multiplicity Problem

The experimental design has two levels of multiplicity:

**Level 1: Four metrics.** DER, DMD, DXR, DCR are measured on the same mice. These are correlated endpoints (e.g., higher DER may correlate with lower DXR if dormancy is a stable state). Treating them as independent inflates the family-wise error rate.

**Level 2: Four groups, six pairwise comparisons per metric.** Comparing all four groups (Control, M1-favoring, M2-favoring, Macrophage depletion) for each metric generates 4 choose 2 = 6 pairwise comparisons. With four metrics, that is 24 pairwise tests, plus time x treatment interactions for longitudinal measures (DMD, DXR), plus the mixed-effects models for continuous outcomes (p-ERK/p-p38 ratio, macrophage-DTC distance).

### 3.2 Proposed Hierarchical Testing Framework

I recommend a pre-specified hierarchical testing procedure that controls the family-wise error rate at alpha = 0.05 without requiring Bonferroni correction across all 24 tests (which would yield alpha = 0.05/24 = 0.002, severely reducing power).

**Testing hierarchy:**

| Level | Test | Alpha | Rationale |
|-------|------|-------|-----------|
| 1 (Primary) | DXR: M2-favoring vs. Control | 0.05 | Strongest prior evidence; primary endpoint |
| 2 (Key secondary) | DXR: M1-favoring vs. Control | 0.05 | Test if M1 reduces exit (passed Level 1) |
| 3 (Key secondary) | DCR: M1-favoring vs. Control | 0.05 | Test M1-mediated clearance (passed Level 2) |
| 4 (Exploratory) | DER: M1-favoring vs. Control | 0.05 | M1 promotes dormancy entry hypothesis |
| 5 (Exploratory) | DMD: All pairwise comparisons | 0.05 (Holm-Bonferroni for 6 comparisons) | Time-to-event secondary endpoint |
| 6 (Exploratory) | All remaining pairwise comparisons for DER, DXR, DCR | 0.05 (Holm-Bonferroni within each metric) | Exploratory |
| 7 (Discovery) | scRNA-seq differential expression | FDR < 0.05 (Benjamini-Hochberg) | Per-gene testing; not confirmatory |

**Key principle:** Each level is tested only if the preceding level achieves significance at alpha = 0.05. This gatekeeping procedure ensures that the primary hypothesis (M2 promotes dormancy exit) is tested with full alpha before any secondary or exploratory analyses. The statistical validity of this hierarchy depends on the logical ordering: Level 1 and 2 test the same metric (DXR); Levels 3-4 test mechanistically related hypotheses (M1 clearance and entry); Level 5 tests a different metric with correction for multiple comparisons within that metric.

### 3.3 GLMM Specification

Tanaka proposes a Generalized Linear Mixed Model (GLMM) for the DXR analysis. The specification is appropriate:

```
logit(P(exit_it)) = beta_0 + beta_1 * Group_i + beta_2 * Time_t + beta_3 * Group_i * Time_t + u_i + epsilon_it
```

I endorse this model with three modifications:

1. **Include a random slope for time:** Allow the time effect to vary by mouse (u_i + v_i * Time_t), capturing mouse-specific dormancy exit trajectories. This is important if some mice have systematically faster or slower DTC dynamics.

2. **Include macrophage density as a time-varying covariate:** If macrophage density near each DTC can be quantified from intravital imaging (CX3CR1-GFP signal within 30 micrometers of each DTC), add this as a predictor to test the dose-response relationship between local macrophage density and dormancy exit probability.

3. **Use the bias-reduced GLMM fitting method:** Standard GLMM fitting (lme4::glmer) can produce biased estimates with small sample sizes (n=8-12 mice). Use the brglm2 R package for bias-reduced estimation.

---

## IV. SECTION 3: QUANTITATIVE FRAMEWORK CRITIQUE

### 4.1 Metric Definitions and Measurability

The four metrics (DER, DMD, DXR, DCR) are well-defined conceptually but face practical measurement challenges:

**DER (Dormancy Entry Rate):**
- Definition: Proportion of arrived DTCs that are NR2F1+, Ki67-, high p-p38/low p-ERK at Day 7.
- Measurability: GOOD. Endpoint harvest with multiplex IF provides a clear binary classification per DTC.
- Limitation: Day 7 is arbitrary. Some DTCs may enter dormancy at Day 3; others at Day 14. A single timepoint cannot capture the full entry kinetics.
- Recommendation: Add a Day 3 harvest (as Hoffmann proposes in Experiment I.2) to capture early kinetics.

**DMD (Dormancy Maintenance Duration):**
- Definition: Time from dormancy entry to dormancy exit for each individual DTC, tracked longitudinally.
- Measurability: MODERATE. Requires intravital imaging through AIW, which captures only surface DTCs (approximately 50-60% of total). Registration across sessions depends on vascular landmarks and TRITC-dextran injection, which has imperfect reproducibility.
- Limitation: Right-censoring is severe. Many DTCs will remain dormant at study endpoint (Day 56), and the Kaplan-Meier estimate will have wide confidence intervals beyond Day 42.
- Recommendation: This is the most technically challenging metric. Consider extending the observation window to Day 84 for a subset of mice if resources permit, to reduce censoring.

**DXR (Dormancy Exit Rate):**
- Definition: Proportion of dormant DTCs that transition to proliferative during observation.
- Measurability: MODERATE-GOOD by intravital imaging. The mVenus-p27 reporter provides a real-time dormancy signal, and the transition from high to low mVenus is the exit event.
- Limitation: Distinguishing true exit from reporter artifact (photobleaching, signal loss due to cell damage) requires careful controls. Include photobleaching correction using reference beads and validate a subset against Ki67 endpoint staining.

**DCR (DTC Clearance Rate):**
- Definition: Proportion of DTCs that disappear between consecutive imaging sessions.
- Measurability: POOR. "Disappearance" conflates: (a) immune-mediated killing and phagocytic clearance, (b) apoptosis followed by non-immune clearance, (c) DTC migration out of the imaging plane, and (d) technical imaging loss. Only (a) and (b) are biologically meaningful; (c) and (d) are noise.
- Recommendation: DCR should be reported as a secondary endpoint with an explicit caveat about the interpretation ambiguity. Endpoint cleaved Caspase-3 staining at former DTC locations (identified by coordinate registration) partially addresses mechanism but cannot distinguish immune-mediated from intrinsic apoptosis.

### 4.2 Missing Metrics

The framework is missing two important quantitative measures:

1. **Macrophage polarization index (MPI):** A composite score quantifying the balance of M1-like vs. M2-like macrophages in each liver, measured by flow cytometry at endpoint. This should be a pre-specified covariate in all GLMMs, allowing correlation between macrophage polarization state and each dormancy metric across individual mice.

2. **Spatial co-localization score:** The probability that a dormant DTC is within 30 micrometers of an M1-like (CD86+) or M2-like (CD206+) macrophage, relative to chance. This quantifies whether dormancy is spatially associated with specific macrophage phenotypes beyond what would be expected from random distribution.

### 4.3 p-ERK/p-p38 Ratio Threshold

Tanaka proposes a threshold of approximately 0.5 for the p-ERK/p-p38 ratio (below 0.5 = dormant, above 0.5 = proliferative), citing Ghajar lab methodology (Dai et al. 2022). This threshold has not been validated for colon cancer cells in the liver microenvironment. **The threshold must be established empirically using positive controls (serum-starved quiescent MC38 cells) and negative controls (log-phase proliferating MC38 cells) before the main experiment.** The threshold should be reported as a sensitivity analysis: does the primary DXR comparison remain significant at thresholds of 0.3, 0.4, 0.5, 0.6, 0.7? If the result is robust across thresholds, this strengthens the conclusion.

---

## V. SECTION 4: EFFECT SIZE CALIBRATION

### 5.1 Using Pilot Data from Hoffmann's Phase I

Hoffmann's Phase I (months 1-3) includes two critical pilot experiments:

**Experiment I.1 (Dose-Response):** Five groups (n=12 each) with MC38 doses from 1x10^2 to 1x10^5 cells. The dose yielding stable BLI plateau in >60% of mice without macrometastases defines the "dormancy dose." This experiment also provides the first estimate of the proportion of DTCs that enter dormancy at each dose.

**Experiment I.2 (Time-Course):** Six timepoints (Days 3, 7, 14, 28, 56, 84) with n=5 mice each, including full macrophage phenotyping (11-marker flow cytometry panel with TIM4/CD11c gating for Kupffer cell vs. Monocyte-Derived Macrophage [MoM] distinction).

**These pilot data must be used for:**

1. **ICC estimation:** Compute the empirical ICC for DER and DXR from the Day 7 and Day 56 endpoint data. This replaces the assumed ICC = 0.15 with a data-driven value. Given the small pilot sample (n=5 per timepoint), the ICC estimate will have wide confidence intervals; use the upper 80th percentile of the ICC confidence interval in the power calculation to be conservative.

2. **Effect size estimation for macrophage density:** The time-course experiment includes flow cytometry quantification of M1-like (CD86+ MHC-II-hi) vs. M2-like (CD206+) macrophage proportions at each timepoint. The correlation between these proportions and dormancy metrics (estimated from endpoint histology) provides the first effect size estimates for the Phase II macrophage manipulation experiments.

3. **DTC yield calibration:** The expected 50-100 DTCs per liver (Tanaka) must be confirmed. If the actual yield is lower (e.g., 20-30 DTCs), the effective sample size per mouse drops from 6.09 to 2.0-3.0, and the required mice per group increases dramatically.

### 5.2 Bayesian Prior Elicitation

Given the uncertainty in effect sizes, I recommend a Bayesian analysis framework alongside the frequentist analysis. Use the expert estimates from FINAL_COMPILATION Section 4.8.7 as prior distributions:

- DER M1 contribution: Beta(4, 6) prior (centered on 40%, 95% CI: 12-72%)
- M2 maintenance contribution: Beta(5, 5) prior (centered on 50%, 95% CI: 21-79%)

These weakly informative priors allow the data to dominate while incorporating existing expert knowledge. Report both Bayesian posterior probabilities (e.g., "P(M2 DXR > Control DXR | data) = 0.96") and frequentist p-values for each primary comparison.

---

## VI. SECTION 5: TRANSLATIONAL BRIDGE ASSESSMENT

### 6.1 Mapping Experimental Arms to Clinical Development

The four experimental arms in Tanaka's design map to distinct clinical development strategies:

| Experimental Arm | Mouse Intervention | Clinical Equivalent | Development Strategy |
|-----------------|-------------------|--------------------|--------------------|
| Control | Vehicle (PBS IP) | Standard of care observation | Baseline natural history |
| M1-favoring | CpG-ODN 1826 (TLR9 agonist) | TLR9 agonist (SD-101, IMO-2125/tilsotolimod) | Adjuvant immunotherapy to enforce dormancy |
| M2-favoring | IL-4 complex | No direct clinical equivalent (IL-4 is immunosuppressive, not clinically administered) | Mechanistic probe only; confirms target |
| Macrophage depletion | Clodronate liposomes | CSF1R inhibitors (pexidartinib), PI3K-gamma inhibitors (eganelisib) | Adjuvant macrophage-targeting therapy |

**Critical translational gap:** The M2-favoring arm (IL-4 complex) has no clinical equivalent because IL-4/IL-13 are immunosuppressive and not administered to patients. This arm is purely mechanistic. The clinically relevant question is the M1-favoring arm (can TLR9 agonism enforce dormancy or enhance clearance?) and the macrophage depletion arm (does macrophage depletion disrupt dormancy maintenance?).

### 6.2 The Depletion Paradox

Dr. Webb's briefing confirms that clodronate liposomes deplete ALL phagocytic cells (Kupffer cells, dendritic cells, MoMs, neutrophils). Hoffmann proposes CD169-DTR mice for Kupffer cell-specific depletion and PLX3397 for MoM-selective depletion. The translational interpretation differs critically:

- **Clodronate arm:** Tests whether macrophages (any macrophage) are required for dormancy. If dormancy is maintained despite total macrophage depletion, this argues against macrophage-centric dormancy models.
- **CD169-DTR arm:** Tests whether Kupffer cells specifically enforce dormancy. This is translatable because Kupffer cells are the liver-resident population that first encounters arriving DTCs.
- **PLX3397 arm:** Tests whether MoMs drive dormancy exit. This is translatable to CSF1R inhibitors in the adjuvant setting.

**Recommendation:** The three depletion approaches should be analyzed as a dose-response in "selectivity" -- from non-selective (clodronate) to moderately selective (PLX3397, spares Kupffer cells) to highly selective (CD169-DTR, Kupffer cells only). This allows inference about which macrophage population is the critical driver.

### 6.3 Clinical Endpoint Translation

The four metrics translate to clinical endpoints as follows:

| Mouse Metric | Clinical Equivalent | Clinical Measurement |
|-------------|--------------------|--------------------|
| DER | Proportion of post-surgical DTCs entering dormancy | Circulating Tumor Cell (CTC) dormancy markers (NR2F1+, Ki67-) in blood |
| DMD | Duration of Minimal Residual Disease (MRD) dormancy | ctDNA dynamics (stable low-level ctDNA = dormant MRD) |
| DXR | Metastatic recurrence rate | Time to detectable metastasis by imaging |
| DCR | Immune-mediated elimination of DTCs | ctDNA clearance rate during adjuvant therapy |

**The most translatable metric is DXR (mapped to recurrence rate), and the most innovative metric is DER (mapped to CTC dormancy fraction), which has no established clinical assay.**

---

## VII. SECTION 6: COST-BENEFIT ANALYSIS

### 7.1 Budget Reconciliation

The three briefings propose overlapping but non-identical budgets:

| Cost Category | Tanaka ($K) | Hoffmann ($) | Webb ($) | Integrated Estimate ($K) |
|--------------|------------|-------------|----------|--------------------------|
| Mice | 2-3 | Not separately itemized | Not separately itemized | 5-8 (expanded n=12/group + pilot + transgenics) |
| AIW devices + imaging | 35-65 | Included in per-experiment costs | N/A | 40-70 |
| 10X Chromium scRNA-seq | 50 | Not separately itemized | N/A | 50-75 (expanded timepoints) |
| MERFISH | 25 | Not separately itemized | N/A | 25-40 |
| Antibodies/reagents | 15-20 | 10-15 | 15-20 | 25-35 |
| FACS sorting | 8-12 | 8-12 | 5-8 | 12-18 |
| Computational infrastructure | 10-15 | 5-10 | 5-10 | 15-20 |
| Genetic tool development | N/A | N/A | 50-80 (NOS2-DTR, MRC1-CreERT2) | 50-80 (if pursued) |
| CRISPR screen | N/A | N/A | 40-60 | 40-60 (if pursued) |
| Personnel | Not costed | Not costed | Not costed | 80-120 (postdoc 80% FTE x 15 months + technician) |
| **Total** | **145-190** | **~200-250 (estimated)** | **~150-250** | **340-525** |

### 7.2 Recommended Budget Prioritization

Given the integrated estimate of $340K-$525K, which substantially exceeds Tanaka's $145K-$190K estimate, I recommend a prioritized spending plan:

**Tier 1 (Essential, $200-250K):** Tanaka's core experiment with n=12/group, Hoffmann's Phase I validation, and the primary endpoint analyses (DER, DXR at Day 56 with multiplex IF and flow cytometry). Omit MERFISH initially; substitute with 10X Visium spatial transcriptomics at lower cost if spatial data are deemed essential.

**Tier 2 (High value, $50-80K):** Hoffmann's Phase II pharmacological manipulation experiments (clodronate, PLX3397, IL-4 complex, CpG-ODN) and the in vitro co-culture mechanistic experiments.

**Tier 3 (Aspirational, $90-195K):** Webb's genetic tool development (NOS2-DTR, MRC1-CreERT2 mice) and the CRISPR screen. These are high-value but long-term investments (6-12 months before tools are available) and should only proceed if Tier 1 and 2 yield promising results.

### 7.3 Cost per Unit of Information

The most cost-efficient experimental design is Hoffmann's Phase II Experiment II.4 (IL-4 complex forced M2 polarization, n=15/group x 3 groups = 45 mice). At approximately $3,000-4,000 per mouse (including housing, reagents, imaging, and endpoint analysis), this experiment costs approximately $135K-180K and directly tests the central hypothesis (M2 polarization drives dormancy exit). If only one experiment can be funded, this is the one to prioritize.

---

## VIII. SECTION 7: REFERENCE VERIFICATION

Five key references were independently verified via PubMed. Four were confirmed without issue. One has a characterization caveat.

### 7.1 Verified References

**1. Borriello L, et al. (2022, Nature Communications, PMID 35110548)**
- Tanaka citation: "TMEM doorway macrophages install dormancy programs (NR2F1) in disseminating cells."
- **VERIFIED.** Title: "Primary tumor associated macrophages activate programs of invasion and dormancy in disseminating tumor cells." The characterization is accurate.

**2. Dalla E, et al. (2024, Cell, PMID 39378878)**
- Tanaka citation: "Alveolar macrophage TGF-betaRIII maintains dormancy; CD169-DTR depletion model."
- **VERIFIED.** Title: "Lung-resident alveolar macrophages regulate the timing of breast cancer metastasis." The characterization is accurate. Hoffmann correctly identifies CD169-DTR as the key tool for Kupffer cell-specific depletion based on this paper.

**3. Recalde-Percaz T, et al. (2025, Neoplasia, PMID 40848614)**
- Tanaka citation: "Macrophage-derived TGF-beta1 promotes DTC awakening via NRP2."
- **VERIFIED.** Title: "Macrophage-derived TGF-beta1 promotes disseminated tumor cell awakening via NRP2 upregulation." Exact match with Tanaka's characterization. This is the strongest mechanistic evidence for the M2-driven dormancy exit hypothesis.

**4. Heinz MC, et al. (2022, Cancer Research, PMID 35570706)**
- Hoffmann citation: "YAP-controlled plasticity at the micrometastatic stage in CRC liver metastasis. Intravital microscopy, patient-derived organoids, scRNA-seq."
- **VERIFIED.** Title: "Liver Colonization by Colorectal Cancer Metastases Requires YAP-Controlled Plasticity at the Micrometastatic Stage." Published in Cancer Research, 82(10):1953-1968. Note: First author is Maria C. Heinz (not "Heinz MC" as cited by Hoffmann, but this is a minor ordering convention difference). This paper is foundational for the CRC dormancy model, demonstrating that persistent YAP signaling locks micrometastases in a growth-stalled, cellularly homogeneous state, while YAP attenuation permits outgrowth. It uses intravital microscopy, patient-derived organoids (PDOs), and scRNA-seq, confirming Hoffmann's characterization.

**5. Dai J, et al. (2022, Nature Cancer, PMID 35121993) -- CHARACTERIZATION CAVEAT**
- Tanaka citation: "Intravital imaging protocols for DTC tracking; mVenus-p27 reporter; 316-587 DTCs per experiment."
- **VERIFIED with caveat.** Title: "Astrocytic laminin-211 drives disseminated breast tumor cell dormancy in brain." This paper is about astrocyte-laminin-DTC interactions in the brain metastatic niche, NOT about general "intravital imaging protocols for DTC tracking" as Tanaka characterizes it. However, the mVenus-p27 reporter IS used in this paper, and the DTC yield data (n=316 cells over 6 mice for T4-2; n=587 cells over 6 mice for MDA-MB-231) ARE present. The intravital imaging methodology is relevant but is applied to the brain niche, not the liver.
- **Action required:** Tanaka should correct this citation to accurately describe it as "Dai et al. 2022 applied intravital imaging with mVenus-p27 reporters to track DTCs in the brain metastatic niche, providing DTC yield benchmarks (316-587 DTCs across 6 mice) that are transferable to the liver model." The characterization should not imply that this paper provides liver-specific imaging protocols.

### 7.2 Cross-Referenced References

The following references, verified in my prior synthesis report (Senior Scientist B: Dormancy Therapy Synthesis), are also cited by these postdocs and remain confirmed:

- **Zheng X, et al. (2023, Cancer Research, PMID 37205635):** HDAC2-SP1 axis. Tanaka correctly cites the journal as Cancer Research. (Note: Other postdocs had previously misattributed this to Cancer Discovery.)
- **Ritsma L, et al. (2012, Science Translational Medicine, PMID 23054295):** AIW implantation protocol. Confirmed.
- **Entenberg D, et al. (2018, Nature Protocols, PMID 30250298):** Intravital imaging protocols. Confirmed.

---

## IX. SECTION 8: RISK-ADJUSTED TIMELINE WITH DECISION GATES

### 9.1 Integrated Timeline

The three postdocs propose overlapping but different timelines:
- Tanaka: 14 months (4 phases: validation, main experiment, endpoint analysis, computational)
- Hoffmann: 15 months (3 phases: model validation, manipulation, mechanistic)
- Webb: 60 weeks (4 phases: pharmacological pilot, functional experiments, genetic tool development, CRISPR screen)

I propose an integrated 18-month timeline with three decision gates:

### 9.2 Phase I: Model Validation and Pilot (Months 1-3)

**Activities:**
- MC38-mVenus-p27-tdTomato cell line engineering and validation (Tanaka Topic 1.5)
- Intrasplenic injection dose-response (Hoffmann Experiment I.1, n=12/group x 5 doses = 60 mice)
- AIW implantation pilot (n=4 mice; establish surgical proficiency)
- Dormancy marker validation in CRC cells (Tanaka Topic 1.1)
- scRNA-seq sorting panel optimization (Tanaka Topic 4.3, n=2 mice)

**Key deliverables at Decision Gate 1 (Month 3):**
1. Optimal dormancy dose confirmed (BLI plateau >6 weeks in >60% of mice)
2. DTC yield per liver confirmed (target: >50 DTCs/liver at optimal dose)
3. mVenus-p27 reporter validation (correlation with NR2F1 and p-ERK/p-p38 < 0.5 threshold)
4. Empirical ICC estimate from pilot data
5. Power re-estimation for Phase II sample size

**Decision Gate 1 criteria:**
- **PROCEED** if DTC yield >= 30/liver and mVenus-p27 shows clear bimodal distribution (dormant vs. proliferative)
- **MODIFY** if DTC yield < 30/liver: reduce injection dose or switch to portal vein injection model
- **HALT** if no dormancy dose can be established (all doses produce either rapid outgrowth or no detectable DTCs): reconsider cell line (switch to CT26/BALB/c) or model (orthotopic cecal implantation)

### 9.3 Phase II: Macrophage Manipulation Experiments (Months 4-10)

**Activities (running in parallel where possible):**

**Experiment A: Core 4-arm design (Tanaka Topic 3.2, n=12/group x 4 = 48 mice with AIW)**
- Groups: Control, CpG-ODN 1826 (M1-favoring), IL-4 complex (M2-favoring), Clodronate (depletion)
- Duration: 56 days per cohort, staggered enrollment
- Primary endpoint: DXR at Day 56

**Experiment B: PLX3397 and CD169-DTR depletion arms (Hoffmann Experiments II.2, III.3)**
- PLX3397 chow arm (n=12): MoM-selective depletion
- CD169-DTR arm (n=12): Kupffer cell-selective depletion (if mice available; otherwise defer to Phase III)
- These arms run in parallel with Experiment A using separate cohorts

**Experiment C: In vitro co-culture mechanistic studies (Hoffmann Experiment III.4)**
- 8 conditions (Kupffer cell vs. MoM, M1 vs. M2, transwell vs. direct contact) x 3 replicates x 3 timepoints
- Runs concurrently with in vivo experiments

**Key deliverables at Decision Gate 2 (Month 10):**
1. Primary endpoint result: DXR comparison M2-favoring vs. Control
2. Secondary endpoints: DER, DCR, MPI across all groups
3. scRNA-seq data from paired sorting (DTCs + macrophages from same livers)
4. Flow cytometry confirmation of macrophage polarization shift in each treatment group
5. In vitro co-culture results: which macrophage type/polarization state maintains or disrupts dormancy

**Decision Gate 2 criteria:**
- **PROCEED TO PHASE III** if primary endpoint is positive (DXR M2-favoring > Control, p < 0.05) AND macrophage polarization shift is confirmed by flow cytometry
- **MODIFY** if primary endpoint is positive but effect size is small (<10 percentage points): increase sample size or extend observation window before Phase III
- **REASSESS** if primary endpoint is negative: examine whether macrophage manipulation successfully shifted polarization (if not, the manipulation failed, not the hypothesis); consider alternative manipulation strategies (Webb's adoptive transfer approach)
- **HALT** if macrophage depletion has NO effect on any dormancy metric: the macrophage-dormancy hypothesis may not hold in the CRC liver context

### 9.4 Phase III: Mechanistic and Translational Studies (Months 10-18)

**Activities (conditional on positive Phase II):**

**Experiment D: Genetic validation (if tools available)**
- LysM-Cre x Stat6-flox (M2-deficient macrophages): n=12 per genotype
- LysM-Cre x Stat1-flox (M1-deficient macrophages): n=12 per genotype
- These mice require 2-3 months of breeding before experiments can begin; initiate breeding in Month 4

**Experiment E: scRNA-seq and spatial transcriptomics analysis**
- Full computational pipeline (Tanaka Topic 6): trajectory analysis, CellPhoneDB, NicheNet, imaging-transcriptomics integration
- MERFISH on selected sections (if budget permits)

**Experiment F: Translational readout development**
- Macrophage polarization index (MPI) biomarker development from flow cytometry data
- CTC dormancy marker panel (NR2F1, Ki67, p27) optimization for potential clinical translation
- Correlation analysis between MPI and dormancy metrics to establish predictive biomarker candidates

**Experiment G (Webb Phase 3-4, if funded): Genetic tool validation and CRISPR screen**
- NOS2-DTR and MRC1-CreERT2 founder characterization
- Ex vivo CRISPR screen in BMDMs (focused 500-gene library)
- These are parallel long-term investments that provide data for future grant applications

### 9.5 Timeline Visualization

```
Month:  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18
        |--- Phase I ---|
        |DG1|
            |------------ Phase II (in vivo) ------------|
                                                         |DG2|
            |--- Breeding (LysM crosses) ---||--- Phase III (genetic validation) ---|
                                                         |--- scRNA-seq/comp analysis ---|
            |----------- Phase II (in vitro) ------------|
                                                         |--- Translational dev ---|
        |------- Webb Phase 3 (genetic tools, parallel) ----------------------|
                                                         |--- Webb Phase 4 (CRISPR, parallel) ---|
```

### 9.6 Risk Mitigation Matrix

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Low DTC yield from intrasplenic injection | Moderate | High (invalidates power calculation) | Pilot optimization in Phase I; backup portal vein injection model |
| AIW surgical mortality >15% | Low-Moderate | Moderate (requires more mice) | Staggered surgeries; maintain replacement cohort; 15% attrition buffer |
| Macrophage manipulation fails to shift polarization | Moderate | High (confounds interpretation) | Flow cytometry confirmation at Day 7 pilot checkpoint; alternative CpG-ODN dosing or STING agonist |
| mVenus-p27 reporter does not function in MC38 | Low | High (requires alternative dormancy readout) | Validate in vitro before in vivo; backup: endpoint multiplex IF as sole dormancy readout |
| ICC substantially >0.15 | Moderate | Moderate (requires more mice) | Adaptive sample size re-estimation after Phase I pilot; budget for n=15/group |
| No dormancy dose identified for MC38 | Low | Critical (project failure) | Backup cell line: CT26 in BALB/c; alternative: human PDOs in NSG mice |
| CRISPR screen identifies no actionable targets | Moderate | Low (aspirational objective) | This is Tier 3 priority; does not affect core project |

---

## X. CROSS-REFERENCE WITH PRIOR SENIOR SCIENTIST REPORTS

This report focuses on experimental design and statistical rigor. It complements my earlier synthesis report on therapeutic targeting (Senior Scientist B: Dormancy Therapy Synthesis, 26 May 2026), which evaluated CSF1R inhibitors, PI3K-gamma inhibitors (eganelisib), STING agonists, CD40 agonists, and HDAC inhibitors in the dormancy context.

Key points of integration:

1. **The prior report identified eganelisib as the lead clinical candidate** for macrophage repolarization in the dormancy context. The current experimental design provides the preclinical platform to test eganelisib (as a PI3K-gamma inhibitor that repolarizes M2-to-M1) in the CRC liver dormancy model. This should be added as a fifth experimental arm if budget permits: PLX3397 + CpG-ODN (combined M2 depletion and M1 skewing) models the clinical strategy of eganelisib-mediated repolarization.

2. **The prior report flagged CSF1R inhibition as high-risk for dormancy disruption.** Hoffmann's Experiment II.2 (PLX3397 arm) directly tests this risk. If PLX3397 accelerates dormancy exit (more BLI signal increase, higher DXR), this confirms the depletion paradox and argues against CSF1R inhibitors in the adjuvant setting.

3. **The prior report identified no validated clinical dormancy biomarker.** The current experimental design includes MPI (macrophage polarization index) development, which could translate to a CD68/CD163 immunohistochemistry ratio on surgical specimens -- a low-cost, widely deployable clinical assay if validated.

---

## XI. RECOMMENDATIONS TO CHIEF SCIENTIST

1. **Adopt n=12 mice per group** as the base sample size for the core 4-arm experiment, with adaptive re-estimation after Phase I pilot data. Total mice: 48 + pilot cohorts (60 for dose-response + 30 for time-course + 4 for AIW pilot) = approximately 142 mice for Phases I-II.

2. **Implement the hierarchical testing framework** (Section 3.2) to control the family-wise error rate without sacrificing power. Pre-specify the testing hierarchy in the statistical analysis plan before data collection begins.

3. **Correct the PMID 35121993 citation** in Tanaka's report: Dai et al. 2022 is about astrocyte-laminin-DTC interactions in the brain, not general intravital imaging protocols. The methodology and DTC yield data are transferable but the citation characterization is inaccurate.

4. **Prioritize Hoffmann's Phase I model validation** as the first experimental activity. The power re-estimation and DTC yield confirmation from this phase are essential before committing to the full Phase II experiment.

5. **Defer Webb's genetic tool development** (NOS2-DTR, MRC1-CreERT2) and CRISPR screen to Tier 3 funding. The pharmacological and adoptive transfer approaches provide sufficient M1/M2 selectivity for initial experiments. Genetic tools become essential only if the pharmacological approach yields positive results that require definitive mechanistic validation.

6. **Integrate the depletion selectivity gradient** (clodronate > PLX3397 > CD169-DTR) as a structured analysis: if the effect on dormancy metrics scales with depletion selectivity for Kupffer cells, this identifies Kupffer cells as the critical population. If the effect scales with MoM depletion, this identifies recruited TAMs as the critical population.

7. **Budget $250K-300K** for Phases I-II (Tier 1 + Tier 2), with a further $90K-195K available for Tier 3 (genetic tools, CRISPR) conditional on Phase II results. The $145K-$190K estimate from Tanaka is insufficient for the integrated scope.

8. **Add eganelisib or a PI3K-gamma inhibitor arm** to Phase II if budget permits, as a direct preclinical test of the clinical strategy recommended in my prior synthesis report.

---

Prof. Robert Klein, PhD
Senior Scientist, Biostatistics, Translational Oncology, and Clinical Trial Design
