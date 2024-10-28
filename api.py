from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/Supalonely', methods=['GET'])
def returnUserInfo():
   id = request.args.get("id")
   pass

   users = {
        1:{
            "name": "Artem",
            "Age": 18
        },
        2: {
            "name": "Alina",
            "Age": 18
        },
        3: {
            "name": "Sanechka",
            "Age": 26
        },
    }

   return jsonify(users[int(id)])

if __name__ == "__main__":
    app.run(debug=True)