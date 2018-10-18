import wolframalpha
import os

#clears the terminal/window screen
os.system('clear')

#Input the api key here, should. Example -> ("G8YTHF-Y2967PT5H1")
client= wolframalpha.Client("G8YTHF-Y2967PT5H1") #Input the api key here, should. Example.      wolframalpha.Client("G8YTHF-Y2967PT5H1")

'''remove comment if the question is pre-written like below
input_string = "What is the weather in toronto today?"
'''

#or ask in python input the question
input_string=input("Ask me a question:")

#outputs the reults
output_string = client.query(input_string)
try:
    print (next(output_string.results).text)

except StopIteration:
    print ("No results")
