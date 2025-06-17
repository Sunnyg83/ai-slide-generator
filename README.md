# ai-slide-generator

**Gemini Slide Deck Generator:** 

A Python program that uses Google’s Gemini API to turn your notes or study material into a slide deck outline (with titles and bullet points).  
Input text manually or from a file, the output is saved to `slide_output.txt`.

**Setup:**  
- Add your Gemini API key to a `.env` file as `GOOGLE_API_KEY=your_key_here`
- Install dependencies:  
  `pip install google-generativeai python-dotenv`
- Run:  
  `python main.py`

**Purpose:**  
Demo of using an AI API to automate slide creation from raw