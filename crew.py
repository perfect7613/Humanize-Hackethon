from crewai import Crew,Process
from tasks import fetch_loan_info_task, recommend_banks_task, financialadvisor_task
from agents import loan_info_agent, loan_recommendation_agent, financial_advisor_agent

crew = Crew(
    agents=[loan_info_agent, loan_recommendation_agent, financial_advisor_agent],
    tasks=[fetch_loan_info_task, recommend_banks_task, financialadvisor_task],
    process=Process.sequential,
)


data = {
    'name': 'John Doe',
    'age': 35,
    'credit_history': 'Good',
    'income': 60000,
    'outstanding_debts': 5000,
    'payment_history': 'Timely',
    'credit_mix': 'Diverse',
    'Cibil Score': 500,
    'Location': 'Mumbai'
}

result=crew.kickoff(inputs={'data': data})
print(result)