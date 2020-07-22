def isSubSequence(String, str2): 
	m = len(String); 
	n = len(str2); 
	j = 0;
	i = 0; 
	while (i < n and j < m): 
		if (String[j] == str2[i]): 
			j += 1; 
		i += 1; 
	return (j == m); 
def findLongestString(name_list, String): 
	result = ""; 
	length = 0; 
	for word in name_list: 
		if (length < len(word) and isSubSequence(word, String)): 
			result = word; 
			length = len(word); 
	return result;  
String =input()
name_list = list(map(str,input().split())) 
print(findLongestString(name_list, String)); 
