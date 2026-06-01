# Simple Rule-Based Chatbot

A basic Python chatbot that demonstrates fundamental programming concepts including if-elif statements, functions, loops, and input/output operations.

## Overview

This chatbot is designed as an educational project to showcase core Python programming concepts while providing an interactive conversational experience. It uses rule-based matching to respond to user inputs with predefined replies.

## Features

### 1. **Time-Based Greetings** 🕐
- Greets users with context-aware messages based on the time of day
- Morning: "Good morning"
- Afternoon: "Good afternoon"  
- Evening: "Good evening"

### 2. **User Personalization** 👤
- Asks for the user's name at the start
- Uses the name throughout the conversation for a personalized experience
- Example: "Good afternoon, John! How can I help you today?"

### 3. **Flexible Input Handling** 🔤
- Handles punctuation variations (hello!, hello?, hello...)
- Case-insensitive matching
- Removes extra spaces automatically
- Recognizes partial keyword matches
- Works with variations like "hi", "hey", "hello"

## Supported Commands

| Command | Examples | Bot Response |
|---------|----------|--------------|
| Greeting | hello, hi, hey | Time-based greeting with personalization |
| How are you | how are you?, how's it going | Responds and asks about user |
| Name inquiry | what's your name?, who are you? | Introduces itself |
| Goodbye | bye, goodbye, see you, exit, quit | Says farewell with personalization |

## Key Programming Concepts

✅ **if-elif statements** - For matching different user inputs  
✅ **Functions** - Modular code organization (`get_response()`, `clean_input()`, `find_keywords()`, etc.)  
✅ **Loops** - while loop for continuous interaction  
✅ **Input/Output** - `input()` and `print()` for user interaction  
✅ **String operations** - Cleaning and matching text patterns  
✅ **Regular expressions** - Pattern matching with `re` module  
✅ **DateTime** - Getting current time for context-aware responses

## Installation

### Requirements
- Python 3.6 or higher

### Setup
1. Navigate to the project directory:
   ```bash
   cd Basic_Chatbot
   ```

2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## Usage

1. **Start the chatbot:**
   ```bash
   python chatbot.py
   ```

2. **Enter your name** when prompted

3. **Chat** using one of the supported commands

4. **Exit** by typing "bye", "goodbye", "see you", "exit", or "quit"

## Example Conversation

```
============================================================
Welcome to the Enhanced Simple Chatbot!
============================================================

What's your name? Alice

Bot: Good afternoon, Alice! Let's chat!
Type 'hello', 'how are you', 'what's your name', or 'bye'
============================================================

You: hello!
Bot: Good afternoon, Alice! How can I help you today?

You: how are you doing???
Bot: I'm doing great, Alice! Thanks for asking. How about you?

You: what is your name
Bot: I'm a Simple Chatbot! It's nice to meet you, Alice!

You: bye
Bot: Goodbye, Alice! It was great chatting with you. Have a wonderful day!
```

## Code Structure

### Main Functions

- **`get_time_greeting()`** - Returns time-appropriate greeting based on current hour
- **`clean_input(user_input)`** - Removes punctuation and normalizes input
- **`find_keywords(user_input, keyword_list)`** - Flexible keyword matching with partial match support
- **`get_response(user_input, user_name)`** - Main logic for generating responses based on user input
- **`run_chatbot()`** - Main loop that orchestrates the chatbot interaction

### Flow

```
Start → Ask for Name → Display Welcome Message
   ↓
Loop:
   ├─ Get User Input
   ├─ Clean & Analyze Input
   ├─ Generate Response (personalized with user's name)
   ├─ Display Response
   └─ Check if User Said Goodbye → Exit or Continue
```

## Potential Enhancements

Future versions could include:
- Sentiment analysis for emotionally intelligent responses
- Random response variations for more natural conversation
- Conversation history tracking and statistics
- More topics and knowledge base expansion
- Chat logging to files
- Multi-language support

## Learning Outcomes

By studying this code, you'll learn:
- How to structure Python programs with functions
- Control flow with if-elif-else statements
- Working with loops for interactive programs
- String manipulation and pattern matching
- DateTime handling for context-aware features
- Regular expressions for flexible text processing

## License

This project is open source and available for educational purposes.

## Author

Created as an educational chatbot project to demonstrate fundamental Python programming concepts.
