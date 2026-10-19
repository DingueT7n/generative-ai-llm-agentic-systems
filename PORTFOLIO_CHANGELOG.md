# Portfolio reorganization changelog

**Prepared:** October 2026  
**Study context:** INGETIS (Paris, France) · 2026–2027  
**Maintainer:** Mohammed Alaa Eddine GUERBOUZ

## What changed

1. Combined the coursework under one themed repository with five learning modules.
2. Gave each unique notebook a descriptive, consistent English filename and a dedicated explanatory README.
3. Added an academic-context Markdown cell to every notebook; original notebook source and code cells are **unchanged**.
4. Added a clear attribution policy and recorded original filenames/hashes in `SOURCE_INVENTORY.csv`.
5. Kept instructor PDFs and other course references in a Git-ignored private folder for local use.
6. Retained the incomplete EcoTrack notebook with its TODOs and supplied sample corpus/test data.
7. Added a separate, testable **post-course enhancement** for EcoTrack, including a CLI, retrieval/evaluation, and tests.

## Identical duplicate notebooks removed from the public project folders

- `Conformite_AI_Act_Gemini_Agent_Module_FR(1).ipynb` duplicated `Jour_4_Conformite_AI_Act_Gemini_Agent_Module_FR.ipynb`.
- `Couche_de_confiance_Pramagent_Gemini_FR(1).ipynb` duplicated `jour_4_Couche_de_confiance_Pramagent_Gemini_FR(1).ipynb`.
- `Pack_Projet_EcoTrack_Assistant.zip` repeats the unpacked EcoTrack materials and is not included again.

## Verification scope

All notebook JSON/cells were checked for structural correctness; code-cell source equivalence was asserted against originals. External API calls, model downloads, and Colab-only steps were **not** run as part of this packaging task.
