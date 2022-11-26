def pick_peaks(arr):
    prev,cur = 0,0
    pos = []
    peaks = []
    for next in range(1,len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        else:
            if arr[next] < arr[cur]:
                if arr[prev] < arr[cur]:
                    pos.append(cur)
                    peaks.append(arr[cur])
                prev = cur
                cur = next

    return {"Pos":pos,"Peaks":peaks}

arr = [3, 2, 3,6, 4, 1, 2, 3, 2, 1, 2, 3]
print(pick_peaks(arr))