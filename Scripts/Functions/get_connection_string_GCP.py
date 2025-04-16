
#getting necessary information from credentials to stablish connection with SQL
def get_connection_string():
    schema = "gans_data_pipeline"  # update "gans_data_pipeline" to your actual MySql database (schema) name
    host = "127.0.0.1"  # update with your own Google Cloud instance IP address
    user = "root"  # update with your MySql username
    password = "password" # update "password" with your actual MySql password
    port = 3306  # update with your own default MySQL port, if different
    
    connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'
    return(connection_string)
