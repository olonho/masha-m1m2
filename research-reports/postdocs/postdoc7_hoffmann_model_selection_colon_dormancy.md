# IN VIVO AND IN VITRO MODEL SELECTION AND OPTIMIZATION

## Experimental Design Briefing for Validating the Quantitative Contribution of M1-like and M2-like Macrophage Phenotypes to Dormancy Entry, Maintenance, and Exit in Colon Cancer

**Prepared for:** Dr. Lena Hoffmann, PhD
**Date:** 26 May 2026

---

## SECTION 1: Colon Cancer Cell Lines with Dormancy Capacity

### 1.1 Literature Landscape and Critical Gap

Unlike breast cancer -- where dormancy models are well established for D2A1, MCF-7, and 4T1-derived lines (Malladi et al., 2016, Cell) -- colon cancer has remarkably few published dormancy-competent cell line systems. A PubMed search for "colon cancer dormancy disseminated tumor cells" returned essentially no direct hits, confirming this gap. The closest relevant model is the Ohsawa et al. (2006, Transplantation) rat colon cancer dormancy model using luciferase-labeled cells, where cyclosporin A (CsA) released cells from dormancy. More recently, Heinz et al. (2022, Cancer Res, PMID: 35570706) demonstrated that colorectal cancer micrometastases in the liver can remain dormant for years, using patient-derived organoids (PDOs) and intravital microscopy in mice. Their work established that YAP (Yes-Associated Protein) signaling dynamics govern the dormancy-to-colonization transition: persistent YAP activity locks micrometastatic lesions in a growth-stalled, cellularly homogeneous state, while attenuation of YAP permits emergence of cancer stem cell (CSC) heterogeneity and outgrowth.

### 1.2 Recommended Murine Cell Lines

**MC38 (C57BL/6 background)**
- Primary recommendation due to extensive use in immunocompetent syngeneic models and compatibility with C57BL/6-based transgenic macrophage tools (LysM-Cre, CD169-DTR).
- VanderVeen et al. (2025) demonstrated MC38 liver metastasis with Kupffer cell phenotyping. Qiao et al. (2023, Cell Death Dis) characterized F4/80+ TAM differentiation in MC38 CRLM models.
- Dormancy induction: Use low-dose inoculation (1x10^3 -- 5x10^3 cells) via intrasplenic injection to generate micrometastatic foci rather than macrometastatic outgrowth. Based on Heinz et al. (2022), low-burden YAP-high lesions should persist as dormant microfoci.
- Engineering requirement: Transduce MC38 with GFP/luciferase dual reporter (e.g., pLenti-PGK-GFP-2A-Luc2) for longitudinal bioluminescence imaging (BLI) and single-cell resolution by flow cytometry. Select clones with stable integration and confirm >90% GFP positivity by FACS before use.

**CT26 (BALB/c background)**
- Secondary murine line. Kruse et al. (2013, Int J Colorectal Dis, PMID: 23657400) used CT26 in orthotopic and liver metastasis models with clodronate liposome macrophage depletion in BALB/c mice.
- Guba et al. (2001, Cancer Res, PMID: 11454710) demonstrated that CT26-derived CT-26 cells form dormant solitary tumor cells in the mouse liver that can be imaged by intravital videomicroscopy (IVVM).
- Note: BALB/c background limits compatibility with LysM-Cre and CD169-DTR tools, which are predominantly on C57BL/6. Cross-breeding or separate parallel studies required.

### 1.3 Recommended Human Cell Lines

**HCT116 (MSI-high, KRAS G13D, PIK3CA H1047R)**
- Well-characterized; forms liver metastases in NSG (NOD-scid IL2Rgamma-null) mice following intrasplenic injection.
- Can be induced into quiescence by serum starvation, TGF-beta treatment (10 ng/mL for 72 h), or culture on Matrigel under low-growth-factor conditions (following protocols adapted from breast cancer dormancy literature).

**HT-29 (MSS, BRAF V600E)**
- Moderately differentiated adenocarcinoma line. Less studied in dormancy context but MSS status is clinically relevant (most CRC liver metastases are MSS).
- Use alongside HCT116 to capture MSI vs MSS biology.

**SW620 (lymph node metastasis-derived)**
- Represents late-stage, metastatically competent cells. Useful as a "dormancy exit" positive control since these cells are more aggressive.
- Less likely to enter dormancy; serves as comparator for dormancy-incompetent phenotype.

**Patient-Derived Organoids (PDOs)**
- Heinz et al. (2022) used clonal PDO outgrowth to model dormancy-to-colonization transitions in vitro. The Hubrecht Organoid Technology (HUB) biobank (van de Wetering et al., 2015, Cell) provides CRC PDOs with matched clinical annotation.
- Protocol: Culture PDOs as single cells in low-Matrigel (2%) conditions without exogenous WNT/R-spondin to induce quiescence. Monitor organoid size and Ki67 staining at days 3, 7, 14. YAP activity can be tracked using a TEAD-responsive fluorescent reporter construct.

### 1.4 Dormancy Induction Protocols (In Vitro)

