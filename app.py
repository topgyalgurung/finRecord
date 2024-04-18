# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app=Flask(__name__)

# Sample data or transactions for testing purpose
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template('transactions.html',transactions=transactions)
# Create operation

# Update operation

# Delete operation

# Run the Flask app
    