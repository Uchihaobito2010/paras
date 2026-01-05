bold_map = {
    'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙',
    'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳',
    '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯'
}

def bold(text):
    return ''.join(bold_map.get(c, c) for c in str(text))

def print(*args, sep=' ', end='\n'):
    __builtins__.print(sep.join(bold(a) for a in args), end=end)
