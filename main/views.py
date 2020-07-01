from django.shortcuts import render
from main.models import College, Student, Review
from collections import Counter 

def Students(request):
	clgs = [s.college for s in Student.objects.all()]

	# sorting the colleges with highnest repeated on at the front
	result = sorted(clgs, key = clgs.count, 
                                reverse = True)
	# removing duplicates from the list
	result = list(dict.fromkeys(result))

	# ordering the students according to last date enroleed
	sts = Student.objects.order_by('-date')

	# comparing the top college and latest completed students and stacking them in a list
	# new = []
	# for c in result:
	# 	for s in sts:
	# 		if(c==s.college):
	# 			new.append(s)

	# doing the above five lines in a easier way:
	new = [s for s in sts for c in result if(c==s.college)]

	return render(request, 'main/home.html', {'Students':new})

def Reviews(request):
	rv = Review.objects.order_by('-date')
	return render(request, 'main/reviews.html', {'Reviews':rv})