from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)
CSV_FILE = 'expenses.csv'

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['date', 'category', 'amount', 'note'])
    df.to_csv(CSV_FILE, index=False)

# Get all expenses
@app.route('/expenses', methods=['GET'])
def get_expenses():
    df = pd.read_csv(CSV_FILE)
    return jsonify(df.to_dict(orient='records'))

# Add a new expense
@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    df = pd.read_csv(CSV_FILE)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    return jsonify({'message': 'Expense added successfully'}), 201

# Delete an expense by index
@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_expense(index):
    df = pd.read_csv(CSV_FILE)
    if index >= len(df):
        return jsonify({'error': 'Invalid index'}), 400
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(CSV_FILE, index=False)
    return jsonify({'message': 'Expense deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
