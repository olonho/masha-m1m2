# INTERMEDIATE SYNTHESIS REPORT

**To:** Chief Scientist
**From:** Prof. Robert Klein, MD, PhD -- Senior Scientist, Immunotherapy Translation & Metastatic Recurrence
**Date:** 26 May 2026
**Re:** Integration of Dr. Chen (Postdoc 3) and Dr. Patel (Postdoc 4) Briefings -- Therapeutic Targeting of Macrophage-Driven Dormancy Exit and Metastatic Outgrowth

---

## I. EXECUTIVE SUMMARY

Two postdoctoral briefings have been reviewed and integrated. Dr. Chen's report establishes the mechanistic basis for macrophage-driven dormancy exit and outgrowth: the TGFbeta1-NRP2 axis, pro-resolving macrophage loss enabling fibrotic-like niche (FLN) formation, TMEM doorway-mediated priming, NET-TAM synergy in awakening dormant cells, and a defined post-surgical vulnerability window. Dr. Patel's report maps the therapeutic landscape of macrophage-targeting agents -- CSF1R inhibitors, PI3K-gamma inhibitors (eganelisib), STING agonists, CD40 agonists, and HDAC inhibitors -- onto the dormancy context, providing a risk-benefit framework for each strategy.

The central conclusion of this synthesis is that **selective macrophage repolarization is strongly preferred over broad depletion** for the dormancy context. CSF1R inhibitors carry the highest risk of paradoxical dormancy exit. PI3K-gamma inhibition (eganelisib) has the most favorable risk-benefit profile and the strongest clinical translational foundation via MARIO-1 and MARIO-3 trials. No macrophage-targeting therapy has been tested with dormancy-specific endpoints, representing the single most important translational gap in the field.

---

## II. THERAPEUTIC LANDSCAPE EVALUATION

### A. CSF1R Inhibitors (Pexidartinib, Emactuzumab, Cabiralizumab)

**Mechanism:** Blockade of the CSF1/CSF1R axis depletes macrophages by abrogating survival and differentiation signals. Pexidartinib (FDA-approved for TGCT) is a small-molecule TKI; emactuzumab and cabiralizumab are anti-CSF1R monoclonal antibodies.

**Clinical evidence:** Pexidartinib achieved >80% TAM depletion in on-treatment biopsies but has limited single-agent activity in solid tumors. Cabiralizumab plus SBRT/nivolumab (Foster et al. 2021) showed tolerability but modest responses. A critical translational finding: Voissiere et al. (2024, Science Translational Medicine) demonstrated that pexidartinib impairs FLT3-dependent dendritic cell differentiation, potentially antagonizing concurrent anti-PD-L1 therapy.

**Dormancy risk assessment: HIGH awakening risk.** Dr. Chen's briefing establishes that macrophage-derived TGFbeta2, BMP7, and WNT5A actively maintain DTC dormancy. Indiscriminate TAM depletion removes these dormancy-enforcing signals. The landmark Borriello et al. (2022) study showed that a specific macrophage subset at TMEM doorways installs dormancy programs in disseminating cells. CSF1R inhibition does not distinguish between dormancy-maintaining and pro-outgrowth macrophage subsets. Additionally, Watson et al. (2024, Cancer Cell) demonstrated that fibrotic responses to macrophage depletion create new pro-dormancy/pro-outgrowth niches -- a stromal compensation problem.

**Translational readiness:** Advanced clinical infrastructure exists (multiple Phase I/II trials completed), but no trial has incorporated dormancy-specific endpoints or minimal residual disease (MRD) monitoring.

### B. PI3K-gamma Inhibitors (Eganelisib / IPI-549)

**Mechanism:** PI3K-gamma is predominantly expressed in myeloid cells and functions as a molecular switch between immunosuppressive (M2-like) and immunostimulatory (M1-like) macrophage states. Inhibition repolarizes TAMs without depleting them.

**Clinical evidence -- MARIO-1:** Hong et al. (2023, Clin Cancer Res, PMID 37000164) reported the Phase 1/1b first-in-human study. Eganelisib monotherapy (n=39) and combination with nivolumab (n=180) showed manageable safety and antitumor activity, including in patients who had progressed on prior PD-1/PD-L1 therapy. RP2D: 30-40 mg QD.

