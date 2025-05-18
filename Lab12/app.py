from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    imt = None
    category = None
    
    if request.method == 'POST':
            # resp = request.get_json()
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100
            
            imt = round(weight / (height ** 2), 2)
            
            match imt:
                case _ if imt < 16:
                    category = "Выраженный дефицит массы тела"
                case _ if 16 <= imt < 18.5:
                    category = "Недостаточная масса тела"
                case _ if 18.5 <= imt < 25:
                    category = "Нормальная масса тела"
                case _ if 25 <= imt < 30:
                    category = "Избыточная масса тела (предожирение)"
                case _ if 30 <= imt < 35:
                    category = "Ожирение первой степени"
                case _ if 35 <= imt < 40:
                    category = "Ожирение второй степени"
                case _:
                    category = "Ожирение третьей степени"
    
    # return jsonify(), 400
    # return app.send_static_file()
    return render_template('index.html', imt=imt, category=category)

if __name__ == '__main__':
    app.run(debug=True)
