class Sol:
    def majority(self,array):
        count=0
        for num in array:
            if count==0:
                candidate=num
            if candidate==num:
                count+=1
            else:
                count-=1
        return candidate


if __name__ == '__main__':
    p1=Sol()
    print(p1.majority([3,2,2,3]))
