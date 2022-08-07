#!/usr/bin/env python3
"""
Initializes the storage module for use by BaseModel.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
