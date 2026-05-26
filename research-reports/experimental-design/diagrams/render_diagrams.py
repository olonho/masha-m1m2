#!/usr/bin/env python3
"""Render experimental workflow diagrams using graphviz."""

import graphviz
import os

OUTDIR = "/home/huawei/src/polariz-masha/research-reports/experimental-design/diagrams"

# ============================================================
# DIAGRAM 1: Overall Project Workflow
# ============================================================
def diagram1_overall_workflow():
    g = graphviz.Digraph('workflow', format='png')
    g.attr(rankdir='TB', size='12,16', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='11')
    g.attr('edge', fontname='DejaVu Sans', fontsize='9')

    # Phase 0
    g.node('A', 'Phase 0: Cell Engineering\n(MC38-GFP-Luc-Fucci2a)\nWeeks 1–4', fillcolor='#e1f5fe')
    g.node('B', 'Phase 0: Mouse Breeding\n(Genetic crosses)\nWeeks 1–6', fillcolor='#e1f5fe')
    g.node('C', 'Phase 0: Dose Pilot\n(3 doses × 5 mice)\nWeek 5', fillcolor='#e1f5fe')

    # Phase I
    g.node('D', 'Phase I: Arm A\nTotal Macrophage Depletion\nWeeks 7–14\n(n=60 mice)', fillcolor='#fff3e0')

    # Phase II
    g.node('E', 'Phase II: Arm B\nM1 Impairment\nWeeks 8–16\n(n=90 mice)', fillcolor='#fce4ec')
    g.node('F', 'Phase II: Arm C\nM2 Impairment\nWeeks 8–16\n(n=90 mice)', fillcolor='#e8f5e9')

    # Phase III
    g.node('G', 'Phase III: Arm D\nTemporal Switch (M2→M1)\nWeeks 10–18\n(n=90 mice)', fillcolor='#f3e5f5')

    # Phase IV
    g.node('H', 'Phase IV: Analysis\nscRNA-seq, Statistics\nManuscript\nWeeks 18–24', fillcolor='#e0f2f1')

    # Decision
    g.node('dec', 'Both M1 and M2\ncontribute?', shape='diamond', fillcolor='#fff9c4', fontsize='10')

    # Outcomes
    g.node('M', 'CONFIRMED:\nProceed to therapeutic\ntesting (Arm D5 strategy)', fillcolor='#c8e6c9')
    g.node('N', 'Only M2 matters:\nFocus on M2-targeted\nmaintenance strategies', fillcolor='#ffccbc')
    g.node('O', 'Only M1 matters:\nFocus on IFN-γ/p38\npathway', fillcolor='#ffccbc')
    g.node('P', 'Neither alone:\nNon-specific\nmacrophage contribution', fillcolor='#ffcdd2')

    g.edge('A', 'D')
    g.edge('B', 'D')
    g.edge('C', 'D', label='optimal\ndose')
    g.edge('D', 'E', label='macrophages\nrequired')
    g.edge('D', 'F')
    g.edge('E', 'G', label='M1 entry\nquantified')
    g.edge('F', 'G', label='M2 maint.\nquantified')
    g.edge('G', 'H')
    g.edge('H', 'dec')
    g.edge('dec', 'M', label='Yes')
    g.edge('dec', 'N', label='Only M2')
    g.edge('dec', 'O', label='Only M1')
    g.edge('dec', 'P', label='Neither')

    g.render(os.path.join(OUTDIR, 'diagram1_workflow'), cleanup=True)
    print("Diagram 1: Overall workflow rendered")

