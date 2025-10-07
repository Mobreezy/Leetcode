#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int cmpfunc (const void * a, const void * b) {
    return ( *(int*)a - *(int*)b );
}

bool containsDuplicate(int* nums, int numsSize){
    if (numsSize <= 1) return false;
    
    int* temp = (int*)malloc(numsSize * sizeof(int));
    memcpy(temp, nums, numsSize * sizeof(int));
    
    qsort(temp, numsSize, sizeof(int), cmpfunc);
    for (int i = 0; i < numsSize - 1; i++){
        if (temp[i] == temp[i+1]){
            free(temp);
            return true;
        }
    }
    
    free(temp);
    return false;  
}

void test_case(int test_num, int* nums, int numsSize, bool expected) {
    int* test_array = (int*)malloc(numsSize * sizeof(int));
    memcpy(test_array, nums, numsSize * sizeof(int));
    
    bool result = containsDuplicate(test_array, numsSize);
    
    printf("Test %d: ", test_num);
    printf("[");
    for (int i = 0; i < numsSize; i++) {
        printf("%d", nums[i]);
        if (i < numsSize - 1) printf(", ");
    }
    printf("] -> %s ", result ? "true" : "false");
    
    if (result == expected) {
        printf("✓ PASSED\n");
    } else {
        printf("✗ FAILED (expected %s)\n", expected ? "true" : "false");
    }
    
    free(test_array);
}

int main() {
    printf("=== Contains Duplicate Test Cases ===\n\n");
    
    printf("Basic Cases:\n");
    int test1[] = {1, 2, 3, 1};
    test_case(1, test1, 4, true);
    
    int test2[] = {1, 2, 3, 4};
    test_case(2, test2, 4, false);
    
    int test3[] = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    test_case(3, test3, 10, true);
    
    printf("\nEdge Cases:\n");
    int test4[] = {1};
    test_case(4, test4, 1, false);
    
    int test5[] = {1, 1};
    test_case(5, test5, 2, true);
    
    int test6[] = {5, 5, 5, 5, 5};
    test_case(6, test6, 5, true);
    
    printf("\nNegative Numbers:\n");
    int test7[] = {-1, -2, -3, -1};
    test_case(7, test7, 4, true);
    
    int test8[] = {-1, -2, -3, -4};
    test_case(8, test8, 4, false);
    
    printf("\nMixed Positive and Negative:\n");
    int test9[] = {-3, 4, -3, 5};
    test_case(9, test9, 4, true);
    
    int test10[] = {-3, 4, 5, 6};
    test_case(10, test10, 4, false);
    
    printf("\nLarge Numbers:\n");
    int test11[] = {1000000000, -1000000000, 1000000000};
    test_case(11, test11, 3, true);
    
    int test12[] = {2147483647, -2147483648, 0};
    test_case(12, test12, 3, false);
    
    printf("\nDuplicate at Different Positions:\n");
    int test13[] = {7, 1, 5, 3, 6, 4, 7};
    test_case(13, test13, 7, true);
    
    int test14[] = {0, 4, 5, 0, 3, 6};
    test_case(14, test14, 6, true);
    
    printf("\n=== All tests completed ===\n");
    
    return 0;
}