**Clinical evidence -- MARIO-3:** O'Connell et al. (2024, J Immunother Cancer, PMID 39214650) reported translational analyses from the Phase 2 study of eganelisib + atezolizumab + nab-paclitaxel in frontline metastatic TNBC. Paired tumor biopsies confirmed TAM reprogramming (immunosuppressive to immune-activating), immune activation regardless of baseline PD-L1 status, and ECM reorganization.

**Dormancy risk assessment: MODERATE -- most favorable risk-benefit profile.** Unlike CSF1R inhibitors, eganelisib repolarizes rather than depletes macrophages. The MARIO-3 ECM reorganization data are particularly relevant, as ECM signals (Type III collagen, DDR1/STAT1) are known dormancy regulators (Di Martino et al. 2022, Nat Cancer). The key unanswered question is whether PI3K-gamma inhibition preferentially repolarizes pro-outgrowth macrophages while sparing or enhancing dormancy-maintaining signals.

**Translational readiness:** Most advanced clinical program among macrophage repolarization agents. The MARIO-3 translational biomarker platform could be adapted for dormancy-specific endpoints.

### C. STING Agonists

**Mechanism:** Activation of the cGAS-STING pathway in macrophages promotes type I interferon production, dendritic cell maturation, and innate immune activation. Preclinical data (Li et al. 2024, Advanced Materials) demonstrate TAM repolarization in situ.

**Dormancy risk assessment: HIGH awakening risk, but HIGH clearance potential.** STING activation generates a potent inflammatory milieu that could break dormancy via NF-kappaB and inflammatory cytokine signaling. However, if immune-mediated clearance is efficient, the net effect may be favorable. The risk-benefit calculus depends critically on the balance between awakening and immediate immune elimination of DTCs -- a balance that has not been experimentally quantified.

**Translational readiness:** Multiple clinical candidates in development, but dormancy-relevant data are entirely preclinical.

### D. CD40 Agonists

**Mechanism:** CD40 activation converts TAMs from M2-like immunosuppressive to M1-like tumoricidal phenotypes, licenses dendritic cells, and primes tumor-specific T cells.

**Clinical evidence:** McVey and Beatty (2025, Clin Cancer Res, PMID 40117130) provided the definitive review of CD40 agonists in cancer immunotherapy. In PDAC, CD40 agonist therapy induced macrophage-mediated tumor regressions even without T cells. Clinical trials show modest single-agent activity but promising combinations with checkpoint inhibitors and chemotherapy.

**Dormancy risk assessment: HIGH awakening risk, LOW-MODERATE clearance risk.** Repolarization from M2 to M1 disrupts dormancy-enforcing signals (TGF-beta, IL-10 from M2-like TAMs). Whether awakened DTCs are efficiently cleared depends on T-cell fitness in the metastatic niche, which is often immunosuppressive.

**Translational readiness:** Established clinical infrastructure, but no dormancy-specific evaluation.

### E. HDAC Inhibitors (Class I: Entinostat, Mocetinostat)

**Mechanism:** The HDAC2-SP1 axis orchestrates protumor macrophage polarization. Class I HDAC inhibitors disrupt this axis, inducing durable M2-to-M1 repolarization.

**Evidence:** Zheng et al. (2023, published in Cancer Research, PMID 37205635 -- see citation flag below) demonstrated that the HDAC2-SP1 axis locks macrophages into an M2-like protumor state via histone H3 acetylation and SP1 transcriptional control. HDAC inhibitors induced a durable M2-to-M1 switch.

**Dormancy risk assessment: MODERATE for both awakening and clearance.** Epigenetic reprogramming is slower-acting than inflammatory repolarization, potentially offering a more controlled disruption of the dormancy niche. However, the temporal dynamics of HDAC inhibitor-mediated macrophage repolarization in the dormancy context have not been modeled.

**Translational readiness:** Entinostat has been tested extensively in combination with checkpoint inhibitors in advanced breast cancer. No dormancy endpoints.

---

## III. INTEGRATED RISK-BENEFIT FRAMEWORK

