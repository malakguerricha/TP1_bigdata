#حفظ البيانات

def save_to_csv(df, path):
    df.to_csv(path, index=False, encoding="utf-8")