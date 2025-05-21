def build_prompt(documents: dict, rules: list) -> str:
    prompt = "You are a compliance auditor. Validate the invoice using these rules:\n"
    prompt += "\n".join([f"{i+1}. {rule}" for i, rule in enumerate(rules)])
    prompt += "\n\nProvided documents (some may be missing):\n"

    for name, content in documents.items():
        if content:
            prompt += f"\n--- {name.upper()} ---\n{content.strip()}\n"

    #prompt += "\n\nReturn a JSON report with each rule, PASS/FAIL, and justification."
    prompt += "\n\nReturn a JSON. Here is the sample output : \nInvoice_INV1001 – Compliance Report  \n✅ PO Matched: PO505 \n✅ GRN Matched: GRN802 \n❌ Quantity Mismatch: Item B (Invoice: 3 > GRN: 2) \n❌ Unit Price Mismatch: Item B ($25 vs $20 in PO) \n✅ Total Amount Within Tolerance \n✅ Invoice Date ≥ GRN Date \n ✅ Vendor Approved (TechSupply Inc.) \n\nFinal Status: FAIL (2 issues found). \nBe very strict in evaluation. No assumptions. Don't tolerate typos. STRICTLY follow the given sample output format. Return ONLY the final JSON report and in given sample format only."
    return prompt