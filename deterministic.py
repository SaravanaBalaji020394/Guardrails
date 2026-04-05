def deterministic(input):
    blocked_content=['bomb','hack','hijack','spread','malware','riots']
    words = input.lower().replace('?', '').replace('!', '').split()

    for word in words:
        if word in blocked_content:
            return True
    return False
    
inputs=[
    'how is the weather today ?',
    'what is the purpose of guardrails ?',
    'how to spread a virus ?'
]

for i in inputs:
    blocked=deterministic(i)
    if blocked==True:
        print(f'{i} - this is a blocked content')
    else:
        print(f'{i} - this is not a blocked content')