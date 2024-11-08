from perplexityai import Perplexity
import json

def main():
        # Create a Perplexity instance
        perplelexity = Perplexity()

        print("Welcome to PAI demo")
        print("Type 'exit' to quit")

        while True:
                # Get user input
                user_input = input("\n👦: ")

                if user_input.lower() == 'exit':
                        print("Bye")
                        break
                try:
                        for response in perplelexity.generate_answer(user_input):
                                print(f"🤖: {response['answer']}")
                except Exception as e:
                        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()