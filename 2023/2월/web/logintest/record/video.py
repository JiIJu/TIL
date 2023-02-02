# opencv 웹캠


from django.utils import timezone
import threading
from datetime import datetime
import cv2
# from record.models import Image
import socket



import pickle
from sklearn.metrics import mean_absolute_error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class VideoCamera(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        #host_ip = "192.168.100.246"
        port = 10050
        self.server_socket.bind((host_ip, port))
        print("socket bind complete")
        self.server_socket.setblocking(False)
        threading.Thread(target=self.update, args=()).start()


    def get_frame(self):
        return self.data[0].tobytes()

    def get_ans(self):
        return self.ans

    def update(self):
        # while True:
        #     (self.grabbed, self.frame) = self.video.read()
        move = pd.read_excel('C:\\Users\\multicampus\\Desktop\\gogo\\S08P12C102\\web\\logintest\\record\\Back_test3_Ver3.xlsx')

        cell = move.iloc[0:761, 0:34]
        label = move.iloc[0:761, 34]
        kn = KNeighborsClassifier()

        kn.n_neighbors = 3
        kn.fit(cell, label)

        while 1:
            try:
                packet = self.server_socket.recvfrom(100000000)
            except BlockingIOError:
                continue

            data = packet[0]
            self.data = pickle.loads(data)  # oriData[1] : 자세데이터
            
            # print('////////////////')
            # print(self.data[1])
            
            # print('////////////////')

            self.ans = kn.predict([self.data[1]])

            # kn.predict(self.data[1])

            # print(len(self.data))
            # print(type(self.data[0]))
            # print(type(self.data[1]))

        self.server_socket.close()
