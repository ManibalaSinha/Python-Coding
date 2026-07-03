arr = [x for x in arr if x != target]

for i in range(len(arr)): #❌ Modifying list while iterating✅ Another common bug
    if arr[i] == target:
        arr.remove(arr[i])
# Fix: arr = [x for x in arr if x != target]
