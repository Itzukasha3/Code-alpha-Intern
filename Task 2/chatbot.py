import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a program, but I'm functioning as expected! How about you?",
        "what is your name": "I'm a chatbot created to assist you. You can call me ChatBot!",
        "bye": "Goodbye! Have a great day!","what can you do": "I can chat with you! Ask me anything, and I'll do my best to help.",
        "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "who created you": "I was created by a itzukasha3 who loves AI and chatbots!",
        "what is AI": "AI stands for Artificial Intelligence, the simulation of human intelligence by machines.",
        "where are you from": "I exist in the digital world, wherever you need me!",
        "thank you": "You're welcome! I'm here to help.",
        "what's the weather like": "I can't check the weather right now, but you can use a weather app!",
        "how old are you": "I was created recently, but in the digital world, time works differently!",
        "tell me a fun fact": "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still good to eat!",
        "do you like music": "I don't have ears, but I know that music is a universal language!",
        "what's your favorite color": "I like all colors equally! But if I had to choose, maybe green—it reminds me of progress!",
        "what's your purpose": "My purpose is to assist and chat with you! Feel free to ask me anything."
    }
    return responses.get(user_input.lower(), "I'm sorry, I don't understand that. Can you rephrase?")

def send_message():
    user_input = entry_field.get()
    if user_input.strip():
        chat_window.insert(tk.END, f"You: {user_input}\n", "user")
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, f"ChatBot: {response}\n", "bot")
        entry_field.delete(0, tk.END)
        chat_window.yview(tk.END)
        
        if user_input.lower() == "bye":
            root.after(1500, root.quit)

# Creating the main GUI window
root = tk.Tk()
root.title("ChatBot")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10, padx=10)
chat_window.config(state=tk.NORMAL)
chat_window.tag_configure("user", foreground="blue")
chat_window.tag_configure("bot", foreground="green")
chat_window.insert(tk.END, "ChatBot: Hello! Type 'bye' to exit.\n", "bot")

# Entry field and send button
entry_field = tk.Entry(root, font=("Arial", 14))
entry_field.pack(pady=5, padx=10, fill=tk.X)
entry_field.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message, bg="#4CAF50", fg="white")
send_button.pack(pady=5)

root.mainloop()
