import random
def chatBot():
     
     print("ChatBot Started")
     print("Type 'bye' to exit.\n")
     
     greetings=["hello","hi","hey"]
     bye_word = ["bye","byee","exit","quit"]
     
     while True:
          user = input("You:").lower()
          
          
          if user in greetings: 
               responses=["hi","Hey there","hey","hello"]
               print("Bot:",random.choice(responses))
                    
                    
          elif user=="how are you":
               responses=["I'm fine","Doing great","All good"]
               print("Bot:",random.choice(responses))
               
               
          elif user=="what is your name":
               print("Bot :I'm a simple chatbot.")
          
          
          elif user in bye_word:
               print("Bot: Goodbye")
               break
          
          else:
               print("Bot: Sorry, I don't understand")
               
chatBot()