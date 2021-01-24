#!/bin/bash

input="$1"
development_input="postgres://{username}:{password}@{hostname}:{port}/{database-name}"
# Default username is postgres, hostname is 127.0.0.1, port is 5432
# password is the password set when installing PostgreSQL
# database_name is set when database is created locally on pgAdmin

production_input="<CONNECTION URL FROM HEROKU>"
development_env_name="development"
production_env_name="production"

if [[ -z "$input" ]]
then
  export ENV="$development_env_name"
  export DATABASE_URL="$development_input"
  python app.py
elif [[ "$input" == 'dbfeed' ]]
then
  export ENV="$development_env_name"
  export DATABASE_URL="$development_input"
  python database_feeder.py
elif [[ "$input" == 'production' ]]
then
  export ENV="$production_env_name"
  export DATABASE_URL="$production_input"
  python database_feeder.py
else
  echo "Unrecognized command: $input"
fi
