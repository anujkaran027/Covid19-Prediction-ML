import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from data_cleaning import load_and_clean_data

def train_model():
    # Load and clean data
    df = load_and_clean_data("data/Covid Dataset.csv")

    # Split features and labels
    X = df.drop(columns=['COVID-19'])
    y = df['COVID-19']

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc*100:.2f}%")

    # Save model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model saved as model.pkl")

if __name__ == "__main__":
    train_model()