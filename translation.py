import gradio as gr
import os
import openai
from openai import OpenAI
from apikey import apikey
from langchain.prompts import PromptTemplate
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
import PyPDF2


os.environ["OPENAI_API_KEY"] = apikey

llm = ChatOpenAI(temperature=0.0)


input_text = gr.components.Textbox(label="Enter text you want to translate")
input_lang = gr.components.Textbox(label="Enter language your translating to")
input_pdf_path = gr.components.Textbox(label="Enter file path to pdf file")


def translate(input_text, input_lang):
    client = OpenAI()
    GPT_MODEL = "gpt-3.5-turbo"
    messages = [
        {
            "role": "system",
            "content": "your an helpful assistant that helps in translation across diverse languages",
        },
        {
            "role": "user",
            "content": f"translate this: {input_text} to this language: {input_lang}",
        },
    ]
    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        temperature=0.4,
    )

    translated_text = response.choices[0].message.content
    return translated_text


# result = translate(
#     "Love your neighbors as yourself",
#     "spanish",
# )
# print(result)


output_translate = gr.components.Textbox(label=f"translation ")

interface = gr.Interface(
    fn=translate,
    inputs=[input_text, input_lang],
    outputs=output_translate,
    title="Language Translator",
    description="translate your text in a jiffy",
).launch(share=True)


def translate_pdf(input_pdf_path, input_lang):
    client = OpenAI()
    pdf_translated_text = ""
    pdf_file_path = input_pdf_path
    pdf_file = open(pdf_file_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(0, len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text().lower()

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "your an helpful assistant that helps in translation across diverse languages",
                },
                {
                    "role": "user",
                    "content": f"translate this: {page_text} to this language: {input_lang}",
                },
            ],
            model="gpt-3.5-turbo",
            temperature=0.2,
            n=3,
            max_tokens=3000,
        )
        page_translate = response.choices[0].message.content
        pdf_translated_text += page_translate + "\n" * 3
        pdf_translated_file = pdf_file_path.replace(
            os.path.splitext(pdf_file_path)[1], "_translated.txt"
        )
        with open(pdf_translated_file, "w+") as file:
            file.write(pdf_translated_text)
    pdf_file.close()
    return page_translate, pdf_translated_file
