import os
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")


def image_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "images", formatted_date, filename)


def report_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "reports", formatted_date, filename)


def structure_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "structures", formatted_date, filename)


def himInfo_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "him_image", formatted_date, filename)


def furie_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "furies", formatted_date, filename)


def rfa_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "rfas", formatted_date, filename)


def krs_upload_path(instance, filename):
    return os.path.join("papers_files", str(instance.paper.id), "krses", formatted_date, filename)
