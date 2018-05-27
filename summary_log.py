from os.path import join

from core.config import TRADE_LOG_DIR


c = {
        'v9888-100000.log': 0,
        'c9888-100000.log': 0,
        'l9888-100000.log': 0,
        'OI888-100000.log': 0,
        'bu888-100000.log': 0,
        'a9888-100000.log': 0,
        'y9888-150000.log': 0,
        'p9888-100000.log': 0,
        'SR888-100000.log': 0,
        'j9888-350000.log': 0,
        'jm888-300000.log': 0,
        'TA888-100000.log': 0,
        'MA888-100000.log': 0,
        'i9888-200000.log': 0,
        'au888-250000.log': 0,
        'al888-200000.log': 0,
        'cu888-300000.log': 0,
        'zn888-250000.log': 0,
        'ni888-150000.log': 0,
        'ag888-100000.log': 0,
    }


def search_file(file_name, ctime, ltime):
    global c
    # with open(join(TRADE_LOG_DIR, 'lou.log'), 'a') as fw:
    with open(join(TRADE_LOG_DIR, file_name), 'r') as fb:
        fb.seek(c[file_name])
        prev = l = fb.readline()
        while l:
            t_time, all_rev, flt_rev, cls_rev, money, volume, ratio = l.split(',')[1:]
            if ctime > float(t_time):
                # if ltime < float(t_time):
                    # fw.write(l)
                c[file_name] = fb.tell()
                l = fb.readline()
                continue
            if ctime == float(t_time):
                c[file_name] = fb.tell()
                return (all_rev, flt_rev, cls_rev, money, volume, ratio)
            if ctime < float(t_time):
                return None
    return None


if __name__ == '__main__':
    file_list = [
        ('1460614620.000000', 'v9888-100000.log'),
        ('1466651240.000000', 'c9888-100000.log'),
        ('1466747900.000000', 'l9888-100000.log'),
        ('1482990700.000000', 'OI888-100000.log'),
        ('1483967070.000000', 'bu888-100000.log'),
        ('1484705590.000000', 'a9888-100000.log'),
        ('1486091180.000000', 'y9888-150000.log'),
        ('1486602530.000000', 'p9888-100000.log'),
        ('1486609850.000000', 'SR888-100000.log'),
        ('1486609950.000000', 'j9888-350000.log'),
        ('1486707450.000000', 'jm888-300000.log'),
        ('1486992990.000000', 'TA888-100000.log'),
        ('1487140770.000000', 'MA888-100000.log'),
        ('1487207060.000000', 'i9888-200000.log'),
        ('1489670740.000000', 'au888-250000.log'),
        ('1489769760.000000', 'al888-200000.log'),
        ('1491400290.000000', 'cu888-300000.log'),
        ('1492444340.000000', 'zn888-250000.log'),
        ('1492754950.000000', 'ni888-150000.log'),
        ('1494439640.000000', 'ag888-100000.log')
    ]

    b = []

    last_time = 0

    with open(join(TRADE_LOG_DIR, 'summary.log'), 'w') as fw:
        with open(join(TRADE_LOG_DIR, 'rb888-100000.log'), 'r') as fb:
            for l in fb:
                pos, t_time, all_rev, flt_rev, cls_rev, money, volume, ratio = l.split(',')
                t_time = float(t_time)
                s_all_rev = float(all_rev)
                s_flt_rev = float(flt_rev)
                s_cls_rev = float(cls_rev)
                s_money = float(money)
                s_volume = int(volume)
                s_ratio = float(ratio)
                if len(file_list) > 0 and t_time >= float(file_list[0][0]):
                    b.append(file_list[0][1])
                    file_list.remove(file_list[0])
                for s in b:
                    line = search_file(s, t_time, last_time )
                    if line:
                        ar, fr, cr, m, v, r = line
                        s_all_rev += float(ar)
                        s_cls_rev += float(cr)
                        s_flt_rev += float(fr)
                        s_volume += int(v)
                        s_ratio += float(r)
                        s_money += float(m)
                    else:
                        last_time = t_time
                        break
                last_time = t_time
                fw.write(
                    '{:.06f},{:.02f},{:.02f},{:.02f},{:.02f},{:d},{:.02f}\n'.format(
                        t_time, s_all_rev, s_flt_rev, s_cls_rev, s_money, s_volume, s_ratio
                    )
                )
                print pos
            print 'Done'
