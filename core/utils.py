import re

import os

from core.config import g_margin, g_hop, g_unit, TRADE_LOG_DIR, TRADE_RES_LOG_DIR, TRADE_RATIO_LOG_DIR


class Params:
    minlen = 1024 * 2048
    # min_data_size = int(minlen * 1.0000005)
    # min_data_size = int(minlen * 1.0005)
    min_data_size = int(minlen * 1.5)
    # min_data_size = int(minlen * 3)
    # min_data_size = int(minlen * 1.8)
    predict_len = 128
    run_status = 0
    delta = 0
    curpos = 0
    queue_pl_size = 10
    queue_cp_size = 10
    interval = 0.1
    inst = ''
    date = ''
    data_len = 1024
    all_len = min_data_size
    level = 0
    imgpath = ''

    def __init__(self):
        pass


def get_params(instrument, thedate, level):
    params = Params()
    params.run_status = 0
    params.delta = 1
    params.inst = instrument
    params.date = thedate
    params.data_len = 1024
    params.level = level
    params.imgpath = '/home/zj/gom/images'
    return params


def get_instrument_code(instrument, nine=False):
    match= re.match(r'([a-z]+)(.*)', instrument, re.I)
    code = ''
    if match:
        items = match.groups()
        code = items[0]
    if len(code) == 1 and nine:
        code += '9'
    return code


def get_margin(instrument):
    return g_margin[get_instrument_code(instrument)]


def get_hop(instrument):
    return g_hop[get_instrument_code(instrument)]


def get_unit(instrument):
    return g_unit[get_instrument_code(instrument)]


def write_trade_log(total, file_name, point, capital):
    # save_time = time.strptime('2018-01-24 23:59:50', '%Y-%m-%d %H:%M:%S')
    # curr_time = time.localtime(total.uptime)
    # if curr_time < save_time:
    #     return
    path = os.path.join(TRADE_LOG_DIR, '%s.log' % file_name)
    ratio = total.cls_rev / capital * 100
    with open(path, 'a') as put:
        all_the_text = '%d,%f,%.02lf,%.02lf,%.02lf,%.02lf,%d,%f\n' % \
                       (
                           point,
                           total.uptime,
                           total.all_rev,
                           total.flt_rev,
                           total.cls_rev,
                           total.money,
                           total.volume,
                           ratio
                       )
        put.writelines(all_the_text)


def load_file(data_path):
    try:
        with open(data_path, 'r') as output:
            lines = output.readlines()
        return lines
    except IOError:
        print "Error: No such data file. Filename: %s" % data_path
        exit(0)


def write_result_log(total, file_name, point, action, direction, vol, ttime):
    path = os.path.join(TRADE_RES_LOG_DIR, '%s.log' % file_name)
    with open(path, 'a') as put:
        all_the_text = '%s,%d,%d,%.02lf,%.02lf,%.02lf,%.02lf,%d,%d,%s\n' % \
                       (
                           action,
                           direction,
                           point,
                           total.all_rev,
                           total.flt_rev,
                           total.cls_rev,
                           total.money,
                           total.volume,
                           vol,
                           ttime
                       )
        put.writelines(all_the_text)


def write_ratio_log(file_name, point, cls_rev, price):
    path = os.path.join(TRADE_RATIO_LOG_DIR, '%s.log' % file_name)
    with open(path, 'a') as put:
        all_the_text = '%d,%.02lf,%.02lf\n' % \
                       (
                           point,
                           cls_rev,
                           price
                       )
        put.writelines(all_the_text)


def array_get(arr, keys):
    values = []
    count = len(arr)
    for k in keys:
        if k >= count:
            k = -1
        values.append(arr[k])
    return values
