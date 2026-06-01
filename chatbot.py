from datetime import datetime
import re


def get_time_greeting():
    """
    Return a greeting based on the current time of day.
    
    Returns:
        str: Time-appropriate greeting
    """
    hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def clean_input(user_input):
    """
    Clean user input by removing punctuation and extra spaces.
    
    Args:
        user_input (str): Raw user input
        
    Returns:
        str: Cleaned input
    """
    # Remove punctuation and convert to lowercase
    cleaned = re.sub(r'[?!.,;:]', '', user_input.lower().strip())
    return cleaned


def find_keywords(user_input, keyword_list):
    """
    Check if any keywords from keyword_list appear in user_input.
    Handles partial matches and punctuation variations.
    
    Args:
        user_input (str): User's message
        keyword_list (list): List of keywords to search for
        
    Returns:
        bool: True if any keyword is found
    """
    cleaned_input = clean_input(user_input)
    
    for keyword in keyword_list:
        keyword_clean = clean_input(keyword)
        # Check for exact match or partial match
        if keyword_clean in cleaned_input or cleaned_input in keyword_clean:
            return True
    
    return False


def get_response(user_input, user_name):
    """
    Match user input to predefined responses with personalization.
    
    Args:
        user_input (str): The user's input message
        user_name (str): The user's name for personalization
        
    Returns:
        str: The chatbot's response
    """
    if not user_input.strip():
        return "Please say something!"
    
    # Greeting keywords
    if find_keywords(user_input, ["hello", "hi", "hey"]):
        time_greeting = get_time_greeting()
        return f"{time_greeting}, {user_name}! How can I help you today?"
    
    # How are you keywords
    elif find_keywords(user_input, ["how are you", "how's it going", "how you doing"]):
        return f"I'm doing great, {user_name}! Thanks for asking. How about you?"
    
    # Name inquiry
    elif find_keywords(user_input, ["what is your name", "what's your name", "who are you"]):
        return "I'm a Simple Chatbot! It's nice to meet you, " + user_name + "!"

    # Feelings inquiry
    elif find_keywords(user_input, ["i love you", "I like you", "I watch you"]):
        return f"Ohhh, I love you too, {user_name}! But you know I'm a simple chatbot, I can't feel emotions. However, I'm here to chat and help you with anything you need!"

    # Goodbye keywords
    elif find_keywords(user_input, ["bye", "goodbye", "see you", "exit", "quit"]):
        return f"Goodbye, {user_name}! It was great chatting with you. Have a wonderful day!"
    
    else:
        return f"I'm sorry, {user_name}, I don't understand that. Try 'hello', 'how are you', 'what's your name', or 'bye'."


def run_chatbot():
    """
    Run the chatbot in a loop until the user says goodbye.
    """
    print("=" * 60)
    print("Welcome to the Enhanced Simple Chatbot!")
    print("=" * 60)
    print()
    
    # Get user's name for personalization
    user_name = input("What's your name? ").strip()
    if not user_name:
        user_name = "Friend"
    
    print()
    time_greeting = get_time_greeting()
    print(f"Bot: {time_greeting}, {user_name}! Let's chat!")
    print("Type 'hello', 'how are you', 'what's your name', or 'bye'")
    print("=" * 60)
    print()
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        # Check for empty input
        if not user_message:
            print("Bot: Please say something!\n")
            continue
        
        # Get and display bot response
        bot_response = get_response(user_message, user_name)
        print(f"Bot: {bot_response}\n")
        
        # Exit if user says goodbye
        if find_keywords(user_message, ["bye", "goodbye", "see you", "exit", "quit"]):
            break


if __name__ == "__main__":
    run_chatbot()