| Cell Line | Dormancy Induction Method | Readout | Timeline |
|-----------|--------------------------|---------|----------|
| MC38-GFP-Luc | TGF-beta1 (5 ng/mL) + serum 0.5% FBS for 72 h | Ki67 negativity, p27/Kip1 upregulation, GFP retention, BLI signal plateau | 72 h induction, maintained for 14 d |
| HCT116 | Serum starvation (0.1% FBS, 48 h) + TGF-beta1 (10 ng/mL) | DiI membrane dye retention (vs. dilution in dividing cells), EdU incorporation negative | 48 h induction, confirmed day 3 |
| PDOs | Withdrawal of WNT3A/R-spondin/Noggin from organoid medium; culture on 2% Matrigel | Organoid size stasis, single-cell RNA-seq showing G0 gene signature, TEAD-YAP reporter | 7--14 d |
| MC38 (in vivo) | Low-dose intrasplenic injection (1x10^3 cells) | BLI signal plateau, absence of macrometastatic nodules at 8--12 weeks, qPCR for GFP+ cells in liver | 4--12 weeks |

---

## SECTION 2: In Vivo Models for Colon Cancer Dormancy

### 2.1 Intrasplenic Injection Model (Primary Recommended Model)

This is the workhorse model for Colorectal Liver Metastasis (CRLM) and can be tuned to generate dormant Disseminated Tumor Cells (DTCs) by adjusting cell number.

**Protocol:**
- **Mouse strain:** C57BL/6J (Jackson Labs, stock 000664), female, 8--10 weeks old (n=10--15 per experimental group for adequate power; see Section 6 for group sizes).
- **Cell preparation:** MC38-GFP-Luc2 cells at 70--80% confluence. Harvest with 0.05% trypsin-EDTA, wash 2x in ice-cold PBS, resuspend at 1x10^3 cells/100 uL PBS (low dose) or 1x10^5 cells/100 uL (high dose for positive control of macrometastatic outgrowth). Keep on ice; use within 30 min.
- **Surgical procedure:** Anesthetize with isoflurane (2--3% induction, 1.5% maintenance). Make 1 cm left flank incision. Expose spleen. Inject 100 uL cell suspension slowly into inferior pole of spleen using 30G insulin syringe over 30 seconds to prevent portal vein backflow. Wait 2 min. Splenectomy (to prevent primary splenic tumor) or leave spleen in situ depending on experimental question (splenectomy eliminates non-liver tumor growth confound). Close peritoneum (Vicryl 5-0) and skin (wound clips). Analgesia: buprenorphine 0.1 mg/kg SC q12h for 48 h.
- **Dormancy monitoring:** BLI weekly using IVIS Spectrum (PerkinElmer). D-luciferin 150 mg/kg IP, image 10 min post-injection, 1 min exposure, medium binning. Dormancy = stable or minimally fluctuating BLI signal for 4+ consecutive weeks without macrometastatic foci on ultrasound or necropsy.

**Critical timing parameters (based on literature and pilot recommendations):**
- **Dormancy entry:** Weeks 1--2 post-injection (DTCs arrive in liver, arrest in sinusoids, undergo initial adaptation).
- **Dormancy maintenance phase:** Weeks 3--12 (stable BLI signal, few to no visible macrometastases in low-dose group).
- **Dormancy exit:** Can be spontaneous (variable) or induced pharmacologically (see Section 3). In Heinz et al. (2022), YAP attenuation correlated with outgrowth; in Ohsawa et al. (2006), immunosuppression with CsA triggered exit.

### 2.2 Portal Vein Injection Model

- More direct delivery to liver; bypasses splenic filtration.
- **Protocol:** Inject 5x10^2 -- 5x10^3 MC38-GFP-Luc2 cells in 100 uL PBS into portal vein via mesenteric vein under surgical microscope. Technically more demanding; higher perioperative mortality (~10%).
- **Advantage:** Ensures all cells reach liver; no splenic tumor confound. Better for controlled dosing experiments.
- **Disadvantage:** Surgical complexity; small mesenteric vein in mice makes injection technically difficult.

### 2.3 Orthotopic Cecal Implantation Model

- Models the full metastatic cascade from primary tumor through dissemination to liver.
- **Protocol:** Inject 5x10^4 MC38-GFP-Luc2 cells in 50 uL PBS:Matrigel (1:1) into cecal subserosa. Allow primary tumor growth for 2--3 weeks, then resect primary tumor surgically. Monitor for liver metastases by BLI.
- **Advantage:** Recapitulates full metastatic cascade including intravasation, circulation, and extravasation. Clinically most relevant.
- **Disadvantage:** Variable metastatic efficiency (typically 30--50% of mice develop liver mets); requires two surgeries (implantation + resection). Longer timeline (12--20 weeks total).

### 2.4 Abdominal Imaging Window (AIW) for Intravital Microscopy

- Heinz et al. (2022) used AIW-based intravital microscopy to monitor real-time CRC micrometastasis formation. Ritsma et al. (2012, Nat Methods) originally described AIW implantation.
- **Protocol:** Surgical implantation of titanium AIW (12 mm diameter) over the left liver lobe. Allow 7--10 d recovery. Image MC38-GFP-Luc2 cells (expressing nuclear H2B-mCherry for single-cell tracking) by two-photon microscopy at days 1, 3, 7, 14, 21 post-intrasplenic injection.
- **Readout:** Single-cell division tracking (H2B-mCherry fluorescence dilution), cell migration velocity, interaction with F4/80-AF647 labeled macrophages (inject IV 30 min prior to imaging).

---

## SECTION 3: Macrophage Depletion and Repolarization Tools for In Vivo Use

### 3.1 Total Macrophage Depletion: Clodronate Liposomes

