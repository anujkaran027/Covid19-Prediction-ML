import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Drop columns not useful for prediction
    df.drop(columns=['Wearing Masks', 'Sanitization from Market'], inplace=True)

    # Encode categorical features
    label_encoder = LabelEncoder()
    for col in df.columns:
        df[col] = label_encoder.fit_transform(df[col])

    return df