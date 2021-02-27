import fakemoney.defaults
import fakemoney.types as types
import fakemoney.utils as utils


fields = { "url": types.url, "filename": str }


validate = utils.isValidConstructor(fields)


def create(url=None, filename=None):
    if url is None:
        url = fakemoney.defaults.picture
    if filename is None:
        filename = url.split("/")[-1]
    return { "url": url, "filename": filename }
