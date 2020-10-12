#!/user/bin/env python3
# -*- coding: utf-8 -*-

def NnNone_dic(dic):
    keys = 1
    for key, value in dic.items():
        if len(value)==0 or value.isspace() ==True:
            keys=0

    return keys

# dic={'as':' ','saf':' '}
#
# print(NnNone_dic(dic))
