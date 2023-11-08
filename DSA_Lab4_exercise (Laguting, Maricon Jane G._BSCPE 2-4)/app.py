from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_1():
    radius = None
    if request.method == 'POST':
        try:
            input_radius= float(request.form.get('inputradius', ''))
            radius = (3.14 * (input_radius**2))
            radius = str(radius)
        except ValueError:
            return render_template('areaOfcircle.html')
    return render_template('areaOfcircle.html', radius=radius)
    
@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def area_2():
    area_triangle = None
    if request.method == 'POST':
        try:
            input_base = request.form.get('base', '')
            input_height = request.form.get('height', '')

            if input_base and input_height:
                input_base = float(input_base)
                input_height = float(input_height)
                area_triangle = input_base * input_height
                area_triangle = str(area_triangle)
        except ValueError:
            return render_template('areaOfTriangle.html')
    return render_template('areaOfTriangle.html', area_triangle=area_triangle)   

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('/works.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
