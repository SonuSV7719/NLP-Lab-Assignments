import speech_recognition as sr
from difflib import SequenceMatcher

# Step 1: Speech Recognition
r = sr.Recognizer()

def transcribe_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {str(e)}")
        return ""

# Step 2: Text Matching
def calculate_similarity(answer, expected_answer):
    similarity = SequenceMatcher(None, answer, expected_answer).ratio()
    return similarity

# Step 3: Examiner Loop
def conduct_oral_exam(expected_answers):
    num_questions = len(expected_answers)
    score = 0

    for i in range(num_questions):
        print(f"Question {i+1}: Speak your answer.")
        user_answer = transcribe_speech()

        similarity = calculate_similarity(user_answer, expected_answers[i])
        score += similarity

        print(f"Similarity with expected answer: {similarity}")

    overall_score = (score / num_questions) * 100
    print(f"Overall Score: {overall_score}%")

# Main function
if __name__ == "__main__":
    # Define expected answers for the oral exam
    expected_answers = [
        "Expected Answer 1",
        "Expected Answer 2",
        "Expected Answer 3",
        # Add more expected answers as needed
    ]

    # Start the oral exam
    conduct_oral_exam(expected_answers)