# ============================================================
# DIAGRAM 2: Intrasplenic Injection Timeline
# ============================================================
def diagram2_timeline():
    g = graphviz.Digraph('timeline', format='png')
    g.attr(rankdir='LR', size='16,6', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='10')
    g.attr('edge', fontname='DejaVu Sans', fontsize='8')

    with g.subgraph(name='cluster_surgery') as c:
        c.attr(label='Day 0: Surgery', style='dashed', color='#1565c0', fontcolor='#1565c0')
        c.node('S1', 'Anesthetize\n(isoflurane 3%)', fillcolor='#e3f2fd')
        c.node('S2', 'Left flank\nincision', fillcolor='#e3f2fd')
        c.node('S3', 'Inject 1×10³ MC38\ninto spleen\n(30 seconds)', fillcolor='#e3f2fd')
        c.node('S4', 'Splenectomy', fillcolor='#e3f2fd')
        c.node('S5', 'Close &\nrecover', fillcolor='#e3f2fd')

    with g.subgraph(name='cluster_seeding') as c:
        c.attr(label='Days 1–3: Seeding', style='dashed', color='#2e7d32', fontcolor='#2e7d32')
        c.node('T1', 'DTCs transit\nportal vein', fillcolor='#f1f8e9')
        c.node('T2', 'Lodge in\nsinusoids', fillcolor='#f1f8e9')
        c.node('T3', 'Extravasation\ninto parenchyma', fillcolor='#f1f8e9')

    with g.subgraph(name='cluster_entry') as c:
        c.attr(label='Days 3–14: Entry', style='dashed', color='#f57f17', fontcolor='#f57f17')
        c.node('E1', 'M1 macrophages\nencounter DTCs\n(IFN-γ/p38/STAT1)', fillcolor='#fff8e1')
        c.node('E2', '~65% DTCs enter\ndormancy\n(NR2F1+, Ki67−)', fillcolor='#fff8e1')
        c.node('E3', '~35% proliferate\nor are cleared', fillcolor='#fff8e1')

    with g.subgraph(name='cluster_maint') as c:
        c.attr(label='Days 14–84: Maintenance', style='dashed', color='#6a1b9a', fontcolor='#6a1b9a')
        c.node('M1', 'M2-like macrophages\ndominate\n(TGF-β2, GJIC)', fillcolor='#e8eaf6')
        c.node('M2', 'Dormant DTCs\npersist\n(stable BLI)', fillcolor='#e8eaf6')
        c.node('M3', 'Variable\nspontaneous exit', fillcolor='#e8eaf6')

    with g.subgraph(name='cluster_exit') as c:
        c.attr(label='Weeks 8–12: Exit', style='dashed', color='#c62828', fontcolor='#c62828')
        c.node('X1', 'M2→M1 switch\nor inflammation', fillcolor='#ffebee')
        c.node('X2', 'p-ERK/p-p38 > 0.5\nCell cycle re-entry', fillcolor='#ffebee')
        c.node('X3', 'Macrometastatic\noutgrowth', fillcolor='#ffebee')

    g.edge('S1', 'S2'); g.edge('S2', 'S3'); g.edge('S3', 'S4'); g.edge('S4', 'S5')
    g.edge('S5', 'T1')
    g.edge('T1', 'T2'); g.edge('T2', 'T3')
    g.edge('T3', 'E1')
    g.edge('E1', 'E2'); g.edge('E1', 'E3')
    g.edge('E2', 'M1')
    g.edge('M1', 'M2'); g.edge('M2', 'M3')
    g.edge('M3', 'X1')
    g.edge('X1', 'X2'); g.edge('X2', 'X3')

    g.render(os.path.join(OUTDIR, 'diagram2_timeline'), cleanup=True)
    print("Diagram 2: Timeline rendered")

