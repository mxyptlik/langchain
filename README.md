GitHub README
🧠 AI-Powered Utility Suite
A comprehensive project combining multiple AI-driven tools to simplify tasks like PDF summarization, translation, YouTube content creation, and more. This suite is built with OpenAI's GPT models, LangChain, and Streamlit/Gradio to empower users with cutting-edge AI capabilities.

🚀 Features
1. YouTube Content Generator
Generate compelling YouTube video titles and scripts based on a given topic.

Input: Topic prompt.
Output: AI-generated video title and script, leveraging Wikipedia research for enhanced context.
Framework: Streamlit.
2. Language Translator
Translate text or entire PDFs into diverse languages.

Input: Text or PDF file and target language.
Output: Translated text or file in the desired language.
Framework: Gradio.
3. PDF Summarizer
Extract and summarize key insights from PDFs.

Input: PDF file path.
Output: Concise AI-generated summary saved as a .txt file.
Frameworks: Gradio & CLI (Command Line Interface).
4. Standalone PDF Summarization Script
A simpler implementation of the summarizer for direct use with no GUI.

📋 How It Works
YouTube Content Generator
Input a topic into the Streamlit app.
Generates:
A YouTube video title based on the topic.
A video script using additional research from Wikipedia.
Output includes a history of titles, scripts, and research results.
Language Translator
Enter the text or upload a PDF in the Gradio app.
Specify the language you want the content translated into.
View and download translated results.
PDF Summarizer
Input a PDF file path into the app or script.
The tool processes each page, generates summaries using GPT, and outputs a .txt file.
🛠️ Installation
Prerequisites
Python 3.9+
OpenAI API Key
Required Python libraries:
bash
Copy code
pip install openai PyPDF2 gradio streamlit langchain tiktoken  
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/ai-utility-suite.git  
Navigate to the project folder:

bash
Copy code
cd ai-utility-suite  
Add your OpenAI API key in a file named apikey.py:

python
Copy code
apikey = "your_openai_api_key"  
Run the desired tool:

YouTube Content Generator:
bash
Copy code
streamlit run youtube_content_generator.py  
Language Translator:
bash
Copy code
python language_translator.py  
PDF Summarizer:
bash
Copy code
python pdf_summarizer.py  
🖼️ Example Usage
YouTube Content Generator
Open the app with:
bash
Copy code
streamlit run youtube_content_generator.py  
Input your topic.
Get a title and script, with research history saved for future reference.
Language Translator
Run the Gradio app:
bash
Copy code
python language_translator.py  
Input text or upload a PDF, then specify the target language.
Download the translated content.
PDF Summarizer
Provide the PDF file path in the input field.
Get the summary saved as a .txt file.
🔧 Tools Used
Frameworks: Streamlit, Gradio
Libraries: LangChain, PyPDF2, Tiktoken
API: OpenAI GPT Models
💡 Future Enhancements
Integration: Combine all tools into a single unified app.
File Uploads: Allow users to upload files directly via the interface.
Customization: Support for advanced settings like summarization depth or translation tone.
🤝 Contributing
Contributions are welcome! If you have ideas or suggestions, feel free to fork the repository and submit a pull request.

📜 License
This project is open-source under the MIT License.

🌟 Acknowledgments
Special thanks to OpenAI and the creators of LangChain, Streamlit, and Gradio for their exceptional tools.
