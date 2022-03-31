import os


def get_url():
    # 获取weekid   courseId 6  stageId 144
    url = 'https://gate.lagou.com/v1/neirong/edu/bigcourse/getStageWeeks?courseId=6&stageId=144'
    # 获取视频url
    url_video = 'https://gate.lagou.com/v1/neirong/edu/bigcourse/getWeekLessons?courseId=6&weekId=155'

    os.system(f'you-get -o D:/003共享网盘/medio{url_video}')


get_url()