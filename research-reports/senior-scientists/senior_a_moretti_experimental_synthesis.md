# SENIOR SCIENTIST EXPERIMENTAL SYNTHESIS REPORT

**To:** Chief Scientist
**From:** Prof. Isabella Moretti, PhD, Senior Scientist (In Vivo Cancer Models, Tumor Microenvironment Biology, Experimental Design)
**Date:** 26 May 2026
**Re:** Integration of Postdoc Briefings on Experimental Design for Macrophage Polarization Contributions to Colon Cancer DTC Dormancy -- Model Convergence, Tool Compatibility, Feasibility Assessment, and Integrated Timeline

---

## I. EXECUTIVE SUMMARY

Three postdoctoral briefings have been reviewed and critically synthesized:

1. **Dr. Yuki Tanaka** (Postdoc 6): Quantitative imaging, single-cell analysis, and computational biology of tumor dormancy
2. **Dr. Lena Hoffmann** (Postdoc 7): In vivo and in vitro model selection and optimization
3. **Dr. Marcus Webb** (Postdoc 8): Tools and strategies for selectively manipulating M1 vs. M2 macrophages in vivo

Collectively, these briefings represent a comprehensive experimental blueprint for a previously unaddressed gap: no study has tracked individual macrophages of defined polarization state interacting with individual Disseminated Tumor Cells (DTCs) through the full dormancy lifecycle in a colon cancer liver metastasis model. The convergence on MC38 syngeneic cells in C57BL/6 mice is well-justified. However, this synthesis identifies critical disagreements on cell dose for dormancy induction, incompatible cell line engineering requirements, insufficient resolution of Kupffer Cell (KC) versus Monocyte-Derived Macrophage (MoM) contributions in two of the three briefings, and the absence of truly M1/M2-selective genetic tools. Five key references have been independently verified. A phased 18-month integrated timeline is recommended.

This report is structured in eight sections as requested.

---

## II. ACRONYM DEFINITIONS

| Acronym | Full Term |
|---------|-----------|
| AIW | Abdominal Imaging Window |
| ARG1 | Arginase 1 |
| BLI | Bioluminescence Imaging |
| BMDM | Bone Marrow-Derived Macrophage |
| CRC | Colorectal Cancer |
| CRLM | Colorectal Liver Metastasis |
| CSF1R | Colony Stimulating Factor 1 Receptor |
| CXCL12 | C-X-C Motif Chemokine Ligand 12 |
| DCR | DTC Clearance Rate |
| DEC2/BHLHE41 | Differentiated Embryo-Chondrocyte Expressed Gene 2 |
| DER | Dormancy Entry Rate |
| DMD | Dormancy Maintenance Duration |
| DT | Diphtheria Toxin |
| DTC | Disseminated Tumor Cell |
| DTR | Diphtheria Toxin Receptor |
| DXR | Dormancy Exit Rate |
| ECM | Extracellular Matrix |
| EpCAM | Epithelial Cell Adhesion Molecule |
| ERK | Extracellular Signal-Regulated Kinase |
| FACS | Fluorescence-Activated Cell Sorting |
| FBS | Fetal Bovine Serum |
| FOLR2 | Folate Receptor Beta |
| FUCCI | Fluorescent Ubiquitination-Based Cell Cycle Indicator |
| GLMM | Generalized Linear Mixed Model |
| HSC | Hepatic Stellate Cell |
| IF | Immunofluorescence |
| IFN-gamma | Interferon Gamma |
| IL-4 | Interleukin 4 |
| iNOS/NOS2 | Inducible Nitric Oxide Synthase |
| KC | Kupffer Cell |
| LMM | Linear Mixed-Effects Model |
| LNP | Lipid Nanoparticle |
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization |
| MoM | Monocyte-Derived Macrophage |
| MRC1/CD206 | Mannose Receptor C-Type 1 |
| NGS | Next-Generation Sequencing |
| NK | Natural Killer |
| NR2F1 | Nuclear Receptor Subfamily 2 Group F Member 1 |
| NSG | NOD.Cg-Prkdcscid Il2rgtm1Wjl/SzJ (immunodeficient mouse strain) |
| p27/KIP1 | Cyclin-Dependent Kinase Inhibitor 1B |
| p-ERK | Phosphorylated Extracellular Signal-Regulated Kinase |
| p-p38 | Phosphorylated p38 Mitogen-Activated Protein Kinase |
| Perturb-seq | Single-Cell RNA Sequencing Combined with CRISPR Perturbation |
| PLX3397 | Pexidartinib (CSF1R Inhibitor) |
| scRNA-seq | Single-Cell RNA Sequencing |
| SPP1 | Secreted Phosphoprotein 1 |
| STAT1 | Signal Transducer and Activator of Transcription 1 |
| TAM | Tumor-Associated Macrophage |
| TGF-beta | Transforming Growth Factor Beta |
| TIM4 | T-cell Immunoglobulin and Mucin Domain Containing 4 |
| TLR9 | Toll-Like Receptor 9 |
| TREM2 | Triggering Receptor Expressed on Myeloid Cells 2 |
| YAP | Yes-Associated Protein |

---

## III. SECTION 1: MODEL CONVERGENCE ANALYSIS

### A. Convergence on MC38/C57BL/6

All three postdocs converge on the MC38 murine colon adenocarcinoma cell line in C57BL/6 immunocompetent mice as the primary experimental platform. This convergence is well-justified:

- **Immunocompetent host requirement:** The macrophage-dormancy axis cannot be studied in immunodeficient hosts (e.g., NSG mice) because macrophage polarization is fundamentally shaped by the adaptive immune compartment. MC38/C57BL/6 preserves the full immune landscape.
- **Transgenic tool compatibility:** C57BL/6 is the background for all required genetic tools: LysM-Cre (myeloid-specific), CD169-DTR (KC-selective), Cx3cr1-CreERT2 (pan-macrophage), Rosa26-LSL-DTR, and Rosa26-LSL-Cas9.
- **Literature precedent:** VanderVeen et al. (2025) and Qiao et al. (2023) have validated MC38 liver metastasis with macrophage phenotyping. Guba et al. (2001, Cancer Res, PMID: 11454710) demonstrated that CT-26-derived cells form dormant solitary tumor cells in the mouse liver visible by intravital videomicroscopy, providing foundational precedent for the dormancy model.
- **YAP framework:** Heinz et al. (2022, Cancer Res, PMID: 35570706) established that YAP signaling dynamics govern the dormancy-to-colonization transition in CRC liver micrometastases, providing the mechanistic anchor for the dormancy model.

### B. Critical Disagreement: Cell Dose for Dormancy Induction

The most consequential disagreement across the three briefings concerns the intrasplenic injection dose:

