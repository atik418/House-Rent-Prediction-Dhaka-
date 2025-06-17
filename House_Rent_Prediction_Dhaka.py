import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("houserentdhaka.csv")

# Clean 'Area' column
df['Area'] = df['Area'].str.replace(',', '').str.replace('sqft', '').astype(float)

# Clean 'Price' column
def convert_price(value):
    value = str(value).replace(',', '').strip()
    if 'Thousand' in value:
        return float(value.replace('Thousand', '').strip()) * 1000
    elif 'Lakh' in value:
        return float(value.replace('Lakh', '').strip()) * 100000
    else:
        return float(value)

df['Price'] = df['Price'].apply(convert_price)

# Define features and target (reverse model)
target_features = ['Area', 'Bed', 'Bath']
input_feature = 'Price'

# Drop missing values
df = df[target_features + [input_feature]].dropna()

X = df[[input_feature]]
y = df[target_features]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# --- User Input ---
try:
    user_price = float(input("Enter the price (in BDT): "))
    prediction = model.predict([[user_price]])[0]
    
    print(f"\nPredicted features for BDT {user_price:,.0f}:")
    print(f"Area: {prediction[0]:.0f} sqft")
    print(f"Bedrooms: {round(prediction[1])}")
    print(f"Bathrooms: {round(prediction[2])}")
    
    # --- Visualization ---
    plt.figure(figsize=(12, 4))
    
    # Plot 1: Area vs Price
    plt.subplot(1, 3, 1)
    plt.scatter(X, y['Area'], alpha=0.3, label='Actual data')
    plt.scatter(user_price, prediction[0], color='red', s=100, label='Your input')
    plt.title('Area vs Price')
    plt.xlabel('Price (BDT)')
    plt.ylabel('Area (sqft)')
    plt.legend()
    
    # Plot 2: Bedrooms vs Price
    plt.subplot(1, 3, 2)
    plt.scatter(X, y['Bed'], alpha=0.3, label='Actual data')
    plt.scatter(user_price, prediction[1], color='red', s=100, label='Your input')
    plt.title('Bedrooms vs Price')
    plt.xlabel('Price (BDT)')
    plt.ylabel('Number of Bedrooms')
    plt.legend()
    
    # Plot 3: Bathrooms vs Price
    plt.subplot(1, 3, 3)
    plt.scatter(X, y['Bath'], alpha=0.3, label='Actual data')
    plt.scatter(user_price, prediction[2], color='red', s=100, label='Your input')
    plt.title('Bathrooms vs Price')
    plt.xlabel('Price (BDT)')
    plt.ylabel('Number of Bathrooms')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
except ValueError:
    print("Invalid input. Please enter a valid number.")