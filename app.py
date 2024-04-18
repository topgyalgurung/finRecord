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

# Create operation: display add transaction form
@app.route("/add",methods=["GET","POST"])
def add_transaction():
    if request.method=="POST":
        # create a new transaction object using form field values
        transaction={
            'id':len(transactions)+1,
            'date':request.form['date'],
            'amount':float(request.form['amount'])
        }
        transactions.append(transaction)
        #redirect to transactions list page
        return redirect(url_for('get_transactions'))
                        
    return render_template("form.html")


# Update operation: Display edit transaction form
@app.route('/edit/<int:transaction_id>',methods=['GET','POST'])
def edit_transaction(transaction_id):
    if request.method=='POST':
        date=request.form['date']
        amount=float(request.form['amount'])

    # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id']==transaction_id:
                transaction['date']=date
                transaction['amount']=amount
                break
        return redirect(url_for("get_transactions"))
# Find the transaction with the matching ID and render the edit form
# if request method is GET
    for transaction in transactions:
        if transaction['id']==transaction_id:
            return render_template('edit.html',transaction=transaction)


# Delete operation: Delete a transaction
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id']==transaction_id:
            transactions.remove(transaction)
# Redirect to the transactions list page
    return redirect(url_for('get_transactions'))



# Run the Flask app
if __name__=="__main__":
    app.run(debug=True)