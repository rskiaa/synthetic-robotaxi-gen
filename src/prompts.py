def build_prompt(schema: dict, n_samples: int = 10) -> str:
    prompt = f'''Generate {n_samples} synthetic sensor logs for a self-driving robotaxi system. 
Each record should contain:
'''
    for field, dtype in schema.items():
        prompt += f"- {field}: {dtype}\n"
    prompt += "Output should be a JSON list of dictionaries."
    return prompt
