from datetime import datetime, timedelta

def solution(lines):
    answer = 0

    complited_t = []
    during_t = []

    for line in lines:
        t = line[:23]
        spend_t = line[24:]

        complited_t.append(datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f'))
        
        s = timedelta(seconds=int(spend_t[:1]))
        if not spend_t[2:-1] == '':
            s += timedelta(milliseconds=int(spend_t[2:-1]))
        during_t.append(s)

    for i in range(len(lines)):
        throughput = 1
        one_seconds = complited_t[i] + timedelta(milliseconds=999)
        four_seconds = complited_t[i] + timedelta(seconds=3,milliseconds=999)

        for j in range(i+1,len(lines)):
            if complited_t[j] > four_seconds:
                break

            started = complited_t[j] - during_t[j] + timedelta(milliseconds=0.001)
                
            if started <= one_seconds:
                throughput += 1

        answer = max(answer, throughput)

    return answer

if __name__ == '__main__':
    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(lines))