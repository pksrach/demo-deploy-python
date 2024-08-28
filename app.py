from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'status': 'ok'
    })


@app.route('/template')
def template():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
