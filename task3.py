from nltk.chat.util import Chat, reflections
import datetime

schedule = []

pairs = [
    ["hi", ["Hello! How can I help you today?", "Hi there! What brings you here?", "Greetings!"]],
    ["how are you", ["I'm doing well, thank you! How about yourself?", "I'm good! How's your day going?", "I'm fine, thanks!"]],
    ["what's your name", ["I'm known as ChatBot. What's your name?", "Call me ChatBot. What about you?", "I go by ChatBot. And you?"]],
    ["what do you do", ["I'm here to chat, assist, and make your day better!", "I chat with users and try to be helpful.", "I'm a virtual assistant designed for conversations."]],
    ["goodbye", ["Goodbye! If you ever need assistance, feel free to return.", "Farewell! Have a fantastic day.", "See you later!"]],
    ["thanks", ["You're welcome! If you have more questions, feel free to ask.", "No problem! Let me know if there's anything else I can help with.", "Glad I could assist you!"]],
    ["how can I use you", ["Feel free to ask me anything or just have a casual chat. I'm here for you!", "You can interact with me by asking questions or just chatting. What do you feel like doing?", "Ask me anything you'd like to know!"]],
    ["I love you", ["Thank you! I'm here to assist you and provide information.", "That's sweet! I'm here to help you with anything you need.", "I appreciate your kind words!"]],
    ["tell me about yourself", ["I'm a friendly chatbot created to make conversations enjoyable.", "I'm your virtual assistant here to chat and provide information.", "I'm a program designed for interactive and engaging conversations."]],
    ["what is your favorite food", ["I don't have a favorite food, but I'd love to hear about yours! What's your favorite?", "Unfortunately, I don't eat, but I'm curious, what's your favorite food?", "I'm not into food, but I can chat about it with you!"]],
    ["manage my schedule", ["Sure, I can help you manage your schedule. What would you like to do? You can ask me to add, view, or remove events from your schedule."]],
    ["add event to schedule", ["Great! Please provide the details of the event you'd like to add. For example, 'Add meeting at 3 PM tomorrow.'"]],
    ["view schedule", ["Sure, let me fetch your schedule for you. Just a moment..."]],
    ["remove event from schedule", ["Certainly! Could you please specify the event you want to remove?"]],
]

def add_event(event_details):
    schedule.append(event_details)
    return f"Event added: {event_details}"

def view_schedule():
    if not schedule:
        return "Your schedule is empty."
    else:
        return "\n".join(schedule)

def remove_event(event_details):
    if event_details in schedule:
        schedule.remove(event_details)
        return f"Event removed: {event_details}"
    else:
        return "Event not found in your schedule."

def chatbot():
    print("Hi there! I'm a friendly chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)

    while True:
        user_input = input("You: ").lower()

        if user_input == 'quit':
            print("Goodbye! It was nice chatting with you.")
            break
        elif "add" in user_input:
            response = add_event(user_input.replace("add", "").strip())
        elif "view schedule" in user_input:
            response = view_schedule()
        elif "remove" in user_input:
            response = remove_event(user_input.replace("remove", "").strip())
        else:
            response = chat.respond(user_input)

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
