import random
# Define variables
name = "OwaspBot"
weather = "cloudy"
# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    # print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    
# Define a dictionary with the predefined responses
responses = {
  "whats your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "whats today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "my name is (.*)":
        ["Hello %1, How are you today ?"],
  "default": ["default message"]
}


# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = random.choice(responses[message])
    else:
        # Return the "default" message
        bot_message = random.choice(responses["default"])
    return bot_message
message=input("USER : ")
send_message(message)
respond(message)
