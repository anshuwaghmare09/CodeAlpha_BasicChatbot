def chatBot():
     
     print("ChatBot Started")
     print("Type 'bye' to exit.\n")

     while True:
          user = input("You:").lower()
          if user=="hello":
               print("Bot: Hii")
          elif user=="how are you":
               print("Bot: I'm fine, thanks")
          elif user=="what is your name":
               print("Bot :I'm simple chatbot.")
          elif user=="bye":
               print("Bot: Goodbye")
               break
          
          else:
               print("Bot: Sorry, I don't understand")
               
chatBot()