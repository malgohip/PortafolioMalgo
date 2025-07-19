

def parse_range(pages_range):
    """Convert range string to a list of pages."""
    result = set()
    parts = pages_range.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.update(range(start, end + 1))
        else:
            result.add(int(part))
    return sorted(result)

def format_pages(pages):
    """Convert a sorted list of pages to a shortest possible format."""
    if not pages:
        return ""
    
    ranges = []
    start = end = pages[0]
    
    for page in pages[1:]:
        if page == end + 1:
            end = page
        else:
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}-{end}")
            start = end = page
    
    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}-{end}")
    
    return ','.join(ranges)

def missing_pages(total_pages, printed_pages):
    """Determine missing pages given total and already printed pages."""
    all_pages = set(range(1, total_pages + 1))
    printed_pages_set = parse_range(printed_pages)
    missing_pages_set = sorted(all_pages - set(printed_pages_set))
    
    return format_pages(missing_pages_set)

def main(input_data):
    lines = input_data.strip().split('\n')
    T = int(lines[0])
    results = []
    
    for line in lines[1:T+1]:
        parts = line.split()
        N = int(parts[0])
        printed_pages = ' '.join(parts[1:])
        results.append(missing_pages(N, printed_pages))
    
    return ' '.join(results)

input_data = """
8
8 8,3
12 3,4,12,4
18 10,11-14,12,13,4
27 27,13-15,4-5,27,3-11,10-14,17-23,15,10-18
29 16,4,28-29,22-29,28,16-26,7-8,8,6-14,22-29,5-6,10
37 7-17,2-11,33,37,16,1,28,6,27-33,11-15,1,16-25,17,14,7-11
42 10-14,15-24,8,17,18,19-23,39-42,27-29,16,24-31,17,11-18
54 9-15,20-21,11,49,27-36,3-5,43-48,52,13-19,51,36-38,27-36,23,3,43,43,19-23
"""

print(main(input_data))