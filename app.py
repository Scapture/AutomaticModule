from multiprocessing import Process
import runModule

def run_in_processes():
    p1 = Process(target=runModule.run, args=(True,))
    p2 = Process(target=runModule.run, args=(False,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    run_in_processes()