# ============================================================
# DIAGRAM 3: Expected Outcomes Decision Tree
# ============================================================
def diagram3_decision_tree():
    g = graphviz.Digraph('decision', format='png')
    g.attr(rankdir='TB', size='14,18', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='10')
    g.attr('edge', fontname='DejaVu Sans', fontsize='9')

    g.node('start', 'Experimental\nResults', fillcolor='#e8eaf6', shape='ellipse')

    g.node('checkA', 'Arm A:\nMacrophages\nrequired?', fillcolor='#fff9c4', shape='diamond')
    g.node('deadend', 'Macrophages NOT required\n→ REVISE HYPOTHESIS', fillcolor='#ffcdd2')

    g.node('checkB', 'Arm B:\nM1 impairment\nreduces entry\n(65% → 40%)?', fillcolor='#fff9c4', shape='diamond')
    g.node('checkC', 'Arm C:\nM2 impairment\nshortens maintenance\n(8wk → 4wk)?', fillcolor='#fff9c4', shape='diamond')
    g.node('checkC2', 'Arm C:\nM2 impairment\nhas effect?', fillcolor='#fff9c4', shape='diamond')

    g.node('s1', 'SCENARIO 1: BOTH CONTRIBUTE ✓\nConfirms Temporal Switch Model\nM1 ~40% entry, M2 ~50% maint.\n→ Proceed to therapeutic testing', fillcolor='#c8e6c9')
    g.node('s2', 'SCENARIO 2: ONLY M1 MATTERS\nM1 drives entry (IFN-γ/p38/STAT1)\n→ Focus on M1-agonist strategies', fillcolor='#ffccbc')
    g.node('s3', 'SCENARIO 3: ONLY M2 MATTERS\nM2 maintains (TGF-β2/GJIC)\n→ Focus on M2-targeted maintenance', fillcolor='#ffccbc')
    g.node('s4', 'SCENARIO 4: REDUNDANT\nOnly total depletion shows effect\n→ Macrophage headcount, not phenotype', fillcolor='#ffcdd2')

    g.node('checkD5', 'Arm D5: anti-PD-1\nconverts awakening\nto clearance?', fillcolor='#fff9c4', shape='diamond')
    g.node('clinical', 'CLINICAL TRANSLATION\nPI3K-γ inhibitor + anti-PD-1\n"Awaken dormant cells,\nthen eliminate with immunity"\n→ Design Phase I trial', fillcolor='#a5d6a7')
    g.node('next', 'Awakening alone insufficient\n→ Test STING agonist\nor CD40 agonist combo', fillcolor='#fff9c4')

    g.edge('start', 'checkA')
    g.edge('checkA', 'deadend', label='No effect')
    g.edge('checkA', 'checkB', label='Depletion\nchanges dormancy')
    g.edge('checkB', 'checkC', label='Yes')
    g.edge('checkB', 'checkC2', label='No')
    g.edge('checkC', 's1', label='Yes')
    g.edge('checkC', 's2', label='No')
    g.edge('checkC2', 's3', label='Yes')
    g.edge('checkC2', 's4', label='No')
    g.edge('s1', 'checkD5')
    g.edge('checkD5', 'clinical', label='Yes')
    g.edge('checkD5', 'next', label='No')

    g.render(os.path.join(OUTDIR, 'diagram3_decision_tree'), cleanup=True)
    print("Diagram 3: Decision tree rendered")

