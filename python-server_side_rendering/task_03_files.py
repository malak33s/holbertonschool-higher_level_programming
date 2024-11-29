import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read products from a JSON file
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Function to read products from a CSV file
def read_csv():
    products = []
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert price to float and id to int for consistency
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None

# Main route to display products
@app.route('/products')
def products():
    source = request.args.get('source')  # Get 'source' query parameter
    product_id = request.args.get('id')  # Get 'id' query parameter (optional)
    
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")
    
    # If no products found or file is missing
    if not products:
        return render_template('product_display.html', error="No products found")

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid id")
    
    # Render the template with products data
    return render_template('product_display.html', products=products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
