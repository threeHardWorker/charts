from os.path import join

import time

from core.config import TRADE_LOG_DIR

if __name__ == '__main__':
    file_list = [
        # 'rb888-100000.log',
        # 'v9888-100000.log',
        # 'c9888-100000.log',
        # 'l9888-100000.log',
        # 'OI888-100000.log',
        # 'bu888-100000.log',
        # 'a9888-100000.log',
        # 'y9888-150000.log',
        # 'p9888-100000.log',
        # 'SR888-100000.log',
        # 'j9888-350000.log',
        # 'jm888-300000.log',
        # 'TA888-100000.log',
        # 'MA888-100000.log',
        # 'i9888-200000.log',
        # 'au888-250000.log',
        # 'al888-200000.log',
        # 'cu888-300000.log',
        # 'zn888-250000.log',
        # 'ni888-150000.log',
        'ag888-100000.log',
    ]

    for f in file_list:
        with open(join(TRADE_LOG_DIR, 'day/%s' % f), 'w') as fw:
            with open(join(TRADE_LOG_DIR, f), 'r') as fb:
                prev = ''
                prev_line = ''
                for l in fb:
                    t_time = float(l.split(',')[1])
                    pos = int(l.split(',')[0])
                    curr = time.strftime('%Y-%m-%d', time.localtime(t_time))
                    if prev != '' and prev != curr:
                        fw.write(prev_line)
                    prev = curr
                    prev_line = l
            fw.write(prev_line)

