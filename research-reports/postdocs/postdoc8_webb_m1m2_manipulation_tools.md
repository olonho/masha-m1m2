# RESEARCH BRIEFING: TOOLS AND STRATEGIES FOR SELECTIVELY MANIPULATING M1 vs M2 MACROPHAGES IN VIVO

**Prepared for:** Dr. Marcus Webb, PhD
**Topic:** Selective macrophage polarization manipulation for colon cancer dormancy studies
**Date:** 2026-05-26

---

## EXECUTIVE SUMMARY

A central challenge in dissecting macrophage contributions to Disseminated Tumor Cell (DTC) dormancy entry, maintenance, and exit is that current macrophage depletion tools -- clodronate liposomes and Colony Stimulating Factor 1 Receptor (CSF1R) inhibitors -- eliminate or inhibit all macrophage subsets indiscriminately. This briefing confirms that **truly M1-selective or M2-selective genetic tools do not exist as commercially available, off-the-shelf reagents**. No Cre driver lines specific for Inducible Nitric Oxide Synthase (NOS2/iNOS), CXCL9, or other M1 markers are available from Jackson Laboratories (JAX). No Mannose Receptor C-type 1 (CD206/MRC1)-CreERT2 or Arginase 1 (ARG1)-CreERT2 lines exist commercially. This gap constitutes the critical bottleneck you have identified.

However, several creative strategies can achieve functional M1/M2 selectivity by combining existing genetic tools with pharmacological skewing, temporal control, and adoptive transfer approaches. Below I outline these strategies across seven sections, with specific mouse strains, constructs, and reagents.

---

## SECTION 1: GENETIC TOOLS FOR M1-SELECTIVE MANIPULATION

### 1A. The Core Problem

No Cre driver line that selectively targets M1-polarized macrophages is commercially available. Inducible Nitric Oxide Synthase (NOS2), the canonical M1 effector enzyme, is not used as a Cre driver because its expression is inducible rather than constitutive, varies widely across tissue contexts, and is expressed in other cell types (neurons, epithelial cells). CXCL9 and CXCL10 chemokines are similarly unsuitable as driver gene candidates due to broad expression.

### 1B. Strategy: Interferon Regulatory Factor 5 (IRF5)-Driven Approaches

IRF5 is a master transcription factor for M1 polarization and is relatively macrophage-restricted in its expression pattern. While no Irf5-Cre mouse exists commercially, two paths are available:

**Option 1 -- Generate Irf5-CreERT2 knock-in mice:**
- Target the Irf5 locus (mouse chromosome 6, syntenic to human 7q32) with a CreERT2-IRES-eGFP cassette inserted after the stop codon
- Use homology-directed repair via CRISPR-Cas9 in C57BL/6J zygotes
- Screening: PCR genotyping with primer pairs flanking the insertion, followed by flow cytometry for eGFP expression in Lipopolysaccharide (LPS)/Interferon-gamma (IFN-gamma)-stimulated Bone Marrow-Derived Macrophages (BMDMs)
- Expected timeline: 8-12 months from design to breeding-age homozygotes
- Validation: Cross to Rosa26-LSL-tdTomato (JAX #007914), treat with tamoxifen, and confirm tdTomato labeling specifically in M1-polarized macrophages (NOS2+, CD86+, MHC-II-hi) but not M2-polarized macrophages (CD206+, ARG1+)

**Option 2 -- Use Signal Transducer and Activator of Transcription 1 (STAT1)-dependent reporter:**
- STAT1 is essential for M1 polarization downstream of IFN-gamma signaling
- STAT1-GFP reporter mice exist (JAX #012795, Stat1(tm1.1Rlu)/J, though availability should be verified)
- Limitation: STAT1 is expressed in many cell types beyond macrophages, requiring additional cell-type-specific intersection

### 1C. Strategy: Intersectional Genetic Approaches

The most powerful near-term approach uses existing tools in combination:

**Construct: Cx3cr1-CreERT2 x LSL-DTR x IFN-gamma stimulation**

- **Cx3cr1-CreERT2** (fractalkine receptor, expressed in monocytes/macrophages/microglia): The Cx3cr1-CreERT2 line has been extensively validated. Two versions exist:
  - Cx3cr1-CreERT2 mice from the Jung lab (described in Yamasaki et al., Cell Rep 2025, PMID: 40928945) -- note line-dependent differences in recombination efficiency and specificity
  - The Cx3cr1-CreERT2 rat line described by Glotfelty et al., Sci Rep 2025 (PMID: 41366001) for tissue-resident macrophage targeting
- **Rosa26-LSL-DTR** (JAX #007900): Diphtheria Toxin Receptor (human Hbegf) flanked by a Lox-Stop-Lox (LSL) cassette, expressed upon Cre-mediated excision
- **Protocol:**
  1. Cross Cx3cr1-CreERT2 x Rosa26-LSL-DTR mice to generate double-transgenic animals
  2. Inject 4-Hydroxytamoxifen (4-OHT, 75 mg/kg intraperitoneally, dissolved in corn oil at 20 mg/mL) to label all Cx3cr1+ macrophages with DTR
  3. Systemically polarize toward M1 using IFN-gamma (1000 U/intraperitoneally daily for 5 days) or intratumorally using TLR9 agonist (CpG-ODN 1826, 50 ug/mouse)
  4. Administer Diphtheria Toxin (DT, 25 ng/g body weight, intraperitoneally) to deplete DTR+ macrophages
  5. **Critical limitation:** This depletes ALL Cx3cr1+ macrophages, not M1-selectively. The selectivity comes from timing -- deplete before or after pharmacological skewing to infer M1-specific contributions

### 1D. Strategy: M1-Selective Ablation via NOS2 Promoter-Driven DTR

**Generate NOS2-DTR transgenic mice:**
- Clone the human Diphtheria Toxin Receptor (DTR, encoded by Hbegf) under the control of the NOS2 promoter (~2.5 kb upstream regulatory region containing the IFN-gamma and LPS-responsive elements)
- Microinject the construct into fertilized C57BL/6J oocytes
- Upon M1 polarization, NOS2 promoter drives DTR expression selectively in M1 macrophages
- Diphtheria Toxin (DT) injection (25 ng/g, intraperitoneal) then ablates only NOS2+ (M1) cells
- Validation: Confirm ablation by flow cytometry loss of NOS2+/CD86+ cells with retention of CD206+/ARG1+ M2 cells
- Expected timeline: 6-9 months
- This is the most direct path to M1-selective ablation but requires de novo mouse generation

### 1E. Existing Ablation Tools (Non-Selective, for Baseline Comparisons)

| Tool | Mouse Strain | Target | Limitation |
|------|-------------|--------|------------|
| CD11b-DTR | Tg(ITGAM-DTR/EGFP)34Lan | CD11b+ myeloid cells | Depletes monocytes, neutrophils, NK cells, not M1/M2 selective |
| CD11c-DTR | Tg(Itgax-DTR/EGFP)57Lan | CD11c+ dendritic cells | Also depletes some macrophage subsets; dendritic cell confound |
| CSF1R antibody | Anti-CSF1R (clone AFS98, Bio X Cell, cat# BE0213) | CSF1R+ macrophages | Depletes all tissue macrophages; blocks monocyte differentiation |

---

## SECTION 2: GENETIC TOOLS FOR M2-SELECTIVE MANIPULATION

### 2A. The CD206/MRC1 Challenge

CD206 (Mannose Receptor C-type 1, encoded by MRC1) is the most commonly used M2 surface marker. A CD206-CreERT2 mouse would be enormously valuable but **does not exist** as a commercial strain. JAX has no listing for any MRC1-driven Cre line.

### 2B. Strategy: Generate MRC1-CreERT2 Knock-In Mice

- Insert CreERT2 cassette into the MRC1 locus via CRISPR-Cas9-mediated homology-directed repair in C57BL/6J zygotes
- Place CreERT2 after the endogenous MRC1 stop codon using a T2A self-cleaving peptide (MRC1-T2A-CreERT2) to preserve endogenous CD206 expression
- Breeding strategy: Cross to Rosa26-LSL-tdTomato (JAX #007914) for fate mapping, or Rosa26-LSL-DTR (JAX #007900) for conditional ablation
- Validation: Treat with tamoxifen (75 mg/kg intraperitoneally for 5 consecutive days), then stimulate mice with Interleukin-4 (IL-4) complex (IL-4/anti-IL-4 antibody clone 11B11, described below) to induce M2 polarization. Confirm tdTomato labeling in CD206+ M2 macrophages and absence in NOS2+ M1 macrophages
- Expected timeline: 8-12 months

### 2C. Strategy: ARG1-Driven Reporter and Ablation

Arginase 1 (ARG1) is a robust M2 marker highly expressed in alternatively activated macrophages.

- **ARG1-eGFP reporter mice** (JAX #028613, B6.129-Arg1tm1.1Mnw/J): Express eGFP under the ARG1 promoter, allowing M2 macrophage identification by flow cytometry
- Limitation: This is a reporter, not an effector line -- it identifies M2 macrophages but cannot ablate or genetically modify them
- However, it can be used for Fluorescence-Activated Cell Sorting (FACS) isolation of M2 macrophages for downstream transcriptomic analysis
- **Note:** JAX strain page access was restricted during my search, so current availability should be verified directly with JAX

### 2D. Strategy: Resistin-Like Alpha (RETNLA/Fizz1)-Driven Tools

RETNLA (Found in Inflammatory Zone 1, Fizz1) is highly M2-specific and has limited expression outside macrophages (also expressed in some epithelial contexts). No Retnla-Cre mouse exists, but the Retnla promoter could be used to drive DTR for M2-selective ablation, similar to the NOS2-DTR approach described above.

### 2E. Near-Term Strategy: Pharmacological M2 Depletion Combined with Pan-Macrophage Tools

Until M2-specific genetic tools can be generated, the best available approach combines:

1. **CSF1R blockade** preferentially depletes M2 macrophages because M2 macrophages are more dependent on CSF1R signaling for survival than M1 macrophages (Wang et al., Leukemia 2017, PMCID: PMC5927777):
   - Anti-CSF1R antibody (clone AFS98, Bio X Cell, cat# BE0213): 1 mg/mouse intraperitoneally, twice weekly
   - Small molecule: PLX3397 (Pexidartinib, Selleckchem, cat# S7818): 290 ppm in chow (formulated by Research Diets)
   - PLX5622 (Formulated chow, Research Diets, cat# D11100402i): 1200 ppm in chow, more brain-penetrant if CNS dormancy niches are relevant

2. **Combined with M1 skewing** (Section 3) to functionally enrich for M1 even as M2 are depleted

---

## SECTION 3: PHARMACOLOGICAL APPROACHES

### 3A. M1-Polarizing Agents for In Vivo Use

| Agent | Mechanism | Dose/Route | Supplier/Catalog | Notes |
|-------|-----------|------------|-------------------|-------|
| **IFN-gamma** | Binds IFNGR, activates JAK1/JAK2-STAT1 pathway | 5000-25000 U/mouse intraperitoneally daily, or 0.5-2.0 ug/mouse | PeproTech, cat# 315-05 (recombinant murine) | Short half-life (~3 hr); requires daily dosing for sustained M1 skewing |
| **Polyinosinic:Polycytidylic Acid (Poly I:C)** | TLR3 agonist, mimics viral dsRNA | 50-200 ug/mouse intraperitoneally, every 2-3 days | InvivoGen, cat# tlrl-pic | Induces Type I IFN and M1 polarization; can cause systemic inflammation |
| **CpG-ODN 1826** | TLR9 agonist, potent M1 inducer | 50 ug/mouse intravenously or intratumorally, weekly | InvivoGen, cat# tlrl-1826 | Mouse-specific TLR9 agonist; well-tolerated at this dose |
| **STING agonist (cGAMP or ADU-S100/MIW815)** | Activates Stimulator of Interferon Genes (STING), robust Type I IFN response | 25-50 ug/mouse intratumorally, weekly | InvivoGen (cGAMP, cat# tlrl-nacga23) or MedChemExpress (ADU-S100, cat# HY-100854) | ADU-S100 is in clinical trials (NCT03010176); potent M1 polarizer in Tumor-Associated Macrophages (TAMs) |
| **Lipopolysaccharide (LPS, ultra-low dose)** | TLR4 agonist | 0.1-1.0 mg/kg intraperitoneally, single dose or every 72 hr | Sigma-Aldrich, cat# L2630 (E. coli O111:B4) | Risk of endotoxic shock at higher doses; use ultra-low dose for chronic M1 skewing |

### 3B. M2-Polarizing Agents for In Vivo Use

| Agent | Mechanism | Dose/Route | Supplier/Catalog | Notes |
|-------|-----------|------------|-------------------|-------|
| **IL-4 complex** | IL-4 bound to anti-IL-4 antibody (clone 11B11) extends half-life from ~2 hr to ~48 hr | 5 ug IL-4 + 25 ug anti-IL-4 antibody per mouse intraperitoneally, every 3-4 days | Bio X Cell (anti-IL-4, clone 11B11, cat# BE0049) + PeproTech (rmIL-4, cat# 214-14) | The gold standard for sustained M2 skewing in vivo; anti-IL-4 antibody acts as a carrier, not a neutralizer, in this context |
| **IL-13** | Binds IL-13Ralpha1/IL-4Ralpha heterodimer, activates STAT6 | 2 ug/mouse intraperitoneally daily | PeproTech, cat# 210-13 (recombinant murine) | Very short half-life; IL-4 complex is preferred |
| **Recombinant IL-10** | Anti-inflammatory cytokine, promotes M2 phenotype | 2.5 ug/mouse intraperitoneally daily | PeproTech, cat# 217-10 | Also immunosuppressive for T cells; confound for dormancy studies |
| **Glucocorticoid (Dexamethasone)** | Glucocorticoid receptor agonist, potent M2 polarizer | 1-5 mg/kg intraperitoneally daily | Sigma-Aldrich, cat# D4902 | Broad immunosuppressive effects; not recommended for dormancy studies due to confounds |

### 3C. Liver-Targeted Nanoparticle Delivery (Critical for Colon Cancer Liver Metastasis Dormancy)

Since your dormancy model involves the liver metastatic niche, systemic cytokine delivery will have off-target effects. Targeted nanoparticle approaches are recommended:

**Liposome-encapsulated clodronate (M2-depletion control, non-selective):**
- Clodronate Liposomes (Liposoma BV, cat# CP-005-005): 200 ul/mouse intravenously, depletes Kupffer cells (liver-resident macrophages) within 24-48 hr
- Non-selective but establishes baseline for liver macrophage contribution to dormancy

**Ionizable Lipid Nanoparticles (LNPs) for liver-tropic mRNA delivery:**
- Modern liver-tropic LNPs (using ionizable lipids such as DLin-MC3-DMA or SM-102) preferentially transfect hepatocytes and liver-resident macrophages when delivered intravenously
- Encapsulate mRNA encoding M1-polarizing cytokines (IFN-gamma mRNA, IL-12 mRNA) or M2-polarizing cytokines (IL-4 mRNA)
- Formulation: Can be synthesized in-house or obtained from commercial partners (Acuitas Therapeutics, Precision NanoSystems)
- Dose: 0.5-2.0 mg/kg mRNA encapsulated in LNPs, intravenously, every 7-14 days
- This approach achieves liver-selective M1 or M2 skewing with minimal systemic exposure

**Mannose-conjugated nanoparticles for M2-selective targeting:**
- CD206 (Mannose Receptor) is highly expressed on M2 macrophages
- Mannose-coated liposomes or polymeric nanoparticles selectively bind and internalize into CD206+ M2 cells
- Can deliver: (a) clodronate for M2-selective depletion, (b) siRNA against ARG1 or MRC1 for M2 gene silencing, or (c) polarizing cargo for M2-to-M1 repolarization
- Reference for concept: Mannosylated liposomes targeting CD206+ TAMs have been described in multiple preclinical studies

---

## SECTION 4: TEMPORAL CONTROL STRATEGIES

Temporal control is critical for your dormancy model because macrophage polarization states are dynamic and may have different roles during dormancy entry (Phase 1), maintenance (Phase 2), and exit (Phase 3).

### 4A. Tamoxifen-Inducible CreERT2 Systems

| Line | Target | Tamoxifen Dose | Onset of Recombination | Duration of Labeling |
|------|--------|---------------|------------------------|---------------------|
| Cx3cr1-CreERT2 | Pan-macrophage (monocytes, tissue-resident macrophages, microglia) | 75 mg/kg intraperitoneally x 5 days (in corn oil) | 24-48 hr after first dose | Permanent (genetic recombination is irreversible) |
| Lyz2-CreERT2 (LysM-CreERT2) | Myeloid cells (macrophages, neutrophils) | 75 mg/kg intraperitoneally x 5 days | 24-48 hr | Permanent |
| Csf1r-CreERT2 | Mononuclear phagocyte system | 75 mg/kg intraperitoneally x 5 days | 48-72 hr | Permanent |

**Critical consideration for dormancy studies:** CreERT2-mediated recombination is permanent -- once triggered, the genetic change persists for the life of that cell. This means:
- For Phase 1 (dormancy entry): Give tamoxifen before or at the time of tumor cell injection
- For Phase 2 (dormancy maintenance): Give tamoxifen after dormancy is established (typically 4-8 weeks post-injection, depending on model)
- For Phase 3 (dormancy exit): Give tamoxifen at the time of exit stimulus

**4-Hydroxytamoxifen (4-OHT) vs Tamoxifen:**
- 4-OHT (Sigma-Aldrich, cat# H7904): Active metabolite, faster onset (6-12 hr), can be used for precise temporal control
- Tamoxifen (Sigma-Aldrich, cat# T5648): Requires hepatic metabolism to 4-OHT, slower onset (24-48 hr), but more stable and widely used
- For dormancy studies: 4-OHT is preferred for Phase 3 (exit) experiments where you need precise timing

### 4B. Doxycycline-Inducible Tet-ON/OFF Systems

For reversible temporal control:
- **Tet-ON:** Express a gene of interest (e.g., DTR, or a dominant-negative STAT6 for M2 blockade) only during doxycycline administration
- **Tet-OFF:** Express a gene constitutively, silence with doxycycline
- Construct: Cross Cx3cr1-CreERT2 x Rosa26-LSL-rtTA x TRE-DTR mice
  - Tamoxifen activates rtTA in macrophages (permanent)
  - Doxycycline (2 mg/mL in drinking water with 5% sucrose, or via doxycycline chow at 200 ppm) activates DTR expression only during doxycycline administration
  - Remove doxycycline = DTR turns off = macrophages are no longer sensitive to DT
  - This allows temporal windows of depletion within the dormancy timeline

### 4C. Diphtheria Toxin Timing

DT-mediated ablation is rapid (cells die within 12-24 hr) but transient (depleted cells are replaced by monocyte infiltration within 5-7 days):
- For sustained depletion: Repeated DT injections every 48-72 hr (25 ng/g intraperitoneally)
- For pulse depletion (single timepoint): Single DT injection, then allow repopulation
- Monitor depletion by flow cytometry of liver tissue: CD45+ F4/80+ CD11b+ population

### 4D. Pharmacological Temporal Control

Pharmacological approaches inherently provide temporal control because they are reversible:

| Agent | Onset | Duration of Effect | Washout |
|-------|-------|-------------------|---------|
| IFN-gamma (recombinant protein) | 4-8 hr | 12-24 hr (single dose) | 24-48 hr after last dose |
| IL-4 complex | 4-12 hr | 48-72 hr (single dose) | 72-96 hr after last dose |
| PLX3397 (CSF1R inhibitor in chow) | 3-5 days | Continuous while on chow | 7-14 days after chow switch |
| CpG-ODN 1826 | 6-12 hr | 5-7 days | 7-10 days after last dose |
| STING agonist (cGAMP) | 6-12 hr | 7-14 days | 14-21 days after last dose |

---

## SECTION 5: MACROPHAGE ADOPTIVE TRANSFER EXPERIMENTS

Adoptive transfer of ex vivo polarized macrophages is the most immediately actionable approach for achieving true M1 vs M2 selectivity, since polarization is controlled in vitro before transfer.

### 5A. Bone Marrow-Derived Macrophage (BMDM) Generation

**Protocol:**
1. Harvest bone marrow from C57BL/6J donor mice (6-12 weeks old, both sexes matched to recipient):
   - Euthanize donor, dissect femurs and tibias
   - Flush marrow with cold Phosphate-Buffered Saline (PBS) using a 25-gauge needle
   - Pass through 70 um cell strainer
   - Lyse red blood cells with ACK lysis buffer (2 min, room temperature)
   - Count cells

2. Differentiate into macrophages:
   - Plate 5 x 10^6 cells per 10 cm non-tissue-culture-treated dish
   - Culture in complete DMEM (Dulbecco's Modified Eagle Medium) supplemented with:
     - 10% Fetal Bovine Serum (FBS), heat-inactivated
     - 1% Penicillin-Streptomycin
     - 20 ng/mL recombinant murine Macrophage Colony Stimulating Factor (M-CSF, PeproTech, cat# 315-02)
   - Incubate at 37 degrees C, 5% CO2 for 7 days
   - Refresh media with M-CSF on day 3 and day 5
   - Expected yield: 5-10 x 10^6 BMDMs per mouse

### 5B. Ex Vivo Polarization

| Polarization | Cytokine Cocktail | Duration | Markers to Confirm |
|-------------|-------------------|----------|-------------------|
| **M1** | 20 ng/mL IFN-gamma (PeproTech #315-05) + 100 ng/mL LPS (Sigma #L2630) | 24 hr (LPS added for final 4-6 hr only) | NOS2+, CD86+, MHC-II-hi, CD206-lo |
| **M2** | 20 ng/mL IL-4 (PeproTech #214-14) + 20 ng/mL IL-13 (PeproTech #210-13) | 24-48 hr | CD206+, ARG1+, RETNLA+, CD163+, NOS2- |

**Quality control before transfer:**
- Flow cytometry panel: CD45-FITC, F4/80-PE, CD11b-PerCP-Cy5.5, CD86-APC, CD206-PE-Cy7, MHC-II-BV421
- Confirm >85% polarization purity
- Confirm viability >90% by propidium iodide or Annexin V exclusion

### 5C. Adoptive Transfer Protocol

**Liver-directed transfer (intravenous or intrahepatic):**
1. Harvest polarized BMDMs by gentle scraping (do NOT use trypsin -- it cleaves surface markers)
2. Wash 3x in sterile PBS
3. Resuspend at 5 x 10^6 cells/mL in sterile PBS
4. Inject 1-2 x 10^6 cells per mouse via tail vein (200 ul) -- cells will home to liver via the reticuloendothelial system
5. Alternatively, inject 0.5 x 10^6 cells directly into the hepatic portal circulation (more invasive but more efficient liver engraftment)

**Labeled macrophage tracking:**
- Use BMDMs from CD45.1 (B6.SJL-Ptprca Pepcb/BoyJ, JAX #002014) donors transferred into CD45.2 (standard C57BL/6J) recipients to distinguish donor vs host macrophages by flow cytometry
- Alternatively, pre-label BMDMs with CellTracker CM-DiI (Thermo Fisher, cat# C7000): 5 uM, 15 min at 37 degrees C, for short-term tracking (7-14 days)
- For long-term tracking, use Actb-GFP mice (C57BL/6-Tg(CAG-EGFP)1Osb/J, JAX #003291) as donors

**Engraftment and persistence:**
- Intravenously transferred BMDMs peak in liver at 24-48 hr
- Persistence: ~7-14 days before being cleared
- For sustained effect: Repeat transfers every 5-7 days
- Monitor engraftment by flow cytometry of liver single-cell suspensions at sacrifice

### 5D. Experimental Design for Dormancy Studies

**Experiment 1: M1 macrophages and dormancy entry**
- Day -1: Inject 1 x 10^6 M1-polarized BMDMs intravenously (or PBS control)
- Day 0: Inject luciferase-expressing colon cancer cells (e.g., DLD-Luc or HT29-Luc) intrasplenically for liver metastatic seeding
- Day +3, +7, +14: Repeat M1 BMDM transfer
- Monitor: Bioluminescence imaging (BLI) weekly; dormancy = low/stable BLI signal
- Endpoint: Assess dormancy markers at day 28 (NR2F1+, Ki67-, p-p38hi in disseminated tumor cells)

**Experiment 2: M2 macrophages and dormancy exit**
- Day 0: Inject luciferase-expressing colon cancer cells intrasplenically
- Wait until dormancy is established (typically 4-8 weeks, confirmed by stable BLI)
- Transfer 1 x 10^6 M2-polarized BMDMs intravenously (or PBS or M1 BMDM controls)
- Monitor: BLI twice weekly for exit signal (increasing BLI = dormancy exit/proliferation)
- Endpoint: Ki67+ tumor cells, metastatic outgrowth

---

## SECTION 6: CRISPR SCREENING APPROACH

### 6A. Rationale

A genome-wide or focused CRISPR screen in macrophages can identify novel genes required for M1 or M2 polarization that could serve as new selective targets. Two recent landmark papers provide the methodological foundation:

1. **de la Rosa et al., Nature Neuroscience 2026 (PMID: 41345278):** Developed an in vivo CRISPR screening pipeline using genetically editable progenitor cells. They screened 100+ cytokine receptors and signaling molecules and identified IFN-gamma, TNF, GM-CSF (Granulocyte-Macrophage Colony Stimulating Factor), and TGF-beta (Transforming Growth Factor beta) as essential regulators of macrophage polarization in vivo. Used Perturb-seq (single-cell RNA sequencing combined with CRISPR perturbation) for readout.

2. **Sheban et al., Cancer Cell 2025 (PMID: 40215981):** Identified ZEB2 (Zinc Finger E-Box Binding Homeobox 2) as a master transcriptional switch controlling the TAM program. Used integrated human tumor scRNA-seq (single-cell RNA sequencing) with a dedicated CRISPR screen and a deep generative model for gene perturbation network analysis. Demonstrated that ZEB2 ablation reprograms TAMs and that selective Zeb2 targeting in vivo achieves tumor clearance.

### 6B. Proposed Screen Design

**Focus area:** Genes controlling M1 vs M2 polarization in the liver metastatic microenvironment

**Library:** Focused library of 500-1000 genes:
- All known transcription factors involved in macrophage polarization (IRF4, IRF5, IRF7, STAT1, STAT3, STAT6, KLF4, PPARG, C/EBPb, NF-kB subunits, ZEB2)
- Cell surface receptors for cytokines/chemokines (IFNGR1, IFNGR2, IL4RA, IL13RA1, CSF1R, CSF2R, CSF3R, CCR2, CX3CR1, TLR2, TLR4, TLR9)
- Epigenetic regulators (DNMT3A, TET2, KDM6A/JMJD3, HDACs, BRD4)
- Metabolic regulators (ARG1, NOS2, IDO1, SLC2A1/GLUT1, SLC7A5)
- Negative controls: 100 non-targeting sgRNAs
- Positive controls: sgRNAs targeting Stat1 (should block M1), sgRNAs targeting Stat6 (should block M2)

**sgRNA design:**
- 4-6 sgRNAs per gene
- Use CRISPRko (CRISPR knockout) library from the Broad Institute (Brunello library subset) or design custom sgRNAs using CRISPick (Broad Institute web tool)
- Clone into lentiviral vector with U6 promoter driving sgRNA and EF1a promoter driving a fluorescent marker (eGFP or mCherry) for tracking

**Delivery method -- Two options:**

**Option A: Ex vivo CRISPR in BMDMs followed by adoptive transfer**
1. Generate Cas9-expressing bone marrow from Rosa26-LSL-Cas9 (JAX #024857, B6;129-Gt(ROSA)26Sortm1(CAG-cas9*,-EGFP)Fezh/J) x Cx3cr1-CreERT2 mice, or use H11-CAG-LSL-Cas9 knock-in mice (JAX #026818) for more robust Cas9 expression
2. Transduce bone marrow progenitors with sgRNA library at MOI ~0.3 (to ensure single sgRNA per cell) in the presence of 8 ug/mL Polybrene (Sigma, cat# H9268) and M-CSF (20 ng/mL)
3. Differentiate into BMDMs over 7 days with M-CSF
4. Polarize with IFN-gamma/LPS (M1) or IL-4/IL-13 (M2) for 24 hr
5. Sort by FACS: M1 markers (CD86+, MHC-II-hi) vs M2 markers (CD206+, ARG1+) vs unpolarized (double-negative)
6. Extract genomic DNA from each population
7. Amplify sgRNA sequences by PCR and perform next-generation sequencing (NGS)
8. Compare sgRNA enrichment/depletion between M1, M2, and unpolarized populations using MAGeCK (Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout) analysis

**Option B: In vivo Perturb-seq (following de la Rosa et al. methodology)**
1. Transduce Cas9+ bone marrow progenitors with the sgRNA library (combined with cell hashing barcodes for sample multiplexing)
2. Transfer transduced progenitors into irradiated recipient mice (lethal irradiation at 9.5 Gy, followed by bone marrow transplant)
3. Allow 8-12 weeks for reconstitution of tissue macrophages from CRISPR-edited progenitors
4. Establish liver dormancy model (intrasplenic injection of colon cancer cells)
5. At desired timepoints (dormancy entry, maintenance, exit), harvest liver macrophages
6. Perform Perturb-seq: Single-cell RNA-seq (10x Genomics Chromium) with simultaneous sgRNA detection
7. Analyze using standard Perturb-seq pipeline (Seurat + custom sgRNA assignment)
8. This approach reveals not just which genes are required for M1/M2 polarization, but also the transcriptional consequences of each perturbation at single-cell resolution

### 6C. Key Readouts for Dormancy Context

For both options, integrate CRISPR screen results with dormancy endpoints:
- **Primary screen readout:** M1 vs M2 marker expression by flow cytometry or Perturb-seq
- **Secondary validation:** Top hits tested individually for effects on DTC dormancy maintenance in vivo
- **Tertiary readout:** Dormancy marker assessment in DTCs (NR2F1+, Ki67-, p-p38hi = dormant; NR2F1-, Ki67+, p-ERKhi = escaped)

---

## SECTION 7: PROPOSED EXPERIMENTAL TIMELINE (WEEK-BY-WEEK)

### Phase 0: Setup and Validation (Weeks 1-4)

| Week | Activity | Details |
|------|----------|---------|
| 1 | Order mouse strains | Cx3cr1-CreERT2, Rosa26-LSL-DTR (JAX #007900), Rosa26-LSL-tdTomato (JAX #007914), C57BL/6J, CD45.1 (JAX #002014), Rosa26-LSL-Cas9 (JAX #024857) |
| 1 | Order reagents | IFN-gamma (PeproTech #315-05), IL-4 (PeproTech #214-14), anti-IL-4 clone 11B11 (Bio X Cell #BE0049), CpG-ODN 1826 (InvivoGen #tlrl-1826), tamoxifen (Sigma #T5648), DT (Sigma #D0564), PLX3397 (Selleckchem #S7818) |
| 1-2 | Breeding setup | Set up Cx3cr1-CreERT2 x Rosa26-LSL-DTR crosses; Cx3cr1-CreERT2 x Rosa26-LSL-tdTomato crosses |
| 2-4 | BMDM optimization | Generate BMDMs from C57BL/6J mice; optimize M1 polarization (IFN-gamma 20 ng/mL + LPS 100 ng/mL for 24 hr); optimize M2 polarization (IL-4 20 ng/mL + IL-13 20 ng/mL for 48 hr); validate by flow cytometry (CD86, CD206, MHC-II) and qPCR (Nos2, Arg1, Retnla) |
| 3-4 | Colon cancer cell line preparation | Generate luciferase-expressing DLD-1 or HT29 cells (lentiviral transduction with pLenti-EF1a-Luc2-P2A-GFP); confirm luciferase activity by BLI; confirm dormancy capacity (serum starvation or TGF-beta treatment to induce NR2F1+, Ki67- state) |

### Phase 1: Pharmacological Pilot Experiments (Weeks 5-12)

| Week | Activity | Details |
|------|----------|---------|
| 5 | Pilot: M1 skewing in vivo | Treat C57BL/6J mice with IFN-gamma (5000 U intraperitoneally daily x 5 days) or CpG-ODN 1826 (50 ug intravenously weekly); sacrifice and analyze liver macrophages by flow cytometry for M1 markers |
| 5 | Pilot: M2 skewing in vivo | Treat C57BL/6J mice with IL-4 complex (5 ug IL-4 + 25 ug anti-IL-4 antibody intraperitoneally, every 3 days x 3 doses); sacrifice and analyze liver macrophages by flow cytometry for M2 markers |
| 6-7 | Pilot: CSF1R inhibitor for M2 depletion | Feed PLX3397 chow (290 ppm) to C57BL/6J mice for 14 days; sacrifice and analyze liver macrophage depletion and residual polarization by flow cytometry |
| 7-8 | Pilot: Adoptive transfer engraftment | Transfer 1 x 10^6 CM-DiI-labeled M1 or M2 BMDMs intravenously into C57BL/6J mice; sacrifice at days 1, 3, 7, 14; quantify liver engraftment by flow cytometry (CM-DiI+ CD45+ F4/80+ cells) |
| 8-12 | Dormancy model establishment | Intrasplenic injection of 1 x 10^5 DLD-Luc cells in C57BL/6J (immunocompromised NSG mice needed for human cell lines; alternatively, use murine MC38-Luc cells in immunocompetent C57BL/6J); weekly BLI to monitor dormancy; sacrifice cohorts at weeks 2, 4, 6, 8 to characterize dormancy kinetics and macrophage infiltration (immunohistochemistry for F4/80, CD206, NOS2) |

### Phase 2: M1/M2 Functional Experiments (Weeks 13-28)

| Week | Activity | Details |
|------|----------|---------|
| 13-16 | Experiment: M1 macrophages in dormancy entry | Groups: (1) M1 BMDM transfer at day -1 and days +3, +7; (2) PBS control; (3) Unpolarized BMDM control. Monitor BLI weekly. Endpoint at week 4: Dormancy markers (NR2F1, Ki67, p-p38) in DTCs by IHC/IF |
| 13-16 | Experiment: M2 macrophages in dormancy entry | Groups: (1) M2 BMDM transfer at day -1 and days +3, +7; (2) PBS control. Same endpoints |
| 17-20 | Experiment: M1 macrophages in dormancy exit | Wait for dormancy establishment (8 weeks). Groups: (1) M1 BMDM transfer; (2) M2 BMDM transfer; (3) PBS; (4) CpG-ODN 1826 (50 ug intravenously weekly). Monitor BLI twice weekly for exit signal |
| 21-24 | Experiment: M2 depletion during dormancy maintenance | PLX3397 chow (290 ppm) or anti-CSF1R (AFS98, 1 mg intraperitoneally twice weekly) during dormancy maintenance phase (weeks 4-8). Monitor BLI weekly for spontaneous exit |
| 25-28 | Experiment: M2-to-M1 repolarization | Combined M2 depletion (PLX3397) + M1 skewing (CpG-ODN 1826) during dormancy maintenance. Assess whether forced M1 environment prevents dormancy exit or prolongs dormancy |

### Phase 3: Genetic Tool Development (Weeks 13-52, parallel with Phase 2)

| Week | Activity | Details |
|------|----------|---------|
| 13-16 | Design NOS2-DTR and MRC1-CreERT2 targeting constructs | Obtain NOS2 promoter region (-2.5 kb); clone DTR-IRES-eGFP; obtain MRC1 targeting strategy with T2A-CreERT2; order sgRNAs for CRISPR knock-in from IDT (Integrated DNA Technologies) |
| 16-24 | Microinjection and founder screening | Send constructs to transgenic core (e.g., University of Michigan Transgenic Core, or Jackson Laboratories Custom Service); expect 3-6 months for founder identification |
| 28-36 | Founder characterization | Cross founders to C57BL/6J; genotype pups; test DTR or CreERT2 expression in polarized BMDMs by flow cytometry (eGFP for NOS2-DTR; tdTomato from Rosa26-LSL-tdTomato cross for MRC1-CreERT2) |
| 36-44 | Selective ablation validation | NOS2-DTR: Polarize to M1 with IFN-gamma/LPS, treat with DT, confirm selective M1 ablation. MRC1-CreERT2 x Rosa26-LSL-DTR: Tamoxifen + DT, confirm selective M2 ablation |
| 44-52 | Apply validated genetic tools to dormancy model | Repeat key experiments from Phase 2 using genetic tools instead of pharmacological approaches; this provides gold-standard M1/M2-selective data |

### Phase 4: CRISPR Screen (Weeks 29-60, parallel with Phase 3)

| Week | Activity | Details |
|------|----------|---------|
| 29-32 | Library design and cloning | Design focused 500-1000 gene library; order oligo pool from Twist Bioscience or Agilent; clone into lentiviral sgRNA vector (lentiGuide-Puro, Addgene #52963) |
| 33-36 | Library validation and titering | Produce lentiviral library in HEK293T cells (psPAX2 + pMD2.G packaging); titer on Cas9+ BMDMs; confirm library representation by NGS |
| 37-40 | Pilot screen (ex vivo, Option A) | Transduce Cas9+ bone marrow progenitors at MOI 0.3; differentiate to BMDMs; polarize M1 or M2; FACS sort; NGS of sgRNA representation; MAGeCK analysis |
| 41-52 | Full screen with Perturb-seq (Option B) | Transduce Cas9+ progenitors; bone marrow transplant into irradiated recipients; 8-12 week reconstitution; establish dormancy model; harvest liver macrophages at dormancy entry/maintenance/exit timepoints; Perturb-seq |
| 53-56 | Hit validation | Test top 10-20 hits individually using single sgRNAs in BMDMs; validate M1/M2 polarization effects by flow cytometry and transcriptomics |
| 57-60 | Top hit in vivo validation | Generate individual knockout BMDMs for top 3-5 hits; adoptive transfer into dormancy model; assess effects on dormancy entry, maintenance, and exit |

---

## APPENDIX: KEY REAGENT SUMMARY TABLE

| Reagent | Supplier | Catalog # | Use |
|---------|----------|-----------|-----|
| Recombinant murine IFN-gamma | PeproTech | 315-05 | M1 polarization |
| Recombinant murine IL-4 | PeproTech | 214-14 | M2 polarization |
| Recombinant murine IL-13 | PeproTech | 210-13 | M2 polarization |
| Recombinant murine M-CSF | PeproTech | 315-02 | BMDM differentiation |
| Anti-IL-4 antibody (clone 11B11) | Bio X Cell | BE0049 | IL-4 complex (M2 skewing) |
| Anti-CSF1R antibody (clone AFS98) | Bio X Cell | BE0213 | Macrophage depletion |
| CpG-ODN 1826 | InvivoGen | tlrl-1826 | TLR9 agonist, M1 polarization |
| cGAMP (2'3'-cGAMP) | InvivoGen | tlrl-nacga23 | STING agonist, M1 polarization |
| PLX3397 (Pexidartinib) | Selleckchem | S7818 | CSF1R inhibitor, M2 depletion |
| PLX5622 | Research Diets | D11100402i | CSF1R inhibitor chow |
| Tamoxifen | Sigma-Aldrich | T5648 | CreERT2 activation |
| 4-Hydroxytamoxifen | Sigma-Aldrich | H7904 | CreERT2 activation (fast onset) |
| Diphtheria Toxin | Sigma-Aldrich | D0564 | DTR-mediated cell ablation |
| Clodronate Liposomes | Liposoma BV | CP-005-005 | Non-selective macrophage depletion |
| LPS (E. coli O111:B4) | Sigma-Aldrich | L2630 | M1 polarization (in vitro) |
| CellTracker CM-DiI | Thermo Fisher | C7000 | Cell labeling for tracking |
| Polybrene | Sigma-Aldrich | H9268 | Lentiviral transduction |
| Cx3cr1-CreERT2 mice | (Jung lab / source to verify) | -- | Pan-macrophage Cre driver |
| Rosa26-LSL-DTR mice | JAX | 007900 | Conditional DTR expression |
| Rosa26-LSL-tdTomato mice | JAX | 007914 | Fate mapping reporter |
| Rosa26-LSL-Cas9 mice | JAX | 024857 | CRISPR Cas9 source |
| CD45.1 mice (B6.SJL) | JAX | 002014 | Adoptive transfer tracking |
| C57BL/6J | JAX | 000664 | Wild-type background |

---

## CRITICAL CAVEATS AND LIMITATIONS

1. **M1/M2 dichotomy is an oversimplification.** In vivo macrophages exist on a polarization continuum, not as discrete M1/M2 populations. Single-cell RNA-seq studies have identified multiple TAM subsets that do not neatly map to the binary M1/M2 framework. Your experimental interpretation should account for this.

2. **Macrophage plasticity confounds long-term experiments.** M1-polarized macrophages can be repolarized to M2-like states in vivo by tissue microenvironment signals, and vice versa. Adoptive transfer experiments should account for the possibility that transferred M1 BMDMs may adopt M2-like features within the liver niche over time.

3. **Kupffer cells vs monocyte-derived macrophages.** The liver contains both tissue-resident Kupffer cells (embryonic origin, self-renewing) and monocyte-derived macrophages (bone marrow origin, recruited during injury/inflammation). These populations have different polarization capacities and may have different effects on DTC dormancy. Cx3cr1-CreERT2 labels monocyte-derived macrophages but only labels Kupffer cells variably. Consider this distinction in your experimental design.

4. **Colon cancer cell line selection matters.** Human cell lines (DLD-1, HT29, HCT116) require immunocompromised hosts (NSG, NOD-scid IL2Rgammanull), which eliminates the adaptive immune compartment. Murine cell lines (MC38, CT26) allow use of immunocompetent hosts but may have different dormancy kinetics. This choice fundamentally affects the macrophage-tumor interaction landscape.

5. **ZEB2 as a potential target.** The Sheban et al. (2025) finding that ZEB2 controls the TAM program suggests that ZEB2 inhibition could be an alternative to M1/M2-selective manipulation -- rather than selectively depleting one subset, you could reprogram existing TAMs. Consider incorporating a ZEB2-targeting arm into your studies.

---

This briefing confirms that the field lacks truly M1/M2-selective genetic tools, validating your identification of this gap as a critical bottleneck. The recommended path forward combines three parallel strategies: (1) immediate pharmacological and adoptive transfer experiments using existing tools, (2) medium-term generation of NOS2-DTR and MRC1-CreERT2 mice for gold-standard selective manipulation, and (3) longer-term CRISPR screening to discover new selective targets. All three approaches can yield actionable data within the proposed timeline.