**Mechanism:** Clodronate (dichloromethylene diphosphonate) encapsulated in liposomes is phagocytosed by macrophages, causing intracellular accumulation and apoptosis.

**Protocol for in vivo use (based on Kruse et al., 2013, PMID: 23657400, and Bader et al., 2018, PMID: 29025731):**
- **Reagent:** Clodronate liposomes (Liposoma BV, Amsterdam; or Encapsula NanoSciences). Use formulation of 5 mg/mL clodronate in PBS liposomes.
- **Dose:** 200 uL IP, twice weekly (e.g., Monday and Thursday).
- **Timing:** Begin 3 days before tumor cell injection (to deplete resident Kupffer cells) and continue throughout experiment.
- **Control:** PBS liposomes (same volume, same schedule).
- **Expected depletion efficiency:** 80--95% depletion of F4/80+ CD11b+ cells in liver (verify by flow cytometry of liver non-parenchymal cells at experimental endpoint).
- **Limitations:** (1) Depletes ALL macrophages (M1 and M2, Kupffer cells and recruited monocyte-derived macrophages). Cannot distinguish M1 vs M2 contributions. (2) Transient depletion (48--72 h per dose). (3) Depletion of circulating monocytes may confound interpretation.

### 3.2 CSF1R Inhibition: Pexidartinib (PLX3397)

**Mechanism:** Colony Stimulating Factor 1 Receptor (CSF1R) signaling is essential for macrophage survival and differentiation, particularly for M2-like/TAM populations. CSF1R inhibitors preferentially deplete TAMs while having variable effects on tissue-resident macrophages.

**Protocol (based on Shimizu et al., 2024, Int J Mol Sci; Wang et al., 2025, Cell Rep Med):**
- **Reagent:** Pexidartinib (PLX3397; Selleckchem, MedChemExpress). Formulated in AIN-76A chow at 290 mg/kg chow (provides approximately 40--60 mg/kg/day oral dosing in mice based on 4 g/day chow consumption).
- **Administration:** Begin 7 days before tumor cell injection. Provide ad libitum in chow. Continue throughout experiment.
- **Alternative IP dosing:** 30 mg/kg pexidartinib in 0.5% hydroxypropyl methylcellulose/0.1% Tween-80, daily IP injection.
- **Expected effect:** Depletion of 60--80% of intra-tumoral F4/80+ CD206+ M2-like macrophages. Less efficient depletion of liver-resident Kupffer cells (which are partially CSF1-independent and maintained by IL-34 via CSF1R and local proliferation). This differential depletion is actually advantageous for our experimental question, as it allows us to selectively target recruited TAMs while preserving Kupffer cells.
- **Note on resistance:** Wang et al. (2025, Cell Rep Med) showed that CTGF (Connective Tissue Growth Factor) can mediate resistance to CSF1R inhibitors in CRC by maintaining TAM survival via integrin-mediated signaling. Consider combination approaches or verify depletion efficiency in pilot experiments.

### 3.3 Anti-CSF1R Antibody (Alternative to Small Molecule)

- **Reagent:** Anti-mouse CSF1R antibody (clone AFS98; Bio X Cell). 1 mg IP, twice weekly.
- **Advantage:** More selective than PLX3397 (which also inhibits c-KIT and FLT3 at higher concentrations). Cleaner pharmacological tool for mechanism studies.
- **Disadvantage:** Higher cost; shorter half-life requiring frequent dosing.

### 3.4 Selective Depletion of Kupffer Cells: CD169-DTR Transgenic Mice

**Mechanism:** CD169 (Siglec-1, sialoadhesin) is expressed on a subset of tissue-resident macrophages, including Kupffer cells. CD169-DTR mice express human Diphtheria Toxin Receptor (DTR) under the CD169 promoter, allowing selective ablation of CD169+ resident macrophages by diphtheria toxin (DT) administration.

**Protocol:**
- **Mouse strain:** CD169-DTR (B6.FVB-Tg(Siglec1-DTR/EGFP)1Mnz/J; if available from collaborators; originally described by Miyake et al.). Alternatively, use CD169-Cre x iDTR (Rosa26-LSL-DTR) for conditional DTR expression.
- **Diphtheria toxin dosing:** 4 ng/g body weight IP, single dose or every 48 h for maintenance. Begin 48 h before tumor cell injection.
- **Expected depletion:** ~80--90% depletion of CD169+ Kupffer cells (cleaved caspase-3 positive at 24 h post-DT). Monocyte-derived macrophages (CD169-negative) are spared.
- **Critical advantage for our study:** Allows dissection of Kupffer cell-specific vs. recruited monocyte-derived TAM contributions to dormancy regulation. This is the key tool for Section 5.

### 3.5 Myeloid-Specific Gene Deletion: LysM-Cre

**Mechanism:** Lysozyme M (LysM) is expressed in myeloid lineage cells (monocytes, macrophages, neutrophils). LysM-Cre mice express Cre recombinase under the LysM promoter, enabling myeloid-specific deletion of floxed genes.

