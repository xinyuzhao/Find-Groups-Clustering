import hierCluster as hier

if __name__ == '__main__':
    with open('blog_data.txt', 'r') as f:
        input = f.readlines()
    f.closed

    data = []
    label = []
    for i in range(1, len(input)):
        tmp = input[i].split('\t')

        row = []
        label.append(tmp[0])
        for j in range(1, len(tmp)):
            row.append(int(tmp[j]))

        data.append(row)

    root = hier.buildTree(data)
    hier.displayTree(root, label)


