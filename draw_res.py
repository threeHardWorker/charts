# -*- coding: UTF-8 -*-
# author: star
# created_at: 18-2-1 20:16
import gc, sys, os


def read_file(data_path):
    zheng = 0
    fu = 0
    count = 0
    try:
        with open(data_path, 'r') as output:
            lines = output.readlines()
            for line in lines:
                line = line.split(': ')[-1]
                # if line.startswith('Open'):
                #     dir, pos = line.split(',')[2:4]
                #     if int(dir) > 0:
                #         self.__o_l.append(int(pos))
                #     else:
                #         self.__o_s.append(int(pos))
                if line.startswith('Close'):
                    count += 1
                    cls_rev = line.split(',')[7]
                    if float(cls_rev) > 0:
                        zheng += 1
                    else:
                        fu += 1
            return zheng, fu, count
    except IOError:
        print "Error: No such data file. Filename: %s" % self.data_path
        exit(0)


if __name__ == '__main__':
    gc.disable()
    gc.enable()

    # if len(sys.argv) < 3:
    #     print 'Usage: python dl6.py <instrument>\n'
    #     exit(0)

    #     instrument = sys.argv[1].encode('ascii')
    data_dir = '/home/zj/v6/v6-4-5-logs'
    count = 0
    count_z = 0
    count_f = 0
    for dirname, dirnames, filenames in os.walk(data_dir):
        for filename in filenames:
            file_path = os.path.join(data.dir, filename)
            z, f, c = read_file(file_path)
            print '%s: Success-%d, Fail-%d, Count-%d, ' % (filename, z, f, c)
            count += c
            count_z += z
            count_f += f

    print 'Result: Success-%d, Fail-%d, Count-%d' % (count_z, count_f, count)
    print 'Done.'