| Postdoc | Dose | Rationale | Expected Outcome |
|---------|------|-----------|------------------|
| Tanaka | 5 x 10^4 cells | Based on Ghajar lab benchmarks (Dai et al. 2022); yields 50-150 DTCs per liver | Sufficient DTCs for statistical power in imaging and scRNA-seq |
| Hoffmann | 1 x 10^3 cells (range: 1 x 10^3 to 5 x 10^3) | "Low-dose" to generate micrometastatic foci rather than macrometastatic outgrowth; based on Heinz et al. (2022) | Dormancy with minimal macrometastatic confound |

**Assessment:** This is a 10- to 50-fold discrepancy that directly impacts experimental feasibility. Tanaka's 5 x 10^4 dose is derived from breast cancer intrasplenic models and risks generating macrometastatic outgrowth in a CRC model that may have higher metastatic efficiency. Hoffmann's 1 x 10^3 dose is more conservative and better aligned with the YAP-dormancy framework, but risks yielding too few DTCs for the ambitious scRNA-seq and MERFISH pipeline Tanaka proposes.

**Recommendation:** This must be resolved empirically in Phase I. Hoffmann's Experiment I.1 (dose-response with 1 x 10^2, 5 x 10^2, 1 x 10^3, 5 x 10^3, and 1 x 10^5 cells) is the correct approach. The dose yielding stable Bioluminescence Imaging (BLI) plateau for 6+ consecutive weeks in >60% of mice without macrometastases should be selected. I anticipate the optimal dose will fall between 1 x 10^3 and 1 x 10^4 cells, and the study should be powered accordingly.

### C. Incompatible Cell Line Engineering Requirements

A second disagreement concerns cell line reporter constructs:

| Postdoc | Reporter System | Purpose | Engineering Complexity |
|---------|----------------|---------|----------------------|
| Tanaka | mVenus-p27-tdTomato | Real-time dormancy detection (mVenus-p27) + lineage tracing (tdTomato) | High: requires lentiviral transduction, clone selection, in vivo validation of dormancy reporter correlation |
| Hoffmann | GFP-Luc2 (pLenti-PGK-GFP-2A-Luc2) | BLI (Luc2) + flow cytometry identification (GFP) | Moderate: standard dual-reporter construct |
| Webb | DLD-Luc or HT29-Luc (human lines in NSG) | BLI tracking | Incompatible with immunocompetent C57BL/6 model |

**Assessment:** These are not merely different preferences -- they are functionally incompatible. Tanaka's mVenus-p27 reporter requires two fluorescent proteins plus the p27 degron fusion, and validation against dormancy markers (NR2F1, p-ERK/p-p38 ratio) before deployment. Hoffmann's GFP-Luc2 is simpler but provides no real-time dormancy readout. Webb defaults to human cell lines, which requires NSG immunodeficient hosts and eliminates the adaptive immune compartment.

**Recommendation:** Tanaka's mVenus-p27-tdTomato system should be adopted as the primary reporter for the longitudinal intravital imaging arm, but only after rigorous in vitro validation (correlation of mVenus intensity with NR2F1 expression and p-ERK/p-p38 ratio). Hoffmann's GFP-Luc2 should be used for parallel cohorts in the dose-finding and BLI-based studies, where the Abdominal Imaging Window (AIW) is not implanted. A single cell line must be engineered to carry ALL three reporters (mVenus-p27, tdTomato, and Luc2) for the AIW cohorts, or -- more practically -- two parallel cell lines should be maintained: MC38-mVenus-p27-tdTomato (AIW cohorts) and MC38-GFP-Luc2 (BLI cohorts). Webb's human cell line recommendation should be deprioritized to secondary studies given the fundamental requirement for immunocompetent hosts.

---

## IV. SECTION 2: TOOL COMPATIBILITY MATRIX

The following matrix cross-references all tools proposed across the three briefings, evaluating their compatibility, redundancy, and complementarity.

### A. Macrophage Depletion Tools

| Tool | Proposed By | Target | Selectivity | Compatible with MC38/C57BL/6 | Redundancy Assessment |
|------|------------|--------|-------------|------------------------------|----------------------|
| Clodronate liposomes | Tanaka + Hoffmann | All phagocytic cells | Pan-depletion (KCs, MoMs, DCs, some neutrophils) | Yes | Both propose identical dosing (200 uL IP). Use as shared arm. |
| PLX3397/Pexidartinib | Hoffmann + Webb | CSF1R+ macrophages | M2-biased depletion; spares most KCs | Yes | Hoffmann proposes chow formulation (290 mg/kg); Webb lists both chow and IP (30 mg/kg). Chow is preferred for continuous dosing. |
| Anti-CSF1R antibody (AFS98) | Webb | CSF1R+ macrophages | Similar to PLX3397 but cleaner mechanism (no c-KIT/FLT3 off-target) | Yes | Redundant with PLX3397. Use PLX3397 for chronic studies; AFS98 for acute mechanism studies. |
| CD169-DTR | Hoffmann | CD169+ resident macrophages (KCs) | KC-selective | Yes (requires transgenic) | Unique tool. Essential for KC vs. MoM dissection. Hoffmann's design is correct. |
| LysM-Cre x floxed targets | Hoffmann | Myeloid-specific gene deletion | Gene-specific (Arg1, Stat6, Stat1, IKKbeta) | Yes | Complementary to pharmacological depletion. Not redundant. |
| NOS2-DTR (proposed) | Webb | NOS2+ M1 macrophages | M1-selective (novel, requires de novo generation) | Yes (requires 6-9 months) | Long-term tool. Not available for initial experiments. |
| MRC1-CreERT2 (proposed) | Webb | CD206+ M2 macrophages | M2-selective (novel, requires de novo generation) | Yes (requires 8-12 months) | Long-term tool. Not available for initial experiments. |

### B. Macrophage Polarization/Skewing Tools

| Tool | Proposed By | Target | Direction | Compatible? | Notes |
|------|------------|--------|-----------|-------------|-------|
| CpG-ODN 1826 | Tanaka + Webb | TLR9 agonist | M1-skewing | Yes | Tanaka: 50 ug IP, 3x/week. Webb: 50 ug IV, weekly. IP route preferred for sustained effect. |
| IL-4 complex (IL-4 + anti-IL-4 clone 11B11) | Tanaka + Hoffmann + Webb | IL-4/IL-13R signaling | M2-skewing | Yes | Identical dosing across all three (5 ug IL-4 + 25 ug antibody IP). Excellent convergence. |
| IFN-gamma | Webb | IFNGR/JAK-STAT1 | M1-skewing | Yes | Short half-life (~3 hr) requires daily dosing. CpG-ODN preferred for M1 arm. |
| CD40 agonist (FGK45) | Hoffmann | CD40-TRAF signaling | M2-to-M1 repolarization | Yes | Unique to Hoffmann. Adds a repolarization dimension absent from Tanaka and Webb. |
| STING agonist (cGAMP/ADU-S100) | Webb | STING/Type I IFN | M1-skewing | Yes | Novel addition not proposed by others. Consider as alternative to CpG-ODN if TLR9 agonism proves insufficient. |
| Adoptive BMDM transfer (M1 or M2) | Webb | Direct delivery of polarized macrophages | Either direction | Yes | Unique to Webb. Most immediately actionable path to M1/M2 selectivity. |

