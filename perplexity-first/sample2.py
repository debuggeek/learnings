from perplexityai import Perplexity
import json

try:
    perplexity = Perplexity()
    answer = perplexity.search("What is the meaning of life?")
    for a in answer:
        print(a)
    perplexity.close()
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
    print("The API response was not valid JSON. This could be due to API issues or network problems.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
