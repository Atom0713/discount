import json
import os

from discount import create_app

json_dev_config = open('development_config.json')
env_vars = json.load(json_dev_config)['environment_variables']
for key, val in env_vars.items():
    os.environ[key] = val

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get('PORT', 5000)))
