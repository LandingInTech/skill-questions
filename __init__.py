import logging
import aiohttp
import json

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex, match_crontab
from opsdroid.events import Message

_LOGGER = logging.getLogger(__name__)


class QuestionsSkill(Skill):
    """Opsdroid question skill for Twitch."""

    def __init__(self, opsdroid, config, *args, **kwargs):
        super().__init__(opsdroid, config, *args, **kwargs)
        self.connector = self.opsdroid.get_connector("twitch")

    @match_regex(r"\!question|question for (?P<question>.*)", case_sensitive=False, matching_condition="search")
    async def question_asked(self, message):
        """Question asked by viewer."""
        question = message.entities["question"]
        _LOGGER.info(question)
        await self.opsdroid.memory.put(
            "questions",
            {"username": message.user, "question": question["value"], "isShown": False, "wasAsked": False},
        )

        await self.connector.send(
            Message(
                f"Thank you for your question {message.user}! I will ask this question as soon as possible."
            )
        )

    @match_crontab('*/15 * * * *')
    async def mention_question_command(self, message):
        """Send message about question command ever 15 minutes."""
        await self.connector.send(Message("Use the command !question to ask a question to the quest."))

