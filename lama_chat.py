import io
import openai
# replace YOUR_API_KEY with your actual API key for the ChatGPT service
openai.api_key = "My key"
text = "What is OOPs? It stands for Object - Oriented Programming. It is based on objects It follows Bottom - up programming approach. It is based on real world. It provides data hiding so it is very secure. It provides reusability feature. What is a clas s? It is a user defined data type that act as a template for creating objects of the identical type. A large number of objects can be created using the same class. Theref ore, Class is considered as the blueprint for the object. What is an object? An object is a real world entity which have properties and functionalities. Object is also called an instance of class. Objects take some space in memory. For eg . Fruit is cl ass and its object s are mango ,apple , banana Furniture is class and its objects are table , chair , desk What is the difference between a class and an object? Class Object 1. It is a collection of objects. It is an instance of a class. 2. It doe sn't take up space in memory. It takes space in memory. 3. Class does not exist physically Object exist physically. 4. Classes are declared just once Objects can be declared as and when required "

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

print(final_result(text))