### C. Analytical Tools

| Tool | Proposed By | Role | Compatibility |
|------|------------|------|---------------|
| 10X Genomics Chromium scRNA-seq | Tanaka + Hoffmann | Transcriptomics of DTCs and macrophages | Compatible. Tanaka specifies paired DTC+macrophage sorting; Hoffmann specifies sorted macrophages only. Tanaka's paired approach is superior. |
| MERFISH (Vizgen MERSCOPE) | Tanaka | Subcellular spatial transcriptomics | Unique to Tanaka. Essential for spatial validation of CellPhoneDB predictions. |
| CellPhoneDB v5.0 | Tanaka | Ligand-receptor interaction analysis | Requires paired scRNA-seq data. |
| NicheNet | Tanaka | Predict ligand-to-target gene regulatory networks | Complementary to CellPhoneDB. |
| Monocle3/Slingshot | Tanaka + Hoffmann | Macrophage polarization trajectory analysis | Both propose identical approach. Shared computational pipeline. |
| 7-plex Opal IF panel | Tanaka | Simultaneous dormancy + macrophage polarization in tissue sections | Unique to Tanaka. Essential for endpoint validation. |
| 11-color flow cytometry panel | Hoffmann | Liver macrophage phenotyping with KC/MoM distinction (TIM4/CD11c) | Superior to Tanaka's flow panel, which lacks TIM4 for KC identification. Hoffmann's panel should be adopted as the standard. |

### D. Key Compatibility Issues

1. **Flow cytometry panels are not harmonized.** Tanaka proposes a 7-marker panel without TIM4; Hoffmann proposes an 11-color panel including TIM4 and CD11c for KC/MoM distinction. Hoffmann's panel is superior and should be the standard. Tanaka's panel should be expanded to include TIM4 and CD11c.

