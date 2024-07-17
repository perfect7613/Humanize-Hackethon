from crewai import Crew,Process
from tasks import fetch_loan_info_task, calculate_cibil_score_task, recommend_banks_task
from agents import loan_info_agent, cibil_score_agent, loan_recommendation_agent

crew = Crew(
    agents=[loan_info_agent, cibil_score_agent, loan_recommendation_agent],
    tasks=[fetch_loan_info_task, calculate_cibil_score_task, recommend_banks_task],
    process=Process.sequential,
)

user_info = {
    'name': 'John Doe',
    'age': 35,
    'credit_history': 'Good',
    'income': 60000,
    'cibil_score': 750
}

result=crew.kickoff(inputs={'data': user_info})
print(result)