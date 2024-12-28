from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import logging
import os

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Load environment variables from the .env file
load_dotenv()

def summarize_text(objective: str, content: str) -> str:
    """
    Summarizes long text content using OpenAI LLM.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500
    )
    docs = text_splitter.create_documents([content])

    map_prompt = PromptTemplate(
        template="""
        Write a summary of the following text for {objective}. The text may contain irrelevant information.
        Only summarize relevant information while keeping factual details intact:
        "{text}"
        SUMMARY:
        """,
        input_variables=["text", "objective"]
    )

    summary_chain = load_summarize_chain(
        llm=llm, chain_type='map_reduce',
        map_prompt=map_prompt, combine_prompt=map_prompt, verbose=True
    )
    return summary_chain.run(input_documents=docs, objective=objective)
