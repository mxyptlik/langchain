import openai
import tiktoken
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.llms import openai
from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from apikey import apikey
import os
import tiktoken
import gradio as gr

os.environ["OPENAI_API_KEY"] = apikey

llm = ChatOpenAI(temperature=0.0)


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    print(encoding.encode(string))
    num_tokens = len(encoding.encode(string))

    return num_tokens


def summarize_pdf(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    docs = loader.load_and_split()
    chain = load_summarize_chain(llm=llm, chain_type="map_reduce")
    summary = chain.run(docs)
    return summary


# pdf_file = input("Enter file path to pdf file")
# summarize = summarize_pdf(pdf_file)

# summarize

# gradio

input_pdf_path = gr.components.Textbox(label="Enter file path to pdf file")
output_summary = gr.components.Textbox(label="Summary")

interface = gr.Interface(
    fn=summarize_pdf,
    inputs=input_pdf_path,
    outputs=output_summary,
    title="PDF summarizer",
    description="Provide PDF path to get the summary",
).launch(share=True)

# 2
#  recall to always add .pdf at the end of the file
