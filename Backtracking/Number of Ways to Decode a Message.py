def decode_ways(digits):

    def dfs(start_index):
        if start_index == len(digits):
            return 1

        ways = 0
        # can't decode string with leading 0
        if digits[start_index] == '0':
          return ways

        # decode one digit
        ways += dfs(start_index + 1)

        # decode two digits
        if 10 <= int(digits[start_index: start_index + 2]) <= 26:
            ways += dfs(start_index + 2)

        return ways


    return dfs(0)

if __name__ == '__main__':
    digits = input()
    res = decode_ways(digits)
    print(res)