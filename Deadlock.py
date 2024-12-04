import threading
import time

# 1. 리스트 내포 구문을 통해 5개의 잠긴 포크 생성
forks = [threading.Lock() for _ in range(5)]

def philosopher(phil_id, left_fork, right_fork):
    while True:
        print(f"철학자 {phil_id}는 생각중입니다...\n", end="")
        time.sleep(1)

        with left_fork:
            print(f"철학자 {phil_id}는 포크 {forks.index(left_fork)}를 집었습니다.\n", end="")
            time.sleep(1)

            with right_fork:
                print(f"철학자 {phil_id}는 포크 {forks.index(right_fork)}를 집었습니다.\n", end="")
                print(f"철학자 {phil_id}는 식사중입니다...\n", end="")
                time.sleep(2)

                print(f"철학자 {phil_id}는 오른쪽 포크를 내려놓습니다.\n", end="")

            print(f"철학자 {phil_id}는 왼쪽 포크를 내려놓고 다시 생각중입니다...\n", end="")

if __name__ == '__main__':
    philosophers = []

    for i in range(5):
        left_fork = forks[i]
        right_fork = forks[(i + 1) % 5]
        t = threading.Thread(target=philosopher, args=(i, left_fork, right_fork))
        philosophers.append(t)

    for t in philosophers:
        t.start()

    for t in philosophers:
        t.join()
        
        
        
        
        
        
        
        
print(forks[i])        


art=123
print(art)