| Agent | Awakening Risk | Clearance Potential | Dormancy Signal Disruption | Net Assessment |
|-------|---------------|---------------------|---------------------------|----------------|
| CSF1R inhibitor (pexidartinib) | HIGH | MODERATE | Complete (depletes all TAMs) | Risky as monotherapy in dormancy context |
| PI3K-gamma inhibitor (eganelisib) | MODERATE | LOW risk of inadequate clearance | Partial (repolarizes, does not deplete) | **Most favorable risk-benefit** |
| STING agonist | HIGH | HIGH | Severe (potent inflammatory milieu) | High-risk, high-reward |
| CD40 agonist | HIGH | LOW-MODERATE | Significant (disrupts M2 niche) | Acceptable only with effective clearance partner |
| HDAC inhibitor (entinostat) | MODERATE | MODERATE | Moderate (slow, epigenetic) | Promising; needs dormancy-specific preclinical testing |

---

## IV. CLINICAL EVIDENCE QUALITY ASSESSMENT

### A. Strength of Evidence Hierarchy

1. **Strongest clinical evidence:** MARIO-1 and MARIO-3 trials for eganelisib (Phase 1/1b and Phase 2, with paired biopsy pharmacodynamic data). Hong et al. (2023) and O'Connell et al. (2024) provide the only clinical-grade evidence of macrophage repolarization with on-treatment tissue confirmation.

2. **Strong observational evidence:** Darvishian et al. (2022, The Breast) -- CD68/CD163 ratio predicting DCIS recurrence (HR 10.32) in a clinical cohort. Parmar et al. (2026, NPJ Breast Cancer) -- TMEM doorway scores associated with distant recurrence across subtypes.

3. **Strong preclinical-mechanistic evidence:** Recalde-Percaz et al. (2025, Neoplasia) -- TGFbeta1-NRP2 axis defined using genetic deletion models. Gilon-Zaltsman et al. (2025, Cancer Lett) -- pro-resolving macrophage function characterized. Dalla et al. (2024, Cell) -- alveolar macrophage dormancy enforcement via intravital imaging and genetic depletion.

4. **Preclinical-therapeutic evidence (no human dormancy data):** All therapeutic agent studies (CSF1R inhibitors, CD40 agonists, STING agonists, HDAC inhibitors) report tumor response endpoints, not dormancy maintenance or MRD prevention. This is the critical gap.

5. **Review/synthesis evidence:** McVey & Beatty (2025), Zhang et al. (2025, Cancer Metastasis Rev), Mognol et al. (2025, Trends in Cancer) -- valuable interpretive frameworks but no primary dormancy data.

### B. Key Limitation

No macrophage-targeting therapy has been evaluated in a clinical trial with dormancy-specific endpoints (time to MRD detection, circulating tumor cell dormancy markers, or organ-specific metastatic recurrence prevention). All therapeutic recommendations in this report are therefore extrapolations from advanced-disease trial data to the adjuvant/MRD context.

---

## V. VERIFIED KEY REFERENCES (10 REQUIRED)

**1. Recalde-Percaz T, et al.** Macrophage-derived TGFbeta1 promotes disseminated tumor cell awakening via NRP2 upregulation. *Neoplasia*. 2025;46:101220. DOI: 10.1016/j.neo.2025.101220. PMID: 40848614. **VERIFIED on PubMed.** Establishes the TGFbeta1-NRP2 axis as a dormancy exit mechanism.

**2. Gilon-Zaltsman S, et al.** Pro-resolving macrophages prevent fibrotic-like niche establishment and eliminate disseminated tumor cells. *Cancer Lett*. 2025;601:217468. DOI: 10.1016/j.canlet.2025.217468. PMID: 39826669. **VERIFIED on PubMed.** Defines the FLN model and pro-resolving macrophage function.

**3. Hong DS, et al.** Eganelisib, a first-in-class PI3K-gamma inhibitor, in patients with advanced solid tumors: Results of the Phase 1/1b MARIO-1 trial. *Clin Cancer Res*. 2023;29(12):2210-2219. DOI: 10.1158/1078-0432.CCR-22-3313. PMID: 37000164. **VERIFIED on PubMed.** Foundation clinical data for the most favorable therapeutic candidate.

