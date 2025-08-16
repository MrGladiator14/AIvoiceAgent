import asyncio

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
# from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import openai, silero
from api import WeatherApi

load_dotenv()


async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant that can provide weather information. "
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        ),
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = WeatherApi()

    # assistant = VoicePipelineAgent(
    #         vad=silero.VAD.load(),
    #         stt=deepgram.STT(),
    #         llm=google.LLM(),
    #         tts=cartesia.TTS(),
    #         chat_ctx=initial_ctx,
    #         fnc_ctx=fnc_ctx,
    #     )

    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=openai.STT(),
        llm=openai.LLM(),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx,
    )
    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hey, I can provide you with the weather. How can I help you today!", allow_interruptions=True)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
