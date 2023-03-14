

def add(pol1, pol2, pol1_len, pol2_len):
    max_range =max(pol1_len, pol2_len)
    results =[0] * (max_range)

    for index in range(pol1_len):
        results[index] = pol1[index]

    for index in range(pol2_len):
        results[index] += pol2[index]

    return results


def main():
    pol1 = [5, -1]
    pol2 =[0, 6]

    results = add(pol1, pol2, len(pol1), len(pol2))
    print(results)

if __name__ == '__main__':
    main()