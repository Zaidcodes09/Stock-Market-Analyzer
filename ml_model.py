from sklearn.ensemble import RandomForestClassifier
import pandas as pd


def train_model(data):

    data = data.copy()

    data["Change"] = data["Close"].pct_change()

    data["Target"] = (
        data["Change"].shift(-1) > 0
    ).astype(int)

    data = data.dropna()

    X = data[["Change"]]
    y = data["Target"]

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model


def predict_market(model, data):

    change = data["Close"].pct_change().iloc[-1]

    prediction_data = pd.DataFrame(
        [[change]],
        columns=["Change"]
    )

    prediction = model.predict(prediction_data)

    confidence = model.predict_proba(prediction_data).max()

    if prediction[0] == 1:
        return "Increasing", round(confidence * 100, 2)

    return "Decreasing", round(confidence * 100, 2)