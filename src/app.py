from flask import Flask
from .config import app_config
from .models import db, bcrypt # add this new line
from .views.UserView import user_api as user_blueprint

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  
  bcrypt.init_app(app) # add this line

  db.init_app(app) # add this line
  
  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app
