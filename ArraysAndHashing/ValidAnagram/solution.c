char selectionSort(char *s){
    int n = strlen(s);
    int temp;
    for(int i = 0; i < n-1; i++){
        for(int j = i + 1; j < n; j++){
            if (s[i] > s[j]){
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    return s;
}

bool isAnagram(char * s, char * t){
    selectionSort(s);
    selectionSort(t);
    int value = strcmp(s, t);
    if(value == 0){
        return true;
    }
    return false;
}