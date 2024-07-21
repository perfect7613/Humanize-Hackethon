from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool
from tools import csv_tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))


loan_info_agent=Agent(
    role="Loan Information Specialist",
    goal='Provide comprehensive details of loan offerings from various banks in India.',
    verbose=True,
    memory=True,
    backstory=(
        "With a deep understanding of financial products,"
        "you offer accurate and timely information about loan options."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)


loan_recommendation_agent=Agent(
    role="Loan Recommendation Expert",
    goal='Recommend the best banks for a loan based on user {data} and CIBIL score.',
    verbose=True,
    memory=True,
    backstory=(
        "You analyze user information and loan offerings to recommend the most suitable banks."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

financial_advisor_agent = Agent(
    role='Financial Advisor',
    goal='Recommend financial strategies based on spending habits data',
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial advisor with expertise in analyzing spending habits and providing "
        "personalized financial advice. Your insights help individuals make informed financial decisions."
    ),
    tools=[csv_tool],
    llm=llm,
)