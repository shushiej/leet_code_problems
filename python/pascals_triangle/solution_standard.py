class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            
            # Generate List of None's until the num_rows
            row = [None for _ in range(row_num+1)]
            # The first and last row elements are always 1.
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle