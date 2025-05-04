class CreateQuizzForm:
    questions_quantity: int = 0
    questions: dict = {}
    """
    {
        1: {
            "question_text": "question text",
            "answers": ["answer 1", "answer 2"],
            "correct_answer": 1 (index to answer list)
        }
    }
    """

    def __str__(self):
        return f"{self.questions}"

    def clear(self):
        self.questions_quantity = 0
        self.questions = {}
