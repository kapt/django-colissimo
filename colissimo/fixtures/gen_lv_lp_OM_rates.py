from decimal import Decimal as D

paliers = [
		   (D(0.02), D(0.76)),
		   (D(0.05), D(1.25)),
		   (D(0.1), D(1.90)),
		   (D(0.25), D(3.05)),
		   (D(0.5), D(4.1)),
		   (D(1.00), D(5.35)),
		   (D(2.00), D(6.80)),
		   (D(3.00), D(7.30)),
		   ]

pas, supplement = D(0.01), D(0.11)

current_val = pas

valeurs = []
for p, palier_price in paliers:
	while current_val.quantize(D('0.01')) <= p:
		prix = palier_price + (current_val / pas) * supplement

		valeurs.append((current_val.quantize(D('0.01')), prix.quantize(D('0.01'))))

		current_val += pas

for weight, rate in valeurs:
	print '%s, %s, 0,0,0,3,9' % (weight, rate)
