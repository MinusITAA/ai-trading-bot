from xgboost import XGBClassifier
import numpy as np

# Modello AI semplificato (può essere sostituito con uno reale addestrato)
def predict_trade(features):
    model = XGBClassifier()
    # Modello fittizio per test: ritorna sempre probabilità casuale
    prob = np.random.uniform(0.7, 0.95)
    prediction = 1 if prob > 0.7 else 0
    return prediction, prob