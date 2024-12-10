import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv('equipes.csv')

# Identify numeric columns
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()

# Impute missing values for numeric columns
imputer = SimpleImputer(strategy='mean')
data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

# Splitting features and target variable
X = data[['TeamA_stats', 'TeamB_stats']]  # Use relevant features here
y = data['Result']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Print the predictions
print(predictions)

# Assuming a threshold of 0 for the predictions
classified_predictions = ['TeamA' if pred > 0 else 'TeamB' for pred in predictions]
print(classified_predictions)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae}")

