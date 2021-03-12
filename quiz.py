question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange \n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n (a) Yellow\n(b) Red\n(c)Blue\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.question_prompt = prompt
        self.answer = answer


questions = {
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
}

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.question_prompt)
        if answer == question.answer:
            score += 1

    print(f"You got {score}/{len(questions)} questions correct")

run_test(questions)
