import os
import openai
from openai import Completion
from openai.openai_object import OpenAIObject
from typing import List, Dict, Any

# type hint
# list API keys as environment variables so that the keys are not exposed as string variables which affects the security
# openai.api_key = os.getenv("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", "")
openai.api_key = "" #insert the openai codex api key here
completion_object: Completion = Completion()

def get_leetcode_solution(leetcode_question: str) -> str:

    prompt: str = f"""
    Give a Python Solution for the leetcode question below. Leave comments for exactly how the solution solves it step-wise.
    
    Leetcode Question: {leetcode_question}
    
    Python Solution:
    
    """

    response: OpenAIObject = completion_object.create(
        model="code-davinci-002",
        prompt=prompt,
        max_tokens=1000,
    )

    # key of type string, value of type any
    leetcode_solution: List[Dict[str, Any]] = response['choices'][0]["text"]
    return leetcode_solution

