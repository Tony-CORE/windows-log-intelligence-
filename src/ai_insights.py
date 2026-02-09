import openai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_operational_insights(summary_df):
    """
    Uses GenAI to convert raw infrastructure logs into
    business-friendly operational insights.
    """

    prompt = f"""
    You are an Infrastructure Operations expert.

    Analyze the following Windows Event Log summary and provide:
    1. Key operational risks
    2. Probable root causes
    3. Actionable remediation steps

    Event Summary:
    {summary_df.to_string(index=False)}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior infrastructure reliability engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    from log_analyzer import analyze_windows_event_failures

    summary = analyze_windows_event_failures("../data/eventlog.csv")
    insights = generate_operational_insights(summary)

    print("\n--- AI Generated Operational Insights ---\n")
    print(insights)
