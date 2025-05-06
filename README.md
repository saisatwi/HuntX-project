# 🏹 HuntX Project – Data Engineering Adventure

A futuristic, story-driven data project where you play as a legendary hunter navigating through AI-powered terrains, hunting rare species, and collecting data along the way. Designed to master real-world data engineering & analytics skills through an immersive game simulation.

---

## 🔥 Project Summary

**Tech Stack:** Python · Pandas · Snowflake · AWS S3 · SQL · QuickSight

- Built with a gamified storyline involving futuristic terrains, AI interactions, and rare creature encounters.
- Designed for learning data engineering (pipelines, ETL, cloud) and analytics (EDA, dashboards, storytelling).

---

## 📅 Progress Log

### ✅ Day 1 – Project Setup
- Created HuntX folder structure.
- Set up `data/`, `pipeline/`, and virtual environment.
- Initialized Git and VSCode workspace.

### ✅ Day 2 – Data Ingestion
- Created `animals.csv` with 10 species, types, rarity.
- Wrote `ingest_data.py` to load raw data and preview it.

### ✅ Day 3 – Synthetic Data Generation
- Generated 1000 synthetic animal entries using Python.
- Included ID, name, species, breed, danger level, rarity.
- Wrote `generate_data.py` to automate the process.

### ✅ Day 4 – Data Transformation
- Cleaned and structured the generated data.
- Removed duplicates, handled missing values.
- Wrote `transform_data.py` for full transformation pipeline.

### ✅ Day 5 – Terrain Creation
- Defined 10 terrain types (e.g., Jungle, Desert, Arctic).
- Created `terrain.csv` with climate, hazards, and rarity.
- Added difficulty levels (1–50) to terrains.

### ✅ Day 6 – Linking Animals to Terrains
- Mapped animals to terrains randomly.
- Integrated terrain and animal datasets.
- Added `terrain_main.csv` to simulate game-world linkages.

### ✅ Day 7 – Hunter Data & Encounter Logs
- Created 1000 unique hunter profiles with XP, health, fame.
- Generated random encounter logs for each hunter based on terrain and actions.
- Saved data in `hunter_stats.csv` and `encounter_logs.csv`.

### ✅ Day 8 – AI Interactions & Universal Travel Key Logs
- Added AI interactions based on hunter actions (voice assistant tracking vitals).
- Simulated usage of the Universal Travel Key to shift between realms.
- Saved data in `ai_interactions.csv` and `travel_logs.csv`.

### ✅ Day 9 – Economy Data & Rewards System
- Created simulated economy data: rewards, items, and hunter earnings.
- Built a rewards system with data on money, fame, and items earned.
- Saved data in `economy_data.csv`.

### ✅ Day 10 – Hunter Achievements, Terrain Logs, AI Interactions
- Generated `terrain_logs.csv` and tracked hunter’s interactions with terrains.
- Saved hunter achievements (kill count, terrain difficulty) in `hunter_achievements.csv`.
- Updated `ai_interactions.csv` for AI and hunter progress tracking.

### ✅ Day 11 – Economy Data and Additional Hunter Stats
- Generated `hunter_stats.csv` with hunter data, including experience points, kills, and earnings.
- Completed terrain logs and achievements for hunters.

---

### ✅ Day 12: Master Data Merging (April 20, 2025)

- Verified column names and structure in:
  - `animals.csv` from `data/raw/`
  - `terrain.csv` from `data/raw/`
  - `hunter.csv` from `data/processed/`
- Standardized data types (e.g., `hunter_id` as string)
- Removed references to missing files like `event.csv`
- Successfully merged all datasets based on:
  - `hunter_id` (animals ↔ hunter)
  - `terrain_name` (animals ↔ terrain)
- Created final enriched dataset `master_data.csv`
- Saved combined output to `data/processed/master_data.csv`
- Previewed sample rows and validated no missing values
- Ready to use this for analytics, dashboards, and event generation

✅ Status: Master data combined and cleaned


## Day 13: Added Hunter Progress Simulation

- Developed `hunter_progress.py` script to simulate and track hunter progress.
  - Tracks terrain exploration, animals hunted, experience points, money, and fame.
  - Data saved in `hunter_progress.csv`.
- Integrated with the overall game data pipeline.


## 📊 Day 14: Power BI Dashboard Sample

A sample dashboard created using the HUNTX master data.

- File: [`HuntX.pbix`](./HuntX.pbix)
- Tool: Power BI Desktop
- Data Used: master_data.csv, hunter_progress.csv, terrain.csv, etc.
- Focus: Game overview, player stats, economy, animal encounters

> 🔍 This dashboard is the starting point for building a futuristic, AI-inspired visualization layer for HuntX.


### Files updated:
- `pipeline/hunter_progress.py`
- `data/hunter_progress.csv` (generated after running the script)

Next steps:
- Use the hunter progress data for analysis and integrate with the ETL pipeline.


## 🚀 Coming Next
- Generate and visualize more advanced realistic detailed dashboards and reports based on collected data.
- Use AWS QuickSight for analysis and reporting.
- Present a complete, data-driven story with visualizations.

---

## 📂 Folder Structure


