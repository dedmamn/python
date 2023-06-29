import os


def image_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "images", filename)


def report_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.additional.paper.id), "reports", filename)


def structure_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.him_info.paper.id), "structure", filename)


def himInfo_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "him_info", filename)
