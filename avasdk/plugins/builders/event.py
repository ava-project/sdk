

def build_event(raw):
    """
    """
    index = 0
    event = {}
    keys = ['action', 'target', 'args']
    for key in keys:
        event[key] = None
    results = ' '.join(raw.split()).split(' ')
    for key, result in zip(keys, results):
        if key == 'args':
            event[key] = ' '.join(map(str, results[index:]))
        else:
            event[key] = result
        index += 1
    return event
