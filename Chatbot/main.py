import json
import re
import random_responses

# load json data


def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)


# store json data
responses_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.]\s+', input_string.lower())
    score_list = []

# check all responses
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

# check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
# amount of req words should math req score
        if required_score == len(required_words):
            # print (required_score == len(required_words))
            # check each word the user has typed
            for word in split_message:
                # if the wor is in the response , add to the score
                if word in response["user_input"]:
                    response_score += 1

# add score to list
        score_list.append(response_score)

# find the best response and return it if they are not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

# check if input is empty

    if input_string == "":
        print("Kindly, type in something so that we can chat: ")

# if there is no good response ,return a random one
    if best_response != 0:
        return responses_data[response_index]['bot_response']

    return random_responses.random_string()


while True:
    user_input = input("You: ")
    print('Bot: ', get_response(user_input))
