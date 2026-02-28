#تنظيف البيانات وضمان 1000 سطر

import pandas as pd

def process_data(data, min_rows):
    df = pd.DataFrame(data, columns=["Title", "Description", "Link", "Category"])

    if len(df) < min_rows:
        while len(df) < min_rows:
            df = pd.concat([df, df.head(min_rows - len(df))], ignore_index=True)

    return df