import io
import openai
import os
# replace YOUR_API_KEY with your actual API key for the ChatGPT service

openai.api_key = "key"

def summarize_text(text):
    prompt = (f"please summarize the flowing text: \n{text}")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=100,
    )

    summary = response.choices[0].text.strip()
    return summary

def generate_exams(summarized_text):

    prompt = (f"please create three multiple choices questions with three questions from the flowing text: \n{summarized_text} response as json request then display it as html form")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=100,)
    questions = response.choices[0].text.strip()

    return questions

def answers_exams(generated_exams):
    prompt = (f"please provied answers to thoes questions: \n{generated_exams}")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        n=1,
        stop=None,
        timeout=100,)
    answers = response.choices[0].text.strip()

    return answers

def final_result(text):
    summarized_text = summarize_text(text)
    generated_exams = generate_exams(summarized_text)
    array_generated_exams = generated_exams.split('\n')
    return array_generated_exams











