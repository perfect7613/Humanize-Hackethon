from crewai import Task
from tools import tool
from agents import loan_info_agent,cibil_score_agent,loan_recommendation_agent


fetch_loan_info_task = Task(
    description=(
        "Retrieve loan offerings from all banks in India based on the provided articles."
    ),
    expected_output='A comprehensive list of loan offerings with details such as interest rates, tenure, and eligibility criteria.',
    tools=[tool],
    agent=loan_info_agent,
)


calculate_cibil_score_task = Task(
    description=(
        "Calculate the CIBIL score based on the user's {data} and financial information."
    ),
    expected_output='The calculated CIBIL score and an explanation of how it impacts loan eligibility.',
    tools=[tool],
    agent=cibil_score_agent,
    async_execution=False,
)

recommend_banks_task = Task(
    description=(
        "Analyze user {data} and CIBIL score to recommend the best banks for a loan."
    ),
    expected_output='A list of recommended banks based on user information and credit score.',
    tools=[tool],
    agent=loan_recommendation_agent,
    async_execution=False,
    output_file='data.md'
)