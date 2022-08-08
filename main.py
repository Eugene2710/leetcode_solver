#streamlit application
import streamlit as st
from openai_utils import get_leetcode_solution

st.header("Leetcode Question:")
leetcode_question: str = st.text_area("copy and paste your leetcode question here", height=650)

if st.button("Get Leetcode Solution:"):
    leetcode_answer: str = get_leetcode_solution(leetcode_question)
    st.header("Leetcode Answer")
    st.text(leetcode_answer)