class Sort:

    def bubbleSort(self, arr):

        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print('Sorted array: ', end='')
        print(arr)

    def selectionSort(self, arr):

        for i in range(len(arr)):

            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print('Sorted array: ', end='')
        print(arr)

    def insertionSort(self, arr):

        for i in range(1, len(arr)):

            key = arr[i]

            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        print('Sorted array: ', end='')
        print(arr)

    def mergeSort(self, arr):

        if len(arr) > 1:

            mid = len(arr) // 2

            L = arr[:mid]

            R = arr[mid:]

            self.mergeSort(L)

            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        print('Sorted array: ', end='')
        print(arr)

    def partition(self, start, end, array):

        pivot_index = start
        pivot = array[pivot_index]

        while start < end:

            while start < len(array) and array[start] <= pivot:
                start += 1

            while array[end] > pivot:
                end -= 1

            if start < end:
                array[start], array[end] = array[end], array[start]

        array[end], array[pivot_index] = array[pivot_index], array[end]

        return end

    def quickSort(self, start, end, array):

        if start < end:
            p = self.partition(start, end, array)

            self.quickSort(start, p - 1, array)
            self.quickSort(p + 1, end, array)