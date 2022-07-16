from esreads import app, db
import subprocess
from flask import jsonify


@app.route('/req')
def refresh_requirements():
    file_name = 'requirements.txt'
    with open('results.txt', 'w') as file:
        result = subprocess.run(f'pip freeze > {file_name}', shell=True, stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        return jsonify({'return_code': result.returncode, 'status': 'success'})
    else:
        return jsonify({'return_code': result.returncode,
                        'status': 'could not gather requirements for the project'})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
