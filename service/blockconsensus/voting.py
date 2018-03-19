import json
import time

import peerproperty.nodeproperty
from peerproperty import nodeproperty
from storage import file_controller
from communication.p2p import sender
from communication.peermgr import peermgr

def blind_voting(merkle_root):

    vote_number = (int(merkle_root, 16) % nodeproperty.Total_peer_num) + 1
    voting = {'To': vote_number,
              'from': nodeproperty.My_IP_address, 'type': 'V'}
    jsonString = json.dumps(voting)

    if nodeproperty.My_peer_num == vote_number:
        file_controller.add_voting(jsonString)
    else:
        index = nodeproperty.My_peer_num - 1
        ip_address = peerproperty.nodeproperty.ConnectedPeerList[index][1]
        sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)

        # if vote_number == 1:
        #     ip_address = nodeproperty.Peer1
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 2:
        #     ip_address = nodeproperty.Peer2
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 3:
        #     ip_address = nodeproperty.Peer3
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 4:
        #     ip_address = nodeproperty.Peer4
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 5:
        #     ip_address = nodeproperty.Peer5
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 6:
        #     ip_address = nodeproperty.Peer6
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 7:
        #     ip_address = nodeproperty.Peer7
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 8:
        #     ip_address = nodeproperty.Peer8
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)
        #
        # elif vote_number == 9:
        #     ip_address = nodeproperty.Peer9
        #     sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)



def result_voting():

    list = file_controller.get_voting_list()

    if len(list) > 8:
        difficulty = 2
        print("result voting : ", len(list))
        print(" ")
        return difficulty
    else:
        difficulty = 0
        return difficulty
