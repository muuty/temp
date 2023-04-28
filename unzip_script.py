import gzip

original = [
    '1.tsv.gz',
    '2.tsv.gz',
    '3.tsv.gz',
    '4.tsv.gz',
    '5.tsv.gz',
]
out_file = 'unzipped.tsv'

line = None
with open(out_file, 'w', encoding='utf-8') as outfile:
    for file in original:
        with gzip.open(file, 'rb') as infile:
            while True:
                try:
                    line = infile.readline()
                    outfile.write(line.decode('utf-8'))
                except Exception as _:
                    try:
                        line = infile.readline()
                    except EOFError as e:
                        break

