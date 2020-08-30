import heapq

def solution(jobs):
    time = 0
    tasks = []
    ptimes = []
    
    while True:
        if not jobs and not tasks:
            break

        for _ in range(len(jobs)):
            job = jobs.pop(0)
            if job[0] <= time:
                heapq.heappush(tasks, [job[1],job[0]])
            else:
                jobs.append(job)
        
        if tasks:
            task = heapq.heappop(tasks)
            time += task[0]
            p_time = time - task[1]
            ptimes.append(p_time)
        else:
            time += 1

    answer = sum(ptimes) // len(ptimes)
                
    return answer

if __name__ == '__main__':
    print(solution([[0, 3], [1, 9], [2, 6]]))