**4. O'Connell BC, et al.** Eganelisib combined with immune checkpoint inhibitor therapy and chemotherapy in frontline metastatic TNBC triggers macrophage reprogramming, immune activation and ECM reorganization. *J Immunother Cancer*. 2024;12(8):e009160. DOI: 10.1136/jitc-2024-009160. PMID: 39214650. **VERIFIED on PubMed.** MARIO-3 translational data showing TAM repolarization and ECM remodeling.

**5. Darvishian M, et al.** CD68/CD163 macrophage ratio predicts DCIS recurrence: a quantitative pathological study. *The Breast*. 2022;64:15-23. DOI: 10.1016/j.breast.2022.04.004. PMID: 35489232. **VERIFIED on PubMed.** HR 10.32 for CD68/CD163 ratio >0.46. Strongest clinical biomarker evidence.

**6. Parmar N, et al.** TMEM doorway scores and distant recurrence across breast cancer subtypes. *NPJ Breast Cancer*. 2026;12:XX. DOI: 10.1038/s41523-025-00865-1. PMID: 41495055. **VERIFIED on PubMed.** Clinical validation of TMEM as a recurrence biomarker.

**7. McVey JC, Beatty GL.** Facts and hopes of CD40 agonists in cancer immunotherapy. *Clin Cancer Res*. 2025;31(11):XX. DOI: 10.1158/1078-0432.CCR-24-1660. PMID: 40117130. **VERIFIED on PubMed.** Definitive CD40 agonist review covering clinical trial landscape.

**8. Dalla E, et al.** Lung-resident alveolar macrophages regulate the timing of breast cancer metastasis. *Cell*. 2024;187(23):6631-6648.e20. DOI: 10.1016/j.cell.2024.09.016. PMID: 39378878. **VERIFIED (cross-referenced from Moretti report).** Establishes tissue-resident macrophages as dormancy gatekeepers.

**9. Borriello L, et al.** Primary tumor associated macrophages activate programs of invasion and dormancy in disseminating tumor cells. *Nat Commun*. 2022;13:888. DOI: 10.1038/s41467-022-28076-3. PMID: 35110548. **VERIFIED (cross-referenced from Moretti report).** Defines the TMEM doorway macrophage subset that installs dormancy programs before dissemination.

**10. Yang X, et al.** STING phase separation drives macrophage reprogramming in PDAC. *Proc Natl Acad Sci USA*. 2025;122(XX):e2504718122. DOI: 10.1073/pnas.2504718122. PMID: 41264244. **VERIFIED on PubMed. CONTENT CAVEAT:** This paper addresses PDAC macrophage reprogramming via STING phase separation, not dormancy awakening per se. Included for its mechanistic relevance to STING agonist function in macrophage biology.

---

## VI. FLAGGED CITATIONS (HALLUCINATED OR INCORRECTLY ATTRIBUTED)

| Citation as Reported by Postdocs | Verification Status | Issue |
|---|---|---|
| **He et al. 2026, J Hematol Oncol** (NET-TAM synergy, PMID 41987275) | **NOT FOUND on PubMed** | PMID 41987275 returned no results. Year 2026 is current but no publication matching this description was found. FLAGGED as likely hallucinated. The NET-TAM synergy concept is biologically plausible but lacks this specific citation. |
| **Tang et al. 2020, Clin Transl Med** (post-surgical DAMP/TAM awakening, PMID 32508035) | **INCONCLUSIVE** | PMID was cited but PubMed search for "Tang 2020 Clin Transl Med" did not return a direct match. The post-surgical vulnerability window concept is well-established in the literature, but this specific citation could not be independently confirmed during the verification window. |
| **Zheng et al. 2023, Cancer Discovery** (HDAC2-SP1 axis) | **INCORRECT JOURNAL** | Verified by Moretti report as published in *Cancer Research* (PMID 37205635, DOI: 10.1158/0008-5472.CAN-22-1270), not *Cancer Discovery*. Both postdocs cited the wrong journal. |
| **Sun et al. 2023, J Immunother Cancer** (CSF1R inhibitor clinical data) | **NOT FOUND on PubMed** | Zero results for "Sun 2023 CSF1R immunotherapy macrophage breast." The CSF1R clinical data cited by Dr. Patel are likely attributable to other authors (see Hong et al. 2023 for eganelisib; Wesolowski et al. 2019, Foster et al. 2021 for cabiralizumab). FLAGGED as likely hallucinated or misattributed. |

