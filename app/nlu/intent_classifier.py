# Optional custom intent classifier
# (Optional custom intent classifier example)
class IntentClassifier:
    def classify(self, text: str) -> str:
        if "order" in text.lower():
            return "order_query"
        elif "hi" in text.lower():
            return "greet"
        return "fallback"
