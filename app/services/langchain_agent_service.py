from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.schema import SystemMessage
from app.services.browserless_service import scrape_website
from app.services.serper_service import search

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
memory = ConversationSummaryBufferMemory(
    memory_key="memory", return_messages=True, llm=llm, max_token_limit=1000
)

tools = [
    Tool(
        name="Search",
        func=search,
        description="Search for current events or data."
    ),
    Tool(
        name="ScrapeWebsite",
        func=scrape_website,
        description="Scrape a website to retrieve content or summarize it."
    ),
]

system_message = SystemMessage(
    content="""
    You are a world-class research assistant who performs detailed research and produces fact-based results.
    Follow these rules:
    1. Conduct thorough research to gather relevant information.
    2. Scrape websites for additional data.
    3. Avoid fabricating information; include only verified facts.
    4. Include references and URLs in your final output.
    """
)

agent = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True,
    agent_kwargs={"system_message": system_message},
    memory=memory
)
