# CloudSQL & SQLAlchemy configuration
# Replace the following values the respective values of your Cloud SQL
# instance.
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = '20CloudComp19!'
CLOUDSQL_DATABASE = 'roomscheddb'
# Set this value to the Cloud SQL connection name, e.g.
#   "project:region:cloudsql-instance".
# You must also update the value in app.yaml.
CLOUDSQL_CONNECTION_NAME = 'room-sched-cloudcomp:us-east4:room-sched-db'

PROJECT_ID = '35.199.58.121'

DATA_BACKEND = 'CloudSQL'