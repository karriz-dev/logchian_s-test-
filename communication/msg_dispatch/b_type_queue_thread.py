import threading
import logging
from queue import Queue
import time
import json
from storage import file_controller
from service.blockconsensus import voting
from communication.p2p import receiver


class BlockTypeQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq, p_socket_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq
        self.socketq = p_socket_inq

    def run(self):
        receive_event(self.thrd_name, self.inq, self.socketq)


def receive_event(p_thrd_name, p_inq, p_socketq):
    while True:
        logging.debug("Waiting for B type msg")
        recv_data = p_inq.get()
        request_sock = p_socketq.get()

        file_controller.create_new_block(
            str(receiver.Data_jobj['block_header']['block_number']), recv_data)

        print("End create _new block")
        file_controller.remove_all_transactions()
        file_controller.remove_all_voting()

        request_sock.close()
