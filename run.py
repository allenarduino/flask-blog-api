# /run.py
import os

from src.app import create_app
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
  env_name = os.environ.get('FLASK_ENV')
  app = create_app(env_name)
  # run app
  app.run()