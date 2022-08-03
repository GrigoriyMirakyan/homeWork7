import data_provider as prov
import logger as log


def name_view():
    data = prov.get_name()
    log.name_logger(data)
    return data


def first_name_view():
    data = prov.get_first_name()
    log.first_name_logger(data)
    return data


def number_phone_view():
    data = prov.get_number_phone()
    log.number_phone_logger(data)
    return data


def description_view():
    data = prov.get_description()
    log.description_logger(data)
    return data
