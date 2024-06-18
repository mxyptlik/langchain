import os
import PyPDF2
import re
import openai
from openai import OpenAI
from apikey import apikey

os.environ["OPENAI_API_KEY"] = apikey
client = OpenAI()

pdf_summary_text = " "
pdf_file_path = (
    r"C:\Users\User\Downloads\Telegram Desktop\ECN111 DEMAND AND SUPPLY ANALYSIS.pdf"
)
pdf_file = open(pdf_file_path, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)

for page_num in range(0, len(pdf_reader.pages)):
    page_text = pdf_reader.pages[page_num].extract_text().lower()

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "your an helpful assistant that is very ood at summarization",
            },
            {
                "role": "user",
                "content": f"summarize this: {page_text}",
            },
        ],
        model="gpt-3.5-turbo",
        temperature=0.2,
        n=3,
        max_tokens=3000
    )
    page_summary = response.choices[0].message.content
    pdf_summary_text += page_summary + "\n" * 3
    pdf_summary_file = pdf_file_path.replace(
        os.path.splitext(pdf_file_path)[1], "_summary.txt"
    )
    with open(pdf_summary_file, "w+") as file:
        file.write(pdf_summary_text)

pdf_file.close()
