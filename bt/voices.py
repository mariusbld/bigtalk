import os

from vocode import ElevenLabsVoiceParams, AgentUpdateParams, ElevenLabsVoiceUpdateParams

from bt.vocode import vocode_client

ELEVEN_LABS_VOICE_ID = os.getenv("ELEVEN_LABS_VOICE_ID")
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


def change_voice():
    number = vocode_client.numbers.get_number(phone_number=PHONE_NUMBER)
    agent = number.inbound_agent

    # elevenlabs_voice = ElevenLabsVoiceParams(
    #     type="voice_eleven_labs",
    #     voice_id=ELEVEN_LABS_VOICE_ID,
    #     api_key=ELEVEN_LABS_API_KEY,
    # )
    # voice = vocode_client.voices.create_voice(request=elevenlabs_voice)

    eleven_labs_voice_update = ElevenLabsVoiceUpdateParams(
        voice_id=ELEVEN_LABS_VOICE_ID,
        api_key=ELEVEN_LABS_API_KEY,
    )

    agent = vocode_client.agents.update_agent(
        id=agent.id,
        request=AgentUpdateParams(voice=eleven_labs_voice_update),
    )
    print(agent)
