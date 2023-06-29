import os


def image_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "images", filename)
