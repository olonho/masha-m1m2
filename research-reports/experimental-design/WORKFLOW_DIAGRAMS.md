# Experimental Workflow and Expected Outcome Diagrams

## Diagram 1: Overall Project Workflow

```mermaid
flowchart TD
    A["Phase 0: Cell Engineering<br/>(Weeks 1–4)"] --> B["Phase 0: Mouse Breeding<br/>(Weeks 1–6)"]
    A --> C["Phase 0: Dose Pilot<br/>(Week 5)"]

    C -->|Optimal dormancy dose determined| D["Phase I: Arm A<br/>Total Macrophage Depletion<br/>(Weeks 7–14)"]
    B --> D

    D -->|Confirm macrophages required| E["Phase II: Arm B<br/>M1 Impairment<br/>(Weeks 8–16)"]
    D -->|Confirm macrophages required| F["Phase II: Arm C<br/>M2 Impairment<br/>(Weeks 8–16)"]

    E -->|M1 entry contribution quantified| G["Phase III: Arm D<br/>Temporal Switch<br/>(Weeks 10–18)"]
    F -->|M2 maintenance contribution quantified| G

    G -->|Switch kinetics measured| H["Phase IV: Analysis<br/>(Weeks 18–24)"]

    H --> I["scRNA-seq &<br/>Spatial Transcriptomics"]
    H --> J["Statistical Analysis<br/>& Model Validation"]
    H --> K["Manuscript<br/>Preparation"]

    J -->|Key decision| L{Both M1 and M2<br/>contribute?}

    L -->|Yes – confirms model| M["Proceed to therapeutic<br/>testing (Arm D5 strategy)"]
    L -->|Only M2 matters| N["Revise model: focus on<br/>M2-targeted maintenance"]
    L -->|Only M1 matters| O["Revise model: focus on<br/>IFN-γ/p38 dormancy entry"]
    L -->|Neither alone| P["Macrophage contribution<br/>is non-specific"]

    style A fill:#e1f5fe
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#e8f5e9
    style G fill:#f3e5f5
    style H fill:#e0f2f1
    style M fill:#c8e6c9
    style N fill:#ffccbc
    style O fill:#ffccbc
    style P fill:#ffccbc
```

---

## Diagram 2: Intrasplenic Injection and Dormancy Timeline

```mermaid
flowchart LR
    subgraph Surgery["Day 0: Surgery"]
        S1["Anesthetize mouse<br/>(isoflurane 3%)"]
        S2["Left flank incision"]
        S3["Inject 1×10³ MC38-GFP-Luc<br/>into spleen (30 sec)"]
        S4["Splenectomy"]
        S5["Close & recover"]
        S1 --> S2 --> S3 --> S4 --> S5
    end

    subgraph Seeding["Days 1–3: Seeding"]
        T1["DTCs transit<br/>portal vein"]
        T2["Lodge in liver<br/>sinusoids"]
        T3["Extravasation into<br/>parenchyma"]
        T1 --> T2 --> T3
    end

    subgraph Entry["Days 3–14: Entry Phase"]
        E1["M1 macrophages encounter DTCs<br/>(IFN-γ/p38/STAT1 signaling)"]
        E2["~65% DTCs enter dormancy<br/>(NR2F1+, Ki67–)"]
        E3["~35% DTCs proliferate<br/>or are cleared"]
        E1 --> E2
        E1 --> E3
    end

    subgraph Maintenance["Days 14–84: Maintenance"]
        M1["M2-like macrophages dominate<br/>(TGF-β2, GJIC)"]
        M2["Dormant DTCs persist<br/>(stable BLI signal)"]
        M3["Variable spontaneous<br/>exit begins"]
        M1 --> M2
        M2 --> M3
    end

    subgraph Exit["Weeks 8–12: Exit Phase"]
        X1["M2 → M1 switch or<br/>inflammatory trigger"]
        X2["p-ERK/p-p38 ratio >0.5<br/>DTCs re-enter cell cycle"]
        X3["Macrometastatic<br/>outgrowth"]
        X1 --> X2 --> X3
    end

    Surgery --> Seeding --> Entry --> Maintenance --> Exit

    style Surgery fill:#e3f2fd
    style Seeding fill:#f1f8e9
    style Entry fill:#fff8e1
    style Maintenance fill:#fce4ec
    style Exit fill:#ffebee
```

