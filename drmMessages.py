def divide(msg):
    mid_idx = len(msg)//2
    return msg[:mid_idx], msg[mid_idx:]


def rotate(msg1, msg2):
    base_num = ord("A")
    nums1 = [ord(x)-base_num for x in msg1]
    nums2 = [ord(x)-base_num for x in msg2]
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    nums1 = [chr(((x+sum1)%26)+base_num) for x in nums1]
    nums2 = [chr(((x+sum2)%26)+base_num) for x in nums2]
    return "".join(nums1), "".join(nums2)


def merge(msg1, msg2):
    base_num = ord("A")
    nums1 = [ord(x)-base_num for x in msg1]
    nums2 = [ord(x)-base_num for x in msg2]
    nums = zip(nums1, nums2)
    sol = [x[0] + x[1] for x in nums]
    sol = [chr((x%26)+base_num) for x in sol]
    return "".join(sol)


def main():
    print(
        merge(
            *rotate(
                *divide(input()))))


main()