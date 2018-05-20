import sqlite3
import flask
import jinja2
import sys
import json

app = flask.Flask(__name__)  

class Product: 

    def __init__(self, prod_id):
        
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        statement  = "SELECT * FROM product WHERE product.product_id = '{}';".format(prod_id)
        c.execute(statement)
        result = c.fetchall()
        
        for i in result:  
            self.id = i[0]
            self.brand = i[1]
            self.name = i[2]
            self.description = i[3]
            self.list_price = i[4]
            self.sale_price = i[5]

                    
    def get_savings_pct(self):
        saving  = ((self.list_price-self.sale_price)/self.list_price)*100  
        return round(float(saving))          
                    
        
    def __str__(self):
        return 'Product: {}'.format(self.name)

    def get_tax(self, state):  
        with open('state_tax.json', 'r') as json_file:
            raw_data = json.load(json_file) 
            rate = raw_data[state]
            result = rate / 100 * self.sale_price 
            return float(result)

def get_all_products():
    
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    statement_2 = "SELECT product_id FROM product"
    c.execute(statement_2) 
    result = c.fetchall()
    id_list = []
    for i in range(len(result)):
        id_list.append(result[i][0])

    product_list = []
    for prod_id in id_list:
        product=Product(prod_id)
        product_list.append(product)

    return product_list

@app.route('/pview')
def view_product():  
    print('*** DEBUG: inside view_product() ***')
    state = 'NY'
    prod_id = flask.request.args.get('prod_id')
    return flask.render_template('view_product.html', product=Product(prod_id), state = state)


@app.route('/plist') 
def list_products():
    print('*** DEBUG: inside list_products() ***')
    return flask.render_template('list_products.html', product_list=get_all_products())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 