---

## Diagram 3: Four Experimental Arms

```mermaid
flowchart TB
    subgraph ArmA["ARM A: Total Macrophage Depletion"]
        direction TB
        A1["PBS liposomes<br/>(Vehicle control)"]
        A2["Clodronate liposomes<br/>from Day 1<br/>(Early depletion)"]
        A3["Clodronate liposomes<br/>from Day 14<br/>(Late depletion)"]
        A4["Clodronate +<br/>CD169-DTR + DT<br/>(Kupffer-selective)"]
    end

    subgraph ArmB["ARM B: M1 Impairment"]
        direction TB
        B1["LysM-Cre × Nos2<sup>fl/fl</sup><br/>(Genetic M1 KO)"]
        B2["LysM-Cre control"]
        B3["Nos2<sup>fl/fl</sup> no-Cre control"]
        B4["Anti-IFN-γ Ab<br/>(from Day –1)"]
        B5["Isotype control"]
        B6["Anti-IFN-γ Ab<br/>(from Day 7, late)"]
    end

    subgraph ArmC["ARM C: M2 Impairment"]
        direction TB
        C1["LysM-Cre × Arg1<sup>fl/fl</sup><br/>(Genetic M2 KO)"]
        C2["LysM-Cre control"]
        C3["Anti-IL-4Rα Ab<br/>(from Day 14)"]
        C4["Isotype control"]
        C5["CD169-DTR + DT<br/>(Kupffer depletion)"]
        C6["Cx3cr1-CreERT2 × DTA<br/>(Recruited MoM depletion)"]
    end

    subgraph ArmD["ARM D: Temporal Switch (M2→M1)"]
        direction TB
        D1["IL-4 complex Days 1–28<br/>→ IFN-γ + LPS Days 28–42"]
        D2["IL-4 complex sustained<br/>(Days 1–42)"]
        D3["IFN-γ + poly(I:C)<br/>sustained (Days 1–42)"]
        D4["PBS vehicle<br/>(Days 1–42)"]
        D5["IL-4 → IFN-γ<br/>+ anti-PD-1"]
        D6["PI3K-γ inhibitor<br/>(eganelisib, Days 28–42)"]
    end

    Question["RESEARCH QUESTION"] --> ArmA
    Question --> ArmB
    Question --> ArmC
    Question --> ArmD

    Question -.->|Are macrophages<br/>required?| ArmA
    Question -.->|Are M1 macs needed<br/>for entry?| ArmB
    Question -.->|Are M2 macs needed<br/>for maintenance?| ArmC
    Question -.->|Does M2→M1 switch<br/>trigger exit?| ArmD

    style Question fill:#1a237e,color:#ffffff
    style ArmA fill:#fff3e0
    style ArmB fill:#fce4ec
    style ArmC fill:#e8f5e9
    style ArmD fill:#f3e5f5
```

---

## Diagram 4: Readout Hierarchy and Analysis Pipeline

