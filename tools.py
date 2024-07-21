from dotenv import load_dotenv
load_dotenv()
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool
from crewai_tools import CSVSearchTool

tool = SerperDevTool()

config = dict(
    llm=dict(
        provider="google",
        config=dict(model='gemini-1.5-flash')
    )
)

csv_tool = CSVSearchTool(csv='./data/Credit_card_transactions_-_India_-_Simple.csv', config=config)