#!/usr/bin/python3
""" reload method for models directory/storage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
