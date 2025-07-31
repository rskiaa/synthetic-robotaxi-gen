import typer
import pandas as pd
from src.prompts import build_prompt
from src.generator import generate_synthetic_data
from src.utils import load_schema

app = typer.Typer()

@app.command()
def generate(schema_path: str = "data/robotaxi_schema.json", n: int = 10):
    schema = load_schema(schema_path)
    prompt = build_prompt(schema, n_samples=n)
    data = generate_synthetic_data(prompt)
    
    if data:
        df = pd.DataFrame(data)
        df.to_csv("synthetic_robotaxi_data.csv", index=False)
        print("✅ Data saved to synthetic_robotaxi_data.csv")
    else:
        print("❌ No data generated.")

if __name__ == "__main__":
    app()
