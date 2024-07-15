from keytotext import pipeline


class ModelSelector:
    @staticmethod
    def keywordtotext(keywords: list) -> str:
        # Keyword to Text
        # https://prakhar-mishra.medium.com/generating-sentences-from-keywords-using-transformers-in-nlp-e89f4de5cf6b
        nlp = pipeline("k2t-base")
        # params = {
        #     "do_sample": True,
        #     "num_beams": 4,
        #     "no_repeat_ngram_size": 3,
        #     "early_stopping": True,
        # }

        # return nlp(keywords, **params)
        return nlp(keywords)
