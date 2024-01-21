class Solution:
     def compress(self, chars: List[str]) -> int:
        wrt_pointer, chk_pointer = 0, 0
        current_char = None
        current_len = 0
        
        while chk_pointer < len(chars):
            if chars[chk_pointer] != current_char:
                # a new character
                if current_len > 1:
                    len_str = []
                    while current_len:
                        len_str.append(str(current_len % 10))
                        current_len = current_len // 10
                    for lstr in len_str[::-1]:
                        chars[wrt_pointer] = lstr
                        wrt_pointer += 1
                chars[wrt_pointer] = chars[chk_pointer]
                wrt_pointer += 1
                current_char = chars[chk_pointer]
                current_len = 1
            else:
                # the same character
                current_len += 1
            chk_pointer += 1
        
        if current_len > 1:
            len_str = []
            while current_len:
                len_str.append(str(current_len % 10))
                current_len = current_len // 10
            for lstr in len_str[::-1]:
                chars[wrt_pointer] = lstr
                wrt_pointer += 1
        return wrt_pointer