**Applications for our study:**
- **LysM-Cre x Arg1-flox:** Delete arginase-1 specifically in myeloid cells, disabling M2 metabolic programming. This tests whether M2-like metabolic function (arginine catabolism) is required for dormancy exit.
- **LysM-Cre x Stat6-flox:** Delete STAT6 (Signal Transducer and Activator of Transcription 6), the master transcription factor for IL-4/IL-13-driven M2 polarization. Prevents M2-like polarization.
- **LysM-Cre x Stat1-flox:** Delete STAT1, the master transcription factor for IFN-gamma-driven M1 polarization. Prevents M1-like polarization.
- **LysM-Cre x NFkappaB-RESC (IKKbeta-flox):** Block NF-kappaB signaling in myeloid cells, impairing M1 pro-inflammatory activation.

**Protocol:**
- Cross LysM-Cre males with floxed females (or vice versa). Genotype pups at weaning (PCR for Cre and floxed allele). Use LysM-Cre+; flox/flox or flox/+ as experimental; LysM-Cre-; flox/flox as littermate controls.
- **Limitation:** LysM-Cre also targets neutrophils and some dendritic cell subsets. Deletion efficiency in Kupffer cells is variable (~60--80% depending on gene and age). Not all tissue-resident macrophages express high LysM.

### 3.6 Macrophage Repolarization Strategies

**M2-to-M1 repolarization:**
- **CD40 agonist antibody (clone FGK45, Bio X Cell):** 100 ug IP, twice weekly. Activates macrophages toward M1 phenotype via CD40-TRAF signaling. Beatty et al. (2011, Science) demonstrated CD40-mediated macrophage activation in pancreatic cancer.
- **TLR agonists:** CpG-ODN (TLR9 agonist, 50 ug IP, twice weekly) or Poly(I:C) (TLR3 agonist, 200 ug IP, weekly). Promote M1 polarization via innate immune activation.

**M1-to-M2 repolarization:**
- **IL-4/IL-13 complex:** IL-4/anti-IL-4 antibody complex (clone 11B11, 5 ug IL-4 + 25 ug antibody IP, twice weekly). Sustained IL-4 signaling drives M2 polarization. This is the experimental tool for testing whether forced M2 polarization promotes dormancy exit.

---

## SECTION 4: Macrophage Polarization Readouts for the Colon Cancer Niche

### 4.1 Flow Cytometry Panel for Liver Macrophage Phenotyping

Based on the markers used in VanderVeen et al. (2025) and Qiao et al. (2023), and following the comprehensive review by Pavlov et al. (2026, J Cancer, "Macrophages in Colorectal Cancer: from Normal Mucosa to Distant Metastasis: Beyond the M1/M2 Paradigm"):

| Marker | Fluorochrome | Cell Population | Notes |
|--------|-------------|-----------------|-------|
| CD45 | BV510 | Leukocytes | Lineage gate |
| CD11b | BV605 | Myeloid cells | Pan-myeloid |
| F4/80 | APC-Cy7 | Macrophages | Pan-macrophage |
| Ly6C | FITC | Monocyte subset | Ly6C-hi = inflammatory monocyte; Ly6C-lo = patrolling |
| Ly6G | PE-Cy7 | Neutrophils | Exclude neutrophils (Ly6G+) from macrophage gate |
| CD86 | PE | M1-like marker | Co-stimulatory molecule, upregulated by M1 polarization |
| CD206 (MMR) | APC | M2-like marker | Mannose receptor, upregulated by M2 polarization |
| MHC-II (I-A/I-E) | PerCP-Cy5.5 | Antigen presentation | High in M1; variable in M2 |
| CD64 | BV410 | Fc-gamma-RI | Distinguishes macrophages (CD64+) from monocytes |
| TIM4 | BV711 | Kupffer cell marker | T-cell immunoglobulin and mucin domain containing 4; marks resident Kupffer cells |
| CD11c | BV785 | Dendritic cells / Kupffer cells | CD11c+ TIM4+ = Kupffer cells; CD11c+ TIM4- = moDC |

**Gating strategy:**
1. Singlets (FSC-H vs FSC-A)
2. Live cells (Zombie NIR negative)
3. CD45+ leukocytes
4. CD11b+ myeloid cells
5. Ly6G- (exclude neutrophils)
6. F4/80+ CD64+ macrophages
7. Subdivide into:
   - **TIM4+ CD11c+** = Kupffer cells (liver-resident)
   - **TIM4- CD11c-** = Monocyte-derived macrophages (recruited TAMs)
   - Within each subset, quantify CD86+ MHC-IIhi (M1-like) vs CD206+ (M2-like)

**Sample preparation:**
- Perfuse liver with 10 mL ice-cold PBS via portal vein (to remove circulating leukocytes).
- Digest liver with 0.05% collagenase IV + 0.01% DNase I in RPMI at 37 deg C for 30 min with shaking.
- Filter through 70 um strainer. Centrifuge at 50 g for 3 min to pellet hepatocytes (discard pellet). Collect supernatant with non-parenchymal cells.
- Resuspend in 40% Percoll, underlay with 70% Percoll, centrifuge 800 g for 20 min. Collect interface (enriched leukocytes).
- Count cells. Stain with Live/Dead dye, then Fc block (anti-CD16/32, clone 93), then surface antibody cocktail.

**Minimum events:** Acquire 500,000 CD45+ events per sample (target: at least 5,000--10,000 F4/80+ macrophages per sample for meaningful M1/M2 quantification).

### 4.2 Immunofluorescence on Liver Sections

