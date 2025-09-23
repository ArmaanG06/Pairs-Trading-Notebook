import os
import pandas as pd
from datetime import datetime

def save_to_csv(df, symbol, duration, bar_size, folder="data\cache\prices"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    now = datetime.now().strftime("%Y%m%d")
    filename = f"{symbol}_{duration}_{bar_size}_{now}.csv"
    path = os.path.join(folder, filename)

    df.to_csv(path, index=False)
    print(f"Saved to {path}")
