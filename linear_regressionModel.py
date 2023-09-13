import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import time

def predict_cpu_usage():
    current_date = datetime.now()
    filenamedate = current_date.strftime('%Y-%m-%d')
    log_file = f"log_{filenamedate}.txt"
    df = pd.read_csv(log_file, names=['date', 'cpu_usage', 'cpu_num', 'mem_usage', 'disk_usage', 'host_ip'], sep=',')
    X = df.index.values.reshape(-1, 1)
    y = df['cpu_usage'].values
    reg = LinearRegression().fit(X, y)
    tomorrow = (current_date + timedelta(days=1)).strftime('%Y-%m-%d')
    prediction = reg.predict([[len(df)]])
    print(f"Predicted CPU usage for {tomorrow}: {prediction[0]}")
    
while True:
    predict_cpu_usage()
    time.sleep(300) # 5 minutes in seconds