# Implemenation of List operations

# (CRUD) == (CAUDS)
# create
# init a list use square bracket
fr = []

# add
# add one element at end of list using append functionality
fr.append("apple") # 0
fr.append("banana") # 1
fr.append("coconut") # 2
fr.append("blueberry") # 3

# update
# Insertion 
# insert an element ata any given index if size-1 range
print("list before insertion : ",fr)
print(f"indexs size of list = {len(fr) - 1} indexs")
fr.insert(1, "cherry") # 1

print(f"After insert Cherry at Index : 1 list = {fr}")

# deletion
value = "blueberry"
fr.remove(value) # 2
fr.pop(2) #  3

#Search & Inspect
value = "apple"
i_apple = fr.index(value)

# size of list 
list_len = len(fr)