# ============================================================
# DIAGRAM 4: Readout Hierarchy
# ============================================================
def diagram4_readouts():
    g = graphviz.Digraph('readouts', format='png')
    g.attr(rankdir='TB', size='12,14', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='10')
    g.attr('edge', fontname='DejaVu Sans', fontsize='8')

    with g.subgraph(name='cluster_primary') as c:
        c.attr(label='PRIMARY READOUTS (all mice)', style='filled', color='#bbdefb', fontcolor='#0d47a1')
        c.node('P1', 'Weekly BLI\n(tumor burden)', fillcolor='#e3f2fd')
        c.node('P2', 'IF: GFP + Ki67 + NR2F1\n(dormancy fraction)', fillcolor='#e3f2fd')
        c.node('P3', 'Flow: CD86 vs CD206\non F4/80+\n(M1:M2 ratio)', fillcolor='#e3f2fd')
        c.node('P4', 'Gross pathology\n(metastasis count)', fillcolor='#e3f2fd')

    with g.subgraph(name='cluster_secondary') as c:
        c.attr(label='SECONDARY READOUTS (subset)', style='filled', color='#fff9c4', fontcolor='#f57f17')
        c.node('S1', 'p-ERK / p-p38 ratio\n(dormancy switch)', fillcolor='#fff8e1')
        c.node('S2', 'Luminex cytokines\n(IFN-γ, TGF-β1/2, IL-10)', fillcolor='#fff8e1')
        c.node('S3', 'Immune infiltration\n(CD8, NK1.1, Tregs)', fillcolor='#fff8e1')
        c.node('S4', 'Fucci2a cell cycle\n(G1 vs S/G2/M)', fillcolor='#fff8e1')

    with g.subgraph(name='cluster_tertiary') as c:
        c.attr(label='TERTIARY READOUTS (dedicated cohort)', style='filled', color='#e1bee7', fontcolor='#4a148c')
        c.node('T1', 'scRNA-seq\n(10× Chromium)', fillcolor='#f3e5f5')
        c.node('T2', 'Spatial transcriptomics\n(Visium / MERFISH)', fillcolor='#f3e5f5')
        c.node('T3', 'Electron microscopy\n(GJIC)', fillcolor='#f3e5f5')
        c.node('T4', 'SHG imaging\n(collagen scaffold)', fillcolor='#f3e5f5')

    g.node('analysis', 'Computational Analysis\nSeurat • CellPhoneDB • NicheNet\nMonocle3 • Statistics', fillcolor='#e8f5e9')

    g.node('output', 'QUANTITATIVE OUTPUT', fillcolor='#1b5e20', fontcolor='white', shape='box3d')
    g.node('q1', 'Dormancy Entry Rate\n(DER) per group', fillcolor='#a5d6a7')
    g.node('q2', 'Maintenance Duration\n(DMD) Kaplan-Meier', fillcolor='#a5d6a7')
    g.node('q3', 'Exit Rate (DXR) per\nmacrophage condition', fillcolor='#a5d6a7')
    g.node('q4', 'M1/M2 contribution\nto each phase (%)', fillcolor='#a5d6a7')

    for n in ['P1','P2','P3','P4','S1','S2','S3','S4','T1','T2','T3','T4']:
        g.edge(n, 'analysis')

    g.edge('analysis', 'output')
    g.edge('output', 'q1'); g.edge('output', 'q2'); g.edge('output', 'q3'); g.edge('output', 'q4')

    g.render(os.path.join(OUTDIR, 'diagram4_readouts'), cleanup=True)
    print("Diagram 4: Readout hierarchy rendered")

