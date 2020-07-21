def solution(message):

    # Helper function to decrypt a single letter
    def decrypt(letter):
        asc = ord(letter)
        return chr(219-asc) if 97 <= asc <= 122 else letter

    return "".join(map(decrypt, message))


if __name__ == '__main__':
    print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
    print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
