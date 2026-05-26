---
title: "Bench Protocols: M1/M2 Macrophage Contributions to Colon Cancer DTC Dormancy"
subtitle: "Step-by-Step Instructions for Postdoctoral Researchers"
date: "May 2026"
version: "1.0"
header-includes:
  - \usepackage{geometry}
  - \geometry{margin=1in}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{M1/M2 Dormancy Protocols}
  - \fancyhead[R]{Page \thepage}
  - \usepackage{xcolor}
  - \definecolor{warnbg}{RGB}{255,240,240}
  - \definecolor{tipbg}{RGB}{235,245,255}
  - \usepackage{tcolorbox}
  - \newtcolorbox{warning}{colback=warnbg,colframe=red!60!black,title=WARNING}
  - \newtcolorbox{tip}{colback=tipbg,colframe=blue!60!black,title=TIP}
  - \usepackage[compact]{titlesec}
---

\newpage

# Document Overview

This document provides **complete, step-by-step bench protocols** for all experimental procedures in the study: "Quantitative Dissection of M1 and M2 Macrophage Contributions to Dormancy Entry, Maintenance, and Exit in Colon Cancer."

**Each protocol includes:** materials list, detailed steps, timing, expected results, and troubleshooting tips.

\begin{tip}
Protocols are organized in experimental execution order. Complete Protocol 1 (cell engineering) before starting Protocol 2 (in vivo work).
\end{tip}

\newpage

# Protocol 1: MC38 Cell Line Engineering

## 1.1 Purpose

Engineer MC38 murine colon adenocarcinoma cells with fluorescent reporters for dormancy detection and longitudinal tracking.

## 1.2 Required Constructs

| Construct | Reporter | Purpose | Lentiviral Vector |
|-----------|----------|---------|-------------------|
| GFP-Luciferase | EGFP + firefly luciferase | BLI tracking + flow cytometry | pLenti-PGK-GFP-2A-Luc2 |
| Fucci2a | mCherry-hCdt1 (G1) + mVenus-hGem (S/G2/M) | Real-time cell cycle | pRRL-Fucci2a |
| H2B-mCherry | Histone H2B-mCherry | Nuclear label for single-cell tracking | pLenti-EF1a-H2B-mCherry |

## 1.3 Lentivirus Production (Day 0-3)

**Materials:**

- HEK293T cells (ATCC CRL-3216)
- Lentiviral packaging plasmids: psPAX2, pMD2.G
- Transfer plasmids (listed above)
- Lipofectamine 3000 (ThermoFisher L3000015)
- DMEM + 10% FBS + 1% Pen/Strep
- 0.45 um PVDF filter units
- Lenti-X Concentrator (Takara 631232)

**Steps:**

1. **Day 0:** Seed HEK293T cells at 5 × 10⁶ cells per 10 cm dish in 10 mL DMEM + 10% FBS. Incubate 37°C, 5% CO2 overnight.
2. **Day 1 (morning):** Confirm ~80% confluence. Prepare transfection mix per dish:
   - Tube A: 375 uL Opti-MEM + 10 ug transfer plasmid + 7.5 ug psPAX2 + 2.5 ug pMD2.G + 50 uL P3000 reagent
   - Tube B: 375 uL Opti-MEM + 60 uL Lipofectamine 3000
   - Combine Tube A + Tube B. Incubate 15 min at RT. Add dropwise to dish.
3. **Day 2:** Replace medium with 10 mL fresh DMEM + 10% FBS + 1% BSA (improves viral stability).
4. **Day 3:** Collect supernatant. Filter through 0.45 um PVDF. Add Lenti-X Concentrator (1:3 ratio). Incubate 4°C overnight. Centrifuge 1500 x g, 45 min, 4°C. Resuspend pellet in 200 uL PBS. Aliquot and store at -80°C.

\begin{warning}
Biosafety Level 2 (BSL-2) required for lentiviral work. Use biosafety cabinet for all steps involving virus.
\end{warning}

## 1.4 MC38 Transduction (Day 0-14)

**Steps:**

1. Seed MC38 cells at 2 × 10⁵ per well in 6-well plate (DMEM + 10% FBS).
2. Add concentrated lentivirus (GFP-Luc2 construct first) at MOI ~5 with 8 ug/mL polybrene.
3. Spin-infect: Centrifuge plate at 800 x g, 30 min, 32°C.
4. Replace medium after 12 h. Culture for 48 h.
5. Sort GFP+ cells by FACS (BD FACSAria or equivalent). Gate: FSC/SSC singlets -> Live (DAPI-) -> GFP+. Collect top 30% brightest GFP+ cells.
6. Expand sorted cells for 5-7 days.
7. Repeat transduction with Fucci2a construct (same MOI). Sort dual-positive cells: GFP+ AND mCherry+ (Fucci2a).
8. Repeat with H2B-mCherry construct.
9. **Final validation:** Culture triple-reporter cells for 2 weeks. Confirm stable GFP, Fucci2a signal (cell cycle-dependent mCherry/mVenus), and nuclear mCherry (H2B) by fluorescence microscopy. Confirm luciferase activity with D-luciferin assay.

\begin{tip}
Freeze multiple vials of validated triple-reporter MC38 cells at each passage. Create a master cell bank at Passage 3-5 post-engineering.
\end{tip}

**Expected result:** >90% GFP+, functional Fucci2a cycling (red in serum-starved quiescence, green in log-phase proliferation), nuclear mCherry in >95% cells.

\newpage

# Protocol 2: Intrasplenic Injection — Liver Metastasis Model

## 2.1 Purpose

Introduce MC38-GFP-Luc-Fucci2a-H2B-mCherry cells into the liver via the splenic-portal vein route to generate disseminated tumor cells (DTCs).

## 2.2 Materials

