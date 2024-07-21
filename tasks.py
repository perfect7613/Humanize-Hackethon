from crewai import Task
from tools import tool
from agents import loan_info_agent,loan_recommendation_agent,financial_advisor_agent
from tools import csv_tool


fetch_loan_info_task = Task(
    description=(
        "Retrieve loan offerings from all banks in India based on the provided articles."
    ),
    expected_output='A comprehensive list of loan offerings with details such as interest rates, tenure, and eligibility criteria.',
    tools=[tool],
    agent=loan_info_agent,
)

recommend_banks_task = Task(
    description=(
        "Analyze user {data} and CIBIL score to recommend the best banks for a loan."
    ),
    expected_output='A list of recommended banks based on user information and credit score.',
    tools=[tool],
    agent=loan_recommendation_agent,
    async_execution=False,
)

financialadvisor_task = Task(
    description=(
        "Analyze the user's spending habits based on the data in the CSV file and perform additional financial analysis. "
        "Provide personalized financial advice based on these analyses. Your recommendations should help the user optimize "
        "their spending and saving strategies."
    ),
    expected_output='A detailed financial recommendation report based on the user’s spending habits and additional analysis.',
    tools=[csv_tool],
    agent=financial_advisor_agent,
    async_execution=False,
    output_file='data.md'
)