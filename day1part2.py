# input is a list of numbers
#Part 2
#code :

INPUT_S = '''\
178
205
212
210
215
220
223
224
230
232
235
225
226
227
238
248
249
251
252
261
273
283
284
286
296
297
303
317
320
333
370
339
'''

numbers = [int(line) for line in INPUT_S.splitlines()]

count = 0

count = sum(
    numbers[i] > numbers[i-3]
    for i in range(3,len(numbers)))
print(count)
