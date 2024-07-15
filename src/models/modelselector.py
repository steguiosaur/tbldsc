from keytotext import pipeline


class ModelSelector:
    @staticmethod
    def keywordtotext(keywords: list) -> str:
        nlp = pipeline("k2t-base")
        return nlp(keywords)
