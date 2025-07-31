# Synthetic Data Generator - Robotaxi 

This project uses OpenAI's GPT model to generate realistic synthetic data for self-driving cars (e.g., Zoox, Waymo). 

## Features
- JSON schema-based prompt construction
- Generate tabular data logs (speed, GPS, object detection, etc.)
- CLI + Streamlit UI
- Easy EDA via notebook

## Run CLI
```bash
python cli.py generate --schema-path data/robotaxi_schema.json --n 20
```

## Run Streamlit UI
```bash
streamlit run streamlit_app.py
```

## Example Output

| timestamp           | speed | object_in_path | ... |
|---------------------|-------|----------------|-----|
| 2025-07-31T10:22:00 | 48.3  | True           |     |
