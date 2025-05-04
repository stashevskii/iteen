from telebot import TeleBot, types
from src.telegram.app.keyboards.reply import remove_keyboard
from src.telegram.app.utils.forms import CreateQuizzForm
from src.telegram.app.utils.phrases import *
from src.telegram.app.utils.validation import validate_question_quantity, validate_poll, check_message_has_poll
from src.telegram.app.сommon.handler import BaseHandler


class CreateQuizzHandler(BaseHandler):
    def __init__(self, bot: TeleBot):
        super().__init__(bot)
        self.quizz = CreateQuizzForm()
        self.current_question = 0

    def quizz_create(self, message: types.Message):
        self.bot.send_message(message.chat.id, how_many_questions_phrase, reply_markup=remove_keyboard)
        self.quizz.clear()
        self.current_question = 1
        self.bot.register_next_step_handler(message, self.how_many_questions)

    def ask_to_send_poll(self, message: types.Message):
        self.bot.send_message(message.chat.id, render_send_poll_phrase(self.current_question))
        self.bot.register_next_step_handler(message, self.handle_input_poll)

    def how_many_questions(self, message: types.Message):
        if not validate_question_quantity(message, self.bot):
            self.bot.register_next_step_handler(message, self.how_many_questions)
            return
        self.quizz.questions_quantity = int(message.text)
        self.ask_to_send_poll(message)

    def handle_input_poll(self, message: types.Message):
        if not check_message_has_poll(message):
            self.ask_to_send_poll(message)
            return

        poll = message.poll
        if not validate_poll(poll):
            self.bot.send_message(message.chat.id, wrong_quizz_params_phrase)
            self.ask_to_send_poll(message)
            return

        self.quizz.questions[self.current_question] = {
            "question_text": poll.question,
            "options": [i.text for i in poll.options],
            "correct": poll.correct_option_id
        }

        if self.current_question == self.quizz.questions_quantity:
            print(self.quizz)
            return

        self.current_question += 1
        self.ask_to_send_poll(message)

    def register_command_handlers(self):
        self.bot.message_handler(func=lambda m: m.text == create_quizz_phrase)(self.quizz_create)
        self.bot.message_handler(content_types=["poll"])(self.handle_input_poll)