# ============================================================
# DIAGRAM 5: Macrophage-DTC Interaction
# ============================================================
def diagram5_interaction():
    g = graphviz.Digraph('interaction', format='png')
    g.attr(rankdir='LR', size='16,10', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='10')
    g.attr('edge', fontname='DejaVu Sans', fontsize='9')

    # DTC
    with g.subgraph(name='cluster_dtc') as c:
        c.attr(label='Disseminated Tumor Cell', style='filled', color='#bbdefb', fontcolor='#0d47a1')
        c.node('NR2F1', 'NR2F1\n(dormancy TF)', fillcolor='#e1f5fe')
        c.node('p27', 'p27/KIP1\n(cell cycle arrest)', fillcolor='#e1f5fe')
        c.node('pp38', 'p-p38 HIGH\n(stress kinase)', fillcolor='#e1f5fe')
        c.node('pERK', 'p-ERK LOW\n(growth kinase)', fillcolor='#e1f5fe')
        c.node('Ki67', 'Ki67 NEGATIVE\n(not proliferating)', fillcolor='#e1f5fe')

    # M1
    with g.subgraph(name='cluster_m1') as c:
        c.attr(label='M1-like Macrophage', style='filled', color='#ef9a9a', fontcolor='#b71c1c')
        c.node('IFNg', 'IFN-γ', fillcolor='#ffcdd2')
        c.node('TNFa', 'TNF-α', fillcolor='#ffcdd2')
        c.node('IL12', 'IL-12', fillcolor='#ffcdd2')
        c.node('CXCL', 'CXCL9/10', fillcolor='#ffcdd2')
        c.node('NO', 'Nitric Oxide\n(iNOS)', fillcolor='#ffcdd2')

    # M2
    with g.subgraph(name='cluster_m2') as c:
        c.attr(label='M2-like Macrophage', style='filled', color='#a5d6a7', fontcolor='#1b5e20')
        c.node('TGFB2', 'TGF-β2', fillcolor='#c8e6c9')
        c.node('IL10', 'IL-10', fillcolor='#c8e6c9')
        c.node('ARG1', 'Arginase-1', fillcolor='#c8e6c9')
        c.node('MMP', 'MMPs', fillcolor='#c8e6c9')
        c.node('GJ', 'Gap Junctions\n(Cx43)', fillcolor='#c8e6c9')

    # Phases
    with g.subgraph(name='cluster_entry') as c:
        c.attr(label='DORMANCY ENTRY', style='filled', color='#ffe082', fontcolor='#e65100')
        c.node('e1', 'IFN-γ activates\np38/STAT1', fillcolor='#fff3e0')
        c.node('e2', 'NR2F1 upregulated', fillcolor='#fff3e0')
        c.node('e3', 'Cell cycle arrest\nat G1/S', fillcolor='#fff3e0')

    with g.subgraph(name='cluster_maint') as c:
        c.attr(label='MAINTENANCE', style='filled', color='#b39ddb', fontcolor='#311b92')
        c.node('m1', 'TGF-β2 maintains\nNR2F1', fillcolor='#e8eaf6')
        c.node('m2', 'GJIC delivers\nquiescence signals', fillcolor='#e8eaf6')
        c.node('m3', 'Low p-ERK /\nhigh p-p38', fillcolor='#e8eaf6')

    with g.subgraph(name='cluster_exit') as c:
        c.attr(label='DORMANCY EXIT', style='filled', color='#ef9a9a', fontcolor='#b71c1c')
        c.node('x1', 'MMPs remodel\nECM', fillcolor='#ffebee')
        c.node('x2', 'Angiogenic\nswitch (VEGF)', fillcolor='#ffebee')
        c.node('x3', 'p-ERK surges\nKi67+ re-entry', fillcolor='#ffebee')

    g.edge('IFNg', 'e1', label='DRIVES', color='#c62828', style='bold')
    g.edge('e1', 'e2'); g.edge('e2', 'e3')
    g.edge('TGFB2', 'm1', label='MAINTAINS', color='#2e7d32', style='bold')
    g.edge('m1', 'm2'); g.edge('m2', 'm3')
    g.edge('MMP', 'x1', label='TRIGGERS', color='#6a1b9a', style='bold')
    g.edge('x1', 'x2'); g.edge('x2', 'x3')

    g.edge('e3', 'm1', style='dashed')
    g.edge('m3', 'x1', style='dashed')

    g.render(os.path.join(OUTDIR, 'diagram5_interaction'), cleanup=True)
    print("Diagram 5: Macrophage-DTC interaction rendered")

