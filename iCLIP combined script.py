with open("rn7sk.extracted.final.iclip1.plus.bedgraph") as inp:
    values = list((line.strip().split('\t') for line in inp))

output = []
for i in range(len(values)):
    num = values[i][1]
    gene = values[i][0]
    if int(num) >= 52995615 and int(num) <= 52995951 and gene == 'chr6':
            values[i].insert(0, str(int(num) - 52995614))
            line = values[i]
            output.append(line)

with open('rn7sk.extracted.gene.numbered.iclip1.plus.bedgraph', 'w') as file:
    file.writelines('\t'.join(i) + '\n' for i in output)