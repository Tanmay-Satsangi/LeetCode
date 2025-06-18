# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    group = {}

    strs.each do |word|
        key = word.chars.sort.join

        group[key] ||= []

        group[key] << word
    end
    group.values
end