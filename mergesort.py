import matplotlib.pyplot as plt

def assigment(new_list, new_list_index, old_list, old_list_index):
    new_list[new_list_index] = old_list[old_list_index]



# This function implements the merge sort algorithm to sort a list in ascending order
def merge_sort(list_to_sort_by_merge):
    # Check if the list has more than one element and is not empty
    if (len(list_to_sort_by_merge) > 1):
        # Find the middle index of the list
        mid_list_index = len(list_to_sort_by_merge) // 2

        # Divide the list into two halves
        left_list = list_to_sort_by_merge[:mid_list_index]
        right_list = list_to_sort_by_merge[mid_list_index:]

        # Recursively call merge_sort on the left and right halves
        merge_sort(left_list)
        merge_sort(right_list)

        # Merge the sorted left and right halves
        left_list_index = 0
        right_list_index = 0
        list_index = 0

        # Compare elements from the left and right halves and merge them in sorted order
        while left_list_index < len(left_list) and right_list_index < len(right_list):
            if left_list[left_list_index] <= right_list[right_list_index]:
                list_to_sort_by_merge[list_index] = left_list[left_list_index]
                left_list_index += 1
            else:
                list_to_sort_by_merge[list_index] = right_list[right_list_index]
                right_list_index += 1
            list_index += 1

        # Copy any remaining elements from the left half
        while left_list_index < len(left_list):
            list_to_sort_by_merge[list_index] = left_list[left_list_index]
            left_list_index += 1
            list_index += 1

        # Copy any remaining elements from the right half
        while right_list_index < len(right_list):
            list_to_sort_by_merge[list_index] = right_list[right_list_index]
            right_list_index += 1
            list_index += 1



import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fig, ax = plt.subplots(ncols=2)
fig.subplots_adjust(wspace=0)
x = range(len(my_list))

ax[0].get_shared_y_axes().join(ax[0], ax[1])
ax[0].bar(x, my_list)
ax[0].set_xlabel("List Index")
ax[0].set_ylabel("Element Value")
ax[0].set_title("Unsorted List")

merge_sort(my_list)

ax[1].bar(x, my_list)
ax[1].set_xlabel("List Index")
ax[1].get_yaxis().set_visible(False)
ax[1].set_title("Sorted List")

plt.show()
