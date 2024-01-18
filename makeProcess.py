from multiprocessing import Process
import runModule

def run(pid):
    p1 = Process(target=runModule.run, args=(True, pid))
    # p2 = Process(target=runModule.run, args=(False, pid))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()

    print("makeProcess_pid: " +pid)
