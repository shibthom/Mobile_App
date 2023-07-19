import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_squared_error
from joblib import dump

# Assuming df is your DataFrame and it already has the necessary pre-processing applied
df = pd.read_csv('data.csv')

X = df[['Resolution x', 'Resolution y', 'Processor', 'RAM (MB)']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#predictions = model.predict(X_test)
#print(f'RMSE: {mean_squared_error(y_test, predictions, squared=False)}')


# Save the model to a file
dump(model, 'model.joblib') 