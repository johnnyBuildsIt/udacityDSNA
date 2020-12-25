class PascalsTriangle:

    def return_nth_row(self, n):
        triangle = [[1]]
        if n == 0:
            return triangle[-1]

        for i in range(1, n + 1):
            prev_row = triangle[i - 1]
            cur_row = [1]
            for j in range(1, i):
                cur_row.append(prev_row[j - 1] + prev_row[j])
            cur_row.append(1)
            triangle.append(cur_row)
        return triangle[-1]