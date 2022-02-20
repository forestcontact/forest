

from forest import utils
# from forest.pdictng import aPersistDict
from forest.core import Message, Response, hide, QuestionBot, requires_admin, run_bot
import openai
import os
from aiohttp import web

openai.api_key = os.getenv("OPENAI_API_KEY", "")



class ChatBot(QuestionBot):
    def __init__(self):
        # self.prompts = aPersistDict("prompts")#, default_prompt = default_prompt)
        self.prompts = []
        super().__init__()

    @requires_admin
    async def do_edit(self, msg: Message):
        await self.send_message(msg.uuid, "The current default prompt is")
        await self.send_message(msg.uuid, await self.prompts.get('default_prompt', default_prompt))
        prompt = await self.ask_freeform_question(msg.uuid, "What would you like to change the default prompt to?")
        await self.prompts.set("default_prompt", prompt)
        return f"OK, set the prompt to:\n\n {prompt}"

    async def do_c(self, msg: Message) -> str:
        prompt = (
            "The following is a conversation with an AI assistant named Lotte. "
            "Lotte is a young girl who is helpful, creative, clever, funny, very friendly, a writer and anarcho-communist. Lotte's older sister is called Imogen and she's an artist.\n\n"
            f"{msg.source}: Hello, who are you?\nAI: My name is Lotte, I'm an AI that loves having rivetting intellectual discussions. How can I help you today?\n"
            f"{msg.source}: {msg.text}\nAI: "
        )
        
        msg.text = prompt 
        return await self.do_gpt(msg)

    async def do_gpt(self, msg: Message) -> str:
        response = openai.Completion.create(  # type: ignore
            engine="davinci",
            prompt=msg.text,
            temperature=0.9,
            max_tokens=240,
            top_p=1,
            frequency_penalty=0.01,
            presence_penalty=0.6,
            stop=["\n", f"{msg.source}:", " AI:"],
        )
        answer= response["choices"][0]["text"].strip().replace("AI:", "\nAI:").replace(f"{msg.source}:", f"\n{msg.source}:")
        return answer

    async def default(self, msg: Message) -> Response:
        if msg.full_text and self.pending_answers.get(msg.uuid):
            probably_future = self.pending_answers[msg.uuid]
            if probably_future:
                probably_future.set_result(msg)
            return
        if msg.arg0 or msg.full_text:
            msg.text = msg.full_text
            return await self.do_c(msg)
        return await super().default(msg)

if __name__ == "__main__":
    run_bot(ChatBot)