- Fix liver tissue in 4% PFA for 24 h, cryoprotect in 30% sucrose, embed in OCT, section at 8 um.
- **Panel 1 (Dormancy + Macrophage):** GFP (tumor cells) + F4/80 (macrophages) + Ki67 (proliferation) + DAPI. Quantify: distance from dormant GFP+ single cells to nearest F4/80+ macrophage (proximity analysis using Imaris or ImageJ).
- **Panel 2 (M1/M2):** GFP + CD86 (M1) + CD206 (M2) + DAPI. Quantify: percentage of macrophages adjacent to dormant vs proliferating GFP+ cells that are CD86+ vs CD206+.

### 4.3 Single-Cell RNA Sequencing (scRNA-seq) of Liver Macrophages

- **Protocol:** Isolate liver non-parenchymal cells as above. Sort CD45+ CD11b+ F4/80+ cells by FACS (purity sort, >95%). Process 5,000--10,000 cells per sample on 10x Genomics Chromium (3' v3.1 chemistry). Sequence to target 50,000 reads/cell.
- **Timepoints:** Day 7 (dormancy entry), Day 28 (dormancy maintenance), Day 56 or upon BLI signal increase (dormancy exit). Include matched groups with and without macrophage depletion.
- **Analysis:** Cluster macrophages using Seurat. Identify M1-like clusters (expressing Nos2, Tnf, Il12b, Cd86, Ccl5) vs M2-like clusters (expressing Arg1, Mrc1/Cd206, Retnla/Fizz1, Chil3/Ym1, Ccl17). Trajectory analysis (Monocle3 or Slingshot) to map macrophage polarization dynamics over dormancy timepoints.
- **Reference:** Bresesti et al. (2025, Cell Rep) performed scRNA-seq of liver metastasis-associated macrophages in CRC and identified reprogrammable TAM subsets via miR-342 pathway.

### 4.4 Cytokine Profiling

- Collect serum and liver tissue lysate at each timepoint.
- **Multiplex panel (Luminex or MSD):** IL-10, TGF-beta1, IL-12p70, TNF-alpha, IFN-gamma, IL-4, IL-13, CCL2 (MCP-1), CXCL10 (IP-10), CSF-1, IL-6.
- **ELISA (confirmation):** IL-10 (M2-associated), IL-12p70 (M1-associated), TGF-beta1 (immunosuppressive/dormancy-promoting).

---

## SECTION 5: Colon Cancer-Specific Considerations -- Kupffer Cells vs Recruited TAMs

### 5.1 Biological Rationale

The liver has two macrophage populations with distinct origins and functions:

1. **Kupffer cells (KCs):** Tissue-resident macrophages derived from fetal yolk sac progenitors. They self-maintain by local proliferation with minimal monocyte input under steady state. They line the hepatic sinusoids, are the first cells to contact arriving DTCs, and express TIM4, CD169, and CD11c. Liu et al. (2025, Neoplasia) demonstrated that CXCL16 drives Kupffer cell polarization via PI3K/AKT/FOXO3a signaling in the context of CRC liver metastasis.

2. **Monocyte-derived macrophages (MoMs):** Recruited from circulating Ly6C-hi inflammatory monocytes in response to tumor-derived chemokines (CCL2, CSF-1). They differentiate into TAMs within the tumor microenvironment and are the primary source of M2-like immunosuppressive TAMs in established metastases.

### 5.2 Why This Distinction Matters for Dormancy

- **Dormancy entry:** DTCs arriving in the liver first encounter Kupffer cells. KCs may initially phagocytose some DTCs (tumor-suppressive) but may also produce TNF-alpha and other cytokines that paradoxically promote dormancy entry via NF-kappaB activation in DTCs. The balance between phagocytic clearance and cytokine-mediated dormancy induction is unknown and is a central question for our study.

- **Dormancy maintenance:** During dormancy maintenance, the permissive niche may be shaped by the balance of M1-like KCs (producing anti-proliferative signals like nitric oxide, IL-12, CXCL9/10) and the gradual recruitment of M2-like MoMs (producing IL-10, TGF-beta, Arg1-mediated immunosuppression).

- **Dormancy exit:** We hypothesize that a shift from M1-dominant to M2-dominant macrophage polarization in the peri-DTC niche triggers dormancy exit. This may occur through: (a) Kupffer cell exhaustion or repolarization, (b) increased recruitment of M2-polarizing monocytes, or (c) local metabolic reprogramming (arginine depletion via Arg1).

### 5.3 Experimental Strategy to Distinguish KC vs MoM Contributions

**Experiment 5A: Kupffer Cell-Specific Depletion (CD169-DTR)**
- Use CD169-DTR mice (or CD169-Cre x iDTR) on C57BL/6 background. Inject DT (4 ng/g IP) 48 h before intrasplenic MC38-GFP-Luc2 injection (1x10^3 cells). Continue DT every 72 h for 4 weeks.
- Groups: (1) CD169-DTR + DT + low-dose MC38; (2) CD169-DTR + PBS + low-dose MC38; (3) Wild-type + DT + low-dose MC38 (DT toxicity control).
- Readouts: BLI weekly; flow cytometry for liver macrophage subsets at weeks 2 and 4; immunofluorescence for dormant GFP+ cells with Ki67 and F4/80 at week 4.
- Prediction: If KCs promote dormancy, their depletion should lead to earlier/larger metastatic outgrowth (more dormancy exit). If KCs initially suppress DTCs via phagocytosis, their depletion might lead to more dormant DTCs surviving.

**Experiment 5B: Recruited Monocyte-Macrophage Depletion (CSF1R inhibitor)**
- PLX3397 chow (290 mg/kg) starting 7 days before intrasplenic injection. Preferentially depletes recruited MoMs while sparing KCs.
- Groups: (1) PLX3397 chow + low-dose MC38; (2) Control chow + low-dose MC38.
- Flow cytometry readout: Quantify TIM4+ CD11c+ (KCs) vs TIM4- (MoMs) at each timepoint to confirm selective depletion.
- Prediction: If recruited M2-like MoMs promote dormancy exit, PLX3397 should prolong dormancy (delayed BLI signal increase).

**Experiment 5C: Combined Depletion (Clodronate Liposomes)**
- Clodronate liposomes (200 uL IP, twice weekly) deplete both KCs and MoMs.
- Serves as a "total macrophage" depletion arm for comparison with selective depletions in 5A and 5B.

### 5.4 In Vitro Co-Culture Models

**Kupffer cell isolation:**
- Perfuse C57BL/6 liver with PBS + 0.05% collagenase IV. Isolate non-parenchymal cells. Sort TIM4+ CD11c+ F4/80+ cells (Kupffer cells) by FACS. Culture in RPMI + 10% FBS + 20 ng/mL M-CSF on collagen-coated plates.

**Co-culture with dormant MC38:**
- Plate 5x10^4 dormant MC38-GFP cells (TGF-beta-induced quiescence, confirmed Ki67-negative) in transwell inserts (0.4 um pores, allowing soluble factor exchange but no direct contact). Plate 1x10^5 Kupffer cells (polarized to M1 with 100 ng/mL LPS + 20 ng/mL IFN-gamma for 24 h, or M2 with 20 ng/mL IL-4 + 20 ng/mL IL-13 for 24 h) in lower chamber.
- Readouts: (1) MC38 proliferation (EdU incorporation) at 24, 48, 72 h; (2) MC38 dormancy marker expression (p27, NR2F1, DEC2) by qRT-PCR; (3) Ki67 by flow cytometry.

---

## SECTION 6: Proposed Experimental Groups with Detailed Protocols

### 6.1 Experiment Series Overview

We propose three sequential experimental phases:

**Phase I: Establish and Validate the Dormancy Model (Months 1--3)**
**Phase II: Macrophage Depletion/Repolarization During Dormancy (Months 3--9)**
**Phase III: Mechanistic Dissection (Months 9--15)**

### 6.2 Phase I: Model Validation

**Experiment I.1: Dose-Response for Dormancy Induction**
- **Objective:** Determine the optimal MC38-GFP-Luc2 cell dose that generates stable dormant liver DTCs (BLI plateau without macrometastatic outgrowth for 8+ weeks).
- **Groups (n=12 mice per group, C57BL/6J females, 8--10 weeks):**

| Group | Cells (intrasplenic) | Expected Outcome |
|-------|---------------------|------------------|
| 1.1 | 1x10^2 | Very few/no detectable DTCs |
| 1.2 | 5x10^2 | Low-level DTCs, may establish dormancy |
| 1.3 | 1x10^3 | Optimal dormancy dose (predicted) |
| 1.4 | 5x10^3 | Mixed dormancy + early outgrowth |
| 1.5 | 1x10^5 | Rapid macrometastatic outgrowth (positive control) |

- **Readouts:** BLI weekly for 12 weeks. At weeks 4 and 12, sacrifice 3 mice per group for flow cytometry (GFP+ DTC quantification, macrophage phenotyping). Liver histology (H&E, GFP IHC, Ki67 IHC).
- **Exit criteria:** The dose yielding BLI signal plateau for 6+ consecutive weeks in >60% of mice without macrometastases defines the dormancy dose.

**Experiment I.2: Time-Course Characterization of Macrophage Polarization During Dormancy**
- **Objective:** Map the natural history of macrophage polarization in the liver during dormancy entry, maintenance, and spontaneous exit.
- **Groups:** Use the optimal dormancy dose from I.1. Sacrifice n=5 mice at each timepoint: Day 3, Day 7, Day 14, Day 28, Day 56, Day 84.
- **Readouts at each timepoint:**
  - BLI (prior to sacrifice)
  - Flow cytometry: Full macrophage panel (Section 4.1) with KC vs MoM distinction
  - qRT-PCR on sorted GFP+ DTCs: dormancy markers (Nr2f1, Dec2/Bhlhe41, p27/Cdkn1b, Foxo3a, Sox2) and proliferation markers (Mki67, Pcna)
  - Serum cytokines (Section 4.4)
  - Liver tissue: snap-frozen for RNA-seq, fixed for IF

### 6.3 Phase II: Macrophage Manipulation During Dormancy

**Experiment II.1: Total Macrophage Depletion During Dormancy Maintenance**
- **Objective:** Determine whether macrophages are required for dormancy maintenance.
- **Starting point:** All mice receive optimal dormancy dose of MC38-GFP-Luc2. Allow dormancy establishment for 14 days (confirmed by BLI plateau).
- **Groups (n=15 per group):**

| Group | Treatment | Schedule | Question |
|-------|-----------|----------|----------|
| II.1.A | Clodronate liposomes (200 uL IP) | Twice weekly, weeks 2--12 | Does total macrophage depletion cause dormancy exit? |
| II.1.B | PBS liposomes (200 uL IP) | Twice weekly, weeks 2--12 | Vehicle control |
| II.1.C | No treatment | Weeks 2--12 | Untreated dormancy control |

- **Readouts:** BLI weekly. Sacrifice n=5 per group at weeks 4, 8, 12. Flow cytometry, IF, scRNA-seq (week 8 timepoint, n=3 per group).

**Experiment II.2: Selective M2 Depletion via CSF1R Inhibition**
- **Objective:** Determine whether M2-like TAMs are specifically required for dormancy exit.
- **Groups (n=15 per group):**

| Group | Treatment | Schedule |
|-------|-----------|----------|
| II.2.A | PLX3397 chow (290 mg/kg) | Day -7 to week 12 |
| II.2.B | PLX3397 chow starting week 4 | Week 4 to week 12 (delayed treatment to target maintenance phase) |
| II.2.C | Control chow | Weeks 0--12 |
| II.2.D | PLX3397 chow + IL-4 complex | Day -7 to week 12 (rescue with forced M2 polarization) |

- **IL-4 complex dosing:** 5 ug IL-4 + 25 ug anti-IL-4 (clone 11B11) IP, twice weekly. This forms a sustained IL-4 signaling complex that can override CSF1R inhibitor-mediated M2 depletion.

**Experiment II.3: Forced M1 Polarization During Dormancy Maintenance**
- **Objective:** Test whether M1-polarized macrophages can enforce dormancy or eliminate DTCs.
- **Groups (n=15 per group):**

| Group | Treatment | Schedule |
|-------|-----------|----------|
| II.3.A | CD40 agonist (FGK45, 100 ug IP) | Twice weekly, weeks 2--12 |
| II.3.B | CpG-ODN 1826 (50 ug IP) | Twice weekly, weeks 2--12 |
| II.3.C | IgG2a isotype control | Twice weekly, weeks 2--12 |

**Experiment II.4: Forced M2 Polarization to Trigger Dormancy Exit**
- **Objective:** Test whether shifting the macrophage balance to M2 is sufficient to trigger dormancy exit.
- **Groups (n=15 per group):**

| Group | Treatment | Schedule |
|-------|-----------|----------|
| II.4.A | IL-4 complex (5 ug IL-4 + 25 ug 11B11 IP) | Twice weekly, weeks 4--12 |
| II.4.B | IL-13 complex (5 ug IL-13 + 25 ug anti-IL-13 IP) | Twice weekly, weeks 4--12 |
| II.4.C | PBS control | Twice weekly, weeks 4--12 |

- **Critical prediction:** If M2 polarization drives dormancy exit, II.4.A and II.4.B should show accelerated BLI signal increase and earlier macrometastatic outgrowth compared to control.

### 6.4 Phase III: Mechanistic Dissection Using Genetic Tools

**Experiment III.1: LysM-Cre x Stat6-flox (M2-Deficient Macrophages)**
- **Objective:** Test whether macrophage M2 polarization is required for dormancy exit in a genetic model.
- **Mice:** LysM-Cre+; Stat6flox/flox (experimental) vs LysM-Cre-; Stat6flox/flox (littermate controls). C57BL/6 background.
- **Groups (n=15 per genotype):** Intrasplenic injection of MC38-GFP-Luc2 at dormancy dose.
- **Readouts:** BLI weekly for 12 weeks. Flow cytometry at weeks 4, 8, 12 with M1/M2 panel. scRNA-seq of liver macrophages at week 8 (compare M2 gene signature between genotypes).

**Experiment III.2: LysM-Cre x Stat1-flox (M1-Deficient Macrophages)**
- **Complementary to III.1.** Tests whether loss of M1 polarization accelerates dormancy exit (predict: more M2-like niche, earlier outgrowth).

**Experiment III.3: CD169-DTR Kupffer Cell Depletion During Dormancy**
- As detailed in Section 5.3, Experiment 5A. n=15 per group.
- **Combined with CSF1R inhibitor:** In separate arms, combine CD169-DTR KC depletion with PLX3397 to deplete both KCs and MoMs, allowing comparison with single-depletion arms.

**Experiment III.4: In Vitro Co-Culture Mechanistic Dissection**
- Dormant MC38-GFP cells co-cultured with sorted KCs or MoMs (M1- or M2-polarized) in transwell or direct contact format.
- **Conditions (each in triplicate, repeated 3 times):**

| Condition | Macrophage Source | Polarization | Contact |
|-----------|------------------|-------------|---------|
| A | Sorted KCs (TIM4+ CD11c+) | M1 (LPS+IFN-gamma) | Transwell |
| B | Sorted KCs | M1 | Direct contact |
| C | Sorted KCs | M2 (IL-4+IL-13) | Transwell |
| D | Sorted KCs | M2 | Direct contact |
| E | Sorted MoMs (TIM4- F4/80+) | M1 | Transwell |
| F | Sorted MoMs | M2 | Transwell |
| G | No macrophages | N/A | N/A |
| H | Unpolarized KCs | None | Transwell |

- **Readouts (24, 48, 72 h):** MC38 EdU incorporation, Ki67 by flow, dormancy gene expression (qRT-PCR: Nr2f1, Dec2, p27), apoptosis (Annexin V/PI).
- **Supernatant analysis:** Luminex cytokine panel at each timepoint.

### 6.5 Statistical Considerations

- **Sample size:** Based on BLI signal as primary endpoint, assuming 50% effect size of macrophage depletion on BLI photon flux (based on Kruse et al., 2013), alpha=0.05, power=0.80: n=12--15 per group (accounting for 20% attrition due to surgical mortality and non-dormant mice).
- **Analysis:** Two-way ANOVA (treatment x time) for longitudinal BLI data with Tukey post-hoc correction. Log-rank test for time-to-dormancy-exit (defined as >3-fold BLI signal increase sustained over 2 consecutive weeks). Mann-Whitney U test for flow cytometry percentage comparisons. Adjust for multiple comparisons using Benjamini-Hochberg for scRNA-seq.
- **Randomization:** Randomly assign mice to treatment groups after confirming BLI dormancy signal at day 14 (stratified randomization based on BLI signal intensity to ensure balanced groups).

### 6.6 Expected Outcomes and Decision Points

| Experiment | Outcome A | Interpretation A | Outcome B | Interpretation B |
|-----------|-----------|-----------------|-----------|-----------------|
| II.1 (Clodronate) | Dormancy exit accelerated | Macrophages maintain dormancy (paradoxical) | Dormancy maintained or prolonged | Macrophages promote exit |
| II.2 (PLX3397) | Dormancy prolonged | M2-TAMs promote exit | No effect | MoMs not involved in exit |
| II.3 (CD40 agonist) | Dormancy maintained/increased DTC clearance | M1 macrophages enforce dormancy | No effect | M1 shift insufficient |
| II.4 (IL-4 complex) | Dormancy exit triggered | M2 sufficient for exit | No effect | Other signals required |
| III.1 (Stat6-KO) | Dormancy prolonged | M2 polarization required for exit | No effect | STAT6-independent M2 pathway |
| III.3 (KC depletion) | Accelerated exit | KCs enforce dormancy | More dormant DTCs survive | KCs suppress DTCs via phagocytosis |

---

## APPENDIX: Key Literature Supporting This Design

1. **Pavlov S et al. (2026, J Cancer)** -- "Macrophages in Colorectal Cancer: from Normal Mucosa to Distant Metastasis: Beyond the M1/M2 Paradigm." Comprehensive review of macrophage diversity in CRC progression and metastasis.

2. **Liu Y et al. (2025, Neoplasia)** -- CXCL16/Kupffer cell polarization via PI3K/AKT/FOXO3a signaling in CRC liver metastasis. Establishes KC-specific signaling pathway.

3. **Bresesti C et al. (2025, Cell Rep)** -- Reprogramming liver metastasis-associated macrophages via miR-342. scRNA-seq of liver TAMs in CRC.

4. **Heinz MC et al. (2022, Cancer Res, PMID: 35570706)** -- YAP-controlled plasticity at the micrometastatic stage in CRC liver metastasis. Intravital microscopy, patient-derived organoids, scRNA-seq. Key model for dormancy-to-colonization transition.

5. **Qiao T et al. (2023, Cell Death Dis)** -- F4/80+ TAM differentiation in MC38 CRLM model. Flow cytometry and functional characterization.

6. **VanderVeen BN et al. (2025)** -- MC38 model with diet-induced obesity demonstrating Kupffer cell phenotypic changes.

7. **Shimizu D et al. (2024, Int J Mol Sci)** -- Pexidartinib depletes M2 macrophages from cancer-associated fibroblasts in CRC.

8. **Wang B et al. (2025, Cell Rep Med)** -- CTGF overcomes CSF1R inhibitor resistance in CRC. Important consideration for CSF1R-based depletion strategies.

9. **Kruse J et al. (2013, Int J Colorectal Dis, PMID: 23657400)** -- Macrophages promote tumor growth and liver metastasis in orthotopic syngeneic CT26/BALB/c model using clodronate liposomes.

10. **Bader JE et al. (2018, Am J Physiol Gastrointest Liver Physiol, PMID: 29025731)** -- Clodronate liposome macrophage depletion in AOM/DSS colon cancer model. Protocol reference (200 uL IP, twice weekly).

11. **Guba M et al. (2001, Cancer Res, PMID: 11454710)** -- Primary tumor promotes dormancy of solitary tumor cells in mouse liver. CT-26/BALB/c model with intravital videomicroscopy.

12. **Ohsawa I et al. (2006, Transplantation)** -- Rat colon cancer dormancy model with luciferase imaging; CsA released cells from dormancy. Foundational dormancy model reference.

13. **Malladi S et al. (2016, Cell)** -- Metastatic latency and immune evasion through autocrine inhibition of WNT (in breast cancer). Framework for dormancy concepts adapted to CRC.

14. **Ganesh K et al. (2020, Cell)** -- L1CAM defines the regenerative origin of metastasis-initiating cells in colorectal cancer. Relevant to CRC dormancy and metastatic initiation.

15. **Cheung P et al. (2022, Cancer Cell)** -- Regenerative reprogramming of intestinal stem cell state via Hippo signaling suppresses metastatic CRC. YAP/Hippo pathway in CRC metastasis.

---

**Note on critical gap:** There is no published in vivo model that specifically combines colon cancer dormancy with selective macrophage phenotype manipulation. The experimental design above is therefore novel and fills a significant gap. The Heinz et al. (2022) YAP-plasticity model provides the dormancy framework, while the macrophage tools (clodronate, PLX3397, CD169-DTR, LysM-Cre crosses) are well-validated individually but have not been applied to the dormancy question in CRC. Our design bridges these two literatures for the first time.