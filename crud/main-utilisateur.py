import pymysql
from app import app

from db_config import mysql
from flask import jsonify
from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

# from werkzeug import generate_password_hash, check_password_hash
@app.route('/capteur/add', methods=['POST'])
def add_capteur():
    try:
        _json = request.json
        _reference = _json['reference']
        _description = _json['description']

        if _reference and _description and request.method == 'POST':
            print("11")
            # save edits
            sql = "INSERT INTO capteur(reference, description) VALUES(%s, %s)"
            data = (_reference, _description)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Capteur added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/capteurs')
def getAll_capteur():
    try:
        conn = mysql.connect()
        print(conn)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM capteur")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/capteur/<int:id>')
def get_capteur(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM capteur WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/capteur/update', methods=['POST'])
def update_capteur():
    try:
        _json = request.json
        _id = _json['id']
        _reference = _json['reference']
        _description = _json['description']
        # validate the received values
        if _reference and _description and request.method == 'POST':
            # save edits
            sql = "UPDATE capteur SET reference=%s, description=%s WHERE Id=%s"
            data = (_reference, _description, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Capteur updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/capteur/delete/<int:id>')
def delete_capteur(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM capteur WHERE Id=%s", (id,))
        conn.commit()
        resp = jsonify('Capteur deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/localisation/add', methods=['POST'])
def add_localisation():
    try:
        _json = request.json
        _nom = _json['nom']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        # validate the received values
        if _latitude and _longitude and _nom and request.method == 'POST':
            print("11")
            # save edits
            sql = "INSERT INTO localisation(latitude, longitude, nom) VALUES(%s,%s,%s)"
            print("1")
            data = (_latitude, _longitude, _nom)
            conn = mysql.connect()
            print("2")
            cursor = conn.cursor()
            cursor.execute(sql, data)
            print("3")
            conn.commit()
            resp = jsonify('Localisation added successfully!')
            print("4")
            resp.status_code = 200
            return resp
        else:
            return not_found()
        print("5")
    except Exception as e:
        print(conn)
        print(e)
    finally:
        cursor.close()
        print("6")
        conn.close()


@app.route('/localisations')
def getAll_localisation():
    try:
        conn = mysql.connect()
        print(conn)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM localisation")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/localisation/<int:id>')
def get_localisaiton(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM localisation WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/localisation/update/<int:id>', methods=['POST'])
def update_localisation(id):
    try:
        _json = request.json
        _nom = _json['nom']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        # validate the received values
        if _latitude and _longitude and _nom and request.method == 'POST':
            # save edits
            sql = "UPDATE localisation SET latitude=%s, longitude=%s, nom=%s WHERE id=%s"
            data = (_latitude, _longitude, _nom, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Localisation updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/localisation/delete/<int:id>')
def delete_localisation(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM localisation WHERE id=%s", (id))
        conn.commit()
        resp = jsonify('Localisation deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/mesure/add', methods=['POST'])
def add_mesure():
    try:
        _json = request.json
        _temperature = _json['temperature']
        _humidite = _json['humidite']
        _releve = _json['releve']
        # validate the received values
        if _temperature and _humidite and _releve and request.method == 'POST':
            print("11")
            # save edits
            sql = "INSERT INTO mesure(temperature, humidite, releve) VALUES(%s, %s, %s)"
            print("1")
            data = (_temperature, _humidite, _releve)
            conn = mysql.connect()
            print("2")
            cursor = conn.cursor()
            cursor.execute(sql, data)
            print("3")
            conn.commit()
            resp = jsonify('Mesure added successfully!')
            print("4")
            resp.status_code = 200
            return resp
        else:
            return not_found()
        print("5")
    except Exception as e:
        print(conn)
        print(e)
    finally:
        cursor.close()
        print("6")
        conn.close()


@app.route('/mesures')
def getAll_mesure():
    try:
        conn = mysql.connect()
        print(conn)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT DATE_FORMAT(releve, \"%d.%m.%y\") releve, temperature, humidite FROM mesure")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/mesure/<int:id>')
def get_mesure(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM mesure WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/mesure/update', methods=['POST'])
def update_mesure():
    try:
        _json = request.json
        _id = _json['id']
        _temperature = _json['temperature']
        _humidite = _json['humidite']
        _releve = _json['releve']
        # validate the received values
        if _temperature and _humidite and _releve and request.method == 'POST':
            # save edits
            sql = "UPDATE mesure SET temperature=%s, humidite=%s, releve=%s WHERE id=%s"
            data = (_temperature, _humidite, _releve, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Mesure updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/mesure/delete/<int:id>')
def delete_mesure(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM mesure WHERE id=%s", (id))
        conn.commit()
        resp = jsonify('Mesure deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _nom = _json['nom']
        _api_key = _json['api_key']
        # _email = _json['email']
        # validate the received values
        if _nom and _api_key and request.method == 'POST':

            # save edits
            sql = "INSERT INTO utilisateur(nom, api_key) VALUES(%s, %s)"

            data = (_nom, _api_key)
            conn = mysql.connect()

            cursor = conn.cursor()
            cursor.execute(sql, data)

            conn.commit()
            resp = jsonify('User added successfully!')

            resp.status_code = 200
            return resp
        else:
            return not_found()
        print("5")
    except Exception as e:
        print(conn)
        print(e)
    finally:
        cursor.close()
        print("6")
        conn.close()


@app.route('/station/add', methods=['POST'])
def add_station():
    try:
        _json = request.json
        _nom = _json['nom']
        _description = _json['description']
        _id_utilisateur = _json['id_utilisateur']

        # validate the received values
        if _nom and _description and request.method == 'POST':
            print("11")
            # save edits
            sql = "INSERT INTO station(nom, description, id_utilisateur) VALUES(%s, %s, %s)"
            print("1")
            data = (_nom, _description, _id_utilisateur)
            conn = mysql.connect()
            print("2")
            cursor = conn.cursor()
            cursor.execute(sql, data)
            print("3")
            conn.commit()
            resp = jsonify('Station added successfully!')
            print("4")
            resp.status_code = 200
            return resp
        else:
            return not_found()
        print("5")
    except Exception as e:
        print(conn)
        print(e)
    finally:
        cursor.close()
        print("6")
        conn.close()


@app.route('/stations')
def getAll_station():
    try:
        conn = mysql.connect()
        print(conn)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM station")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/station/<int:id>')
def get_station(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM station WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/station/update/<int:id>', methods=['POST'])
def update_station(id):
    try:
        _json = request.json
        _nom = _json['nom']
        _description = _json['description']
        _id_utilisateur = _json['id_utilisateur']
        # validate the received values
        if _nom and _description and _id_utilisateur and request.method == 'POST':
            # save edits
            sql = "UPDATE station SET nom=%s, description=%s, id_utilisateur=%s WHERE id=%s"
            data = (_nom, _description, _id_utilisateur, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Station updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/station/delete/<int:id>')
def delete_station(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM station WHERE id=%s", (id))
        conn.commit()
        resp = jsonify('Station deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/users')
def getAll_users():
    try:
        conn = mysql.connect()
        print(conn)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM utilisateur")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/<int:id>')
def get_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM utilisateur WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/update/<int:id>', methods=['POST'])
def update_user(id):
    try:
        _json = request.json
        _nom = _json['nom']
        _api_key = _json['api_key']
        _email = _json['email']
        # validate the received values
        if _nom and _api_key and _email and request.method == 'POST':
            # save edits
            sql = "UPDATE utilisateur SET nom=%s, api_key=%s, email=%s WHERE id=%s"
            data = (_nom, _api_key, _email, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/delete/<int:id>')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM utilisateur WHERE id=%s", (id))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run()
