---
name: research-team
description: Deploy a multi-agent scientific research team (postdocs, senior scientists, chief scientist, rival reviewer) to analyze a research topic with web-verified references and adversarial peer review
version: 1.0.0
---

# Research Team Skill

Deploy a structured multi-agent research team to perform deep literature analysis on any scientific topic. The pipeline runs 4 phases:

1. **Parallel Postdoc Search** (4-5 agents)
2. **Senior Scientist Synthesis** (2 agents)
3. **Chief Scientist Review** (1 agent)
4. **Adversarial Rival Critique** (1 agent)
5. **Feedback Integration** (improves all reports)

## Arguments

The user should provide:
- `topic` — the research topic or question to analyze
- `focus_areas` (optional) — specific subtopics to assign to each postdoc

If `focus_areas` is not provided, the skill will decompose the topic into 4-5 sub-angles automatically.

## Instructions

### Phase 1: Decompose Topic and Launch Postdocs

Decompose the research topic into 4-5 distinct research angles. For each angle, launch a background Agent with:

- **Role**: Postdoc with a specific name and expertise
- **Prompt template**: See below
- **run_in_background**: true
- Each postdoc gets a distinct focus area covering a non-overlapping aspect of the topic

**Postdoc prompt template:**

```
You are **Dr. [NAME], PhD** — a postdoctoral researcher specializing in [EXPERTISE]. You are part of a research team analyzing [TOPIC].

**Your assigned focus: [SPECIFIC ANGLE]**

Perform thorough web searches and provide a structured initial analysis covering:

1. **Key Papers (2020–current year)**: Identify at least 5–8 landmark and recent papers. Include authors, journal, year, DOI/PMID, and key findings. Use WebSearch to find real, verifiable papers. Do NOT fabricate citations.

2. **Mechanistic Insights**: What are the known molecular/cellular mechanisms?

3. **Models and Methods**: Which experimental models are used?

4. **Open Questions**: What remains unresolved or controversial?

5. **Key Data Points**: Any quantitative findings (fold-changes, hazard ratios, concentrations, effect sizes).

Format your output as a formal research briefing suitable for review by senior scientists. All acronyms must be defined on first use with the full term in parentheses.

IMPORTANT: Use WebSearch extensively. Only report papers you have verified exist. Provide PMID or DOI for every citation.
```

Create a `research-reports/postdocs/` directory and save each briefing as `postdoc[N]_[lastname]_[topic_slug].md`.

### Phase 2: Launch Senior Scientists (2 parallel agents)

Once all postdocs report, launch 2 Senior Scientist agents:

**Senior Scientist A** — Fundamental Mechanisms & Models Synthesis:
- Integrates postdoc findings on basic biology, mechanisms, and experimental models
- Verifies at least 8 key references using WebSearch
- Identifies convergent themes and contradictions
- Flags unverifiable citations
- Every acronym defined on first use

**Senior Scientist B** — Clinical Translation & Therapeutic Outlook:
- Integrates findings on clinical evidence, therapeutic strategies, and translational potential
- Verifies at least 8 key references using WebSearch
- Assesses evidence quality hierarchy
- Identifies clinical development gaps
- Every acronym defined on first use

Save reports to `research-reports/senior-scientists/senior_[a/b]_[lastname]_synthesis.md`.

### Phase 3: Launch Chief Scientist

Launch a Chief Scientist agent that:
1. Critically reviews ALL postdoc and senior scientist reports
2. Performs reference integrity audit (CONFIRMED / CORRECTED / UNVERIFIABLE)
3. Identifies inconsistencies between reports
4. Creates individual feedback directives for each team member
5. Compiles a **Master Acronym Glossary** of every abbreviation used
6. Produces unified conclusions and prioritized research agenda
7. Verifies disputed references using WebSearch

Save to `research-reports/chief-scientist/final_report_[lastname].md`.

### Phase 4: Launch Rival Lab Critique

Launch an adversarial reviewer agent that:
1. Grades each major claim as STRONG / MODERATE / WEAK / UNSUPPORTED
2. Identifies misconceptions (correlation vs causation, overextrapolation, model limitations)
3. Provides alternative interpretations the team did not consider
4. Lists missing evidence and critical unperformed experiments
5. Gives specific directives for improving reports
6. Provides a "Devil's Advocate" top-5 most damaging criticisms

Save to `research-reports/chief-scientist/rival_critique_[lastname].md`.

### Phase 5: Feedback Integration

Read both the Chief Scientist report and Rival Critique. Then:
1. Create a consolidated `IMPROVEMENTS.md` listing all required corrections
2. Update each postdoc report with corrections (citation fixes, qualification of claims, added caveats)
3. Update senior scientist reports with corrections
4. Produce a final **compiled report** at `research-reports/FINAL_COMPILATION.md` that includes:
   - Executive Summary
   - Verified Reference Table (only confirmed/corrected citations)
   - Integrated Mechanistic Framework (with acronym glossary)
   - Therapeutic Landscape Assessment
   - Critical Limitations and Caveats
   - Adversarial Review Response (how each criticism was addressed)
   - Prioritized Research Agenda
   - Complete Master Acronym Glossary (alphabetical, every term defined)

### Directory Structure

```
research-reports/
├── postdocs/
│   ├── postdoc1_[name]_[topic].md
│   ├── postdoc2_[name]_[topic].md
│   ├── postdoc3_[name]_[topic].md
│   ├── postdoc4_[name]_[topic].md
│   └── postdoc5_[name]_[topic].md  (optional)
├── senior-scientists/
│   ├── senior_a_[name]_synthesis.md
│   └── senior_b_[name]_synthesis.md
├── chief-scientist/
│   ├── final_report_[name].md
│   └── rival_critique_[name].md
├── IMPROVEMENTS.md
└── FINAL_COMPILATION.md
```

### Key Principles

1. **No fabricated citations** — Every reference must be verified via WebSearch. Flag anything unverifiable.
2. **Define all acronyms** — On first use in every document, and compile a master glossary.
3. **Adversarial review is essential** — The rival critique catches what friendly review misses.
4. **Feedback loop must close** — Criticisms must be addressed in the final compilation.
5. **Track tasks** — Use TaskCreate/TaskUpdate to track each phase.
6. **Parallel execution** — Postdocs run in parallel; Senior Scientists run in parallel; Chief and Rival can run in parallel.
