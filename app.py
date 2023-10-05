from flask import Flask, request

app = Flask(__name__)

@app.route('/api/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print(request)
        print(request.data)
        data = request.data.decode()
        print(data)
        return 'salut'









if __name__ == '__main__':
    app.run(debug=True, port=5000)