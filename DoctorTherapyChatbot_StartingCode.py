"""
File: DoctorTherapyChatbot_StartingCode.py

Conducts an interactive session of nondirective psychotherapy.
"""
import random

# hedges and qualifiers list
hedges = [
    "Please tell me more.",
    "Many people feel the same way.",
    "Go on, I’m listening.",
    "That’s interesting, please continue.",
    "Can you tell me more about that?"
]
qualifiers = [
    "Why do you say that ",
    "You seem to think that ",
    "Can you explain why ",
    "What makes you feel that ",
    "Do you believe that "
]
# switch words --first person to second person
replacements = {
    "i": "you",
    "me": "you",
    "my": "your",
    "am": "are",
    "we": "you",
    "us": "you",
    "mine": "yours"
}

skip_words = ["yes", "no", "well", "um", "uh", "umm", "uhh", "kinda", "kind of"]


def changePerson(sentence):
    """Change first-person words to second-person words."""
    words = sentence.split()
    new_words = []

    for word in words:
        lower_word = word.lower()  
        if lower_word in replacements:
            new_words.append(replacements[lower_word])
        else:
            new_words.append(word)
    return " ".join(new_words)

def cleanSentence(sentence):
    """Removing filler words from the start."""
    words = sentence.split()
    while words and words[0].lower() in skip_words:
        words.pop(0)
    return " ".join(words)

def reply(sentence):
    """Generate reply using a hedge or qualifier."""
    check_sentence = sentence.lower()

    # Special responses
    if "they are my co-workers" in check_sentence:
        return "Oh, your co-workers. How do you feel about them?"
    elif "we are working with them" in check_sentence:
        return "It sounds like teamwork is important to you."
    elif "you are not a helpful therapist" in check_sentence:
        return "I’m sorry you feel that way. Why do you think that?"

    if random.randint(1, 3) == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def main():
    print("Hello, I hope you are well today.")
    print("Let's start off with you telling me how you are currently feeling today.")
    print('(Type "quit" to end the session.)')

    while True:
        user_input = input("\n>> ")
        if user_input.lower() == "quit":
            print("Have a wonderful day!")
            break
        print(reply(user_input))

# Run chatbot
main()