# ============================================================
# DIAGRAM 6: Tissue Processing Pipeline
# ============================================================
def diagram6_tissue():
    g = graphviz.Digraph('tissue', format='png')
    g.attr(rankdir='TB', size='14,16', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='9')
    g.attr('edge', fontname='DejaVu Sans', fontsize='8')

    g.node('sac', 'Sacrifice mouse\n(Day 7, 21, 42, or 84)', fillcolor='#e8eaf6')
    g.node('perf', 'Portal vein perfusion\n(10 mL ice-cold PBS)', fillcolor='#e8eaf6')
    g.node('exc', 'Excise liver\nRecord weight', fillcolor='#e8eaf6')
    g.node('split', 'Divide into 4 portions', fillcolor='#e8eaf6')

    # Branch 1: IF
    g.node('fix', '4% PFA fix 24h', fillcolor='#e3f2fd')
    g.node('cryo', 'Sucrose → OCT', fillcolor='#e3f2fd')
    g.node('sect', '8 μm cryosections', fillcolor='#e3f2fd')
    g.node('IF', 'Multiplex IF\nGFP/Ki67/NR2F1/CD68', fillcolor='#e3f2fd')
    g.node('q1', 'Dormancy fraction\nMacrophage proximity\np-ERK/p-p38 ratio', fillcolor='#bbdefb')

    # Branch 2: Flow
    g.node('fresh', 'Fresh on ice', fillcolor='#fff8e1')
    g.node('dig', 'Collagenase IV\n30 min, 37°C', fillcolor='#fff8e1')
    g.node('per', 'Percoll gradient\n40%/70%', fillcolor='#fff8e1')
    g.node('flow', 'Flow cytometry\n12-color panel', fillcolor='#fff8e1')
    g.node('q2', 'M1:M2 ratio\nKC vs MoM\nDepletion efficiency', fillcolor='#fff9c4')

    # Branch 3: scRNA-seq
    g.node('snap1', 'Snap-freeze\n(liquid N₂)', fillcolor='#f3e5f5')
    g.node('facs', 'FACS sorting\nDTCs + Macrophages', fillcolor='#f3e5f5')
    g.node('sc', 'scRNA-seq\n(10× Chromium)', fillcolor='#f3e5f5')
    g.node('bio', 'Clustering\nTrajectory\nCellPhoneDB', fillcolor='#f3e5f5')
    g.node('q3', 'DTC dormancy\ntranscriptome\nMacrophage-DTC\ninteractions', fillcolor='#e1bee7')

    # Branch 4: Cytokines
    g.node('snap2', 'Snap-freeze\n(liquid N₂)', fillcolor='#ffebee')
    g.node('hom', 'Homogenize\n(RIPA buffer)', fillcolor='#ffebee')
    g.node('cyt', 'Luminex multiplex\n(12-plex)', fillcolor='#ffebee')
    g.node('q4', 'IFN-γ, TNF-α (M1)\nTGF-β2, IL-10 (M2)', fillcolor='#ffcdd2')

    # Integration
    g.node('int', 'DATA INTEGRATION', fillcolor='#1b5e20', fontcolor='white')
    g.node('rep', 'Per-mouse report:\nDER • DMD • DXR • DCR\nM1:M2 ratio • Cytokines', fillcolor='#a5d6a7')

    g.edge('sac', 'perf'); g.edge('perf', 'exc'); g.edge('exc', 'split')
    g.edge('split', 'fix', label='Left lobe 30%'); g.edge('fix', 'cryo'); g.edge('cryo', 'sect'); g.edge('sect', 'IF'); g.edge('IF', 'q1')
    g.edge('split', 'fresh', label='Median 30%'); g.edge('fresh', 'dig'); g.edge('dig', 'per'); g.edge('per', 'flow'); g.edge('flow', 'q2')
    g.edge('split', 'snap1', label='Right 20%'); g.edge('snap1', 'facs'); g.edge('facs', 'sc'); g.edge('sc', 'bio'); g.edge('bio', 'q3')
    g.edge('split', 'snap2', label='Caudate 20%'); g.edge('snap2', 'hom'); g.edge('hom', 'cyt'); g.edge('cyt', 'q4')

    g.edge('q1', 'int'); g.edge('q2', 'int'); g.edge('q3', 'int'); g.edge('q4', 'int')
    g.edge('int', 'rep')

    g.render(os.path.join(OUTDIR, 'diagram6_tissue_pipeline'), cleanup=True)
    print("Diagram 6: Tissue processing pipeline rendered")

