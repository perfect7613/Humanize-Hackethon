# CrewAI Financial Assistant

The CrewAI Financial Assistant is a sophisticated Python application designed to provide comprehensive financial advice, loan information, and bank recommendations tailored to users' specific financial data. Utilizing advanced AI agents, the application analyzes users' financial data, spending habits, and credit scores to offer personalized advice and recommendations.

- **Youdata Dataset Used Link: https://www.youdata.ai/datasets/65d5c7915e04f50586a72f9c

## Features

- **Loan Information Retrieval**: Fetches detailed information about loan offerings from various banks in India, including interest rates, tenure, and eligibility criteria.
- **Bank Recommendations**: Analyzes users' financial data and CIBIL scores to recommend the best banks for obtaining a loan.
- **Financial Advice**: Provides personalized financial strategies based on users' spending habits, aiming to optimize their spending and saving strategies.

## How It Works

The application leverages the `Crew` framework from the `crewai` package, orchestrating the interaction between different AI agents and tasks. Each agent is specialized in a particular domain:

- **Loan Information Specialist**: Gathers comprehensive details of loan offerings.
- **Loan Recommendation Expert**: Recommends suitable banks for loans based on user data and CIBIL score.
- **Financial Advisor**: Offers financial strategies based on the analysis of spending habits.

These agents utilize tools defined in `tools.py`, including `SerperDevTool` for development purposes and `CSVSearchTool` for analyzing CSV data related to credit card transactions.

## Setup

1. Clone the repository to your local machine.
2. Ensure Python 3.8+ is installed.
3. Create a virtual environment and activate it:

   ```sh
   python -m venv myvenv
   source myvenv/bin/activate # On Windows use `myvenv\Scripts\activate`
4. Install required dependencies by pip install -r requirements.txt