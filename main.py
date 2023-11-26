from bt.vocode import vocode_client
from bt.agent import update_prompt
from bt.voices import change_voice


def list_numbers():
    list_numbers_response = vocode_client.numbers.list_numbers()
    print(list_numbers_response)


if __name__ == "__main__":
    #list_numbers()
    #update_prompt()
    change_voice()
