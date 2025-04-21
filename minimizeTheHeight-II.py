class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        
        # Agar sirf ek element ho, toh difference 0 hoga
        if n == 1:
            return 0

        # Step 1: Sort karo array ko
        arr.sort()

        # Step 2: Initial difference without any modification
        ans = arr[-1] - arr[0]

        # Step 3: Loop through array to consider every possible partition
        for i in range(1, n):
            if arr[i] - k < 0:
                continue  # Height negative nahi ho sakti

            # Maximum and minimum values after modification
            max_elem = max(arr[i - 1] + k, arr[-1] - k)
            min_elem = min(arr[0] + k, arr[i] - k)

            # Update answer if smaller difference mila
            ans = min(ans, max_elem - min_elem)

        return ans


# -------- Driver Code --------
if __name__ == "__main__":
    k = int(input("Enter value of k: "))
    arr = list(map(int, input("Enter array of heights: ").split()))
    
    sol = Solution()
    print("Minimum possible difference:", sol.getMinDiff(arr, k))