# ============================================================
# DIAGRAM 7: Four Experimental Arms Summary
# ============================================================
def diagram4_arms():
    g = graphviz.Digraph('arms', format='png')
    g.attr(rankdir='TB', size='16,20', dpi='200')
    g.attr('node', shape='box', style='rounded,filled', fontname='DejaVu Sans', fontsize='9')
    g.attr('edge', fontname='DejaVu Sans', fontsize='8')

    g.node('Q', 'RESEARCH QUESTION:\nHow do M1 and M2 macrophages\nquantitatively contribute to\ndormancy in colon cancer?', fillcolor='#1a237e', fontcolor='white', shape='box3d')

    # Arm A
    with g.subgraph(name='cluster_a') as c:
        c.attr(label='ARM A: Total Macrophage Depletion (n=60)', style='filled', color='#ffe0b2', fontcolor='#e65100')
        c.node('A1', 'A1: PBS liposomes\n(vehicle control)\nn=15', fillcolor='#fff3e0')
        c.node('A2', 'A2: Clodronate liposomes\nfrom Day 1 (early)\nn=15', fillcolor='#fff3e0')
        c.node('A3', 'A3: Clodronate liposomes\nfrom Day 14 (late)\nn=15', fillcolor='#fff3e0')
        c.node('A4', 'A4: Clodronate +\nCD169-DTR + DT\n(Kupffer-selective)\nn=15', fillcolor='#fff3e0')

    # Arm B
    with g.subgraph(name='cluster_b') as c:
        c.attr(label='ARM B: M1 Impairment – Dormancy Entry (n=90)', style='filled', color='#f8bbd0', fontcolor='#880e4f')
        c.node('B1', 'B1: LysM-Cre × Nos2fl/fl\n(Genetic M1 KO)\nn=15', fillcolor='#fce4ec')
        c.node('B2', 'B2: LysM-Cre control\nn=15', fillcolor='#fce4ec')
        c.node('B3', 'B3: Anti-IFN-γ Ab\n(from Day -1)\nn=15', fillcolor='#fce4ec')
        c.node('B4', 'B4: Anti-IFN-γ Ab\n(from Day 7, late)\nn=10', fillcolor='#fce4ec')
        c.node('B5', 'B5: Isotype control\nn=10', fillcolor='#fce4ec')

    # Arm C
    with g.subgraph(name='cluster_c') as c:
        c.attr(label='ARM C: M2 Impairment – Dormancy Maintenance (n=90)', style='filled', color='#c8e6c9', fontcolor='#1b5e20')
        c.node('C1', 'C1: LysM-Cre × Arg1fl/fl\n(Genetic M2 KO)\nn=15', fillcolor='#e8f5e9')
        c.node('C2', 'C2: Anti-IL-4Rα Ab\n(from Day 14)\nn=15', fillcolor='#e8f5e9')
        c.node('C3', 'C3: CD169-DTR + DT\n(Kupffer depletion)\nn=15', fillcolor='#e8f5e9')
        c.node('C4', 'C4: Cx3cr1-CreERT2 × DTA\n(Recruited MoM depletion)\nn=15', fillcolor='#e8f5e9')
        c.node('C5', 'C5: Controls\nn=15', fillcolor='#e8f5e9')

    # Arm D
    with g.subgraph(name='cluster_d') as c:
        c.attr(label='ARM D: Temporal Switch M2→M1 (n=90)', style='filled', color='#e1bee7', fontcolor='#4a148c')
        c.node('D1', 'D1: IL-4 complex Days 1-28\n→ IFN-γ+LPS Days 28-42\n(Switch)\nn=15', fillcolor='#f3e5f5')
        c.node('D2', 'D2: IL-4 complex sustained\n(M2 throughout)\nn=15', fillcolor='#f3e5f5')
        c.node('D3', 'D3: IFN-γ + poly(I:C)\n(M1 throughout)\nn=15', fillcolor='#f3e5f5')
        c.node('D4', 'D4: Switch + anti-PD-1\n(Awaken + eliminate)\nn=15', fillcolor='#f3e5f5')
        c.node('D5', 'D5: PI3K-γ inhibitor\n(Eganelisib)\nn=15', fillcolor='#f3e5f5')
        c.node('D6', 'D6: PBS vehicle\nn=15', fillcolor='#f3e5f5')

    g.edge('Q', 'A1', label='Are macrophages\nrequired?')
    g.edge('Q', 'B1', label='Are M1 macs\nneeded for entry?')
    g.edge('Q', 'C1', label='Are M2 macs\nneeded for maint?')
    g.edge('Q', 'D1', label='Does M2→M1\ntrigger exit?')

    g.render(os.path.join(OUTDIR, 'diagram7_four_arms'), cleanup=True)
    print("Diagram 7: Four experimental arms rendered")


# Run all
diagram1_overall_workflow()
diagram2_timeline()
diagram3_decision_tree()
diagram4_readouts()
diagram5_interaction()
diagram6_tissue()
diagram4_arms()

print("\nAll diagrams rendered to:", OUTDIR)