```mermaid
flowchart TD
    subgraph Primary["PRIMARY READOUTS (all mice)"]
        P1["Weekly BLI<br/>(tumor burden kinetics)"]
        P2["IF: GFP + Ki67 + NR2F1<br/>(dormancy fraction)"]
        P3["Flow: CD86 vs CD206<br/>on F4/80+ cells<br/>(M1:M2 ratio)"]
        P4["Gross pathology<br/>(metastasis count)"]
    end

    subgraph Secondary["SECONDARY READOUTS (subset)"]
        S1["p-ERK / p-p38 ratio<br/>(dormancy signaling switch)"]
        S2["Luminex cytokines<br/>(IFN-γ, TGF-β1, TGF-β2, IL-10)"]
        S3["Immune infiltration<br/>(CD8, NK1.1, Tregs)"]
        S4["Fucci2a cell cycle<br/>(G1 vs S/G2/M)"]
    end

    subgraph Tertiary["TERTIARY READOUTS (dedicated cohort)"]
        T1["scRNA-seq<br/>(10× Chromium)"]
        T2["Spatial transcriptomics<br/>(10× Visium / MERFISH)"]
        T3["Electron microscopy<br/>(GJIC confirmation)"]
        T4["SHG imaging<br/>(collagen scaffold)"]
    end

    Primary --> Analysis

    subgraph Analysis["COMPUTATIONAL ANALYSIS"]
        A1["Cell Ranger → Seurat<br/>(scRNA-seq pipeline)"]
        A2["Dormancy scoring<br/>(Nr2f1 + Bhlhe41 + Cdkn1b)"]
        A3["M1/M2 module scoring<br/>(Nos2, Tnf, Arg1, Mrc1)"]
        A4["CellPhoneDB / NicheNet<br/>(ligand–receptor analysis)"]
        A5["Trajectory analysis<br/>(Monocle3)"]
        A6["Statistical testing<br/>(Fisher's, Kaplan-Meier, ANOVA)"]
    end

    Secondary --> Analysis
    Tertiary --> Analysis

    Analysis --> QuantOutput["QUANTITATIVE OUTPUT"]
    QuantOutput --> Q1["Dormancy Entry Rate (DER)<br/>per experimental group"]
    QuantOutput --> Q2["Dormancy Maintenance Duration (DMD)<br/>(Kaplan-Meier)"]
    QuantOutput --> Q3["Dormancy Exit Rate (DXR)<br/>per macrophage condition"]
    QuantOutput --> Q4["M1/M2 contribution<br/>to each phase (%)"]

    style Primary fill:#e3f2fd
    style Secondary fill:#fff8e1
    style Tertiary fill:#f3e5f5
    style Analysis fill:#e8f5e9
    style QuantOutput fill:#1b5e20,color:#ffffff
```

---

## Diagram 5: Expected Outcomes Decision Tree

```mermaid
flowchart TD
    Start["Experimental Results"] --> CheckA{Arm A:<br/>Macrophages required?}

    CheckA -->|No effect of depletion| DeadEnd["Macrophages are NOT<br/>required for dormancy<br/>in colon cancer liver mets<br/>→ REVISE HYPOTHESIS"]
    CheckA -->|Depletion changes dormancy| CheckB{Arm B:<br/>M1 impairment<br/>reduces entry?}

    CheckB -->|Yes: 65% → 40%| CheckC{Arm C:<br/>M2 impairment<br/>shortens maintenance?}
    CheckB -->|No effect| CheckC2{Arm C:<br/>M2 impairment<br/>shortens maintenance?}

    CheckC -->|Yes: 8wk → 4wk| Scenario1["SCENARIO 1: BOTH CONTRIBUTE<br/>✓ Confirms Temporal Switch Model<br/>M1 ~40% entry, M2 ~50% maintenance<br/><br/>ACTION: Proceed to therapeutic testing<br/>Arm D5 validates 'awaken & eliminate'"]

    CheckC -->|No effect| Scenario2["SCENARIO 2: ONLY M1 MATTERS<br/>M1 drives entry via IFN-γ/p38/STAT1<br/>M2 contribution overestimated<br/><br/>ACTION: Focus on IFN-γ pathway<br/>Explore M1-agonist strategies"]

    CheckC2 -->|Yes| Scenario3["SCENARIO 3: ONLY M2 MATTERS<br/>M2 maintains dormancy via TGF-β2/GJIC<br/>M1 entry contribution overestimated<br/><br/>ACTION: Focus on M2-targeted<br/>maintenance strategies"]

    CheckC2 -->|No| Scenario4["SCENARIO 4: REDUNDANT<br/>Neither M1 nor M2 alone is required<br/>Only total depletion shows effect<br/><br/>ACTION: Macrophage contribution<br/>is non-specific (headcount, not phenotype)"]

    Scenario1 --> D5check{Arm D5: anti-PD-1<br/>converts awakening<br/>to clearance?}

    D5check -->|Yes| Clinical["CLINICAL TRANSLATION<br/>PI3K-γ inhibitor + anti-PD-1<br/>= 'awaken dormant cells,<br/>then eliminate with immunity'<br/><br/>→ Design Phase I trial"]
    D5check -->|No| NextStep["Awakening alone insufficient<br/>Need additional immune activation<br/>→ Test combination with<br/>STING agonist or CD40 agonist"]

    style Start fill:#e8eaf6
    style DeadEnd fill:#ffcdd2
    style Scenario1 fill:#c8e6c9
    style Scenario2 fill:#ffccbc
    style Scenario3 fill:#ffccbc
    style Scenario4 fill:#ffcdd2
    style Clinical fill:#a5d6a7
    style NextStep fill:#fff9c4
```

