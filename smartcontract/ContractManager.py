import threading
import json
from queue import Queue
from service.transactionmanager.contract_transaction import ContractTransaction

contract_transaction_queue = Queue()
contract_state = {}


class ContractManager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if contract_transaction_queue.qsize() > 0:
                transaction = json.loads(contract_transaction_queue.get())

                if transaction['type'] == 'CT':
                    # extract parameters
                    # Contract Runner
                    contract_state = 'end'
                    pass
                elif transaction['type'] == 'RT':
                    # extract parameters
                    # Excute Contract
                    contract_state = 'end'
                    pass

    def contract_deploy(self, filePath):
        # DeployContract Tx 생성
        transaction = ContractTransaction(filePath)
        if transaction != None:
            # tx 전파
            return 'OK'
        else:
            return None

    def contract_execute(self):
        # run tx 생성
        pass
