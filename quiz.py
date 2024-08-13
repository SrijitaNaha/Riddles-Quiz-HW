import tkinter as tk
from tkinter import messagebox

questions = [
    "What is middle of Paris ?",
    "Which word is spelt wrong in every dictionary?",
    "What can you catch but not throw?",
    "What animal can run the fastest- an elephant, squirrel or a mouse?",
    "I am an odd number, but if you take away just a single letter I become even. Can you guess my number?",
    "I'm tall when I'm young, and I'm short when I'm old, what am I?",
    "What is so fragile that saying its name breaks it?",
    "What has four eyes but can't see?",
    "What has a head, a tail, but no body?",
    "Where can you find cities, towns, shops, and streets but no people?",
    "What has a neck but no head?"
]
answers = [
    "A",
    "Wrong",
    "cold",
    "mouse",
    "Seven",
    "candle",
    "Silence",
    "potato",
    "coin",
    "map",
    "bottle"
]

current_question = 0
score = 0

def check_answer():
    global current_question, score
    user_answer = answer_entry.get()
    if user_answer.lower() == answers[current_question].lower():
        score += 1
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {answers[current_question]}")
    current_question += 1
    if current_question < len(questions):
        question_label['text'] = questions[current_question]
        answer_entry.delete(0, tk.END)
    else:
        question_label['text'] = "Quiz finished!"
        answer_entry.delete(0, tk.END)
        answer_entry['state'] = 'disabled'
        submit_button['state'] = 'disabled'
    score_label['text'] = f"Score: {score}"

root = tk.Tk()
root.title("Quiz App")

root.configure(bg='#f0f0f0')  # Set the background color of the root window

question_label = tk.Label(root, text=questions[current_question], wraplength=400, font=('Arial', 14), fg='#00698f', bg='#f0f0f0')  # Set the font, foreground and background color of the question label
question_label.pack(pady=20)

answer_entry = tk.Entry(root, width=50, font=('Arial', 14), fg='#00698f', bg='#ffffff')  # Set the font, foreground and background color of the answer entry
answer_entry.pack(pady=20)

submit_button = tk.Button(root, text="Submit", command=check_answer, font=('Arial', 14), fg='#ffffff', bg='#00698f')  # Set the font, foreground and background color of the submit button
submit_button.pack(pady=20)

score_label = tk.Label(root, text="Score: 0", font=('Arial', 14), fg='#00698f', bg='#f0f0f0')  # Set the font, foreground and background color of the score label
score_label.pack(pady=20)

root.mainloop()