---

## Diagram 6: Macrophage-DTC Interaction Model

```mermaid
flowchart LR
    subgraph DTC["Disseminated Tumor Cell"]
        direction TB
        NR2F1["NR2F1<br/>(dormancy TF)"]
        p27["p27/KIP1<br/>(cell cycle arrest)"]
        p38["p-p38 HIGH<br/>(stress kinase)"]
        ERK["p-ERK LOW<br/>(growth kinase)"]
        Ki67["Ki67 NEGATIVE<br/>(not proliferating)"]
    end

    subgraph M1mac["M1-like Macrophage"]
        direction TB
        IFNg["IFN-γ"]
        TNFa["TNF-α"]
        IL12["IL-12"]
        CXCL10["CXCL9/10"]
        NO["Nitric Oxide (iNOS)"]
    end

    subgraph M2mac["M2-like Macrophage"]
        direction TB
        TGFB2["TGF-β2"]
        IL10["IL-10"]
        ARG1["Arginase-1"]
        MMP["MMPs"]
        GJ["Gap Junctions<br/>(Connexin 43)"]
    end

    subgraph EntryPhase["DORMANCY ENTRY"]
        direction TB
        E1["IFN-γ activates<br/>p38/STAT1 in DTC"]
        E2["p38 phosphorylates<br/>ATF2/CREB"]
        E3["NR2F1 upregulated"]
        E4["Cell cycle arrest<br/>at G1/S"]
        E1 --> E2 --> E3 --> E4
    end

    subgraph MaintPhase["DORMANCY MAINTENANCE"]
        direction TB
        M1["TGF-β2 maintains<br/>NR2F1 expression"]
        M2["GJIC delivers<br/>quiescence signals"]
        M3["Low p-ERK /<br/>high p-p38 sustained"]
        M1 --> M2 --> M3
    end

    subgraph ExitPhase["DORMANCY EXIT"]
        direction TB
        X1["MMPs remodel ECM"]
        X2["Angiogenic switch<br/>(VEGF)"]
        X3["p-ERK surges,<br/>p-p38 drops"]
        X4["Ki67+, cell cycle<br/>re-entry"]
        X1 --> X2 --> X3 --> X4
    end

    M1mac -->|DRIVES| EntryPhase
    M2mac -->|MAINTAINS| MaintPhase
    M2mac -->|TRIGGERS| ExitPhase
    EntryPhase --> MaintPhase --> ExitPhase

    style DTC fill:#e1f5fe
    style M1mac fill:#ffcdd2
    style M2mac fill:#c8e6c9
    style EntryPhase fill:#fff3e0
    style MaintPhase fill:#e8eaf6
    style ExitPhase fill:#ffebee
```

---

## Diagram 7: Tissue Processing Pipeline at Each Timepoint

