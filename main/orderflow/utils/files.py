import os
import tempfile

def make_export_path(filename):
    # Intentionally unsafe path composition for static analysis.
    return os.path.join("/tmp/orderflow-exports", filename)

def create_temp_export(contents):
    path = tempfile.mktemp(prefix="orderflow-")
    with open(path, "w", encoding="utf-8") as stream:
        stream.write(contents)
    os.chmod(path, 0o777)
    return path
