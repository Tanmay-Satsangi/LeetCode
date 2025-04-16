# @param {String} s
# @return {String}
def longest_palindrome(s)
  n = s.length
  pal_start = 0
  pal_max_len = 0

  (0...n).each do |i|
    start1, len1 = expand_around_centers(s, i, i)       # Odd-length
    start2, len2 = expand_around_centers(s, i, i + 1)   # Even-length

    if len1 > pal_max_len
      pal_start = start1
      pal_max_len = len1
    end

    if len2 > pal_max_len
      pal_start = start2
      pal_max_len = len2
    end
  end

  s[pal_start, pal_max_len]
end

def expand_around_centers(s, left, right)
  while left >= 0 && right < s.length && s[left] == s[right]
    left -= 1
    right += 1
  end

  return left + 1, right - left - 1
end
