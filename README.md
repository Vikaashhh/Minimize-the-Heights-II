# 🏔️ Day-9: Minimize the Height II

This repository contains an optimal Python implementation for the **"Minimize the Height II"** problem, a classic **Greedy Algorithm** challenge. The objective is to **minimize the difference** between the tallest and shortest tower after modifying each tower’s height by either increasing or decreasing it by `k`.

---

## 📌 Problem Statement

You are given an array of heights and a value `k`. You can either **increase or decrease** each height by `k` (only once per height).  
Your task is to **minimize the maximum difference** between the tallest and shortest towers after the modification.

---

## 🧠 Approach & Intuition

### Strategy:
- First, **sort** the array to simplify comparison.
- Set an initial answer as the difference between max and min (unmodified).
- Traverse the array to simulate dividing it into two segments:
  - For the left segment: Add `k`
  - For the right segment: Subtract `k`
- Skip any operation that results in negative height.
- Update the minimum difference based on new `min_elem` and `max_elem`.

---

## 🔄 Algorithm Steps

1. Sort the array.
2. Calculate the initial `ans = max - min`.
3. Traverse from index 1 to `n-1`:
   - Skip if reducing `arr[i]` by `k` gives a negative number.
   - Compute:
     - `max_elem = max(arr[i-1] + k, arr[n-1] - k)`
     - `min_elem = min(arr[0] + k, arr[i] - k)`
   - Update `ans` with the new difference if smaller.

---

## 🧪 Sample Input/Output

**Input:**
Enter value of k: 2, 
Enter array of heights: 1 5 8 10

**Output:**
Minimum possible difference: 5

---
✅ Complexity Analysis
- Time Complexity: O(n log n) — due to sorting

- Space Complexity: O(1)

---

📅 Challenge Tag
```
#gfg160 #geekstreak2025 #Day9
```
---
## ✨ About the Creator
Crafted with precision by Vikash Joshi, a passionate UI/UX designer and DSA enthusiast committed to mastering algorithms, one day at a time.

If you found this helpful, drop a ⭐️ and share it with your peers. Let's grow together 🚀