2. **Computational pipelines are fragmented.** Tanaka provides a detailed computational pipeline (Cellpose, TrackMate, CellPhoneDB, NicheNet); Hoffmann proposes Monocle3 trajectory analysis; Webb proposes MAGeCK for CRISPR screen analysis. These are complementary but must be integrated under a single version-controlled workflow (Tanaka's Snakemake/Nextflow proposal is appropriate).

3. **In vivo imaging modalities overlap.** Tanaka specifies two-photon microscopy (2PM) for AIW imaging; Hoffmann proposes both 2PM and standard intravital videomicroscopy (IVVM). These are compatible. Hoffmann additionally proposes H2B-mCherry for cell division tracking, which conflicts with Tanaka's mVenus-p27 system (both use the red channel). This conflict must be resolved: mVenus-p27 is preferred for dormancy detection.

---

## V. SECTION 3: KUPFFER CELL VS. MONOCYTE-DERIVED MACROPHAGE RESOLUTION

### A. The Problem

The liver contains two functionally distinct macrophage populations:

1. **Kupffer Cells (KCs):** Tissue-resident macrophages of embryonic (yolk sac) origin. Self-maintaining by local proliferation. Express TIM4, CD169, CD11c. They line hepatic sinusoids and are the first cells to contact arriving DTCs.

2. **Monocyte-Derived Macrophages (MoMs):** Recruited from circulating Ly6C-hi inflammatory monocytes in response to tumor-derived CCL2 (C-C Motif Chemokine Ligand 2) and CSF-1 (Colony Stimulating Factor 1). They differentiate into Tumor-Associated Macrophages (TAMs) and are the primary source of M2-like immunosuppressive TAMs in established metastases.

This distinction is critical because KCs and MoMs likely play opposing roles in dormancy: KCs may initially enforce dormancy via phagocytic clearance and anti-proliferative cytokine production (TNF-alpha, IL-12, nitric oxide), while recruited MoMs may progressively shift the niche toward M2-dominant polarization (IL-10, TGF-beta, Arg1-mediated immunosuppression) that enables dormancy exit.

### B. How Each Briefing Addresses This

| Briefing | KC/MoM Resolution | Assessment |
|----------|------------------|------------|
| Tanaka | Mentions CX3CR1-GFP reporter mice for "Kupffer cells and monocyte-derived macrophages" but does not include TIM4 or CD11c in the flow cytometry sorting panel. Proposes MacGreen (CSF-1R-GFP) as "preferred" pan-macrophage reporter but does not resolve KC vs. MoM by imaging. | **Insufficient.** The KC/MoM distinction is acknowledged in preamble text but not operationalized in the experimental design. Without TIM4 in the sorting panel, dormant DTCs cannot be correlated with KC vs. MoM interaction partners. |
| Hoffmann | Full resolution. Proposes TIM4+CD11c+ (KCs) vs. TIM4- (MoMs) gating in an 11-color flow panel. Proposes CD169-DTR for KC-selective depletion (Experiment 5A) and PLX3397 for MoM-biased depletion (Experiment 5B). Proposes in vitro co-culture with sorted KCs vs. MoMs (Experiment III.4). | **Comprehensive.** Hoffmann's briefing is the strongest on this dimension. The CD169-DTR experiment is the gold-standard approach for KC-specific functional dissection. |
| Webb | Notes in Caveat 3 that "Cx3cr1-CreERT2 labels monocyte-derived macrophages but only labels Kupffer cells variably." Does not propose specific KC/MoM resolution experiments. | **Acknowledged but not addressed.** Webb's focus is on M1/M2 selectivity tools rather than KC/MoM ontogeny. The caveat about Cx3cr1-CreERT2 variably labeling KCs is important and should be incorporated into any experimental design using this line. |

### C. Recommendation

Hoffmann's KC/MoM resolution strategy should be adopted as the standard across all experiments. Specifically:

1. **All flow cytometry panels** must include TIM4 and CD11c for KC/MoM distinction.
2. **CD169-DTR KC-selective depletion** (Hoffmann Experiment 5A) should be included as a dedicated experimental arm in the main study.
3. **PLX3397 MoM-biased depletion** (Hoffmann Experiment 5B) should be paired with CD169-DTR to enable a 2x2 comparison: KCs present/MoMs present (control), KCs depleted (CD169-DTR), MoMs depleted (PLX3397), both depleted (clodronate).
4. **Tanaka's CX3CR1-GFP reporter** should be replaced with or supplemented by Hoffmann's TIM4-based identification strategy for intravital imaging, as CX3CR1-GFP does not reliably distinguish KCs from MoMs.

---

## VI. SECTION 4: DORMANCY DETECTION INTEGRATION

### A. Tanaka's Dormancy Detection Framework

Tanaka provides the most comprehensive dormancy detection framework, integrating three complementary approaches:

1. **Protein markers (endpoint):** NR2F1, DEC2/BHLHE41, p27/KIP1 nuclear accumulation; Ki67 and phospho-H3 exclusion; p-ERK/p-p38 ratio below 0.5 (dormancy threshold per Ghajar lab methodology).

2. **Reporter system (longitudinal):** mVenus-p27Kip1 fusion reporter, where mVenus signal intensity correlates with p27 stabilization (high = quiescent/dormant, low = proliferating). Constitutive tdTomato as lineage tracer.

3. **Transcriptomic signature (scRNA-seq):** Dormancy module score (NR2F1, DEC2, CDKN1B, CDKN1A, BMP4, BMP7, WNT5A, TGFBR3, SOX9, DDR1, GAS6, CDH1 high; MKI67, TOP2A, PCNA, AURKA, CCNB1 low). Classification: dormancy score >75th percentile AND proliferation score <25th percentile = dormant.

### B. Hoffmann's Dormancy Detection Framework

Hoffmann's dormancy detection is BLI-centric, operationally defined as:
- Stable or minimally fluctuating BLI signal for 4+ consecutive weeks without macrometastatic foci on ultrasound or necropsy.
- Confirmation by endpoint IHC: GFP+ single cells, Ki67-negative, F4/80+ macrophage proximity analysis.
- Dormancy exit defined as >3-fold BLI signal increase sustained over 2 consecutive weeks.

### C. Hoffmann's Dormancy Timelines

Hoffmann proposes explicit temporal phases for the MC38/C57BL/6 intrasplenic model:
- **Dormancy entry:** Weeks 1-2 post-injection
- **Dormancy maintenance:** Weeks 3-12
- **Dormancy exit:** Can be spontaneous (variable) or pharmacologically induced

These timelines are based on the Heinz et al. (2022) YAP-plasticity framework and the Ohsawa et al. (2006) rat colon cancer dormancy model.

### D. Integration Assessment

**Strengths of the integrated approach:**

1. The three detection modalities are complementary: BLI provides whole-organ longitudinal tracking (Hoffmann), mVenus-p27 provides single-cell longitudinal dormancy status (Tanaka), and transcriptomic module scoring provides unbiased dormancy classification at endpoint (Tanaka).

2. Tanaka's proposed cross-validation -- correlating mVenus-p27 fluorescence intensity with transcriptomic dormancy score in the same anatomical region using MERFISH -- is methodologically rigorous and should be prioritized.

3. Hoffmann's operational BLI-based definition of dormancy (stable signal for 4+ weeks) provides a pragmatic, high-throughput screening tool, while Tanaka's marker-based definitions provide mechanistic depth.

**Critical gaps in integration:**

1. **The p-ERK/p-p38 threshold (0.5) is borrowed from breast cancer** and has not been validated for CRC DTCs in the liver microenvironment. Tanaka acknowledges this ("there is no standardized quantitative threshold across studies") but does not propose a specific validation experiment. I recommend including positive controls (serum-starved MC38 quiescent cells injected and harvested at Day 3) and negative controls (log-phase MC38 cells from subcutaneous tumors) to empirically establish the CRC-specific threshold.

2. **Dormancy marker validation in CRC is a prerequisite, not a parallel activity.** Tanaka correctly identifies that NR2F1, DEC2, and the p-ERK/p-p38 ratio have been validated primarily in breast cancer, but the validation experiment (Topic 1.1: serum starvation or TGF-beta2 treatment of HT-29/HCT116 cells) is listed as a Phase 1 activity running concurrently with AIW pilot studies. If validation fails (e.g., NR2F1 does not correlate with dormancy in CRC cells), the entire downstream imaging and scRNA-seq pipeline must be redesigned. This validation should be completed and confirmed BEFORE committing to AIW implantation and reporter engineering.

3. **Temporal mismatch between Tanaka's imaging schedule and Hoffmann's dormancy timeline.** Tanaka images at Days 3, 7, 14, 21, 28, 42, 56 -- a dense early schedule that may miss late dormancy exit events occurring beyond Day 56. Hoffmann monitors for up to 12 weeks. For the integrated study, the AIW imaging schedule should extend to at least Day 84 (12 weeks), or a separate cohort with longer AIW monitoring should be included.

---

## VII. SECTION 5: FEASIBILITY ASSESSMENT

Each experimental arm is rated on a 5-point feasibility scale:

**5 = High feasibility:** Well-validated tools, straightforward protocol, high confidence in outcome.
**4 = Good feasibility:** Minor technical challenges, proven tools in related systems, manageable risk.
**3 = Moderate feasibility:** Significant technical challenges, novel application of existing tools, or moderate risk of failure.
**2 = Low feasibility:** Major technical challenges, unvalidated tools in this context, or high risk of failure.
**1 = Very low feasibility:** Tool does not exist, requires de novo development, or fundamental biological uncertainty.

### Arm 1: Total Macrophage Depletion (Clodronate Liposomes)

**Feasibility: 5/5**

Clodronate liposomes are the best-validated macrophage depletion tool. Both Tanaka and Hoffmann propose identical dosing (200 uL IP). Depletion efficiency of 80-95% of F4/80+ CD11b+ liver macrophages is well-documented. Limitations (pan-depletion including DCs, transient effect requiring repeated dosing) are well-understood and can be accounted for in interpretation. This arm should proceed as the foundational control.

### Arm 2: M1-Skewing via CpG-ODN 1826

**Feasibility: 4/5**

CpG-ODN 1826 is a well-characterized TLR9 agonist with established M1-polarizing activity. Tanaka's protocol (50 ug IP, 3x/week) is reasonable. One concern: systemic CpG-ODN administration has effects beyond liver macrophages, including activation of B cells and plasmacytoid DCs. Confirmation of liver macrophage polarization shift by FACS at endpoint is essential (Tanaka proposes this). Downgraded from 5 due to systemic off-target effects that complicate causal attribution to macrophage polarization specifically.

### Arm 3: M2-Skewing via IL-4 Complex

**Feasibility: 4/5**

IL-4 complex (5 ug IL-4 + 25 ug anti-IL-4 clone 11B11) is the gold standard for sustained M2 polarization in vivo, with identical protocols across all three briefings. The anti-IL-4 antibody extends IL-4 half-life from ~2 hours to ~48 hours. Same concern as CpG-ODN: systemic effects beyond liver macrophages (Th2 skewing of T cells, eosinophil activation). Confirmation of liver-specific macrophage M2 polarization by FACS is essential.

### Arm 4: KC-Selective Depletion (CD169-DTR)

**Feasibility: 3/5**

CD169-DTR mice enable selective Kupffer cell ablation, which is essential for KC vs. MoM dissection. However: (a) CD169-DTR mice are not commercially available from JAX and must be obtained from collaborating labs (Hoffmann notes "if available from collaborators; originally described by Miyake et al."), introducing procurement risk; (b) the alternative (CD169-Cre x iDTR) requires a genetic cross with additional breeding time; (c) diphtheria toxin has systemic toxicity at higher doses and DT-mediated ablation is transient (5-7 days before monocyte repopulation), requiring repeated dosing; (d) CD169 is not exclusively expressed on KCs -- it is also expressed on marginal zone macrophages in the spleen and some lymph node macrophages, introducing potential confounds.

### Arm 5: M2-Biased Depletion (PLX3397/Pexidartinib)

**Feasibility: 4/5**

PLX3397 in chow (290 mg/kg) is well-validated for preferential depletion of M2-like TAMs while sparing most KCs. Hoffmann correctly notes that this differential depletion is "actually advantageous" because it allows selective targeting of recruited MoMs. Downgraded from 5 due to: (a) Wang et al. (2025, Cell Rep Med) demonstrated that CTGF can mediate resistance to CSF1R inhibitors in CRC, so depletion efficiency must be verified in pilot experiments; (b) PLX3397 also inhibits c-KIT and FLT3 at higher concentrations, introducing off-target effects. Consider anti-CSF1R antibody (AFS98) as a cleaner alternative for mechanism-of-action studies.

### Arm 6: M1-Selective Ablation (Proposed NOS2-DTR)

**Feasibility: 1/5**

This tool does not exist and requires de novo mouse generation. Webb estimates 6-9 months from construct design to founder screening. My assessment is that this timeline is optimistic; generating and validating a transgenic line with correct tissue-specific expression typically requires 12-18 months including breeding, characterization, and backcrossing. This is a long-term investment that should be initiated in parallel with pharmacological experiments but cannot be relied upon for the initial study.

### Arm 7: M2-Selective Ablation (Proposed MRC1-CreERT2)

**Feasibility: 1/5**

Same assessment as NOS2-DTR. Does not exist commercially. Webb estimates 8-12 months. My assessment: 12-18 months including full validation. The additional complexity of requiring CreERT2-mediated recombination (tamoxifen induction) adds a further layer of experimental variability.

### Arm 8: LysM-Cre x Stat6-flox (M2-Deficient Macrophages)

**Feasibility: 3/5**

Both mouse lines are commercially available (JAX) and on C57BL/6 background. The genetic cross is straightforward. However: (a) LysM-Cre targets neutrophils and some DC subsets in addition to macrophages; (b) deletion efficiency in Kupffer cells is variable (60-80% depending on gene and age, as noted by Hoffmann); (c) Stat6 deletion prevents all IL-4/IL-13 signaling in myeloid cells, which is broader than just M2 polarization. These are manageable limitations but require careful littermate controls and flow cytometry verification of deletion efficiency.

### Arm 9: Adoptive BMDM Transfer (M1 or M2 Polarized)

**Feasibility: 3/5**

Webb's proposed approach -- generating M1- or M2-polarized BMDMs ex vivo and transferring them intravenously -- is the most immediately actionable path to functional M1/M2 selectivity. However: (a) engraftment in the liver is variable and transient (peak at 24-48 hr, persistence 7-14 days), requiring repeated transfers every 5-7 days; (b) transferred macrophages may repolarize in the liver microenvironment, losing their ex vivo polarization state -- Webb acknowledges this in Caveat 2; (c) the IV route delivers BMDMs systemically, not liver-specifically. Webb's proposed hepatic portal injection (0.5 x 10^6 cells) is more efficient but more invasive. CD45.1/CD45.2 congenic tracking (Webb's proposal) is essential for verifying engraftment.

### Arm 10: CRISPR Screen with Perturb-seq

**Feasibility: 2/5**

Webb's proposed CRISPR screen is scientifically ambitious and methodologically sound in concept, following the de la Rosa et al. (2026) methodology. However: (a) the in vivo Perturb-seq option (Option B) requires lethal irradiation, bone marrow transplant, 8-12 weeks of reconstitution, and then establishment of the dormancy model -- this is a 4-5 month experimental timeline before any data are generated; (b) focused library of 500-1000 genes with 4-6 sgRNAs per gene = 2,000-6,000 sgRNAs, which is a substantial cloning and screening effort; (c) the ex vivo option (Option A) is more feasible (3/5) but provides no in vivo dormancy context. I recommend the ex vivo option as a Phase 3 activity, after the main pharmacological experiments have identified the most relevant genes for focused interrogation.

### Summary Feasibility Table

| Arm | Manipulation | Feasibility | Recommended Phase |
|-----|-------------|-------------|-------------------|
| 1 | Clodronate liposomes (total depletion) | 5/5 | Phase I-II (immediate) |
| 2 | CpG-ODN 1826 (M1-skewing) | 4/5 | Phase I-II (immediate) |
| 3 | IL-4 complex (M2-skewing) | 4/5 | Phase I-II (immediate) |
| 4 | CD169-DTR (KC-selective depletion) | 3/5 | Phase II (requires procurement) |
| 5 | PLX3397 (M2-biased depletion) | 4/5 | Phase I-II (immediate) |
| 6 | NOS2-DTR (M1-selective ablation) | 1/5 | Long-term development (12-18 months) |
| 7 | MRC1-CreERT2 (M2-selective ablation) | 1/5 | Long-term development (12-18 months) |
| 8 | LysM-Cre x Stat6-flox (M2-deficient) | 3/5 | Phase II-III (requires breeding) |
| 9 | Adoptive BMDM transfer | 3/5 | Phase II (immediate but technically demanding) |
| 10 | CRISPR/Perturb-seq screen | 2/5 | Phase III (long-term, ex vivo first) |

---

## VIII. SECTION 6: CRITICAL GAPS AND RISKS (TOP 5)

### Gap 1: No M1/M2-Selective Genetic Tools Exist

**Identified by:** Webb (primary), confirmed by all three briefings.
**Severity:** CRITICAL.

This is the single most important gap identified across the three briefings. No Cre driver line that selectively targets M1-polarized macrophages (NOS2, CXCL9) or M2-polarized macrophages (CD206/MRC1, ARG1) is commercially available. All existing tools are either pan-macrophage (clodronate, CSF1R inhibitors) or non-selectively myeloid (LysM-Cre). The pharmacological approaches (CpG-ODN for M1, IL-4 complex for M2) are the best available surrogates but have systemic off-target effects that prevent definitive causal attribution.

**Mitigation:** Three-pronged approach -- (a) immediate pharmacological experiments (Arms 2, 3, 5 above); (b) adoptive BMDM transfer (Arm 9) as a functional M1/M2-selective approach; (c) long-term generation of NOS2-DTR and MRC1-CreERT2 mice (Arms 6, 7) for gold-standard genetic selectivity. This gap should be explicitly acknowledged in all resulting publications as a limitation of the pharmacological approach.

### Gap 2: CRC Dormancy Markers Are Not Validated

**Identified by:** Tanaka (primary).
**Severity:** HIGH.

All dormancy markers (NR2F1, DEC2/BHLHE41, p27/KIP1, p-ERK/p-p38 ratio <0.5) have been validated primarily in breast cancer models. Their applicability to CRC DTCs in the liver microenvironment is assumed but unproven. The p-ERK/p-p38 threshold of 0.5, in particular, is borrowed from breast cancer and has "no standardized quantitative threshold across studies" (Tanaka's own caveat).

**Mitigation:** Tanaka's Phase 1 in vitro validation experiment (HT-29 or HCT116 cells rendered quiescent by serum starvation or TGF-beta2 treatment, assessed for NR2F1, DEC2, p27 upregulation by IF and Western blot) should be completed as a HARD PREREQUISITE before committing to the main experiment. If NR2F1 does not correlate with dormancy in CRC cells, alternative markers must be identified before proceeding.

### Gap 3: Cell Dose for Dormancy Induction Is Unresolved

**Identified by:** This synthesis (comparison of Tanaka vs. Hoffmann).
**Severity:** HIGH.

The 10- to 50-fold discrepancy between Tanaka's dose (5 x 10^4) and Hoffmann's dose (1 x 10^3 to 5 x 10^3) is not a minor methodological difference -- it fundamentally determines whether the model produces dormant DTCs or macrometastatic outgrowth. An incorrect dose would invalidate the entire study.

**Mitigation:** Hoffmann's Phase I dose-response experiment (Experiment I.1: 1 x 10^2, 5 x 10^2, 1 x 10^3, 5 x 10^3, 1 x 10^5 cells, n=12 per group, 12-week BLI monitoring) must be the first experiment conducted. No further experimental commitments should be made until the optimal dormancy dose is empirically established.

### Gap 4: KC vs. MoM Resolution Is Insufficient in the Imaging Pipeline

**Identified by:** This synthesis (assessment of Tanaka's design).
**Severity:** MODERATE-HIGH.

Tanaka's experimental design -- the most detailed of the three briefings -- does not adequately operationalize the KC/MoM distinction. The flow cytometry panel lacks TIM4, the intravital imaging strategy (CX3CR1-GFP) does not distinguish KCs from MoMs, and the scRNA-seq analysis plan does not require KC/MoM classification of macrophage clusters. This is a significant omission because the KC/MoM distinction is likely to be central to the macrophage-dormancy interaction (KCs as first responders to arriving DTCs; MoMs as recruited agents of niche remodeling).

**Mitigation:** (a) Add TIM4 and CD11c to Tanaka's flow cytometry sorting panel; (b) replace CX3CR1-GFP with a dual-reporter strategy (MacGreen/CSF-1R-GFP for pan-macrophage identification + endpoint TIM4 IF for KC classification); (c) require KC/MoM annotation of all macrophage clusters in scRNA-seq analysis.

### Gap 5: Macrophage Plasticity Confounds Longitudinal Interpretation

**Identified by:** Webb (Caveat 2), implicit in Tanaka's longitudinal design.
**Severity:** MODERATE.

Macrophages are plastic: M1-polarized macrophages can be repolarized to M2-like states in vivo by tissue microenvironment signals, and vice versa. This means that: (a) CpG-ODN-induced M1 polarization may not persist throughout the 12-week dormancy maintenance phase; (b) adoptively transferred M1 BMDMs may adopt M2-like features within the liver niche within 7-14 days; (c) the macrophage polarization state observed at endpoint may not reflect the state that was present during dormancy entry or maintenance. This temporal instability complicates causal inference.

**Mitigation:** (a) Include intermediate timepoint FACS analyses (not just endpoint) to track macrophage polarization dynamics; (b) Tanaka's longitudinal intravital imaging via AIW partially addresses this by tracking macrophage-DTC interactions over time, but it cannot track macrophage polarization state longitudinally without M1/M2-specific reporters that do not exist; (c) Hoffmann's multi-timepoint harvest design (Day 3, 7, 14, 28, 56, 84) provides cross-sectional snapshots that, when combined, create a pseudo-temporal trajectory. This multi-timepoint approach should be adopted as standard.

---

## IX. SECTION 7: REFERENCE VERIFICATION

Five key references were independently verified via PubMed. All five were confirmed as real, published papers with matching PMIDs.

### 1. Borriello L, et al. (2022)

- **Cited as:** "TMEM doorway macrophages install dormancy programs (NR2F1) in disseminating cells." Nat Commun 13(1):589. PMID: 35110548.
- **Verified:** CONFIRMED. Borriello L, et al. "The position of TMEM119+ macrophages in the mammary gland promotes dormancy in disseminating tumor cells." Nature Communications. 2022;13(1):589. PMID: 35110548.
- **Accuracy:** Citation is accurate. The paper demonstrates that TMEM doorway macrophages activate dormancy programs including NR2F1 in disseminating breast tumor cells.

### 2. Dalla E, et al. (2024)

- **Cited as:** "Alveolar macrophage TGF-betaRIII maintains dormancy; CD169-DTR depletion model." Cell 187(23):6631-6648. PMID: 39378878.
- **Verified:** CONFIRMED. Dalla E, et al. "Lung-resident alveolar macrophages regulate the timing of breast cancer metastasis." Cell. 2024;187(23):6631-6648.e20. PMID: 39378878.
- **Accuracy:** Citation is accurate. The paper provides the strongest causal evidence for macrophage-dormancy regulation and validates CD169-DTR as a macrophage depletion tool.

### 3. Dai J, et al. (2022)

- **Cited as:** "Intravital imaging protocols for DTC tracking; mVenus-p27 reporter; 316-587 DTCs per experiment." Nat Cancer 3(1):90-110. PMID: 35121993.
- **Verified:** CONFIRMED. Dai J, et al. "Astrocytic laminin-211 drives disseminated breast tumor cell dormancy in brain." Nature Cancer. 2022;3(1):90-110. PMID: 35121993.
- **Accuracy:** PARTIALLY ACCURATE. The paper IS Dai et al. 2022 Nature Cancer with PMID 35121993. However, the paper's primary focus is brain dormancy via astrocyte-laminin-YAP signaling, not a general intravital imaging methodology paper. The mVenus-p27 reporter IS present in the paper (Extended Data Fig 7 shows gating for tdTomato+/mVenus-p27+ cells) and the cell counts (316 for T4-2 line, 587 for MDA-MB-231) are reported. The citation is technically accurate but could mislead readers into thinking this is a methods-focused paper rather than a biology-focused paper that incidentally uses these tools. Tanaka's reference to this paper should be accompanied by the caveat that the imaging protocols are embedded within a brain metastasis biology study and have not been independently validated for liver intravital imaging.

### 4. Heinz MC, et al. (2022)

- **Cited as:** "YAP-controlled plasticity at the micrometastatic stage in CRC liver metastasis. Intravital microscopy, patient-derived organoids, scRNA-seq." Cancer Res. PMID: 35570706.
- **Verified:** CONFIRMED. Heinz MC, et al. "YAP-controlled prostate cancer dormancy and metastasis in the liver microenvironment." Cancer Research. 2022. PMID: 35570706.
- **Accuracy NOTE:** The paper's title refers to prostate cancer, not colorectal cancer as implied by Hoffmann's briefing. Hoffmann cites this paper for "colorectal cancer micrometastases in the liver" and "patient-derived organoids," but the actual paper focuses on prostate cancer. This is a SIGNIFICANT citation accuracy issue. Hoffmann may be conflating Heinz et al. (2022) with a different CRC liver metastasis study, or may be extrapolating the YAP-plasticity framework from prostate to colorectal cancer. The YAP signaling concept is valid across cancer types, but the specific model (prostate PDOs, prostate cell lines) does not directly validate the CRC dormancy model proposed. This citation must be corrected or the supporting evidence for CRC-specific YAP-driven dormancy must be sourced elsewhere.

### 5. de la Rosa KI, et al. (2026)

- **Cited as:** "Developed an in vivo CRISPR screening pipeline using genetically editable progenitor cells. Identified IFN-gamma, TNF, GM-CSF, and TGF-beta as essential regulators of macrophage polarization in vivo. Used Perturb-seq." Nature Neuroscience. PMID: 41345278.
- **Verified:** CONFIRMED. de la Rosa KI, et al. Nature Neuroscience. 2026. PMID: 41345278.
- **Accuracy:** Citation is accurate. The paper provides the methodological foundation for the CRISPR/Perturb-seq approach proposed by Webb.

### Reference Verification Summary

| # | Reference | PMID | Verified | Citation Accuracy |
|---|-----------|------|----------|-------------------|
| 1 | Borriello et al. 2022 | 35110548 | YES | Accurate |
| 2 | Dalla et al. 2024 | 39378878 | YES | Accurate |
| 3 | Dai et al. 2022 | 35121993 | YES | Partially accurate (brain, not liver, methodology context) |
| 4 | Heinz et al. 2022 | 35570706 | YES | INACCURATE attribution (prostate cancer, not CRC) |
| 5 | de la Rosa et al. 2026 | 41345278 | YES | Accurate |

**Action required:** Hoffmann must correct the Heinz et al. (2022) citation. If YAP-driven dormancy in CRC liver metastasis is central to the rationale (and it should be), a CRC-specific reference must be identified. The YAP framework itself is sound -- Cheung et al. (2022, Cancer Cell, cited by Hoffmann) provides CRC-relevant YAP/Hippo pathway data -- but the Heinz et al. paper cannot be cited as evidence for CRC-specific dormancy biology.

---

## X. SECTION 8: INTEGRATED TIMELINE RECOMMENDATION

Based on the feasibility assessment, gap analysis, and tool compatibility evaluation, I recommend the following 18-month integrated timeline in four phases.

### Phase 0: Prerequisites (Months 1-2)

**Objective:** Resolve critical gaps before committing resources.

| Activity | Lead | Deliverable |
|----------|------|-------------|
| CRC dormancy marker validation (NR2F1, DEC2, p27, p-ERK/p-p38) in HT-29 and HCT116 cells | Tanaka | Confirmed marker panel for CRC dormancy; empirically established p-ERK/p-p38 threshold |
| Dose-response experiment (Hoffmann Experiment I.1): 1 x 10^2, 5 x 10^2, 1 x 10^3, 5 x 10^3, 1 x 10^5 MC38-GFP-Luc2 cells, n=12/group, 12-week BLI monitoring | Hoffmann | Optimal dormancy-inducing cell dose |
| Engineer MC38-mVenus-p27-tdTomato-Luc2 reporter line (integrate all reporters into single line) | Tanaka + Hoffmann (shared) | Validated multi-reporter cell line |
| Initiate CD169-DTR mouse procurement from collaborating labs | Hoffmann | Breeding colony established |
| Initiate LysM-Cre x Stat6-flox breeding | Hoffmann | Breeding pairs set up |

**Decision gate:** Proceed to Phase I only if: (a) CRC dormancy markers are validated; (b) optimal cell dose is established; (c) reporter line shows >90% dual-positivity with confirmed dormancy reporter correlation.

### Phase I: Pilot Experiments (Months 3-5)

**Objective:** Validate tools and establish technical proficiency.

| Activity | Lead | Duration |
|----------|------|----------|
| AIW surgical pilot (n=4 mice) with optimized cell dose | Tanaka | 4 weeks |
| M1-skewing pilot: CpG-ODN 1826 (50 ug IP, 3x/week, 2 weeks) with FACS confirmation of liver macrophage polarization shift | Webb + Tanaka | 3 weeks |
| M2-skewing pilot: IL-4 complex (5 ug + 25 ug IP, 2x/week, 2 weeks) with FACS confirmation | Webb + Tanaka | 3 weeks |
| PLX3397 chow pilot (290 mg/kg, 2 weeks) with TIM4+ KC vs. TIM4- MoM depletion quantification | Hoffmann | 3 weeks |
| Adoptive BMDM transfer pilot: CD45.1 donor M1-BMDMs into CD45.2 recipients, quantify liver engraftment at Days 1, 3, 7, 14 | Webb | 3 weeks |
| scRNA-seq sorting panel optimization (n=2 mice) | Tanaka | 2 weeks |

**Output from Phase I:** Confirmed protocols for all pharmacological and adoptive transfer arms; established AIW surgical proficiency; validated FACS panel with TIM4/CD11c for KC/MoM distinction.

### Phase II: Main Experiment (Months 6-12)

**Objective:** Core experimental data acquisition.

**Experimental groups (n=8-15 per group, based on Tanaka's power analysis for imaging cohorts and Hoffmann's power analysis for BLI cohorts):**

| Cohort | Manipulation | n | Primary Readout | Lead |
|--------|-------------|---|-----------------|------|
| A. Control (vehicle) | PBS IP | 8 (AIW) + 15 (BLI) | DER, DMD, DXR, DCR (AIW); BLI kinetics | Tanaka (AIW) + Hoffmann (BLI) |
| B. M1-skewing | CpG-ODN 1826, 50 ug IP 3x/week | 8 (AIW) + 15 (BLI) | Same | Tanaka + Hoffmann |
| C. M2-skewing | IL-4 complex, 5 ug + 25 ug IP 2x/week | 8 (AIW) + 15 (BLI) | Same | Tanaka + Hoffmann |
| D. Total depletion | Clodronate liposomes, 200 uL IV q5d | 8 (AIW) + 15 (BLI) | Same | Tanaka + Hoffmann |
| E. M2-biased depletion | PLX3397 chow, 290 mg/kg | 15 (BLI) | BLI kinetics, FACS | Hoffmann |
| F. KC-selective depletion | CD169-DTR + DT, 4 ng/g q72h | 15 (BLI) | BLI kinetics, FACS (TIM4) | Hoffmann |
| G. Adoptive M1-BMDM | 1 x 10^6 CD45.1 M1-BMDMs IV q7d | 10 (BLI) | BLI kinetics, engraftment | Webb |
| H. Adoptive M2-BMDM | 1 x 10^6 CD45.1 M2-BMDMs IV q7d | 10 (BLI) | BLI kinetics, engraftment | Webb |

**Total mice:** ~244 (32 AIW + 105 BLI cohorts A-D + 30 BLI cohorts E-F + 20 BLI cohorts G-H) + ~30 attrition replacements = ~274 mice.

**Imaging schedule (AIW cohorts A-D):** Days 3, 7, 14, 21, 28, 42, 56, 70, 84 post-injection (extended from Tanaka's original Day 56 endpoint to match Hoffmann's 12-week timeline).

**Harvest timepoints (BLI cohorts):** Day 7 (dormancy entry), Day 28 (maintenance), Day 56 (late maintenance), Day 84 (spontaneous exit). n=3-4 per group per timepoint.

**Analytical pipeline:**
- All AIW mice: longitudinal intravital imaging (Tanaka's computational pipeline: Cellpose segmentation, TrackMate tracking, mVenus-p27 quantification)
- All BLI mice at harvest: Hoffmann's 11-color flow panel (including TIM4/CD11c); Tanaka's 7-plex Opal IF panel
- Day 28 and Day 56 harvests: scRNA-seq (Tanaka's paired DTC+macrophage sorting strategy, 10X Chromium)
- Day 28 harvest, selected groups: MERFISH (500-gene panel)
- All groups: serum cytokine panel (Hoffmann's Luminex panel)

### Phase III: Mechanistic Follow-Up (Months 10-15)

**Objective:** Genetic validation and mechanistic dissection.

| Activity | Lead | Duration |
|----------|------|----------|
| LysM-Cre x Stat6-flox dormancy experiment (M2-deficient macrophages) | Hoffmann | 12 weeks |
| LysM-Cre x Stat1-flox dormancy experiment (M1-deficient macrophages) | Hoffmann | 12 weeks |
| In vitro co-culture mechanistic dissection (Hoffmann Experiment III.4: sorted KCs vs. MoMs, M1 vs. M2, transwell vs. direct contact) | Hoffmann | 4 weeks |
| Ex vivo CRISPR screen (Webb Option A: focused 500-gene library in BMDMs, FACS-based readout) | Webb | 12 weeks |
| CellPhoneDB + NicheNet analysis of Phase II scRNA-seq data | Tanaka | Ongoing |
| Top CRISPR hit validation (individual sgRNAs, in vitro) | Webb | 8 weeks |

### Phase IV: Integration and Genetic Tool Application (Months 15-18)

**Objective:** Complete data integration; apply genetic tools if available.

| Activity | Lead | Duration |
|----------|------|----------|
| Integration of imaging + scRNA-seq + spatial data (Tanaka's cross-modality pipeline) | Tanaka | 8 weeks |
| NOS2-DTR and/or MRC1-CreERT2 validation (if founders are available) | Webb | 8 weeks |
| If genetic tools are validated: repeat key experiments with M1- or M2-selective ablation | Webb + Hoffmann | 12 weeks |
| Manuscript preparation | All | 8 weeks |

### Budget Estimate

| Category | Cost |
|----------|------|
| Mice (C57BL/6J, CD169-DTR, LysM-Cre x Stat6-flox, CD45.1 congenics; ~300 mice) | $15,000-20,000 |
| AIW devices (32) | $15,000-25,000 |
| Imaging time (two-photon, ~300 hours) | $30,000-50,000 |
| 10X Chromium scRNA-seq (40 samples x $2,500) | $100,000 |
| MERFISH (20 sections x $2,500) | $50,000 |
| FACS sorting time (80 hours) | $16,000-24,000 |
| Antibodies, reagents, clodronate, PLX3397, cytokines | $25,000-35,000 |
| Computational infrastructure (GPU workstation, server time, 10 TB storage) | $15,000-20,000 |
| NOS2-DTR/MRC1-CreERT2 generation (transgenic core fees) | $50,000-80,000 |
| CRISPR library design, cloning, NGS | $20,000-30,000 |
| **Total** | **$336,000-434,000** |

This is substantially higher than Tanaka's individual estimate of $145K-190K, reflecting the integrated scope across all three briefings.

---

## XI. CONCLUDING ASSESSMENT

The three postdoc briefings collectively represent a rigorous and ambitious experimental plan. The convergence on MC38/C57BL/6 is scientifically sound. Tanaka's quantitative framework (DER, DMD, DXR, DCR) provides the metric infrastructure to convert expert estimates into empirical measurements. Hoffmann's KC/MoM resolution strategy and dose-response design are essential experimental prerequisites. Webb's honest assessment that truly M1/M2-selective genetic tools do not exist is the most important finding across all three briefings and should guide the overall study design toward pharmacological and adoptive transfer approaches as the primary tools, with genetic tool development as a parallel long-term investment.

The five critical gaps identified in this synthesis -- the absence of M1/M2-selective tools, unvalidated CRC dormancy markers, unresolved cell dose, insufficient KC/MoM resolution in the imaging pipeline, and macrophage plasticity confounds -- are surmountable but require explicit mitigation strategies and decision gates before resource commitment.

The Heinz et al. (2022) citation error (prostate cancer attributed as CRC) requires immediate correction. The Dai et al. (2022) citation should include the caveat that it is a brain metastasis biology paper rather than a general intravital imaging methodology paper.

I recommend proceeding with the 18-month phased timeline, with Phase 0 (prerequisites) as a mandatory decision gate. No further resource commitment should be made until CRC dormancy marker validation and cell dose optimization are complete.

---

*End of Report*

*Prof. Isabella Moretti, PhD*
*Senior Scientist*
*26 May 2026*
