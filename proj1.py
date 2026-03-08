import random
questions={
    "What is  the keyword to a function in python?":"def",
    "Which data type is used to store the true and false?":"Boolean",
    "what is the coorect file extension for python?":".py",
    "Which symbol is used to comment in python?":"#",
    "what the function is used to get the input fomr user?":"input",
    "how do you start a for loop in python?":"for",
    "what is the output for 2**3?":"8",
    "what the keyword is used to import a module in python?":"import",
    "what does the length func returns?":"Length",
    "What is the result of 10//3 in python?":"3"
}
q_list=list(questions.keys())
total_questions=5
score=0
selected_questions=random.sample(q_list,total_questions)

for  idx,question in enumerate(selected_questions):
    print(f"{idx+1}.{question}")
    
    user_answer=input("enter your answer:").lower().strip()
    correct_answer=questions[question]
    if user_answer==correct_answer.lower():
        print("Correct!\n")
        score+=1
    else:
        print(f"Wrong.the coorect answer is:{correct_answer}.\n")
        print(f"game over! your final score is:{score}/{total_questions}")


