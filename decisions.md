# Analysis Decision Log

This file records analytical decisions made throughout the project.

Each entry should include:
- what we found,
- what decision we made,
- why we made it,
- what alternatives we considered,
- and what effect it had on the dataset or model.

---

## 2026-04-15: Repository initialization

Found:
The initial repository only contained a README and a raw dataset archive in the root, which was not sufficient for a reproducible data science workflow.

Decision:
Restructured the repository into separate folders for raw data, processed data, notebooks, source code, and outputs. Added placeholder files so Git can track empty folders. Added a decision log, requirements file, and .gitignore.

Why:
This project will be developed incrementally and must be understandable and reproducible by instructors and collaborators. Separating raw data from processed outputs reduces accidental manual edits and keeps the workflow transparent.

Alternatives considered:
Keeping a single flat directory with one notebook and the dataset in the root. Rejected because it is harder to document, harder to reproduce, and harder to maintain collaboratively.

Effect:
Repository now has a reproducible project skeleton and is ready for notebook-based analysis.