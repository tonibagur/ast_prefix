import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ast_persist.settings")
    from ast_model import scan_files
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    scan_files.main()