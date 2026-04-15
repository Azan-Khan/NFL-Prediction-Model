# NFL Prediction Model

## Project Overview
This project is the final course project for CS 231: Introduction to Data Science.

Our goal is to study historical NFL team statistics and build a data science workflow that identifies which regular-season characteristics are most associated with Super Bowl success. We will use team-level NFL data from the 2003–2023 seasons and apply exploratory analysis, data cleaning, feature selection, model comparison, and evaluation.

This repository is organized for reproducibility and documentation. Every major project step is recorded in code, markdown, and the project decision log.

## Research Question
Which regular-season NFL team statistics are most associated with winning the Super Bowl, and can we build a model that identifies realistic championship contenders from historical team data?

## Dataset
Source: Kaggle NFL Team Data 2003–2023  
Dataset URL: https://www.kaggle.com/datasets/nickcantalupa/nfl-team-data-2003-2023

The raw dataset is stored locally in `data/raw/` and is not manually edited. Any transformed or cleaned dataset versions will be created by code and saved to `data/processed/`.

## Repository Structure

```text
NFL-Prediction-Model/
├── data/
│   ├── raw/           # original downloaded data, never manually edited
│   └── processed/     # cleaned/model-ready outputs created by code
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_cleaning.ipynb
│   └── 03_modeling.ipynb
├── src/               # shared helper code if needed
├── outputs/           # generated figures and model artifacts
├── decisions.md       # analytical decision log
├── requirements.txt   # project dependencies
├── README.md
└── .gitignore

## Workflow

The project will be completed in the following order:

1. Repository setup and documentation
2. Exploratory data analysis in 01_eda.ipynb
3. Data cleaning and feature preparation in 02_cleaning.ipynb
4. Model development and comparison in 03_modeling.ipynb
5. Final written report and presentation materials

## Reproducibility Rules

- Raw data is never manually edited.
- All transformations happen in code.
- Random seeds will be set where needed.
- Notebooks must run top-to-bottom on a clean kernel.
- Analytical decisions must be documented in markdown and in decisions.md.

## Team Members
Andrew Blasko
Seid Cubro
Azan Khan

## Status

Repository initialized. Documentation and notebook scaffolding are in place. Analysis has not started yet.
  
