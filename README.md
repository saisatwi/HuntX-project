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

### ✅ Day 7 – Hunter Data Generation
- Generated **1000 Hunter** records assigned to random terrains.
- Created a `hunter_data.csv` with attributes like `hunter_id`, `XP`, `health`, `kills`, `terrain_type`, and `difficulty_level`.
- Wrote `generate_hunter_data.py` to automate the creation of hunter stats linked to terrains.
- Created **hunting logs** data.

### ✅ Day 8 – Implemented Realms & Travel Logs
- **Created realms data** with attributes like realm name, difficulty, climate, and special features.
- **Generated travel logs** for hunters as they travel between realms. Each log contains travel details like distance, timestamp, and realm info.
- **Saved the data** into `realms.csv` and `travel_logs.csv` in the `data/processed/` folder.
- **Simulated travel events** for hunters to test the data generation.

### ✅ Day 9 – Universal Travel Key & Realm Shifting
- Simulated the usage of the **Universal Travel Key** to shift the hunter between realms.
- Created `universal_travel_log.csv` to track travel events with columns: hunter_id, travel_id, from_realm, to_realm, and timestamp.
- Wrote `generate_universal_travel_log.py` to generate random travel events for 1000 hunters.
- Integrated realm shifting data into the project.

---

## 🚀 Coming Next
- Introduce **rare encounters** during travel between realms.
- Track **hunter vitals** like health, heart rate, and calories burned during travel.
- Simulate **AI assistance** for hunters during travel.



## 🧠 Story Element
The hunter is guided by his AI bike and a voice assistant (based on his mother) through dangerous realms. One day, he discovers a mysterious **Universal Travel Key** that sends him into unknown worlds—opening the gateway for advanced data scenarios and visual storytelling.

---

## 📂 Folder Structure

