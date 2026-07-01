from severnaya_pchela.cookiecutter_const import *

def project_context(request):
    return {
        "PROJECT_NAME": PROJECT_NAME_RUS,
        "PROJECT_DESCRIPTION": PROJECT_DESCRIPTION,
    }