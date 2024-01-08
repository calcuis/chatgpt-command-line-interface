from llama_cpp import Llama
llm = Llama(model_path="chat.gguf")
import time

while True:
      ask = input("Enter a Question (Q for quit): ")

      if ask == "q" or ask == "Q":
            break

      output = llm("Q: "+ask, max_tokens=2048, echo=True)
      answer = output['choices'][0]['text']
      
      for word in answer.split():
        print(word, end=' ', flush=True)
        time.sleep(0.01)

      print("\n")

print("Goodbye!")