```mermaid
flowchart TD
    Sacrifice["Sacrifice mouse<br/>(Day 7, 21, 42, or 84)"]
    Sacrifice --> Perfusion["Portal vein perfusion<br/>(10 mL ice-cold PBS)"]

    Perfusion --> LiverExcision["Excise liver<br/>Record weight"]

    LiverExcision --> Split["Divide into 4 portions"]

    Split --> L1["Left lobe (~30%)"]
    Split --> L2["Median lobe (~30%)"]
    Split --> L3["Right lobe (~20%)"]
    Split --> L4["Caudate lobe (~20%)"]

    L1 --> Fix["4% PFA fixation, 24h"]
    Fix --> Cryo["30% sucrose → OCT"]
    Cryo --> Section["8 μm cryosections"]
    Section --> IF["Multiplex IF<br/>(GFP/Ki67/NR2F1/CD68)"]
    IF --> Quant["Quantify:<br/>• Dormancy fraction<br/>• Macrophage proximity<br/>• p-ERK/p-p38 ratio"]

    L2 --> Fresh["Fresh on ice"]
    Fresh --> Digest["Collagenase IV digestion<br/>30 min, 37°C"]
    Digest --> Percoll["40%/70% Percoll gradient"]
    Percoll --> Flow["Flow cytometry<br/>(12-color panel)"]
    Flow --> M1M2["Quantify:<br/>• M1:M2 ratio<br/>• KC vs MoM<br/>• Depletion efficiency"]

    L3 --> Snap1["Snap-freeze<br/>(liquid N₂)"]
    Snap1 --> FACS["FACS sorting<br/>DTCs + Macrophages"]
    FACS --> scRNA["scRNA-seq<br/>(10× Chromium)"]
    scRNA --> Bioinfo["Bioinformatics:<br/>• Clustering<br/>• Trajectory analysis<br/>• CellPhoneDB"]

    L4 --> Snap2["Snap-freeze<br/>(liquid N₂)"]
    Snap2 --> Homog["Tissue homogenization<br/>(RIPA buffer)"]
    Homog --> Cytokine["Luminex multiplex<br/>(12-plex panel)"]
    Cytokine --> CytData["Cytokine levels:<br/>• IFN-γ, TNF-α (M1)<br/>• TGF-β2, IL-10 (M2)"]

    Quant --> Integrate["DATA INTEGRATION"]
    M1M2 --> Integrate
    Bioinfo --> Integrate
    CytData --> Integrate

    Integrate --> Report["Per-mouse report:<br/>DER, DMD, DXR, DCR<br/>M1:M2 ratio, cytokine profile"]

    style Sacrifice fill:#e8eaf6
    style Integrate fill:#1b5e20,color:#ffffff
    style Report fill:#a5d6a7
```

---

## Diagram 8: Budget and Timeline Summary

```mermaid
gantt
    title Project Timeline (28 weeks total)
    dateFormat  YYYY-MM-DD
    axisFormat  %b %W

    section Phase 0
    Cell engineering (MC38-GFP-Luc-Fucci2a)  :p0a, 2026-06-01, 28d
    Mouse breeding (genetic crosses)          :p0b, 2026-06-01, 42d
    Dose-response pilot (3 doses × 5 mice)   :p0c, 2026-07-01, 14d
    Reagent validation (PK/PD)                :p0d, 2026-07-07, 14d

    section Phase I
    Arm A: Total macrophage depletion          :p1a, 2026-08-01, 84d
    Arm A tissue processing                    :p1b, 2026-08-08, 84d

    section Phase II
    Arm B: M1 impairment                       :p2a, 2026-08-15, 84d
    Arm C: M2 impairment                       :p2b, 2026-08-15, 84d

    section Phase III
    Arm D: Temporal switch                     :p3a, 2026-09-15, 84d

    section Phase IV
    scRNA-seq library prep & sequencing        :p4a, 2026-11-01, 42d
    Data analysis                              :p4b, 2026-11-15, 42d
    Manuscript preparation                     :p4c, 2026-12-01, 28d
    Independent replicate                      :p4d, 2026-12-15, 56d
```

---

## How to Render These Diagrams

1. **Online:** Paste any diagram block into [Mermaid Live Editor](https://mermaid.live)
2. **VS Code:** Install "Mermaid Markdown Syntax Highlighting" extension
3. **GitHub:** Diagrams render natively in `.md` files with `mermaid` code blocks
4. **PDF export:** Use `mmdc` (mermaid-cli) to convert to PNG/SVG, then embed in documents:

```bash
npm install -g @mermaid-js/mermaid-cli
mmdc -i WORKFLOW_DIAGRAMS.md -o workflow_diagrams.pdf
# or individual diagrams:
mmdc -i diagram1.mmd -o diagram1.png -w 2400 -H 1600
```
