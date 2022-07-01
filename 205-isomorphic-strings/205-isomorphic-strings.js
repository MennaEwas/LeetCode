/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let arr1 = {}
    let arr2 = {}
    for (let i=0;i<s.length;i++) {
        if(arr1[s[i]] !== arr2[t[i]]) {
            return false
        }else{
            arr1[s[i]] = i,
            arr2[t[i]] = i
        }
    }
    return true
};