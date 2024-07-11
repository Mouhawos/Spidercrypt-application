from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint pour recevoir les informations d'inscription de Clerk
@app.route('/api/signup', methods=['POST'])
def signup():
    # Récupérer les informations d'inscription envoyées par Clerk
    data = request.json
    token = data.get('token')
    user = data.get('user')

    # Vous pouvez créer un nouvel utilisateur dans votre base de données
    # Utiliser les données d'utilisateur envoyées par Clerk (par exemple, user['email'], user['username'], etc.)

    # Exemple simple de réponse avec un message de confirmation
    response = {
        'message': 'Signed up successfully',
        'token': token,
        'user': user
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
