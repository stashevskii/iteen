greet_phrase = "Привет 🖐️! Я - Quizzy, бот в которым ты можешь создавать викторины и играть в них вместе с друзьями!"
create_quizz_phrase = "Создать викторину ✍"
how_many_questions_phrase = "Сколько будет вопросов в вашей викторине?"
how_many_answers_phrase = "Сколько будет вариатов ответа?"
enter_number = "Введите число!"
enter_question_phrase = "Введите текст вопроса:"
enter_number_more_than_zero = "Количество вопросов должно быть больше нуля!"


def render_send_poll_phrase(curr: int):
    return f"Оправьте мне опрос (Это будет ваш вопрос под номером {curr}) (Обязательно включите режим викторины!)"


wrong_quizz_params_phrase = "Вы выбрали не те парамертры при создании опроса!"
