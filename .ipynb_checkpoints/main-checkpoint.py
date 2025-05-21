import json
from file_loader import extract_text_from_file
from prompt_builder import build_prompt
from compliance_validator import validate_compliance

def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    groq_config = config["groq"]
    file_paths = config["files"]
    rules = config["rules"]

    # Loading and extracting documents...
    documents = {}
    for name, path in file_paths.items():
        try:
            documents[name] = extract_text_from_file(path)
            #print(f"Loaded: {name} from {path}")
        except Exception as e:
            #print(f"Skipped {name}: {e}")
            documents[name] = None

    # Building prompt...
    prompt = build_prompt(documents, rules)

    # Sending the prompt to Groq
    response = validate_compliance(prompt, groq_config)

    response_list = response.split("\n")

    final_response = ""
    for i in range(2, len(response_list)-1):
        final_response = final_response + response_list[i] + "\n"

    print("Invoice_" + file_paths["invoice"].split("/")[-1].split(".")[0] + " – Compliance Report\n")
    print(final_response)

if __name__ == "__main__":
    main()