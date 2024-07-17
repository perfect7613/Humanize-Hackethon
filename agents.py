from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool
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


cibil_score_agent=Agent(
    role="CIBIL Score Calculator",
    goal='Calculate the CIBIL score of a user based on their financial {data}.',
    verbose=True,
    memory=True,
    backstory=(
        "Your expertise in credit scoring helps users understand their creditworthiness and eligibility for loans."
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
)