- C57BL/6J mice, female, 8-10 weeks (Jackson Labs #000664)
- MC38-GFP-Luc-Fucci2a cells (from Protocol 1)
- Isoflurane vaporizer and induction chamber
- Surgical microscope or loupe magnification
- 30G insulin syringes (BD Ultra-Fine)
- Microsurgical instruments: fine forceps (Dumont #5), micro-scissors, needle holder
- 5-0 Vicryl sutures (absorbable, for peritoneum)
- Wound clips (9 mm Autoclip) + clip applier
- Buprenorphine (0.3 mg/mL) for analgesia
- Sterile saline, sterile gauze, sterile drapes
- Heat pad (maintain 37°C during surgery)

## 2.3 Cell Preparation (Day of Surgery)

1. Harvest MC38-GFP-Luc-Fucci2a cells at 70-80% confluence (use cells at passage <20 post-engineering).
2. Wash with PBS. Trypsinize with 0.05% trypsin-EDTA, 3 min at 37°C.
3. Neutralize with DMEM + 10% FBS. Centrifuge 300 x g, 5 min.
4. Wash 2x with ice-cold PBS. Resuspend at **1 × 10³ cells per 50 uL PBS** (low dose for dormancy) or 1 × 10⁵ cells per 50 uL (high dose for positive control).
5. Keep on ice. Use within 30 minutes of preparation.

\begin{warning}
Cell viability must be >95% (verify by Trypan Blue). Dead cells cause inflammation that confounds dormancy analysis.
\end{warning}

## 2.4 Surgical Procedure

1. **Anesthesia:** Place mouse in induction chamber. Isoflurane 3% in 1 L/min O2. After induction (~2 min), transfer to nose cone on heated surgical platform. Maintain at 1.5-2% isoflurane.
2. **Preparation:** Apply ophthalmic ointment to eyes. Shave left flank. Disinfect with betadine followed by 70% ethanol, x3 alternating.
3. **Incision:** Make 1 cm left flank incision through skin and peritoneum.
4. **Spleen exposure:** Gently exteriorize spleen using moistened cotton swab. Place on sterile gauze moistened with warm saline.
5. **Injection:** Using 30G insulin syringe, slowly inject **50 uL cell suspension** (1 × 10³ cells) into the inferior pole of the spleen over **30 seconds**. Too-fast injection causes backflow and peritoneal seeding.
6. **Wait:** Hold needle in place for 60 seconds after injection to prevent back-bleeding.
7. **Withdraw** needle gently. Apply gentle pressure with cotton swab to injection site.
8. **Splenectomy (optional but recommended):** Ligate splenic vessels with 5-0 silk suture. Remove spleen to prevent local tumor growth at injection site. This step is critical for eliminating confounding primary splenic tumors.
9. **Closure:** Close peritoneum with 5-0 Vicryl (continuous suture). Close skin with wound clips (2-3 clips).
10. **Recovery:** Place mouse in clean cage on heat pad. Monitor until ambulatory (typically 15-30 min).
11. **Analgesia:** Buprenorphine 0.1 mg/kg SC every 12 h for 48 h post-surgery.

**Post-operative monitoring:** Daily health checks for 7 days. Remove wound clips at Day 10-14.

\begin{tip}
Practice the injection technique on cadaver mice first. The key is SLOW injection (30 sec) to allow cells to transit the splenic vein into the portal circulation before back-pressure builds up.
\end{tip}

## 2.5 Expected Timeline Post-Injection

| Day | Phase | Expected Biology |
|-----|-------|-----------------|
| 0-1 | Seeding | DTCs transit portal vein, lodge in liver sinusoids |
| 1-3 | Early extravasation | DTCs exit sinusoids into liver parenchyma |
| 3-7 | Dormancy entry | DTCs either enter dormancy or begin proliferating |
| 7-14 | Dormancy establishment | Stable NR2F1+ Ki67- DTCs present in liver |
| 14-84 | Maintenance / Exit | Variable: some DTCs remain dormant, others exit |

\newpage

# Protocol 3: Macrophage Depletion and Polarization Manipulation

## 3.1 Total Macrophage Depletion — Clodronate Liposomes

**Reagent:** Clodronate liposomes (Liposoma BV, Amsterdam, Cat# CP-005-005)

**Dosing schedule:**

| Timing | Dose | Route | Frequency |
|--------|------|-------|-----------|
| 3 days before injection | 200 uL | IV tail vein | Single |
| Day 1 onward | 200 uL | IV tail vein | Twice weekly (e.g., Mon + Thu) |

**Control:** PBS liposomes (Liposoma BV, Cat# PB-005-005), same volume and schedule.

**Preparation:**

1. Remove clodronate liposomes from 4°C storage. **Do NOT freeze.**
2. Gently invert tube 5x to resuspend. **Do NOT vortex** (damages liposomes).
3. Draw 200 uL into 1 mL syringe with 30G needle.
4. Warm to room temperature before injection.

**Injection technique (tail vein):**

1. Place mouse in restraint tube. Warm tail with heat lamp or warm water soak for 1-2 min to dilate veins.
2. Identify lateral tail vein. Clean with 70% ethanol.
3. Insert 30G needle at 10-20° angle, bevel up, 2-3 cm from tail base.
4. Inject slowly over 15-20 seconds. No resistance should be felt.
5. Withdraw needle, apply gentle pressure with gauze.

\begin{warning}
Depletion efficiency must be verified at each sacrifice timepoint by flow cytometry. Target: >80% reduction in CD11b+ F4/80+ cells in liver. If depletion is <70%, switch to IP route (200 uL IP, 3x weekly).
\end{warning}

## 3.2 Kupffer Cell-Specific Depletion — CD169-DTR Mice

**Mouse strain:** CD169-DTR (B6.FVB-Tg(Siglec1-DTR/EGFP)1Mnz/J)

**Reagent:** Diphtheria toxin (DT), Sigma D0564

**DT preparation:**

1. Reconstitute DT in sterile PBS to 1 mg/mL stock. Aliquot 10 uL. Store at -80°C.
2. Working solution: Dilute stock to 1 ug/mL in sterile PBS on day of use.
3. **Dose:** 4 ng/g body weight IP. Example: 25 g mouse = 100 uL of 1 ug/mL solution.

**Schedule:**

- **Day -2:** First DT injection (48 h before tumor cell injection)
- **Day 0:** Tumor cell injection
- **Day 2, 5, 8, 11, ...:** Repeat DT every 72 h for maintenance

**Depletion verification:** At sacrifice, stain liver non-parenchymal cells for TIM4+ CD11c+ (Kupffer cells). Target: >80% depletion of TIM4+ cells.

\begin{warning}
DT is EXTREMELY toxic. The therapeutic window is narrow. Do NOT exceed 10 ng/g. Include wild-type + DT control mice to control for DT off-target effects.
\end{warning}

## 3.3 M1 Polarization — CpG-ODN 1826

**Reagent:** CpG-ODN 1826 (InvivoGen tlrl-1826), mouse-specific TLR9 agonist

**Preparation:** Resuspend in sterile endotoxin-free H2O to 1 mg/mL. Aliquot and store at -20°C.

**Dose:** 50 ug per mouse IP, 3 times per week (e.g., Mon/Wed/Fri)

**Schedule:** Begin Day -3 (3 days before injection). Continue throughout experiment.

**Expected effect:** Shifts liver macrophages toward M1-like phenotype. Verify by flow cytometry: increased CD86+ MHC-II-high fraction among F4/80+ cells at Day 7.

## 3.4 M2 Polarization — IL-4 Immune Complex

**Reagents:**

- Recombinant mouse IL-4 (BioLegend 574302)
- Anti-IL-4 antibody, clone 11B11 (BioLegend 504111)

**Complex preparation (prepare fresh each time):**

1. In 200 uL sterile PBS, mix 5 ug IL-4 + 25 ug anti-IL-4 antibody.
2. Incubate at 37°C for 30 min to form immune complexes.
3. Inject 200 uL IP immediately.

**Schedule:** Twice weekly (e.g., Tue + Fri). Begin Day -3 or Day 1 as per experimental arm.

**Expected effect:** Sustained M2 polarization. Verify by flow cytometry: increased CD206+ fraction among F4/80+ cells.

## 3.5 Anti-IFN-gamma Neutralization

**Reagent:** Anti-mouse IFN-gamma antibody, clone XMG1.2 (Bio X Cell BP0055)

**Dose:** 200 ug per mouse IP, twice weekly

**Control:** Rat IgG1 isotype control (Bio X Cell BP0088), same dose

## 3.6 Anti-IL-4Ralpha Blockade

**Reagent:** Anti-mouse IL-4Ralpha antibody, clone M1 (Bio X Cell)

**Dose:** 200 ug per mouse IP, twice weekly, starting Day 14

**Purpose:** Blocks both IL-4 and IL-13 signaling, preventing M2 skewing.

\newpage

# Protocol 4: Bioluminescence Imaging (BLI)

## 4.1 Purpose

Weekly monitoring of tumor burden to detect dormancy exit (BLI signal increase indicates proliferative outgrowth).

## 4.2 Materials

- IVIS Spectrum or Lumina III (PerkinElmer)
- D-Luciferin potassium salt (GoldBio LUCK-1G)
- Isoflurane anesthesia system compatible with IVIS

## 4.3 Procedure

1. **Prepare luciferin:** 15 mg/mL D-luciferin in sterile PBS. Filter-sterilize (0.22 um). Store aliquots at -20°C (stable for 6 months).
2. **Inject luciferin:** 150 mg/kg IP (e.g., 25 g mouse = 250 uL of 15 mg/mL). Record exact time of injection.
3. **Wait 10 minutes** for peak luminescence. Place mice in IVIS under isoflurane anesthesia (1.5%).
4. **Image settings:**
   - Exposure: Auto (or start with 1 min, adjust if saturated)
   - Binning: Medium (8)
   - F/stop: 1
   - Emission filter: Open
5. **Acquire image.** Save as .nii or .tif. Record total flux (photons/sec) using Living Image software or open-source IVIS-compatible software.

## 4.4 Analysis

1. Draw region of interest (ROI) around the liver area for each mouse.
2. Record total flux (photons/sec) per ROI.
3. **Dormancy = stable or decreasing BLI signal for 4+ consecutive weeks.**
4. **Dormancy exit = >2-fold increase in total flux above baseline plateau.**
5. Export data to spreadsheet. Plot longitudinal BLI curves per mouse.

\begin{tip}
Dormant single DTCs are BELOW the BLI detection limit (approximately 10³–10⁴ cells). BLI can only detect proliferative outgrowth. A mouse with stable low BLI signal still harbors dormant DTCs that will be visible by IF on tissue sections.
\end{tip}

\newpage

# Protocol 5: Liver Tissue Harvest and Processing

## 5.1 Purpose

Collect liver tissue at defined timepoints for immunofluorescence, flow cytometry, and molecular analysis.

## 5.2 Timepoints

| Day | Phase | Mice per group | Analysis |
|-----|-------|:--------------:|----------|
| 7 | Dormancy entry | 3-4 | IF, flow, cytokines |
| 21 | Dormancy established | 3-4 | IF, flow, scRNA-seq |
| 42 | Maintenance | 3-4 | IF, flow, scRNA-seq |
| 84 | Late/outgrowth | 3-4 | IF, flow, pathology |

## 5.3 Euthanasia and Perfusion

1. Euthanize by CO2 asphyxiation followed by cervical dislocation.
2. **Portal vein perfusion (CRITICAL for flow cytometry):**
   - Make midline abdominal incision. Identify portal vein.
   - Insert 24G angiocatheter into portal vein. Secure with suture.
   - Cut inferior vena cava to allow outflow.
   - Slowly perfuse 10 mL ice-cold PBS over 2-3 minutes. Liver should blanch to pale tan color.
   - **Purpose:** Removes circulating leukocytes that would contaminate liver-resident immune cell analysis.
3. Excise liver. Record total weight and photograph.

## 5.4 Tissue Allocation

Divide each liver into portions:

| Portion | Weight | Processing | Analysis |
|---------|--------|-----------|----------|
| Left lobe (~30%) | ~300 mg | Fix in 4% PFA, 24 h at 4°C | Immunofluorescence (Protocol 6) |
| Median lobe (~30%) | ~300 mg | Fresh, on ice | Flow cytometry (Protocol 7) |
| Right lobe (~20%) | ~200 mg | Snap-freeze in liquid N2 | scRNA-seq (Protocol 8) or store -80°C |
| Caudate lobe (~20%) | ~200 mg | Snap-freeze in liquid N2 | Cytokine analysis, RNA, protein |

\begin{warning}
Process flow cytometry samples within 30 min of harvest. Cell viability drops rapidly after 1 hour on ice.
\end{warning}

\newpage

# Protocol 6: Multiplex Immunofluorescence on Liver Sections

## 6.1 Purpose

Detect and quantify dormant DTCs, macrophage polarization, and macrophage-DTC spatial relationships in situ.

## 6.2 Tissue Sectioning

1. After 24 h PFA fixation, transfer liver tissue to 30% sucrose in PBS at 4°C until tissue sinks (24-48 h).
2. Embed in OCT compound. Freeze on dry ice. Store at -80°C.
3. Cut 8 um cryosections at -20°C. Mount on Superfrost Plus slides.
4. Air dry 30 min. Store at -80°C until staining.

## 6.3 Multiplex IF Panel — Dormancy + Macrophage

| Channel | Marker | Purpose | Primary Antibody | Dilution |
|---------|--------|---------|-----------------|----------|
| DAPI | Nuclear | Cell ID | -- | -- |
| Opal 520 | pan-Cytokeratin | DTC identification | AE1/AE3 (Dako) | 1:200 |
| Opal 570 | NR2F1 | Dormancy marker | P1H2 (Santa Cruz) | 1:100 |
| Opal 620 | Ki67 | Proliferation | MIB-1 (Dako) | 1:200 |
| Opal 690 | p27/KIP1 | Cell cycle arrest | DCS-60.F6 | 1:200 |
| Opal 780 | CD68 | Pan-macrophage | PG-M1 (Dako) | 1:100 |

**Alternative: serial sections for M1 vs M2** (on adjacent sections):

| Section | Panel |
|---------|-------|
| Section A | GFP + F4/80 + Ki67 + DAPI (DTC detection + macrophage + proliferation) |
| Section B | GFP + CD86 + CD206 + DAPI (M1 vs M2 macrophage polarization) |

## 6.4 Staining Procedure (Opal/tyramide method)

1. **Fix sections:** 4% PFA, 10 min, RT. Wash 3x PBS.
2. **Antigen retrieval:** Citrate buffer pH 6.0, microwave 20 min (or pressure cooker 125°C, 3 min). Cool 20 min. Wash 3x PBS.
3. **Block:** 5% normal goat serum + 0.3% Triton X-100 in PBS, 1 h, RT.
4. **Primary antibody incubation:** Dilute antibody in blocking buffer. Incubate overnight at 4°C in humidified chamber.
5. **Wash** 3x PBS-T (0.05% Tween-20), 5 min each.
6. **HRP-secondary:** Species-appropriate HRP-conjugated secondary, 1 h, RT.
7. **Wash** 3x PBS-T.
8. **Opal fluorophore:** Dilute Opal reagent 1:100 in amplification buffer. Incubate 10 min, RT.
9. **Wash** 3x PBS-T.
10. **Microwave strip:** Citrate buffer pH 6.0, microwave 20 min to remove antibodies while retaining deposited Opal fluorophore. Cool, wash.
11. **Repeat steps 4-10** for each subsequent marker in the panel.
12. **DAPI:** 1 ug/mL in PBS, 5 min, RT.
13. **Mount** with ProLong Gold antifade. Cure 24 h at RT in dark.

## 6.5 Imaging and Quantification

**Imaging:** Scan slides on Vectra Polaris (Akoya) or equivalent multispectral imaging system at 20x. Unmix spectra using single-stained controls.

**Quantification (per mouse):**

1. **DTC detection:** Count all pan-CK+ cells in 10 randomly selected 20x fields per section.
2. **Dormancy classification:** For each DTC, score:
   - NR2F1: positive (nuclear) or negative
   - Ki67: positive or negative
   - p27: positive (nuclear) or negative
   - **Dormant DTC = NR2F1+ AND Ki67- AND p27+**
   - **Proliferating DTC = Ki67+ AND (NR2F1- OR p27-)**
3. **Macrophage proximity:** Measure distance from each DTC to nearest CD68+ cell (or F4/80+ cell) using image analysis software (QuPath, HALO, or ImageJ).
4. **Minimum count:** Score at least 200 DTCs per condition for statistical power.

\begin{tip}
Use QuPath (free, open-source) for automated cell detection and classification. Train the classifier on manually annotated examples from 5-10 fields, then batch-process all sections.
\end{tip}

\newpage

# Protocol 7: Liver Macrophage Flow Cytometry

## 7.1 Purpose

Quantify macrophage polarization (M1-like vs M2-like) and depletion efficiency in liver tissue.

## 7.2 Liver Non-Parenchymal Cell Isolation

1. After portal vein perfusion (Protocol 5.3), excise liver and mince with scissors into ~1 mm pieces in RPMI on ice.
2. Transfer to 15 mL tube with 5 mL digestion buffer:
   - RPMI + 0.05% collagenase IV + 0.01% DNase I + 2% FBS
3. Incubate 37°C, 30 min, shaking at 200 rpm.
4. Pass through 70 um cell strainer. Rinse with 5 mL RPMI + 2% FBS.
5. **Hepatocyte removal:** Centrifuge 50 x g for 3 min at 4°C. Discard pellet (hepatocytes). Collect supernatant (non-parenchymal cells).
6. **Percoll enrichment:** Resuspend cells in 3 mL 40% Percoll in PBS. Underlay with 3 mL 70% Percoll. Centrifuge 800 x g, 20 min, 4°C, no brake.
7. Collect interface layer (leukocyte-enriched). Wash with PBS + 2% FBS. Centrifuge 400 x g, 5 min.
8. Count cells. Expected yield: 2-5 × 10⁶ leukocytes per liver.

## 7.3 Antibody Staining Panel

| Marker | Fluorochrome | Clone | Purpose | Dilution |
|--------|-------------|-------|---------|----------|
| Live/Dead | Zombie NIR | -- | Viability | 1:1000 |
| CD45 | BV510 | 30-F11 | Leukocytes | 1:200 |
| CD11b | BV605 | M1/70 | Myeloid cells | 1:200 |
| F4/80 | APC-Cy7 | BM8 | Macrophages | 1:100 |
| Ly6G | PE-Cy7 | 1A8 | Neutrophils (exclude) | 1:200 |
| Ly6C | FITC | HK1.4 | Monocyte subsets | 1:200 |
| CD86 | PE | GL-1 | M1-like marker | 1:100 |
| CD206 (MMR) | APC | C068C2 | M2-like marker | 1:100 |
| MHC-II | PerCP-Cy5.5 | M5/114.15.2 | Antigen presentation | 1:200 |
| CD64 | BV410 | X54-5/7.1 | Macrophage vs monocyte | 1:100 |
| TIM4 | BV711 | RMT4-54 | Kupffer cells | 1:100 |
| CD11c | BV785 | N418 | Dendritic cells / KCs | 1:200 |

## 7.4 Staining Procedure

1. **Fc block:** Add anti-CD16/32 antibody (clone 93), 1:100 in PBS + 2% FBS, 10 min on ice.
2. **Live/Dead stain:** Add Zombie NIR, incubate 15 min on ice, protected from light.
3. **Wash** with PBS + 2% FBS.
4. **Surface antibody cocktail:** Add all surface antibodies in 100 uL staining buffer. Incubate 30 min on ice, protected from light.
5. **Wash** 2x with PBS + 2% FBS.
6. **Fix** with 1% PFA in PBS (if not proceeding to intracellular staining).
7. Acquire on flow cytometer (BD LSRFortessa, Cytek Aurora, or equivalent). Collect minimum 500,000 CD45+ events per sample.

## 7.5 Gating Strategy

1. **Singlets:** FSC-H vs FSC-A
2. **Live cells:** Zombie NIR-negative
3. **Leukocytes:** CD45+
4. **Myeloid cells:** CD11b+
5. **Exclude neutrophils:** Ly6G-negative
6. **Macrophages:** F4/80+ CD64+
7. **Kupffer cells vs recruited:** TIM4+ CD11c+ (Kupffer cells) vs TIM4- CD11c- (monocyte-derived)
8. **M1 vs M2:** Within macrophage gate, quantify:
   - M1-like: CD86+ MHC-II-high
   - M2-like: CD206+
   - **Report M1:M2 ratio** for each subset

\begin{tip}
Run Fluorescence Minus One (FMO) controls for CD86 and CD206 to set accurate gating boundaries. These markers have continuous expression, not bimodal.
\end{tip}

\newpage

# Protocol 8: Single-Cell RNA Sequencing

## 8.1 Purpose

Profile transcriptomic states of DTCs and macrophages at single-cell resolution during each dormancy phase.

## 8.2 Sample Preparation

1. Isolate liver non-parenchymal cells (Protocol 7.2).
2. **FACS enrichment (required due to DTC rarity):**

**Sort two populations per sample:**

| Population | Sort Gate | Target Count |
|-----------|-----------|:------------:|
| DTCs | tdTomato+ / EpCAM+ / CD45- / Live | All recoverable (50-150) |
| Macrophages | CD45+ / CD11b+ / F4/80+ / Live | 5,000-10,000 |

3. **Post-sort:** Collect sorted cells into RPMI + 20% FBS on ice. Count and assess viability (>85% required).
4. **Load on 10X Chromium:** Follow manufacturer's protocol for Chromium Next GEM Single Cell 3' v3.1.
   - DTC channel: Load all sorted DTCs
   - Macrophage channel: Load 10,000 cells
5. **Sequencing target:** 50,000 reads per cell, paired-end.

## 8.3 Key Timepoints

| Day | Phase | Samples |
|-----|-------|---------|
| 7 | Entry | 3 mice per group |
| 21 | Established dormancy | 3 mice per group |
| 42 | Maintenance | 3 mice per group |

## 8.4 Basic Analysis Pipeline

1. **Cell Ranger** (10x Genomics): Demultiplex, align to mouse genome (mm10) with GFP/tdTomato transgene reference added.
2. **Quality control (Seurat v5):**
   - Remove cells with <200 genes detected
   - Remove cells with >20% mitochondrial reads
   - Remove doublets (Scrublet or DoubletFinder)
3. **Integration:** Harmony or Seurat RPCA across samples/timepoints.
4. **Clustering:** Leiden algorithm, resolution 0.5-1.0.
5. **Cell type annotation:** SingleR + manual marker verification.
6. **Dormancy scoring:** Module score for Nr2f1, Bhlhe41, Cdkn1b (p27), Cdkn1a (p21).
7. **Macrophage polarization:** Module scores for M1 genes (Nos2, Tnf, Il12b, Cxcl9, Cd86) and M2 genes (Arg1, Mrc1, Chi3l3, Retnla, Ccl17).
8. **Ligand-receptor analysis:** NicheNet or CellPhoneDB v5.0 between macrophage and DTC populations.

\begin{warning}
DTCs are extremely rare. If <30 DTCs are recovered per sample, pool 2-3 mice of the same group and timepoint (pseudobulk by group). Report the pooling strategy.
\end{warning}

\newpage

# Protocol 9: Cytokine Profiling

## 9.1 Purpose

Measure M1-associated and M2-associated cytokines in liver tissue homogenates and serum.

## 9.2 Sample Collection

**Serum:**

1. Collect 500 uL blood by retro-orbital bleed or cardiac puncture at sacrifice.
2. Allow to clot 30 min at RT. Centrifuge 2000 x g, 10 min, 4°C.
3. Collect serum. Store at -80°C.

**Liver homogenate:**

1. Weigh 100 mg snap-frozen liver tissue.
2. Homogenize in 1 mL RIPA buffer + protease inhibitor cocktail + phosphatase inhibitors using bead homogenizer (TissueLyser, Qiagen).
3. Centrifuge 14,000 x g, 15 min, 4°C. Collect supernatant.
4. Measure total protein by BCA assay. Normalize all cytokine readings to mg total protein.

## 9.3 Multiplex Panel (Luminex or MSD)

Measure the following analytes:

| Cytokine | M1/M2 Association | Relevance to Dormancy |
|----------|-------------------|-----------------------|
| IFN-gamma | M1 | Dormancy entry (p38/STAT1 axis) |
| TNF-alpha | M1 | Pro-inflammatory, NF-kB signaling |
| IL-12p70 | M1 | Th1 polarization |
| IL-10 | M2 | Immunosuppression |
| TGF-beta1 | M2 (and others) | Dormancy exit (NRP2 axis) |
| TGF-beta2 | M2 (and others) | Dormancy maintenance |
| IL-4 | M2 polarizing | M2 induction |
| IL-13 | M2 polarizing | M2 induction |
| CCL2/MCP-1 | Monocyte recruitment | Macrophage recruitment |
| CXCL10/IP-10 | M1 | T cell chemoattractant |
| CSF-1 | Macrophage survival | TAM maintenance |
| IL-6 | Pro-inflammatory | Pleiotropic |

## 9.4 Data Analysis

1. Generate standard curves per analyte using 5-parameter logistic (5PL) regression.
2. Report concentrations as pg/mg total protein (liver) or pg/mL (serum).
3. Compare across experimental groups by one-way ANOVA with Tukey post-hoc correction.
4. **Key comparison:** TGF-beta2 / TGF-beta1 ratio — should decrease with M2 impairment (Arm C).

\newpage

# Protocol 10: In Vitro Dormancy Co-Culture Validation

## 10.1 Purpose

Validate in vivo findings in a controlled system using Bone Marrow-Derived Macrophages (BMDMs) co-cultured with dormant MC38 cells.

## 10.2 BMDM Generation

1. Euthanize C57BL/6 mouse. Harvest femurs and tibiae.
2. Flush marrow with 10 mL cold PBS using 25G needle.
3. Pass through 70 um strainer. Centrifuge 300 x g, 5 min.
4. Resuspend in RBC lysis buffer, 2 min RT. Wash with PBS.
5. Culture at 1 × 10⁶ cells/mL in DMEM + 10% FBS + 20 ng/mL M-CSF (recombinant mouse, PeproTech 315-02) on non-tissue-culture-treated Petri dishes.
6. Incubate 37°C, 5% CO2 for 7 days. Add fresh M-CSF on Day 4.
7. Day 7: Verify >90% F4/80+ by flow cytometry. Harvest with cell scraper.

## 10.3 Macrophage Polarization

| Phenotype | Stimulus | Concentration | Duration |
|-----------|----------|---------------|----------|
| M1 (classically activated) | LPS + IFN-gamma | 100 ng/mL + 20 ng/mL | 24 h |
| M2 (alternatively activated) | IL-4 + IL-13 | 20 ng/mL + 20 ng/mL | 24 h |
| M0 (unpolarized) | M-CSF only | 20 ng/mL | continued |

## 10.4 Dormancy Induction in MC38

1. Seed MC38-Fucci2a cells at 5 × 10⁴ per well in 24-well plate.
2. Induce dormancy: culture in DMEM + 0.5% FBS + 5 ng/mL TGF-beta1 for 72 h.
3. **Verify dormancy:** >80% Fucci-red (G1), Ki67-negative, p27-high by flow cytometry.

## 10.5 Co-Culture Setup

1. Plate 1 × 10⁵ polarized BMDMs in lower chamber of 24-well transwell plate (0.4 um pore).
2. Plate 5 × 10⁴ dormant MC38-Fucci2a cells in transwell insert (0.4 um pore allows soluble factor exchange, no direct contact).
3. **Co-culture conditions (n=4 per condition):**

| Condition | Lower chamber | Insert | Purpose |
|-----------|--------------|--------|---------|
| M1 co-culture | M1 BMDMs | Dormant MC38 | Does M1 maintain dormancy? |
| M2 co-culture | M2 BMDMs | Dormant MC38 | Does M2 promote exit? |
| M0 co-culture | M0 BMDMs | Dormant MC38 | Unpolarized control |
| No macrophages | Media only | Dormant MC38 | Baseline |

4. **Readouts at 24, 48, 72 h:**
   - MC38 proliferation: EdU incorporation (Click-iT EdU Alexa Fluor 647, ThermoFisher)
   - Fucci2a cell cycle: Flow cytometry for mCherry (G1) vs mVenus (S/G2/M)
   - Dormancy markers: qRT-PCR for Nr2f1, Bhlhe41, Cdkn1b
   - p-ERK/p-p38: Western blot

\newpage

# Protocol 11: Data Recording and Reporting

## 11.1 Required Records Per Mouse

Every mouse must have a record sheet containing:

| Field | Details |
|-------|---------|
| Mouse ID | Unique identifier (e.g., A1-001) |
| Genotype | Wild-type, LysM-Cre x Nos2fl/fl, etc. |
| Birth date | dd/mm/yyyy |
| Injection date | dd/mm/yyyy |
| Cell dose | Number of cells injected |
| Treatment group | Clodronate, CpG-ODN, IL-4 complex, etc. |
| Treatment start date | dd/mm/yyyy |
| BLI data | Weekly total flux (photons/sec) |
| Health observations | Daily for first 7 days, then 3x weekly |
| Sacrifice date | dd/mm/yyyy |
| Tissue allocation | Which lobes to which analysis |

## 11.2 Key Calculation Formulas

**Dormancy Entry Rate (DER):**

DER = (Ki67- NR2F1+ GFP+ cells) / (total GFP+ cells) at Day 7

**Dormancy Exit Rate (DXR):**

DXR = (DTCs exiting dormancy during observation) / (total dormant DTCs at start of observation)

**M1:M2 Ratio:**

M1:M2 = (CD86+ MHC-II-high F4/80+ cells) / (CD206+ F4/80+ cells)

**p-ERK/p-p38 Ratio:**

Ratio = (mean fluorescence intensity of p-ERK) / (mean fluorescence intensity of p-p38) per cell

\begin{tip}
Threshold: p-ERK/p-p38 < 0.5 = dormant. This threshold must be validated for MC38 cells using serum-starved (dormant) vs. log-phase (proliferating) controls.
\end{tip}

## 11.3 Statistical Tests by Comparison

| Comparison | Test | Correction |
|-----------|------|-----------|
| Dormancy fraction across groups | Fisher's exact test | Bonferroni (6 arms) |
| Time to metastasis | Kaplan-Meier + log-rank | Bonferroni |
| p-ERK/p-p38 ratio | Mann-Whitney U | Holm-Bonferroni |
| scRNA-seq DEGs | Wilcoxon rank-sum | Benjamini-Hochberg FDR |
| Cytokine levels | One-way ANOVA + Tukey | Tukey HSD |
| Longitudinal BLI | Mixed-effects model | FDR |

\newpage

# Quick Reference: Experimental Arms Summary

## Arm A — Total Macrophage Depletion

| Group | Mice | Treatment | Start |
|-------|:----:|-----------|-------|
| A1 | 15 | PBS liposomes (control) | Day 1 |
| A2 | 15 | Clodronate liposomes (early) | Day 1 |
| A3 | 15 | Clodronate liposomes (late) | Day 14 |
| A4 | 15 | Clodronate + CD169-DTR + DT | Day 14 |

## Arm B — M1 Impairment (Dormancy Entry)

| Group | Mice | Genotype/Treatment | Start |
|-------|:----:|-------------------|-------|
| B1 | 15 | LysM-Cre x Nos2fl/fl | Genetic |
| B2 | 15 | LysM-Cre (Cre control) | Genetic |
| B3 | 15 | Nos2fl/fl (no Cre control) | Genetic |
| B4 | 15 | Anti-IFN-gamma Ab | Day -1 |
| B5 | 15 | Isotype control Ab | Day -1 |
| B6 | 10 | Anti-IFN-gamma Ab (late) | Day 7 |
| B7 | 10 | Isotype control Ab (late) | Day 7 |

## Arm C — M2 Impairment (Dormancy Maintenance)

| Group | Mice | Genotype/Treatment | Start |
|-------|:----:|-------------------|-------|
| C1 | 15 | LysM-Cre x Arg1fl/fl | Genetic |
| C2 | 15 | LysM-Cre (Cre control) | Genetic |
| C3 | 15 | Anti-IL-4Ralpha Ab | Day 14 |
| C4 | 15 | Isotype control Ab | Day 14 |
| C5 | 15 | CD169-DTR + DT | Day 14 |
| C6 | 15 | Cx3cr1-CreERT2 x DTA + tamoxifen | Day 14 |

## Arm D — Temporal Switch (M2 -> M1)

| Group | Mice | Treatment | Timing |
|-------|:----:|-----------|--------|
| D1 | 15 | IL-4 complex -> IFN-gamma + LPS | Days 1-28 -> Days 28-42 |
| D2 | 15 | IL-4 complex (sustained) | Days 1-42 |
| D3 | 15 | IFN-gamma + poly(I:C) (sustained) | Days 1-42 |
| D4 | 15 | PBS vehicle | Days 1-42 |
| D5 | 15 | IL-4 complex -> IFN-gamma + anti-PD-1 | Days 1-28 -> Days 28-42 |
| D6 | 15 | PI3K-gamma inhibitor (eganelisib) | Days 28-42 |

\newpage

# Appendix A: Master Acronym Glossary

| Acronym | Full Term |
|---------|-----------|
| AIW | Abdominal Imaging Window |
| ARG1 | Arginase 1 |
| BLI | Bioluminescence Imaging |
| BMDM | Bone Marrow-Derived Macrophage |
| BSL-2 | Biosafety Level 2 |
| CRC | Colorectal Cancer |
| CRLM | Colorectal Liver Metastasis |
| CSF1R | Colony Stimulating Factor 1 Receptor |
| CX3CR1 | C-X3-C Motif Chemokine Receptor 1 |
| DER | Dormancy Entry Rate |
| DMD | Dormancy Maintenance Duration |
| DT | Diphtheria Toxin |
| DTC | Disseminated Tumor Cell |
| DTR | Diphtheria Toxin Receptor |
| DXR | Dormancy Exit Rate |
| EGFP | Enhanced Green Fluorescent Protein |
| EpCAM | Epithelial Cell Adhesion Molecule |
| ERK | Extracellular Signal-Regulated Kinase |
| FACS | Fluorescence-Activated Cell Sorting |
| FBS | Fetal Bovine Serum |
| FDR | False Discovery Rate |
| Fucci2a | Fluorescent Ubiquitination-based Cell Cycle Indicator 2a |
| GFP | Green Fluorescent Protein |
| GJIC | Gap Junctional Intercellular Communication |
| HSC | Hepatic Stellate Cell |
| IF | Immunofluorescence |
| IFN-gamma | Interferon gamma |
| IL | Interleukin |
| iNOS | Inducible Nitric Oxide Synthase (NOS2) |
| IP | Intraperitoneal |
| IV | Intravenous |
| KC | Kupffer Cell |
| LPS | Lipopolysaccharide |
| LysM | Lysozyme M |
| M-CSF | Macrophage Colony-Stimulating Factor |
| MHC | Major Histocompatibility Complex |
| MMP | Matrix Metalloproteinase |
| MOI | Multiplicity of Infection |
| NOS2 | Nitric Oxide Synthase 2 (iNOS) |
| NR2F1 | Nuclear Receptor Subfamily 2 Group F Member 1 |
| NRP2 | Neuropilin 2 |
| p-ERK | Phospho-Extracellular Signal-Regulated Kinase |
| p-p38 | Phospho-p38 |
| PD-1 | Programmed Cell Death Protein 1 |
| PDO | Patient-Derived Organoid |
| PI3K-gamma | Phosphoinositide 3-Kinase Gamma |
| RT | Room Temperature |
| SC | Subcutaneous |
| scRNA-seq | Single-Cell RNA Sequencing |
| STAT1 | Signal Transducer and Activator of Transcription 1 |
| TAM | Tumor-Associated Macrophage |
| TGF-beta | Transforming Growth Factor Beta |
| TLR | Toll-Like Receptor |

\newpage

# Appendix B: Reagent and Vendor List

| Reagent | Vendor | Catalog # | Notes |
|---------|--------|-----------|-------|
| Clodronate liposomes | Liposoma BV | CP-005-005 | Store 4°C, do NOT freeze |
| PBS liposomes | Liposoma BV | PB-005-005 | Control |
| CpG-ODN 1826 | InvivoGen | tlrl-1826 | 1 mg/mL in endotoxin-free H2O |
| Recombinant mouse IL-4 | BioLegend | 574302 | Aliquot, store -80°C |
| Anti-IL-4 Ab (clone 11B11) | BioLegend | 504111 | For IL-4 complex |
| Anti-IFN-gamma (clone XMG1.2) | Bio X Cell | BP0055 | In vivo grade |
| Anti-IL-4Ralpha (clone M1) | Bio X Cell | -- | In vivo grade |
| Isotype control (rat IgG1) | Bio X Cell | BP0088 | Control for XMG1.2 |
| D-Luciferin potassium salt | GoldBio | LUCK-1G | 15 mg/mL in PBS |
| Diphtheria toxin | Sigma | D0564 | EXTREMELY toxic |
| Pexidartinib (PLX3397) | Selleckchem | S7818 | PI3K-gamma inhibitor |
| Collagenase IV | Worthington | LS004188 | Liver digestion |
| DNase I | Roche | 10104159001 | Liver digestion |
| Percoll | Cytiva | 17-0891-01 | 40%/70% gradient |
| Zombie NIR viability dye | BioLegend | 423105 | Live/Dead for flow |
| Anti-CD16/32 (clone 93) | BioLegend | 101319 | Fc block |
| Opal 7-plex kit | Akoya | NEL811001KT | Multiplex IF |
| Buprenorphine | Patterson Veterinary | 07-890-6657 | Analgesia |
| Isoflurane | VetOne | 501017 | Anesthesia |

\newpage

# Appendix C: Troubleshooting Guide

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| Low DTC yield at Day 7 | Injection technique (backflow), cell viability | Practice slow injection (30 sec); verify >95% viability; try portal vein injection instead |
| No BLI signal | Luciferase reporter loss, insufficient cells | Re-check GFP expression before injection; increase cell dose in pilot |
| Clodronate depletion <70% | IV injection failure (tail vein misses) | Switch to IP route, 3x weekly; verify technique with trypan blue test injection |
| High background in IF | Incomplete stripping between Opal rounds | Extend microwave time to 25 min; verify stripping with secondary-only control |
| Low macrophage yield from liver | Incomplete digestion, hepatocyte contamination | Increase collagenase IV to 0.1%; ensure hepatocyte spin (50 x g) removes parenchymal cells |
| Fucci2a signal lost | Transgene silencing | Re-sort for Fucci-positive cells; use early passage cells (<P20 post-engineering) |
| DT toxicity in CD169-DTR mice | Overdosing | Confirm dose calculation; never exceed 10 ng/g; use wild-type + DT controls |
| Poor scRNA-seq viability | Processing delay, mechanical stress | Process within 30 min; use gentle pipetting; keep cold; add 0.04% BSA to PBS |
| Variable BLI between mice | Inconsistent luciferin timing | Standardize: always image at exactly 10 min post-luciferin injection; same person injects and times |
| M1:M2 ratio doesn't shift with CpG/IL-4 | Dose insufficient, mouse strain background | Titrate CpG up to 100 ug; verify IL-4 complex formation (37°C, 30 min pre-incubation) |
