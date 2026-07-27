import json

from ai.llm import ask_gemini


def analyze_intent(user_question):
    """
    Analyze the user's question and return structured intent.
    """

    prompt = f"""
You are an AI Intent Analyzer.

Your ONLY job is to understand the user's question.

DO NOT generate SQL.

Return ONLY valid JSON.

Extract:

1. intent
2. entity
3. metric
4. operation
5. limit
6. filters

Possible intents:

- aggregation
- ranking
- filtering
- comparison
- listing
- trend
- count
- unknown

Possible operations:

- sum
- avg
- max
- min
- count
- top
- bottom
- list
- compare
- trend

Return EXACTLY this JSON format:

{{
    "intent": "",
    "entity": "",
    "metric": "",
    "operation": "",
    "limit": null,
    "filters": []
}}

USER QUESTION:

{user_question}
"""

    response = ask_gemini(prompt)

    try:
        return json.loads(response)

    except Exception:

        return {
            "intent": "unknown",
            "entity": "",
            "metric": "",
            "operation": "",
            "limit": None,
            "filters": []
        }