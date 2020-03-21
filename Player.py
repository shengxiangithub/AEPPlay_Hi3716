# encoding=utf-8
import subprocess, threading, time
import Constant


class Player(object):
    """
    [
        {
            "volume":12,
            "streaming_url":"rtsp://117.27.128.45:1054/68591239687180288.sdp",
            "level":795,
            "action":"play",
            "task_number":"202002252309482925",
            "text":" "
        },
        {
            "volume":13,
            "streaming_url":"rtsp://117.27.128.45:1054/68591239687180299.sdp",
            "level":796,
            "action":"play",
            "task_number":"202002252309482925",
            "text":" "
        }
    ]
    """

    # __slots__ = ('task_array', 'now_playing_task', 'queue')

    def __init__(self):
        self.task_array = []
        self.now_playing_task = None
        # self.queue = Queue(10)
        # play_status_thread = threading.Thread(target=self.play_status_thread,
        #                                       name='play_status_thread')
        # play_status_thread.start()

    def add_task(self, task):
        if len(self.task_array) > 0:
            for i in range(len(self.task_array)):
                if task.get("task_number") == self.task_array[i].get("task_number") and task.get("streaming_url") == \
                        self.task_array[i].get("streaming_url"):
                    print("重复任务")
                    return
        self.task_array.append(task)

    def add_tasks(self, tasks):
        if tasks is None:
            return
        for i in range(len(tasks)):
            if tasks[i] is not None and tasks[i].get("streaming_url") is not None and tasks[i].get(
                    "task_number") is not None and tasks[i].get("level") is not None:
                self.add_task(tasks[i])
        self.choise_one_to_play()

    def choise_one_to_play(self):
        self.sort_by_level_desc(self.task_array)
        if self.task_array is not None and len(self.task_array) > 0:
            print("有任务需要被播放")
            if self.now_playing_task is None:
                self.now_playing_task = self.task_array[0]
                self.play(self.now_playing_task)
            else:
                if self.now_playing_task.get("level") >= self.task_array[0].get("level"):
                    print("当前在播的任务就是优先级最高的任务")
                else:
                    self.stop_play()
                    print("当前任务被打断，暂停当前任务")
                    self.now_playing_task = self.task_array[0]
                    self.play(self.now_playing_task)
        else:
            print("暂无任务")

    def play(self, task):
        play_thread = threading.Thread(target=self.play_thread, args=[task], name='play_thread')
        play_thread.start()

    def play_thread(self, task):
        print("开始播放：" + str(task))
        Constant.STATUS = 2
        time.sleep(1)  # 收到指令的时候流还没推上去
        if Constant.msg_queue is not None:
            Constant.TASK_NUM = task.get("task_number")
            Constant.msg_queue.put({"aep_heart": "volume_on"})
        volume = task.get("volume")
        if volume is None:
            volume = Constant.VOLUME
        Constant.VOLUME = volume
        volume = "-" + str(int(50 - (volume / 2) * 0.8))
        cmd = "mplayer -af volume=" + volume + " -rtsp-stream-over-tcp -vo null  -ac ffmp3 " + task.get(
            "streaming_url")  # -ac mad
        begin_play = int(time.time())
        popen = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
        popen.wait()
        end_play = int(time.time())
        if end_play - begin_play < 10:  # 播放时间太短，可能有问题，重试一次
            cmd = "mplayer -af volume=" + volume + " -rtsp-stream-over-tcp -vo null " + task.get("streaming_url")
            popen = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
            popen.wait()
        Constant.STATUS = 1
        if Constant.msg_queue is not None:
            Constant.TASK_NUM = ""
            Constant.msg_queue.put({"aep_heart": "volume_off"})
        print("播放完成")
        self.now_playing_task = None
        try:
            self.task_array.remove(task)
        except Exception as e:
            print("err" + str(e) + "\n")
            print("平台播完自动下发了停播指令")
        if Constant.msg_queue is not None:
            Constant.msg_queue.put({"play_next": "play_next"})

    # 停止播放
    def stop_play(self):
        popen = subprocess.Popen("killall -9 mplayer", shell=True, stdin=subprocess.PIPE)
        popen.wait()
        time.sleep(0.5)

    # 取消播放
    def cancle_task(self, task_number):
        if self.task_array is not None and len(self.task_array) > 0:
            for i in range(len(self.task_array)):
                if task_number == self.task_array[i].get(task_number):
                    self.task_array.remove(self.task_array[i])
                    print("从任务队列里面移除任务" + str(task_number))
        if self.now_playing_task is not None and task_number == self.now_playing_task.get("task_number"):
            print("取消的是正在播放的任务")
            self.stop_play()
        else:
            print("取消的是任务队列里的任务")

    # 对任务进行排序
    def sort_by_level_desc(self, tasks):
        if tasks is None or len(tasks) == 0:
            return
        for i in range(len(tasks) - 1):
            for j in range(len(tasks) - 1 - i):
                if tasks[j].get("level") < tasks[j + 1].get("level"):
                    tmp = tasks[j]
                    tasks[j] = tasks[j + 1]
                    tasks[j + 1] = tmp
        print(tasks)

    # def play_status_thread(self):
    #     print("waite play_next msg...")
    #     try:
    #         while True:
    #             queue_msg = self.queue.get()
    #             if queue_msg is not None:
    #                 print(str(queue_msg))
    #                 key = list(queue_msg.keys())[0]
    #                 if key == "play_next":  # 播放下一条指令
    #                     self.choise_one_to_play()
    #     except Exception as e:
    #         print("waite play_next msg:" + str(e))
    #         self.play_status_thread()
# if __name__ == '__main__':
#     a = Player()
#     task0 = {
#         "volume": 0,
#         "streaming_url": "rtsp://117.27.128.45:1054/68591239687180288.sdp",
#         "level": 0,
#         "action": "play",
#         "task_number": "202002252309482925",
#         "text": " "
#     }
#     task1 = {
#         "volume": 1,
#         "streaming_url": "rtsp://117.27.128.45:1054/68591239687180288.sdp",
#         "level": 1,
#         "action": "play",
#         "task_number": "202002252309482925",
#         "text": " "
#     }
#     task2 = {
#         "volume": 2,
#         "streaming_url": "rtsp://117.27.128.45:1054/68591239687180288.sdp",
#         "level": 2,
#         "action": "play",
#         "task_number": "202002252309482925",
#         "text": " "
#     }
#     task3 = {
#         "volume": 3,
#         "streaming_url": "rtsp://117.27.128.45:1054/68591239687180288.sdp",
#         "level": 3,
#         "action": "play",
#         "task_number": "202002252309482925",
#         "text": " "
#     }
#     tasks = [task1, task0, task3, task2, task2, task2, task2]
#     a.sort_by_level_desc(tasks)