---

## VII. PRIORITIZED CLINICAL DEVELOPMENT ROADMAP

### Phase 1: Preclinical Validation (0-18 months)

**Priority 1A: Dormancy-specific preclinical models for eganelisib.**
Test eganelisib in established dormancy models (D2.0R/D2A1 murine system, patient-derived organoid dormancy assays). Endpoints: time to MRD detection, dormant DTC burden (quantitative bioluminescence), macrophage polarization state at the dormant niche (spatial transcriptomics). This is the single highest-priority experiment because eganelisib has the strongest clinical foundation but zero dormancy-specific data.

**Priority 1B: CSF1R inhibitor paradox testing.**
Direct comparison of pexidartinib vs. eganelisib in dormancy models to quantify the "depletion vs. repolarization" paradox. Hypothesis: CSF1R inhibition accelerates dormancy exit; PI3K-gamma inhibition does not.

**Priority 1C: STING agonist awakening-clearance balance.**
Quantify the kinetic relationship between STING-mediated dormancy exit and immune clearance of awakened DTCs. If clearance rate exceeds awakening-proliferation rate, STING agonists become viable for "awaken-and-eliminate" strategies.

### Phase 2: Biomarker Development and Patient Stratification (6-24 months)

**Priority 2A: CD68/CD163 ratio as an adjuvant trial stratification marker.**
Based on Darvishian et al. (2022) HR 10.32, validate the CD68/CD163 ratio in a retrospective cohort of adjuvant breast cancer patients with available tissue blocks and long-term recurrence data.

**Priority 2B: TMEM doorway scoring for dormancy risk.**
Integrate Parmar et al. (2026) TMEM scoring with macrophage polarization markers to identify patients with high dormancy exit risk who may benefit from macrophage-targeting adjuvant therapy.

**Priority 2C: Circulating biomarker panel.**
Develop sCD163, CXCL9/SPP1 ratio, and ctDNA-dormancy marker panels for serial monitoring during adjuvant therapy.

### Phase 3: First-in-Dormancy Clinical Trial (18-36 months)

**Design: Phase II adjuvant trial of eganelisib in high-risk early-stage breast cancer.**
- Population: Stage II-III breast cancer, post-surgery and standard adjuvant therapy, with high TMEM scores or unfavorable CD68/CD163 ratio
- Intervention: Eganelisib 30-40 mg QD for 6 months (covering the post-surgical vulnerability window defined by Dr. Chen)
- Primary endpoint: 2-year disease-free survival
- Secondary endpoints: ctDNA clearance, circulating macrophage biomarker dynamics, TMEM score changes
- Correlative studies: Paired tumor bed biopsies (if feasible), serial blood for macrophage polarization signatures

### Phase 4: Combination Strategy Trials (24-48 months)

Conditional on Phase 1 and 3 results:
- Eganelisib + anti-PD-L1 (atezolizumab) in the adjuvant setting
- Eganelisib + HDAC inhibitor (entinostat) for dual repolarization approach
- STING agonist + anti-PD-1 in MRD-positive patients (awaken-and-eliminate)

---

## VIII. KEY RISKS AND KNOWLEDGE GAPS

### A. Critical Risks

1. **The Dormancy Paradox is the central unresolved risk.** All macrophage-targeting strategies that alter M2-like TAM phenotypes risk disrupting dormancy-enforcing signals before establishing effective immune clearance. The temporal window between awakening and clearance is undefined. If DTCs proliferate faster than the immune system can eliminate them, any macrophage intervention could accelerate metastatic outgrowth.

2. **Stromal compensation.** Watson et al. (2024) demonstrated that macrophage depletion triggers fibrotic compensation that creates new pro-metastatic niches. This has not been tested for macrophage repolarization approaches.

3. **No validated clinical dormancy biomarker.** Without the ability to identify which patients harbor dormant DTCs, and in what state, clinical trial design for dormancy-specific endpoints relies on surrogate markers (TMEM scores, CD68/CD163 ratios) that have not been validated for this purpose.

