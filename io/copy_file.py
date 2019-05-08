source = r'C:\Users\ooo654\everything-python\io\formatting.py'
dest = r'C:\Users\ooo654\everything-python\io\formatting2.py'
with open(source) as f: 
    source_lines = list(f)
    print(repr(source_lines[0]))
    with open(dest, 'w') as g:
        for x in source_lines:
            g.write(x)
        