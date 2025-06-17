Rent Price Predictor - Dhaka, Bangladesh 🏠💰  

This Python script predicts key housing features (Area, Bedrooms, Bathrooms) based on a given rent price in Dhaka, Bangladesh. It uses Linear Regression on a cleaned dataset to reverse-predict features from price.  

---

 📌 Key Features  
✅ Data Cleaning - Handles price formats like "Lakh" and "Thousand" and removes commas for numeric conversion.  
✅ Reverse Prediction Model - Instead of predicting price from features, it predicts features from price (Area, Bedrooms, Bathrooms).  
✅ User Input - Takes a price (in BDT) and returns predicted housing features.  
✅ Visual Comparison - Shows scatter plots comparing the predicted values with actual data points.  

---

 📂 File Structure  
```
📦House-Rent-Predictor-Dhaka/
├── 📜houserentdhaka.csv          Dataset (ensure this is uploaded)
├── 📜rent_price_predictor.py     Main Python script
└── 📜README.md                   Project documentation
```

---

 🛠️ Dependencies  
- Python 3.10+  
- Libraries:  
  ```bash
  pandas scikit-learn matplotlib
  ```
  Install them via:  
  ```bash
  pip install pandas scikit-learn matplotlib
  ```

---

 🚀 How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/House-Rent-Predictor-Dhaka.git
   cd House-Rent-Predictor-Dhaka
   ```
2. Run the script:  
   ```bash
   python rent_price_predictor.py
   ```
3. Enter a price in BDT (e.g., `50000` or `150000`) when prompted.  
4. See the predicted features and interactive plots!  

---

 📊 Example Output  
 Terminal Output:  
```
Enter the price (in BDT): 50000

Predicted features for BDT 50,000:
Area: 850 sqft
Bedrooms: 2
Bathrooms: 1
```
 Graph Output:  
![image](https://github.com/user-attachments/assets/2b664a2f-a9f6-4acc-84e5-13cc99b919b7) 

---

 📝 Notes  
- The dataset (`houserentdhaka.csv`) should be in the same directory.  
- The model is linear regression-based, meaning it assumes a linear relationship between price and features.  
- For better accuracy, consider using polynomial regression or other ML models in future updates.  

---

 📜 License  
This project is open-source under the MIT License.  

---

 💡 Future Improvements  
🔹 Add more features (location, floor level, etc.)  
🔹 Implement a web app using Flask/Django for easier use  
🔹 Try different ML models (Random Forest, Neural Networks)  

---

 ⭐ Star the repo if you find it useful!  
 🔄 Contributions & Issues welcome!
