from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import secrets
import responses
import button
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.secret_key = secrets.token_hex(16)
jwt = JWTManager(app)

def prediction(text):
    return responses.response(text)

def generate_token(session_id):
    expiration_time = timedelta(minutes=10)
    token = create_access_token(identity=session_id, expires_delta=expiration_time)
    return token

def generate_buttons(received_message):
    buttons = button.gen_but(received_message)
    return buttons

    
@app.route('/api', methods=['POST'])
def api_endpoint():
    if 'session_id' not in session or 'token' not in session:
        session['session_id'] = secrets.token_hex(16)
        session['token'] = generate_token(session['session_id'])
        received_message = request.json.get('message')
        received_message = received_message.lower()
        pred = prediction(received_message)
        answer = pred['response']
        buttons = generate_buttons(received_message)

        generated_response = {
            "session_id": session['session_id'],
            "token": session['token'],
            "text": answer,
            "status": 200,
            "buttons": buttons
        }
        return jsonify([generated_response])

    received_session = request.json.get('session_id')
    received_token = request.json.get('token')
    received_message = request.json.get('message')
    received_message = received_message.lower()
    if received_token == session['token'] and received_session == session['session_id']:
        pred = prediction(received_message)
        answer = pred['response']
        buttons = generate_buttons(received_message)
        
        generated_response = {
            "session_id": session['session_id'],
            "token": session['token'],
            "text": answer,
            "status": 200,
            "buttons": buttons
        }
        return jsonify([generated_response])

    else:
        generated_response = {
            "session_id": session['session_id'],
            "token": session['token'],
            "text": 'Token or session not matched',
            "status": 400
        }
        return jsonify([generated_response])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
