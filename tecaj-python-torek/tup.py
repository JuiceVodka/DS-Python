our_list = [1, 2, 3, 4, 5, 6, 7]
our_dict = {
	"a": 2,
	"b": 5,
	"c": 8,
	"d": 12,
	"e": 357,
	"f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

our_dict["d"] = our_list[4]
our_list.remove(our_list[4])

tup = tuple(our_dict.values())

if(tup == our_tuple):
	print("ENAKA!")
else:
	print("NEENAKA!")