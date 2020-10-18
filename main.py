from flask import request
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)


users = {
    0: 'Zeroberto',
    1: 'Humberto',
    2: 'Doisberto',
    3: 'Tresberto'
}


@app.route('/users/', methods=['GET'])
def user_list():
    return users


@app.route('/users/<int:key>/', methods=['GET'])
def user_show(key):
    if key not in users:
        raise exceptions.NotFound()
    return users[key]


@app.route('/users/', methods=['POST'])
def user_create():
    user = str(request.data.get('name', ''))
    idx = max(users.keys()) + 1
    users[idx] = user
    return user, status.HTTP_201_CREATED


@app.route('/users/<int:key>/', methods=['PUT'])
def user_update(key):
    if key not in users:
        raise exceptions.NotFound()
    user = str(request.data.get('name', ''))

    users[key] = user
    return user


@app.route('/users/<int:key>/', methods=['DELETE'])
def user_delete(key):
    if key not in users:
        raise exceptions.NotFound()
    users.pop(key, None)
    return '', status.HTTP_204_NO_CONTENT


if __name__ == "__main__":
    app.run(debug=False)
