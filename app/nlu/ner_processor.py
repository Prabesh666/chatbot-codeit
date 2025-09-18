# Optional NER processor
# (Optional NER processing example)
import re

class NERProcessor:
    def extract_numbers(self, text: str):
        return re.findall(r"\d+", text)
