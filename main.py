import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env and configure Gemini
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

def build_prompt(text):
    return f"""
You are an AI study assistant. Given the following study material, break it down into a slide deck format.

Instructions:
- Create 3 to 5 slides.
- Each slide should have a short, clear title and 3 to 5 concise bullet points.
- Use simple, student-friendly language.
- Don't copy the input directly—summarize and rephrase clearly.

Input Text:
{text}
"""

def generate_slides(text):
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = build_prompt(text)
    response = model.generate_content(prompt)
    return response.text

def read_input_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def save_output_to_file(output, filename="slide_output.txt"):
    with open(filename, 'w') as f:
        f.write(output)
    print(f"\n Slide deck saved to {filename}")

if __name__ == "__main__":
    print("AI Slide Deck Generator (Gemini Version)")
    choice = input("Use text from file? (y/n): ").strip().lower()

    if choice == 'y':
        path = input("Enter file path (default: sample_input.txt): ").strip() or "sample_input.txt"
        input_text = read_input_file(path)
    else:
        print("Enter your text (end with an empty line):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        input_text = "\n".join(lines)

    print("\n Generating slides...")
    slides = generate_slides(input_text)
    print("\n Slide Deck Output:\n")
    print(slides)
    save_output_to_file(slides)