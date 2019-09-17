from app import app as application
import os
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
  application.run(host='0.0.0.0', port=port)