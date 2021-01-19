import re
import datetime


def write_info(filename, info):
    with open(filename, 'wb') as fo:
        fo.write(info)
    print(datetime.datetime.now(), filename, '写入完毕')


def macth(rule, doc):
    return re.compile(rule, re.DOTALL).findall(doc)


# 1) 目录的预处理
# with open('./README.md', 'rb') as fi:
#     doc = fi.read()
#     L_job1 = macth(
#         rb'<!-- menu_base -->(.*?)<!-- menu_base -->', doc)
#     L_job2 = macth(
#         rb'<!-- menu_write -->.*?<!-- menu_write -->', doc)

# if L_job1 and L_job2:
#     menu = b'<!-- menu_write -->' + L_job1[0] + b'<!-- menu_write -->'
#     menu = b'\r\n'.join((x.strip() for x in menu.splitlines()))
#     with open('./README.md', 'wb') as fo:
#         fo.write(doc.replace(L_job2[0], menu))


# 2) sidebar和intro匹配
L_jobs = []
with open('./README.md', 'rb') as fi:
    doc = fi.read().replace(b'/docs/', b'')
    L_jobs.extend(
        # [('./docs/_sidebar.md',
        [('./_sidebar.md',
          macth(rb'<!-- menu -->.*?<!-- menu -->', doc)),
         # ('./00.Python/Introduction.md',
         #  macth(rb'<!-- introduction -->.*?<!-- introduction -->', doc))
         ]
    )

# write_info('./docs/README.md', doc)

for filename, L_job in L_jobs:
    if L_job:
        write_info(filename, L_job[0])
