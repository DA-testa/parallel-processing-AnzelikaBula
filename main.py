def parallel_processing(n, m, data):

    output = []

    finish = [0] * n

    for i, job_time in enumerate(data):

        mintime = min(finish)
        minthread = finish.index(mintime)
        output.append((minthread, mintime))
        finish[minthread] += job_time

    return output

def main():

    a, b = map(int, input().split())

    data = list(map(int, input().split()))

    resultats = parallel_processing(a, b, data)

    for z, c in resultats:

        print(z,c)

if __name__ == "__main__":

    main()