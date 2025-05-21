from groq import Groq

def validate_compliance(prompt: str, groq_config: dict) -> str:
    groq_client = Groq(api_key=groq_config["api_key"])
    response = groq_client.chat.completions.create(
        model=groq_config["model"],
        messages=[
            {"role": "system", "content": "You are a finance and procurement auditor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content