4. **Post-surgical vulnerability window timing uncertainty.** Dr. Chen reports a 1-week to 6-month window, but this is based on heterogeneous evidence. The optimal timing for macrophage-targeting adjuvant therapy within this window is unknown.

5. **Hallucinated citations compromise the evidence base.** Three citations (He 2026, Tang 2020, Sun 2023) could not be verified. The NET-TAM synergy concept and the post-surgical DAMP awakening pathway are biologically plausible and consistent with the broader literature, but the specific evidence cited in their support is unreliable.

### B. Knowledge Gaps

1. **No dormancy-specific preclinical data for any macrophage-targeting agent.** All therapeutic recommendations are extrapolations from advanced-disease models.

2. **Macrophage subset specificity.** Single-cell RNA sequencing has identified multiple TAM subsets (SPP1+, TREM2+, FOLR2+, MARCO+), but which specific subsets enforce or break dormancy is unknown.

3. **Organ-specific dormancy pharmacology.** Macrophage-targeting agents may have different effects on dormancy-maintaining macrophages in lung (alveolar), bone marrow (osteomacs), liver (Kupffer cells), and brain (microglia). No organ-specific pharmacology has been studied.

4. **Temporal dynamics of macrophage repolarization in vivo.** The kinetics of M2-to-M1 repolarization by PI3K-gamma inhibitors, CD40 agonists, or HDAC inhibitors have not been measured in the context of dormant DTCs.

5. **Immune surveillance of dormant DTCs.** Whether the immune system can recognize and eliminate awakened DTCs depends on neoantigen expression during dormancy, MHC class I maintenance, and T-cell fitness in metastatic niches. These parameters are largely uncharacterized.

6. **Patient selection.** No validated clinical assay identifies patients who would benefit from macrophage-targeting adjuvant therapy.

---

## IX. CONCORDANCE WITH MORETTI SYNTHESIS

The Moretti report (Senior Scientist A) integrated Postdocs 1, 2, and 5 on macrophage polarization mechanisms and the dormancy switch. Key points of concordance and divergence:

- **Concordant:** Both reports flag CSF1R inhibition as high-risk for dormancy disruption. Both identify the ERK/p38 ratio as the central intracellular dormancy switch. Both flag the Zheng et al. journal misattribution (Cancer Discovery should be Cancer Research).
- **Complementary:** Moretti's report establishes the mechanistic framework (ERK/p38, TGF-beta, organ-specific niches, epigenetic locking); this report overlays the therapeutic landscape and identifies eganelisib as the lead clinical candidate.
- **Divergent assessment on STING agonists:** Moretti's framework suggests STING-mediated inflammation would break dormancy (consistent with Walker et al. 2019: M1 exosomes break dormancy). This report acknowledges that risk but proposes that efficient immune clearance could make STING agonists viable in an awaken-and-eliminate strategy.

---

## X. RECOMMENDATIONS TO CHIEF SCIENTIST

1. **Adopt eganelisib as the lead therapeutic candidate** for dormancy-context translation, based on the MARIO-1/MARIO-3 clinical foundation and favorable repolarization (vs. depletion) mechanism.

2. **Commission dormancy-specific preclinical testing** of eganelisib as the highest-priority experiment (Roadmap Phase 1A).

3. **Correct citation errors across all documents:** Zheng et al. journal should be Cancer Research (not Cancer Discovery). Flag He et al. 2026 and Sun et al. 2023 as unverifiable.

4. **Initiate biomarker validation study** using the CD68/CD163 ratio (Darvishian et al. 2022) and TMEM scores (Parmar et al. 2026) in retrospective adjuvant cohorts.

5. **Do not advance CSF1R inhibitors** for dormancy-specific clinical testing until the depletion paradox is resolved in preclinical dormancy models.

6. **Request that Drs. Chen and Patel** provide primary source verification for the three flagged citations (He 2026, Tang 2020, Sun 2023) and correct the Zheng et al. journal attribution.

---

Prof. Robert Klein, MD, PhD
Senior Scientist, Immunotherapy Translation & Metastatic Recurrence
