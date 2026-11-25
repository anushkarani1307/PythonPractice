crm_ids = ['C01', 'C02', 'C03', 'C04', 'C07']
billing_ids = ['C02', 'C04', 'C05', 'C06', 'C04']

a = crm_ids
b = [x for x in crm_ids if x in billing_ids]
c = [x for x in crm_ids if x not in billing_ids]
d = list(set(billing_ids) - set(crm_ids))
d.sort()
e = len(set(crm_ids + billing_ids))

print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("E:", e)