import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Processor:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        nltk.download('vader_lexicon')
        self.weapons = self._read_weapons("../data/weapon_list.txt")

    @staticmethod
    def _read_weapons(file_path: str) -> list:
        """Read weapons from a text file."""
        try:
            with open(file_path, "r") as file:
                weapons = [line.strip() for line in file if line.strip()]
            return weapons
        except FileNotFoundError as e:
            raise Exception(f"File not found: {e}") from e
        except Exception as e:
            raise Exception(f"Failed to read weapons: {e}") from e

    def range_emotion(self,column: str = "Text") -> pd.DataFrame:
        sid = SentimentIntensityAnalyzer()
        self.data['sentiment'] = self.data[column].apply(lambda x: sum(sid.polarity_scores(str(x)).values()))
        labels = ['negative', 'neutral', 'affirmative']
        bins = [float("-inf"), -0.5, 0.49, float("inf")]
        self.data['sentiment'] = pd.cut(self.data['sentiment'], bins=bins, labels=labels)
        return self.data

    def rare_word(self, column: str = "Text") -> pd.DataFrame:
        pass

    def list_weapons(self, column: str = "Text") -> pd.DataFrame:
        """Check if any of the weapons are mentioned in the specified column."""
        self.data['weapons'] = self.data[column].apply(
            lambda x: [weapon for weapon in self.weapons if weapon.lower() in str(x).lower()]
        )
        return self.data




