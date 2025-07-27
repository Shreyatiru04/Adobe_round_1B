import os
import json
from PyPDF2 import PdfReader
from datetime import datetime

def summarize(pdf_path):
    reader = PdfReader(pdf_path)
    content = []
    for page_num, page in enumerate(reader.pages, 1):
        text = page.extract_text()
        if text:
            content.append((page_num, text.strip()))
    return content

def main():
    input_dir = "/app/input"
    persona_file = os.path.join(input_dir, "persona.json")

    with open(persona_file, "r") as f:
        persona_data = json.load(f)

    result = {
        "metadata": {
            "input_documents": [f for f in os.listdir(input_dir) if f.endswith(".pdf")],
            "persona": persona_data["persona"],
            "job": persona_data["job"],
            "timestamp": str(datetime.now())
        },
        "extracted_sections": []
    }

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            content = summarize(os.path.join(input_dir, file))
            for i, (page, text) in enumerate(content[:3]):  # Simple top-3 pages heuristic
                result["extracted_sections"].append({
                    "document": file,
                    "page_number": page,
                    "section_title": text.split("\n")[0][:100],
                    "importance_rank": i + 1,
                    "refined_text": text[:500]
                })

        # Write final JSON output
    with open("/app/output/output.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
